import django
from django.conf.urls import include, url
from django.contrib import admin

from AuthApp import views

urlpatterns = [
    url(r'^$', views.HomeJWTView.as_view(), name='home'),

    url(r'^api/login/', include('rest_social_auth.urls_jwt_pair')),

    url(r'^api/user/jwt/', views.UserJWTDetailView.as_view(), name="current_user_jwt"),

]
