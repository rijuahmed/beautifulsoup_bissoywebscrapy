import requests
from bs4 import BeautifulSoup
import json
'''Riju'''

url = "https://www.bissoy.com/original-answers?page="
page_num = 1
questions = []
answers = []

while page_num <= 335:
    print("Starting index ", page_num)
    res = requests.get(url + str(page_num))
    soup = BeautifulSoup(res.text, "html.parser")

    question = soup.find_all('h1', {'class': 'card-title mb-1'})
    for string in question:
        name = string.text.strip()
        questions.append(name)

    # answer = soup.find_all('div', {'class': 'ans-cont px-2 position-relative'})
    # for item in answer:
    #     string = item.find_all('p')
    #     for item in string:
    #         final = item.text.strip()
    #         answers.append(final)
    answer = soup.find_all('div', {'class': 'ans-cont px-2 position-relative'})
    for item in answer:
        string = item.find_all('p')
        final = ''.join(p.text.strip() for p in string)
        answers.append(final)

    next_page = soup.find('a', {'page-link'})
    if next_page:
        page_num += 1
        continue
    else:
        break

# print(questions)
# print(answers)
data = []
for i in range(len(questions)):
    data.append({'question': questions[i], 'answer': answers[i]})
# print(data)

with open('data.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False)
