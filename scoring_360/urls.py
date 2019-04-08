from django.urls import path

from . import views

app_name = 'scoring_360'

urlpatterns = [
    path('questions/list/', views.questions360_list, name='questions360_list'),
    path('question/add/', views.question360_add, name='question360_add'),
    path('question/<int:question_id>/edit/', views.question360_edit, name='question360_edit'),
]
