from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from events.models import Country, Athlete, Event


class EventList(View) :
    def get(self, request):
        ac = Athlete.objects.all().count();
        el = Event.objects.all();

        ctx = { 'athlete_count': ac, 'event_list': el };
        return render(request, 'events/event_list.html', ctx)
