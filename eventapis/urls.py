from django.urls import path
from .views import *


urlpatterns = [
    path('create_country',CountryCreateApi.as_view()),
    path('events_list',EventsApi.as_view()),
    path('update_athlete/<int:pk>',AthleteUpdateApi.as_view()),
    path('delete_comment/<int:pk>',CommentDeleteApi.as_view()),

]
