from django.urls import path
from . import views

urlpatterns = [
    path('', views.login),
    path('administrator/', views.administrator),
    path('operator/', views.operator),
    path('student/', views.student),
]
