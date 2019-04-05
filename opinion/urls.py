from django.urls import path

from . import views

app_name = 'opinion'

urlpatterns = [
    path('add/<int:seaman_id>/', views.opinion_add, name='opinion_add'),
    path('edit/<int:seaman_id>/<int:opinion_id>/', views.opinion_edit, name='opinion_edit'),
]
