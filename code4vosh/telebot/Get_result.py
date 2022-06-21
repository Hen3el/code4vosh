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
    try:
        info = response['tsInfo']['contents']
        max_score = info[0]['contents']['contestMaxScore']
        tag = info[1]['tag']
        user_score = info[1]['contents']['userScore']
        user = response['tsUser']['userName']
        text = f'Ученик {user} набрал {user_score} из {max_score} баллов'
        return text
    except:
        TypeError

tokens = [
    'tii27/sch771547/7/r89387',
    'tii27/sch771547/7/7w9827',
    'tii27/sch771547/7/r349g7',
    'tii27/sch771547/6/753667',
    'tii27/sch771547/7/75gwz7',
    'tii27/sch771547/6/753667',
    'tii27/sch771547/6/rqw6gr',
    'tii27/sch771547/6/7g5q67',
    'tii27/sch771547/7/r99v9r',
    'tii27/sch771547/6/7g5267',
    'tii27/sch771547/6/7g5467',
    'tii27/sch771547/6/7g5367',
    'tii27/sch771547/6/7g5q67',
    'tii27/sch771547/6/7wgq97',
    'tii27/sch771547/7/r89487',
    'tii27/sch771547/6/r3z337',
    'tii25/sch771547/4/733r87',
    'tii25/sch771547/4/72q6r5',
    'tii25/sch771547/4/5zz3q5',
    'tii25/sch771547/4/593gv5',
    'tii25/sch771547/4/7wz925',
    'tii25/sch771547/4/74r297',
    'tii25/sch771547/4/7g6g25',
    'tii25/sch771547/4/764287',
    'tii25/sch771547/4/58zgg5',
    'tii25/sch771547/4/5q32w5',
    'tii25/sch771547/4/5vrzr5',
    'tii25/sch771547/4/7rrg47',
    'tii25/sch771547/4/733487',
    'tii25/sch771547/4/72qzr5',
    'tii25/sch771547/4/5zzrq5',
    'tii25/sch771547/4/5936v5',
    'tii25/sch771547/4/7wzg25',
    'tii25/sch771547/4/74r397',
    'tii25/sch771547/4/7g6325',
    'tii25/sch771547/4/764v87',
    'tii25/sch771547/4/58z6g5',
    'tii25/sch771547/4/5q3ww5',
    'tii25/sch771547/4/5vrwr5',
    'tii25/sch771547/4/7rr247',
    'tii25/sch771547/4/733z87',
    'tii25/sch771547/4/5vrvr5',
    'tii25/sch771547/4/7rr947',
    'tii25/sch771547/4/72qqr5',
    'tii25/sch771547/4/733987',
    'tii25/sch771547/4/5zzzq5',
]
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