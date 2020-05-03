from django.urls import path
from . import views

urlpatterns = [
#    path('', views.login),
    path('', views.SigninView.as_view(), name='login'),
    path('administrator/', views.administrator, name = 'administrator'),
    path('operator/', views.operator, name = 'operator'),
    path('student/', views.student),
    path('bookTicket/', views.BookTicketView.as_view()),
    path('adjustTicket/', views.AdjustTicketView.as_view()),
    path('cancelTicket/', views.CancelTicketView.as_view()),
]
