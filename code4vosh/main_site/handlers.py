from django.db import IntegrityError

from codes.models import IssuedCodes, Code
from .models import SchoolSubject, Group
from users.models import UserProfile


class CodesDistributionHandler():

    def __init__(self, request=None, form=None):
        self.request = request
        try:
            self.users_bio = self.request.session['users_bio']
            self.users_parallel = self.request.session['users_parallel']
        except KeyError:
            self.users_bio = self.request.user.get_bio()
            self.users_parallel = self.request.user.get_parallel()
            self.save_params_in_session()
        self.get_issued_codes()
        self.get_subj_choices()

    def has_perms_to_recieve_codes(self):
        if not self.user_is_teacher:
            self.user_has_perms_to_recieve_codes = True
            return True
        self.user_has_perms_to_recieve_codes = False
        return False

    def check_params_in_session(self):
        if 'users_parallel' in self.request.session:
            return True
        else:
            return False

    def get_issued_codes(self):
        self.issued_codes = self.request.user.issued_code.all().select_related('subj')
        self.already_selected_subject = self.issued_codes.values_list('subj', flat=False)
        '''
        try:
            self.issued_codes = IssuedCodes.objects.filter(
                pupil=self.users_bio
                ).select_related('code', 'code__subj')
            self.already_selected_subject = self.issued_codes.values_list('code__subj', flat=False)
        except IssuedCodes.DoesNotExist:
            self.issued_codes = None
'''
    def get_subj_choices(self):
        self.subj_choices = SchoolSubject.objects.filter(start_parallel__lte=self.users_parallel).exclude(
            subject__in=self.already_selected_subject
            )
        
    def register_code(self):
        self.selected_subject = self.form.cleaned_data['subject']
        code = Code.objects.filter(
            subj=self.selected_subject, parallel=self.users_parallel, 
            issued_to=None
        ).first()
        try:
            if code is not None:
                code.issued_to = self.request.user
                code.set_issue_date()
                code.save()
                return True
            else:
                self.error_message = (
                    f'Код по предмету {self.selected_subject} не найден. Возможно, он будет добавлен позже'
                )
                return False
        except IntegrityError:
            pass
        '''
        self.selected_subject = self.form.cleaned_data['subject']
        code = Code.objects.filter(
            subj=self.selected_subject, parallel=self.users_parallel, 
            issued=False
        ).select_related('subj').first()
        try:
            if code is not None:
                self.issue = IssuedCodes(
                    code=code,
                    pupil=self.users_bio,
                )
                self.issue.save()
                code.issued = True
                code.save()
                return True
            else:
                self.error_message = (
                    f'Код по предмету {self.selected_subject} не найден. Возможно, он будет добавлен позже'
                )
                return False
        except IntegrityError:
            pass
        '''
    
    def save_params_in_session(self):
        self.request.session['users_parallel'] = self.users_parallel
        self.request.session['users_bio'] = self.users_bio
        

class TeachersCabTableHandler():

    def __init__(self, request):
        self.request = request
        self.users_classroom = self.request.user.classroom
        self.users_classroom_pupils = self.users_classroom.pupil_class.all()
        print(self.users_classroom_pupils)
        self.issued_codes = UserProfile.objects.filter(classroom)
        print(self.issued_codes)
        #self.issued_codes = self.users_classroom_pupils.select_related('issued_code')
        #self.issued_codes = IssuedCodes.objects.filter(
        #    pupil__in=self.users_classroom_pupils
        #    ).select_related('code').values('pupil', 'code__subj', 'result')
        
        #self.get_pupils_list()

    def get_pupils_list(self):
        self.pupils = Group.pupil_class.filter()
        print(self.pupil)