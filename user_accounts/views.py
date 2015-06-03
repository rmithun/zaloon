
""" 
Views 
"""
#standard library imports
from datetime import timedelta, datetime

#third party imports
from django.shortcuts import get_object_or_404, render_to_response,redirect, \
render
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import redirect
from social.apps.django_app.utils import psa
from utils.generic_utils import *
#from permissions import IsUserThenReadPatch, ReadOnlyAuthentication
from rest_framework.generics import ListAPIView,RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from oauth2_provider.ext.rest_framework import OAuth2Authentication, TokenHasScope, TokenHasReadWriteScope

#application imports
from serializers import *

@login_required
def home(request):

	return render(request,'user_accounts/home.html',{})

def login_view(request):
    data = redirect("/login/facebook/")
    return HttpResponse(data)

@login_required
def logout_view(request):
  auth.logout(request)
  return HttpResponseRedirect("/")

@psa('social:complete')
def register_by_access_token(request, backend):
    try:
        token = request.body
        user = request.backend.do_auth(token)
        if user:
            login(request, user)
        else:
            return HttpResponse(status = 500)
    except Exception,e:
        print repr(e)
        return HttpResponse(status = 500)
    else:
        return access_token_gen(user)


class UserMixin(object):
    authentication_classes = [OAuth2Authentication]
    permission_classes = (TokenHasScope,)
    serializer_class = UserProfileSerializer()
    def get_queryset(self):
        print self.request
        return UserProfile.objects.all()


class GetUserDetail(UserMixin, ListAPIView):
    pass