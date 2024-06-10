from django.contrib.auth import login
import logging

from .models import Teacher, Pupil


class UserRegHandler():
    ''' Класс-помощник регистрации нового пользователя '''
    def __init__(self, form, request):
        self.form = form
        self.request = request

    def find_user_in_school_members(self):
        ''' Функция поиска введённых данных в БД коллектива школы '''
        try:
            bio = (
                self.form.cleaned_data['surname'] +
                ' ' + self.form.cleaned_data['name'] +
                ' ' + self.form.cleaned_data['middle_name']
            )
            self.member = Teacher.objects.get(bio=bio)
            logging.info(f'Учитель {bio} найден в БД')
            return True
        except Teacher.DoesNotExist:
            try: 
                bio = bio[0:bio.rfind(' ')]
                self.member = Pupil.objects.get(bio=bio)
                logging.info(f'Ученик {bio} найден в БД')
                return True
            except Pupil.DoesNotExist:
                logging.warning(f'{bio} не найден в БД')
                return False

    def create_new_user(self):
        self.user = self.form.save(commit=False)
        self.user.is_teacher = isinstance(self.member, Teacher)
        self.user.classroom = self.member.classroom
        self.user.save()
        self.member.registered = True
        self.member.save()
        logging.info(f'{self.member} зарегистрировался на сайте как {self.user}')

    def login_and_autenticate_user(self):
        login(self.request, self.user)



