from django.urls import path
from . import views

urlpatterns = [
    path('', views.login),
    path('/student/', views.student),
    path('/adjustTicket/', views.adjustTicket),
    path('/cancelTicket/', views.cancelTicket),
    path('/bookTicket/', views.bookTicket),
    path('/index/', views.index),
    path('/timeSlot/', views.timeSlot)
]
