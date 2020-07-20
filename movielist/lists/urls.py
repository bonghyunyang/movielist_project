from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'lists_api'
urlpatterns = [
    url('', views.ListView.as_view()),
]
