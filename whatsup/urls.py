from django.urls import path
from whatsup import views

urlpatterns=[
    path('profile/',views.profile,name='profile')
]