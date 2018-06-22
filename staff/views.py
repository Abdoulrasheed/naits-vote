# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import ListOfStaff
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger



@login_required
def staffs(request):
    staffs_list = ListOfStaff.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(staffs_list, 12)
    try:
        staffs = paginator.page(page)
    except PageNotAnInteger:
        staffs = paginator.page(1)
    except EmptyPage:
        staffs = paginator.page(paginator.num_pages)
    return render(request, 'naits/staffs_list.html', {'staffs': staffs})


