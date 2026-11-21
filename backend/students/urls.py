
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    
    path('login/', views.login_page, name='login'),

    path('dashboard/', views.dashboard, name='dashboard'),

    path('register/', views.register, name='register'),

    path('students/', views.student_list, name='student_list'),

    path('logout/', views.logout_page, name='logout'),
    
    path('products/', views.products,name='products')
]
#ctrl+shift+`~`
#{{}}