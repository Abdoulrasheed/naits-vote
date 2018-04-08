#-*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views import generic

from .models import Aspirant, Office


class IndexView(generic.ListView):
    template_name = 'naits/index.html'
    context_object_name = 'latest_poll_list'

    def get_queryset(self):
        return Office.objects.all()[:5]


class DetailView(generic.DetailView):
    model = Office
    template_name = 'naits/detail.html'


class ResultsView(generic.DetailView):
    model = Office
    template_name = 'naits/results.html'


def vote(request, poll_id):
    p = get_object_or_404(Office, pk=poll_id)
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
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('results', args=(p.id,)))
