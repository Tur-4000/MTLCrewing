from django.urls import path
from . import views


urlpatterns = [
    path('', views.seamans_list, name='seamans_list'),
    path('seaman/', views.seamancard, name='seamancard'),
    path('seaman/add/', views.seaman_add, name='seaman_add'),
]