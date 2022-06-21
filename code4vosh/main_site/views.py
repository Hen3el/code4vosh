from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import TeacherCreationForm


def main(request):
    template = 'main_site/main.html'
    return render(request, template)


def teacher_create(request):
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
