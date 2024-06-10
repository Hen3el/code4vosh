from django.shortcuts import render, redirect

from .handlers import UserRegHandler
from .forms import UserCreation


def user_create(request):
    form = UserCreation(
        request.POST or None
    )
    template = 'users/signup.html'
    if not form.is_valid():
        return render(request, template, {'form': form})
    reg_handler = UserRegHandler(form=form, request=request)
    if reg_handler.find_user_in_school_members():
        reg_handler.create_new_user()
        reg_handler.login_and_autenticate_user()
        del reg_handler
        return redirect('main_site:main')
    else:
        return redirect('users:reg_failed')


def register_failed(request):
    template = 'main_site/register_failed.html'
    return render(request, template)
