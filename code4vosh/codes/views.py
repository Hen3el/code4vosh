from django.shortcuts import render, redirect
from django.db import IntegrityError
from .models import IssuedCodes, Code
from .forms import SubjForm


def code_choice(request):
    user = request.user.get_bio()
    choices = Code.objects.filter(pupil=user).values_list('code', 'subj')
    form = SubjForm(
        request.POST or None,
        choices=choices,
    )
    template = 'main_site/lk_form.html'
    context = {
        'form': form
    }
    if not form.is_valid():
        return render(request, template, context)
    codes = form.cleaned_data['subject']
    for code in codes:
        try:
            code = Code.objects.get(code=code)
            issue = IssuedCodes(code=code, subject=code.subj, pupil=code.pupil)
            issue.save()
        except IntegrityError:
            pass
    return redirect('main_site:user_cab')
