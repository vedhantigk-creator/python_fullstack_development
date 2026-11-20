
from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_page, name='login'),

    path('dashboard/', views.dashboard, name='dashboard'),

    path('students/add/', views.student_form, name='student_form'),

    path('students/', views.student_list, name='student_list'),

    path('logout/', views.logout_page, name='logout'),
]
