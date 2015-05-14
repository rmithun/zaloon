
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
from django.http import HttpResponseRedirect

#application imports

@login_required
def home(request):

	return render(request,'user_accounts/home.html',{})

@login_required
def logout_view(request):
  auth.logout(request)
  # Redirect to a success page.
  return HttpResponseRedirect("/")