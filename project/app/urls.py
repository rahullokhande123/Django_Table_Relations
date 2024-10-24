
from django.urls import path
from app import views

urlpatterns = [
    path('',views.home,name='home'),
    path('userdata/',views.userdata,name='userdata'),
    # path('profiledata/',views.profiledata,name='profiledata')
]