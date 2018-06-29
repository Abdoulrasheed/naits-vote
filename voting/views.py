#-*- coding: utf-8 -*-
from .forms import ProfileForm
from django.views import generic
from django.contrib import messages
from messenger.models import Message
from voting.decorators import ajax_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from .models import Aspirant, Office, Voter, User
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# User Update modules
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm, UserChangeForm

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
    students_list = User.objects.filter(is_active=True).order_by('-id')
    page = request.GET.get('page', 1)
    paginator = Paginator(students_list, 9)
    try:
        students = paginator.page(page)
    except PageNotAnInteger:
        students = paginator.page(1)
    except EmptyPage:
        students = paginator.page(paginator.num_pages)
    return render(request, 'students/students_list.html', {'students': students})


@login_required
def excos(request):
    excos_list = User.objects.filter(is_exco=True).order_by('-level')
    page = request.GET.get('page', 1)
    paginator = Paginator(excos_list, 12)
    try:
        excos = paginator.page(page)
    except PageNotAnInteger:
        excos = paginator.page(1)
    except EmptyPage:
        excos = paginator.page(paginator.num_pages)
    return render(request, 'students/excos_list.html', {'excos': excos})



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
def ProfileUpdate(request):
    user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            user.first_name = form.cleaned_data.get('first_name')
            user.last_name = form.cleaned_data.get('last_name')
            user.level = form.cleaned_data.get('level')
            user.email_address = form.cleaned_data.get('email_address')
            user.mobile = form.cleaned_data.get('mobile')
            user.hall_of_residence = form.cleaned_data.get('hall_of_residence')
            user.state_of_origin = form.cleaned_data.get('state_of_origin')
            user.profile_picture = form.cleaned_data.get('profile_picture')
            user.is_updated = True
            user.save()
            messages.success(request, 'Your profile was successfully edited.')

    else:
        form = ProfileForm(instance=user, initial={
            'first_name': user.first_name,
            'last_name': user.last_name,
            'level': user.level
            })

    return render(request, 'account/profile_update.html', {'form': form})



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
def check_messages(request):
    count = Message.objects.filter(user=request.user, is_read=False).count()
    return render(request, 'notifications/notifications.html', {'unread': count})