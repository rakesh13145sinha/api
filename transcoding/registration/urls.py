from django.urls import path
from registration import views
urlpatterns=[
    path('user/',views.user_document),
    path('signup/',views.signup),
    path('user_login/',views.userlogin)
]