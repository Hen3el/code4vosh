import requests
from http import HTTPStatus

link_reg = 'https://online.olimpiada.ru/smt-portal/register/login'
link_result = 'https://online.olimpiada.ru/smt-portal/test'

class InvalidTokenError(Exception):
    """Токен неверный"""


def register(token):
    
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36",
    }
    data = {"token": token}
    response = requests.post(link_reg, json=data)
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        return False
    return response.json()

def get_answer(response):
    if 'canPassTest' not in response:
        return False
    data = response['canPassTest']
    payload = {
        'regQuizId': data['liContestId'],
        'sid': data['liSessionId']
    }
    response = requests.get(link_result, params=payload)
    return response.json()

def get_result(response):
    tags = {}
    try:
        info = response['tsInfo']['contents']
        tags['max_score'] = info[0]['contents']['contestMaxScore']
        tags['tag'] = info[1]['tag']
        tags['user_score'] = info[1]['contents']['userScore']
        tags['user'] = response['tsUser']['userName']

        return tags
    except:
        TypeError

tokens = input()
for token in tokens:
    response = register(token)
    if not response:
        print(f'{token} недействителен')
        continue
    answer = get_answer(response)
    if not answer:
        print(f'{token} не был использован')
        continue
    result = get_result(answer)
    print(result)