from django import forms
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.core.mail import EmailMessage, BadHeaderError, send_mail
from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.utils import timezone

from .utils import *

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return redirect("/activation/dashboard")
    
    context = {}
    return render(request, "activation/index.html", context)

def dashboard(request):
    if not request.user.is_authenticated:
        return redirect("/activation/login")

    ## Register user sccording to their class, and display relevant information
    load_user(request)
    
    context = {}
    return render(request, "activation/dashboard.html", context)

## Login request (no HTML code visual)
def login_user(request):
    ## Redirect user if not POST, since consistent with a form submission
    if request.method != "POST":
        return redirect("/activation/login")
    if request.user.is_authenticated:
        return redirect("/activation/dashboard")

    ## Fetch the information sent by the login form, in the POST request
    post_data = dict(request.POST.items())
    username = post_data["username"]
    password = post_data["password"]

    ## Authenticate user details
    user = authenticate(request, username=username, password=password)
    if user is not None:
        ## Successful authentication, and login user to access their accounts
        login(request, user)
        response = redirect("/activation/dashboard")
        return response
    else:
        ## Append error message to request in order to show user in case no matches found in database
        messages.add_message(request, messages.ERROR, """No accounts found under current login. If you
                             feel that this is an error, please contact us as soon as possible so we
                             can help you out.""")
        return redirect("/activation/login")

def actions(request):
    context = {}
    return render(request, "activation/actions.html", context)

def respond_to_request(request, verify_id):
    ## TODO: Verify that ID is valid
    
    context = {}
    return render(request, "activation/response_api.html", context)

def response_handle(request):
    return HttpResponse("Registered...")

def send_activation(request):
    post_data = dict(request.POST.items())
    subject = "ACTIVATION ALERT"
    region = post_data["region"]
    content = post_data["content"]


    ## Register new Activation
    
    packet = {
        "email":"2508866514@msg.telus.com",
        "subject":subject,
        "body":"Region: {}\n Content: {}".format(region,content)
    }
    send_email(packet)
    return redirect("/activation/actions/")

def logout_user(request):
    logout(request)
    return redirect("/activation/login")
