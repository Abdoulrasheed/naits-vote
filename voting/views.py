#-*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.views import generic
from django.contrib.auth.decorators import login_required
from voting.decorators import ajax_required
from .models import Aspirant, Office, Voter, User

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
import datetime
from django.utils import timezone

# students paginator imports

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# change password imports

from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm

from django.views.generic.edit import CreateView, UpdateView, DeleteView

@method_decorator([login_required], name='dispatch')
class IndexView(generic.ListView):
    template_name = 'naits/index.html'
    context_object_name = 'latest_poll_list'
    paginate_by = 2

    def get_queryset(self):
        return Office.objects.all()[:5]

@method_decorator([login_required], name='dispatch')
class DetailView(generic.DetailView):
    model = Office
    template_name = 'naits/detail.html'

@login_required
def profile(request, pk):
    student_page = get_object_or_404(User, id=pk)
    return render(request, 'account/profile.html', {
    'student_data': student_page
    })

@login_required
def students(request):
    students_list = User.objects.filter(is_active=True).order_by('-level')
    page = request.GET.get('page', 1)
    paginator = Paginator(students_list, 10)
    try:
        students = paginator.page(page)
    except PageNotAnInteger:
        students = paginator.page(1)
    except EmptyPage:
        students = paginator.page(paginator.num_pages)
    return render(request, 'naits/students_list.html', {'students': students})


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

@method_decorator([login_required], name='dispatch')
class ProfileUpdate(UpdateView):
    model = User
    template_name = 'account/User_form.html'
    fields = ['first_name','last_name','hall_of_residence','profile_picture', 'is_updated']


@login_required
def vote(request, poll_id):
    p = get_object_or_404(Office, pk=poll_id)
    if Voter.objects.filter(office_id=poll_id, student_id=request.user.id).exists():
        return render(request, 'naits/detail.html', {
            'office': p, 
            'error_message': 'You already vote'
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
        return HttpResponseRedirect('/')

@login_required
@ajax_required
def notifications(request):
    no_of_offices = Office.objects.all().count()
    notifications = ()
    if len(Voter.objects.filter(student_id=request.user.id)) == no_of_offices:
        continue_voting = '<a href="/"><small>you need to finsh casting your votes here</a></small>'
        notifications = (continue_voting,)
    else:
        notifications = ()
    if not request.user.is_updated:
        update = "<small><a href='/edit/" + str(request.user.id)+"'" + " title='update profile'> Please update your profile information</a></small>"
        notifications += (update,)
    else:
        if timezone.now() < request.user.updated_at - datetime.timedelta(days=30):
            need_update = "<small>its more than 30 days since you updated your profile,\
             <a href='/edit/" + str(request.user.id)+"'"\
             + " title='update profile'> would you like to review it ?</a></small>"
            notifications += (need_update,)
    return render(request, 'account/notifications.html', {'notifications': notifications})

