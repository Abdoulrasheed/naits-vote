#-*- coding: utf-8 -*-
from django.views import generic
from bitpoint.messenger.models import Message
from decorators import ajax_required
from django.http import HttpResponseRedirect
from .models import Aspirant, Office, Voter, User
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


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
def students(request):
    students_list = User.objects.filter(is_active=True, is_student=True).order_by('-id')
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
def staffs(request):
    staffs_list = User.objects.filter(is_active=True, is_d_staff=True).order_by('-id')
    page = request.GET.get('page', 1)
    paginator = Paginator(staffs_list, 9)
    try:
        staffs = paginator.page(page)
    except PageNotAnInteger:
        staffs = paginator.page(1)
    except EmptyPage:
        staffs = paginator.page(paginator.num_pages)
    return render(request, 'staffs/staffs_list.html', {'staffs': staffs})

@login_required
def excos(request):
    excos_list = User.objects.filter(is_active=True, is_exco=True).order_by('-id')
    page = request.GET.get('page', 1)
    paginator = Paginator(excos_list, 9)
    try:
        excos = paginator.page(page)
    except PageNotAnInteger:
        excos = paginator.page(1)
    except EmptyPage:
        excos = paginator.page(paginator.num_pages)
    return render(request, 'excos/excos_list.html', {'excos': excos})
