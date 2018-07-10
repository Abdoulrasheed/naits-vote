# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
from PIL import Image
from django.contrib.auth.decorators import login_required
# User Update modules
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from .forms import ProfileForm
from django.conf import settings as django_settings
from django.contrib import messages



from django.shortcuts import get_object_or_404, render
from bitpoint.messenger.models import Message
from django.db.models import Q
from .models import User



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