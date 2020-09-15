from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name='events'


urlpatterns = [
    path('', views.EventList.as_view(), name='all'),
]
