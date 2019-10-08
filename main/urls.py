"""marksheet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', IndexPage.as_view(), name='index_page_url'),
    path('sign-up/', SignUp.as_view(), name='signup_page_url'),
    path('sign-in/', SignIn.as_view(), name='signin_page_url'),
    path('dashboard/', dashboardIndex, name='dashboard_index_url'),
    path('sign-out/', signOut, name='logout_page_url'),
    path('create-class/<str:code>', CreateClass.as_view(), name='create_class_url'),
    path('classes/index/', ClassesList.as_view(), name='classes_index_url'),
    path('classes/view/', ClassView.as_view(), name='class_view_url'),
    path('classes/students/add/<int:c_id>', AddStudent.as_view(), name='add_student_url'),
]
