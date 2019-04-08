from django.urls import path

from . import views

app_name = 'opinion'

urlpatterns = [
    path('<int:seaman_id>/add/', views.opinion_add, name='opinion_add'),
    path('<int:seaman_id>/<int:opinion_id>/edit/', views.opinion_edit, name='opinion_edit'),
]
