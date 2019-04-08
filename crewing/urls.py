from django.urls import path
from . import views


urlpatterns = [
    path('', views.seamans_list, name='seamans_list'),
    path('seaman/', views.seamancard, name='seamancard'),
    path('seaman/<int:seaman_id>/card/', views.seamancard, name='seamancard'),
    path('seaman/add/', views.seaman_add, name='seaman_add'),
    path('seaman/<int:seaman_id>/edit/', views.seaman_edit, name='seaman_edit'),
    path('seaman/<int:seaman_id>/contract/add/', views.contract_add, name='contract_add'),
    path('seaman/<int:seaman_id>/contract/<int:contract_id>/edit/', views.contract_edit, name='contract_edit'),
    path('rank/list/', views.rank_list, name='rank_list'),
    path('rank/add/', views.rank_add, name='rank_add'),
    path('rank/<int:rank_id>/edit/', views.rank_edit, name='rank_edit'),
    path('vessel/list/', views.vessels_list, name='vessels_list'),
    path('vessel/add/', views.vessel_add, name='vessel_add'),
    path('vessel/<int:vessel_id>/edit/', views.vessel_edit, name='vessel_edit'),
]
