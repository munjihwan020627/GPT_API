##################data 생성 부분###############################

import sys
import os
import pandas as pd


sys.stdout.reconfigure(encoding='utf-8-sig')


def save_expenses_to_csv(income, expense_categories, filename="expense_item.csv"):
    data = {"월급": [income]}
    data.update(expense_categories)

    df = pd.DataFrame(data)
    df.to_csv(filename, index=False, encoding="utf-8-sig")

    

income = 3000000
expense_categories = {
    "기부금": 0,
    "저축": 0,
    "공과금과통신비": 0,
    "주거비": 0,
    "식비": 0,
    "교통비": 0,
    "생활비": 0,
    "교육비": 0,
    "의료비": 0,
    "보험료": 0,
    "문화/여가비": 0,
    "자기개발비": 0,
    "기타": 0,   
    
}

save_expenses_to_csv(income, expense_categories)



##################### GPT 내용 #############################################
import openai

import ast




def get_completion(prompt, model="gpt-4o-mini"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,
    )
    return response['choices'][0]['message']['content']

openai.api_key = "MY_KEY"  



df = pd.read_csv("expense.csv",encoding="utf-8-sig")

for index,row in df.iterrows():
    a = row.to_string()

    tmp = a.split()
    tmp = list(tmp[2].split("\\t"))
    usermessage = tmp[0]+"에 " + tmp[1] + "원 을 지불 할 때 내가 지불한 것이 13개의 항목 중 가장 가까운 한개의 항목에 숫자로 더해질건데 기부금, 저축, 공과금과통신비, 주거비, 식비, 교통비, 생활비, 의료비, 보험료, 문화/여가비, 자기개발비 중에 하나야 이걸 ['항목명', 금액] 형식의 리스트로 표현해줘 예를들어 국민은행에 200000원 지불시 [저축, 200000]           답변은 반드시 ['항목명', 금액] 형식의 리스트로만 답변해야 해 예제: ['식비', 15000]"
    response = get_completion(usermessage)
    
    
    print(response)
    
    tmp_response = ast.literal_eval(response)
    item, amount = tmp_response[0], tmp_response[1]
    if item in expense_categories:
        expense_categories[item] += amount
                
                
print(expense_categories)
save_expenses_to_csv(income, expense_categories)
