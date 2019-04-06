from django.urls import path
from . import views


urlpatterns = [
    path('', views.seamans_list, name='seamans_list'),
    path('seaman/', views.seamancard, name='seamancard'),
    path('seaman/card/<int:seaman_id>/', views.seamancard, name='seamancard'),
    path('seaman/add/', views.seaman_add, name='seaman_add'),
    path('seaman/edit/<int:seaman_id>/', views.seaman_edit, name='seaman_edit'),
    # path('seaman/<int:seaman_id>/opinion/add/', views.opinion_add, name='opinion_add'),
    # path('seaman/<int:seaman_id>/opinion/edit/<int:opinion_id>/', views.opinion_edit, name='opinion_edit'),
    path('seaman/<int:seaman_id>/contract/add/', views.contract_add, name='contract_add'),
    path('seaman/<int:seaman_id>/contract/edit/<int:contract_id>/', views.contract_edit, name='contract_edit'),
    path('rank/list/', views.rank_list, name='rank_list'),
    path('rank/add/', views.rank_add, name='rank_add'),
    path('rank/edit/<int:rank_id>/', views.rank_edit, name='rank_edit'),
    path('vessel/list/', views.vessels_list, name='vessels_list'),
    path('vessel/add/', views.vessel_add, name='vessel_add'),
    path('vessel/edit/<int:vessel_id>/', views.vessel_edit, name='vessel_edit'),
    # path('seamans_questions/list/', views.seamans_questions_list, name='seamans_questions_list'),
    # path('seamans_question/add/', views.seamans_question_add, name='seamans_question_add'),
    # path('seamans_question/edit/<int:question_id>/', views.seaman_questuion_edit, name='seamans_question_edit'),
    path('seaman/<int:seaman_id>/rating/add/', views.seaman_rating_add, name='seaman_rating_add'),

]