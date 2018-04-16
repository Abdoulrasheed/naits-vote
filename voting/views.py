#-*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.views import generic
from django.contrib.auth.decorators import login_required
from .models import Aspirant, Office, Voter, User

# change password imports

from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm



class IndexView(generic.ListView):
    template_name = 'naits/index.html'
    context_object_name = 'latest_poll_list'

    def get_queryset(self):
        return Office.objects.all()[:5]


class DetailView(generic.ListView):
    model = Office
    template_name = 'naits/detail.html'


class ResultsView(generic.DetailView):
    model = Office
    template_name = 'naits/results.html'


@login_required
def settings(request):
    return render(request, 'account/settings.html')

@login_required
def profile(request, pk):
    student_page = get_object_or_404(User, id=pk)
    return render(request, 'account/profile.html', {
    'student_data': student_page
    })

@login_required
def students(request):
    students_list = User.objects.filter(is_active=True).order_by('-level')
    return render(request, 'naits/students_list.html', {'students': students_list})


@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
        else:
            messages.error(request, 'Please correct the errors below. ')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'account/change_password.html', {
        'form': form
        })

@login_required
def vote(request, poll_id):
    p = get_object_or_404(Office, pk=poll_id)
    if Voter.objects.filter(office_id=poll_id, student_id=request.user.id).exists():
        return render(request, 'naits/detail.html', {
            'office': p, 
            'error_message': 'sorry! you already voted'
            })
    try:
        selected_choice = p.aspirant_set.get(pk=request.POST['aspirants'])
    except (KeyError, Aspirant.DoesNotExist):
        # Redisplay the poll voting form.
        return render(request, 'naits/detail.html', {
            'office': p,
            'error_message': "You didn't select an aspirant.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        setuser = Voter(student=request.user, office=p)
        setuser.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('results', args=(p.id,)))
