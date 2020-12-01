from django.views.generic import TemplateView
from django.contrib.auth import logout, get_user_model
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_social_auth.serializers import UserSerializer
from rest_social_auth.views import JWTAuthMixin, KnoxAuthMixin, SimpleJWTAuthMixin


class HomeJWTView(TemplateView):
    template_name = 'AuthApp/home.html'


class BaseDetailView(generics.RetrieveAPIView):
    permission_classes = IsAuthenticated,
    serializer_class = UserSerializer
    model = get_user_model()

    def get_object(self, queryset=None):
        return self.request.user


class UserJWTDetailView(SimpleJWTAuthMixin, BaseDetailView):
    pass
