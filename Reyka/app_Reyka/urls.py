from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.Home.as_view(),name='home'),
    path('page2/',views.page2),
    path('about/',views.about),
    path('about_me/',views.about_me),
    path('page3/',views.page3),
    path('page4/',views.page4),
    path('page5/',views.page5),
    path('register/',views.register),
    path('loginn/',views.login),
    path('registerr',views.Register.as_view(),name='reg'),
    path('login/',views.LoginPage.as_view(),name='login'),
    path('create_project/',views.Projects.as_view(),name='crpr'),
    path('test/',views.TestsForm.as_view(),name='/'),
    path('projects_redict/<int:pk>/',views.projects_redict.as_view()),
    path('task_redict/<int:pk>/',views.task_redict.as_view()),
    path('task/<int:id>',views.task)


]