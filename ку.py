import requests
import fake_useragent

url = 'https://online.olimpiada.ru/smt-portal/register/login'
user = fake_useragent.UserAgent().random
header = {
    "user-agent": user
}

datas = {
    "token": "thi27/sch771547/7/r8z45r"
}
response = requests.post(url, data=datas, headers=header)
print(response)
