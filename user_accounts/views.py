
""" 
Views 
"""
#standard library imports
from datetime import timedelta, datetime
import logging
import traceback


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
from rest_framework.generics import ListAPIView,RetrieveUpdateAPIView,ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from oauth2_provider.ext.rest_framework import OAuth2Authentication, TokenHasScope, TokenHasReadWriteScope
from rest_framework.response import Response
from rest_framework.throttling import UserRateThrottle
from rest_framework import status

#application imports
from serializers import *
#from models import *
from utils.permission_class import PostWithoutAuthentication
from django.conf import settings


logger_user = logging.getLogger('log.user_account')
logger_error = logging.getLogger('log.errors')

@login_required
def user_account(request):

	return render(request,'user_accounts/my_accounts.html',{})

def login_view(request):
    data = redirect("/login/facebook/")
    return HttpResponse(data)

@login_required
def logout_view(request):
  auth.logout(request)
  return HttpResponseRedirect("/")

class AuthView(APIView ):
    
    authentication_classes = [OAuth2Authentication]



    def delete(self, request,*args,**kwargs):
        auth.logout(request)
        return Response({})

    def post(self,request,*args,**kwargs):
        try:
            token = self.request.DATA
            user = request.backend.do_auth(token)
            if user:
                login(request,user)
            else:
                return Response(status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception,e:
            print repr(e)
            return Response(status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            data = access_token_gen(user)
            return Response(data, status.HTTP_200_OK)

    def get(self,request,*args,**kwargs):
        try:
            permission_classes = (TokenHasScope,)
            required_scopes = ['read']
            data = User.objects.filter(email = self.request.user)
            serializer = UserNameOnlySerializer(data, many = True)
        except Exception,e:
            print repr
            return None
        else:
            return Response(serializer.data)




@psa('social:complete')
def register_by_access_token(request, backend):
    try:
        token = request.body
        user = request.backend.do_auth(token)
        logger_user.info("adding new user "+str(user))
        logger_user.info("user adding request "+str(request))
        if user:
            login(request, user)
        else:
            logger_error.error(traceback.format_exc())
            return HttpResponse(status = 500)
    except Exception,e:
        print repr(e)
        logger_error.error(traceback.format_exc())
        return HttpResponse(status = 500)
    else:
        return access_token_gen(user)


class UserMixin(object):
    authentication_classes = [OAuth2Authentication]
    permission_classes = (TokenHasScope,)
    serializer_class = UserProfileSerializer
    required_scopes = ['write','read']
    def get_queryset(self):
        return UserProfile.objects.filter(user_acc = self.request.user)


class GetUserDetail(UserMixin, ListAPIView, RetrieveUpdateAPIView):

    def put(self,request,*args,**kwargs):
        try:
            user = self.request.user
            data = self.request.DATA
            mobile = data['mobile_no']
            area = data['area']
            first_name = data['first_name']
            logger_user.info("updated user data "+str(data))
            UserProfile.objects.filter(user_acc_id = user).update(area = area,  \
                mobile = mobile)
            User.objects.filter(email = user).update(first_name = first_name)
        except Exception,e:
            logger_error.error(traceback.format_exc())
            return Response(status = status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response(status = status.HTTP_200_OK)

class ActiveBookingMixin(object):
    #authentication_classes = [OAuth2Authentication]
    #permission_classes = (TokenHasScope,)
    #serializer_class = UserProfileSerializer
    #required_scopes = ['write','read']
    def get_queryset(self):
        return UserProfile.objects.filter(user_acc = self.request.user)

class GetActiveBookings(ActiveBookingMixin, ListAPIView):
    pass


class InviteUserMixin(object):
    permission_classes = (PostWithoutAuthentication,)
    throttle_classes = (UserRateThrottle,)
    serializer_class = InviteUserSerializer
    queryset = UserInvites.objects.all()

class InviteUser(InviteUserMixin,ListCreateAPIView):
   pass

def getFBkey(request):
    """function which returns the FB key for making authentication"""
    return  HttpResponse(settings.FBAPIKEY)





