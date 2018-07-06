#-*- coding: utf-8 -*-
import os
from django.db.models import Q
from PIL import Image
from .forms import ProfileForm
from django.views import generic
from django.contrib import messages
from messenger.models import Message
from voting.decorators import ajax_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from .models import Aspirant, Office, Voter, User
from django.conf import settings as django_settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# User Update modules
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm


class IndexView(generic.ListView):
    template_name = 'naits/index.html'
    context_object_name = 'latest_poll_list'
    paginate_by = 2

    def get_queryset(self):
        return Office.objects.all()[:5]


class DetailView(generic.DetailView):
    model = Office
    template_name = 'naits/detail.html'

@login_required
def profile(request, ID_Number):
    page_user = get_object_or_404(User, ID_Number=ID_Number)
    messages_count = Message.objects.filter(
        Q(from_user=page_user) | Q(user=page_user)).count()

    data = {
        'page_user': page_user,
        'msg': messages_count,
        }
    return render(request, 'account/profile.html', data)

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
            user.email = form.cleaned_data.get('email')
            user.mobile = form.cleaned_data.get('mobile')
            user.hall_of_residence = form.cleaned_data.get('hall_of_residence')
            user.state_of_origin = form.cleaned_data.get('state_of_origin')
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
def picture(request):
    uploaded_picture = False
    try:
        if request.GET.get('upload_picture') == 'uploaded':
            uploaded_picture = True
            
    except Exception:  # pragma: no cover
        pass

    return render(request, 'account/picture.html',
                  {'uploaded_picture': uploaded_picture})


@login_required
def upload_picture(request):
    try:
        profile_pictures = django_settings.MEDIA_ROOT + '/profile_pictures/'
        if not os.path.exists(profile_pictures):
            os.makedirs(profile_pictures)

        f = request.FILES['picture']
        filename = profile_pictures + request.user.ID_Number + '_tmp.jpg'
        with open(filename, 'wb+') as destination:
            for chunk in f.chunks():
                destination.write(chunk)

        im = Image.open(filename)
        width, height = im.size
        if width > 350:
            new_width = 350
            new_height = (height * 350) / width
            new_size = new_width, new_height
            im.thumbnail(new_size, Image.ANTIALIAS)
            im.save(filename)

        return redirect('/settings/picture/?upload_picture=uploaded')

    except Exception:
        return redirect('/settings/picture/')

@login_required
def save_uploaded_picture(request):
    try:
        x = int(request.POST.get('x'))
        y = int(request.POST.get('y'))
        w = int(request.POST.get('w'))
        h = int(request.POST.get('h'))
        tmp_filename = django_settings.MEDIA_ROOT + '/profile_pictures/' +\
            request.user.ID_Number + '_tmp.jpg'
        filename = django_settings.MEDIA_ROOT + '/profile_pictures/' +\
            request.user.ID_Number + '.jpg'
        im = Image.open(tmp_filename)
        cropped_im = im.crop((x, y, w+x, h+y))
        cropped_im.thumbnail((200, 200), Image.ANTIALIAS)
        cropped_im.save(filename)
        os.remove(tmp_filename)

    except Exception:
        pass

    return redirect('/settings/picture/')


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