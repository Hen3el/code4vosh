from django.shortcuts import render, redirect
from .forms import UserCreation
from .models import Staff


def is_staff(form):
    bio = form.cleaned_data['surname'] + ' ' + form.cleaned_data['name'] + ' ' + form.cleaned_data['middle_name']
    print(bio)
    if Staff.objects.filter(bio=bio):
        return True
    return False


def user_create(request):
    form = UserCreation(
        request.POST or None
    )
    template = 'users/signup.html'
    if not form.is_valid():
        return render(request, template, {'form': form})
    if not is_staff(form):
        return redirect('users:reg_failed')
    new_teacher = form.save(commit=False)
    new_teacher.save()
    return redirect('main_site:main')


def register_failed(request):
    template = 'main_site/register_failed.html'
    return render(request, template)