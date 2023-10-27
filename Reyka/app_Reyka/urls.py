from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('page2/',views.page2),
    path('about/',views.about),
    path('about_me/',views.about_me),
    path('page3/',views.page3),
    path('page4/',views.page4)
]