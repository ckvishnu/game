from django.urls import path
from .import views

urlpatterns=[
    path('',views.home),
    path('click',views.buttonclick),
    path('click2',views.buttonclick2),
]