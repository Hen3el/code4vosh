from cmath import nan
import pandas as pd
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError

import json
from django.core.serializers.json import DjangoJSONEncoder

from .models import SchoolSubject
from users.models import Pupil
from .forms import TeacherCreationForm
from codes.models import IssuedCodes, Code
from codes.forms import IssueCodeForm
from .handlers import CodesDistributionHandler, TeachersCabTableHandler




def main_page(request):
    all_code = IssuedCodes.objects.exclude(result=None, max_result=None)
    queryset = []
    for issued_code in all_code:
        try:
            result = float(issued_code.result)
            max_result = float(issued_code.max_result)
        except ValueError:
            continue
        if result/max_result > 0.5:
            queryset.append(issued_code)
    context = {
        'codes': queryset,
    }
    template = 'main_site/main.html'
    return render(request, template, context)


@login_required
def pupils_cab(request):
    if request.user.is_teacher:
        return redirect('main_site:lk_teacher')
    handler = CodesDistributionHandler(request=request)
    form = IssueCodeForm(
        request.POST or None,
        choices=handler.subj_choices,
    )
    template = 'main_site/lk-pupil.html'
    context = {
        'issued_codes': handler.issued_codes,
        'user': handler.users_bio,
        'form': form,
    }
    if not form.is_valid():
        return render(request, template, context)
    handler.form = form
    if not handler.register_code():
        context['code_not_found'] = handler.error_message
    return render(request, template, context)
'''
    if request.method == 'GET':
        handler = CodesDistributionHandler(request=request)

        form = IssueCodeForm(
            request.POST or None,
            choices=handler.subj_choices,
        )
        template = 'main_site/lk.html'
        context = {
            'issued_codes': handler.issued_codes,
            'user': handler.users_bio,
            'form': form,
        }
        if not form.is_valid():
            return render(request, template, context)
        handler.form = form
        if not handler.register_code():
            context['code_not_found'] = handler.error_message
        return render(request, template, context)
    else:
        form = IssueCodeForm(
            request.POST or None,
            choices=handler.subj_choices,
        )
        handler.form = form
        if not handler.register_code():
            context['code_not_found'] = handler.error_message
        return render(request, template, context)
'''       

  

'''
    user = request.user.get_bio()
    try:
        issued_codes = IssuedCodes.objects.filter(pupil=user)
        issued_subj = issued_codes.values_list('subject')
    except IssuedCodes.DoesNotExist:
        issued_codes = None
    parallel = request.user.get_parallel()
    choices = SchoolSubject.objects.filter(start_parallel__lte=parallel).exclude(subject__in=issued_subj)
    '''
'''
    subject = form.cleaned_data['subject']
    try:
        code = Code.objects.filter(subj=subject, parallel=parallel, issued=False).first()
        if code is not None:
            issue = IssuedCodes(code=code, subject=code.subj, pupil=user, result_date=code.subj.result_date)
            issue.save()
            code.issued = True
            code.save()
        else:
            context['code_not_found'] = f'Код по предмету {subject} не найден. Возможно, он будет добавлен позже'
            return render(request, template, context)
    except IntegrityError:
        pass
    return render(request, template, context)
'''
@login_required
def teachers_cab(request):
    if not request.user.is_teacher:
        return redirect('main_site:lk')
    handler = TeachersCabTableHandler(request=request)
    context = {
        'data': handler.issued_codes
    }
    '''
    parallel = request.user.get_parallel()
    pupils = Pupil.objects.filter(classroom=request.user.classroom)
    subjects = list(subj.subject for subj in SchoolSubject.objects.filter(start_parallel__lte=parallel))
    subjects.insert(0, 'Ученики')
    cls_table = pd.DataFrame(columns=(subjects))
    for pupil in pupils:
        row = [pupil.bio]
        for subj in subjects[1:]:
            try:
                code = IssuedCodes.objects.get(pupil=pupil, subject=subj)
                if code.max_result:
                    row.append(f'{code.result} из {code.max_result}')
                else:
                    row.append('+')
            except IssuedCodes.DoesNotExist:
                row.append(nan)
            except IssuedCodes.MultipleObjectsReturned:
                code = IssuedCodes.objects.filter(pupil=pupil, subject=subj).last()
                if code.max_result:
                    row.append(f'{code.result} из {code.max_result}')
                else:
                    row.append('Участие')
        cls_table.loc[len(cls_table)] = row
    #json_records = cls_table.reset_index().to_json(default_handler=str)
    #data = []
    #data = json.loads(json_records)
    #print(data)
    cls_table.index += 1
    data = cls_table.to_html(bold_rows=True, na_rep='')
    #data = ClassroomTable(extra_columns=json_records)
    context = {
        'subjects': subjects,
        'd': data
        }
    '''
    template = 'main_site/lk-teacher.html'
    return render(request, template, context)

def somth(request):
    form = TeacherCreationForm(
        request.POST or None
    )
    template = 'main_site/main.html'
    if not form.is_valid():
        return render(request, template, {'form': form})
    new_teacher = form.save(commit=False)
    new_teacher.save()
    for i in form.cleaned_data['school_subj']:
        new_teacher.school_subj.add(i)
    
    #new_teacher = form.save(commit=False)
    #new_teacher.save()

    #new_teacher = form.cleaned_data['school_subj'].save(commit=False)
    #choosen_subj_list = list([str(i) for i in choosen_subj])
    #choosen_subj_list.save()
    return redirect('main_site:main')


'''
def teacher_create(request):
    if request.method == 'POST':
        form = TeacherCreationForm(request.POST)
        if form.is_valid():
            choosen_subj = form.cleaned_data['school_subj'] #result as QuerySet
            choosen_subj_list = list([str(i) for i in choosen_subj]) #you can convert it to list or anything you need             

            return render(request, 'main_site/main.html')

        context = {
            'form': form,
            }
        return render(request, 'main_site/main.html', context)

    else:
        form = TeacherCreationForm()
    context = {
        'form': form,
        }
    return render(request, 'main_site/main.html', context)
'''


'''
link_reg = 'https://online.olimpiada.ru/'
link_result = 'https://online.olimpiada.ru/smt-portal/test'


def entry_by_token(request, token):
    import http.client
    import json

    conn = http.client.HTTPSConnection("online.olimpiada.ru")
    payload = json.dumps({
        "token": "tek27/sch771547/7/7g3987"
    })
    headers = {
        'Content-Type': 'application/json'
    }
    conn.request("POST", "/smt-portal/register/login", payload, headers)
    res = conn.



def entry_by_token(request, token):
    import requests
    data = {"token": 'tek27/sch771547/7/7g3987'}
    return redirect(link_reg)
    response = response.json()
    print(response)
    #if 'canPassTest' not in response:
    #    return False
    data = response['canPassTest']
    payload = {
        'regQuizId': data['liContestId'],
        'sid': data['liSessionId']
    }
    return redirect(link_result, params=payload)
    # return redirect(link_reg, json=data)
'''