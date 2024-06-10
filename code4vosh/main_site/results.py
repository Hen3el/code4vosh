import requests
from http import HTTPStatus
from django.core import serializers
from django.http import JsonResponse

from codes.models import IssuedCodes

REG_LINK = 'https://online.olimpiada.ru/smt-portal/register/login'
RESULT_LINK = 'https://online.olimpiada.ru/smt-portal/test'

class InvalidTokenError(Exception):
    """Токен неверный"""


class TokenResult:
    short_description = "Обновить результаты выбранных кодов"

    def __new__(cls, modeladmin, request, queryset):
        result = cls.check_result(modeladmin, request, queryset)
        return result

    def modelJSON(request, pk):
        IssuedCodes_json = serializers.serialize("json", IssuedCodes.objects.filter(id=pk))
        data = {"IssuedCodes_json": IssuedCodes_json}
        return JsonResponse(data)

    def register(token):
        data = {"token": token}
        response = requests.post(REG_LINK, json=data)
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
        response = requests.get(RESULT_LINK, params=payload)
        return response.json()

    def get_tags(response):
        try:
            info = response['tsInfo']['contents']
            max_score = info[0]['contents']['contestMaxScore']
            tag = info[1]['tag']
            user_score = info[1]['contents']['userScore']
            user = response['tsUser']['userName']
            text = f'{user_score} из {max_score}'
            return user_score, max_score
        except:
            TypeError

    @classmethod
    def check_result(cls, modeladmin, request, queryset):
        for token in queryset:
            token = IssuedCodes.objects.filter(pk=token.pk)
            code = token.values_list('code')[0][0]
            response = cls.register(code)
            if not response:
                token.update(result='Код недействителен')
                continue
            answer = cls.get_answer(response)
            if not answer:
                token.update(result='Код не был использован')
                continue
            user_score, max_score = cls.get_tags(answer)
            token.update(result=user_score, max_result=max_score)
