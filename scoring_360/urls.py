from django.urls import path

from . import views

app_name = 'scoring_360'

urlpatterns = [
    path('', views.test),  # заглушка
]
