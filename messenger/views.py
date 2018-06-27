import json

from django.contrib.auth.decorators import login_required
from voting.models import User
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import redirect, render

from voting.decorators import ajax_required
from .models import Message


@login_required
def inbox(request):
    conversations = Message.get_conversations(user=request.user)
    active_conversation = None
    messages = None
    if conversations:
        conversation = conversations[0]
        active_conversation = conversation['user'].ID_Number
        messages = Message.objects.filter(user=request.user,
                                          conversation=conversation['user'])
        messages.update(is_read=True)
        for conversation in conversations:
            if conversation['user'].ID_Number == active_conversation:
                conversation['unread'] = 0

    return render(request, 'messenger/inbox.html', {
        'messages': messages,
        'conversations': conversations,
        'active': active_conversation
        })


@login_required
def messages(request, ID_Number):
    conversations = Message.get_conversations(user=request.user)
    active_conversation = ID_Number
    messages = Message.objects.filter(user=request.user,
                                      conversation__ID_Number=ID_Number)
    messages.update(is_read=True)
    for conversation in conversations:
        if conversation['user'].ID_Number == ID_Number:
            conversation['unread'] = 0

    return render(request, 'messenger/inbox.html', {
        'messages': messages,
        'conversations': conversations,
        'active': active_conversation
        })


@login_required
def new(request):
    if request.method == 'POST':
        from_user = request.user
        to_user_ID_Number = request.POST.get('to')
        try:
            to_user = User.objects.get(ID_Number=to_user_ID_Number)

        except Exception:
            try:
                to_user_ID_Number = to_user_ID_Number[
                    to_user_ID_Number.rfind('(')+1:len(to_user_ID_Number)-1]
                to_user = User.objects.get(ID_Number=to_user_ID_Number)

            except Exception:
                return redirect('/messages/new/')

        message = request.POST.get('message')
        if len(message.strip()) == 0:
            return redirect('/messages/new/')

        if from_user != to_user:
            Message.send_message(from_user, to_user, message)

        return redirect('/messages/{0}/'.format(to_user_ID_Number))

    else:
        conversations = Message.get_conversations(user=request.user)
        return render(request, 'messenger/new.html',
                      {'conversations': conversations})


@login_required
@ajax_required
def delete(request):
    return HttpResponse()


@login_required
@ajax_required
def send(request):
    if request.method == 'POST':
        from_user = request.user
        to_user_ID_Number = request.POST.get('to')
        to_user = User.objects.get(ID_Number=to_user_ID_Number)
        message = request.POST.get('message')
        if len(message.strip()) == 0:
            return HttpResponse()
        if from_user != to_user:
            msg = Message.send_message(from_user, to_user, message)
            return render(request, 'messenger/includes/partial_message.html',
                          {'message': msg})

        return HttpResponse()
    else:
        return HttpResponseBadRequest()


@login_required
@ajax_required
def users(request):
    users = User.objects.filter(is_active=True)
    dump = []
    template = '{0} ({1})'
    for user in users:
        if user.get_short_name() != user.ID_Number:
            dump.append(template.format(user.profile.get_screen_name(),
                                        user.ID_Number))
        else:
            dump.append(user.ID_Number)
    data = json.dumps(dump)
    return HttpResponse(data, content_type='application/json')


@login_required
def check(request):
    count = Message.objects.filter(user=request.user, is_read=False).count()
    user = request.user
    notifications = Message.objects.filter(user=user)
    unread = Message.objects.filter(user=user, is_read=False)
    for notification in unread:
        notification.is_read = True  # pragma: no cover
        notification.save()  # pragma: no cover

    return render(request, 'notifications/notifications.html',
                  {'notifications': notifications, 'count': count})