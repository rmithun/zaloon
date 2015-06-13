
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
from rest_framework.generics import ListAPIView,RetrieveUpdateAPIView,ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from oauth2_provider.ext.rest_framework import OAuth2Authentication, TokenHasScope, TokenHasReadWriteScope
from rest_framework.response import Response
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
    serializer_class = UserProfileSerializer
    required_scopes = ['write']
    def get_queryset(self):
        return UserProfile.objects.filter(user_acc = self.request.user)


class GetUserDetail(UserMixin, ListAPIView, RetrieveUpdateAPIView):
    
    def put(self,request,*args,**kwargs):
        try:
            user = self.request.user
            data = self.request.DATA
            mobile_no = data['mobile_no']
            area = data['area']
            first_name = data['first_name']
            UserProfile.objects.filter(user_acc).update(area = area,  \
                mobile_no = mobile_no)
            User.objects.filter(email = user).update(first_name = first_name)
        except Exception,e:
            return Response(status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response(status.HTTP_200_OK)

class ActiveBookingMixin(object):
    #authentication_classes = [OAuth2Authentication]
    #permission_classes = (TokenHasScope,)
    #serializer_class = UserProfileSerializer
    #required_scopes = ['write','read']
    def get_queryset(self):
        return UserProfile.objects.filter(user_acc = self.request.user)

class GetActiveBookings(ActiveBookingMixin, ListAPIView):
    pass


class InviteUser(object):
    permission_classes = ()
    serializer_class = InviteUserSerializer
    queryset = UserInvites.objects.all()

class InviteUser(InviteUserMixin,ListCreateAPIView):
    pass