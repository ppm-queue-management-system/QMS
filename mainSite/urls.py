from django.urls import path
from . import views

urlpatterns = [
    path('', views.login),
    path('administrator/', views.administrator),
    path('operator/', views.operator),
    path('student/', views.student),
    path('adjustTicket/', views.AdjustTicketView.as_view()),
    path('cancelTicket/', views.CancelTicketView.as_view()),
    path('bookTicket/', views.BookTicketView.as_view()),
]
