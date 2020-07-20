from django.urls import path
from . import views

app_name = 'lists_api'
urlpatterns = [
    path('', views.ListView.as_view()),
    path('<int:movie_id>', views.ListView.as_view())
]
