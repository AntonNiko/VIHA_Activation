from django import forms
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.core.mail import EmailMessage, BadHeaderError, send_mail
from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.utils import timezone

from .utils import *
from .models import *
import random

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return redirect("/activation/dashboard")
    
    context = {}
    return render(request, "activation/index.html", context)

def dashboard(request):
    if not request.user.is_authenticated:
        return redirect("/activation/login")
    
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

def respond_to_request(request, activation_id, verify_id):
    activation_obj = Activation_Message.objects.get(msg_id = activation_id)
    if activation_obj.verify_id != verify_id:
        return redirect("/activation/dashboard")
    
    context = {"verify_id":verify_id}
    return render(request, "activation/response_api.html", context)

def response_handle(request, verify_id):
    ## Redirect user if not POST, since consistent with form submission
    if request.method != "POST":
        return redirect("/activation/login")
    if request.user.is_authenticated:
        return redirect("/activation/dashboard")

    post_data = dict(request.POST.items())
    if "activation_responding" in list(post_data.keys()):
        response_obj = Response_Message.objects.create(
            response_id = random.randrange(10000),
            sent_date = timezone.now(),
            location_coord = "NA",
            response_success = True
        )
        response_obj.save()
        response_obj.activation.add(Activation_Message.objects.get(verify_id=verify_id))
    elif "activation_warning" in list(post_data.keys()):
        response_obj = Response_Message.objects.create(
            response_id = random.randrange(10000),
            sent_date = timezone.now(),
            location_coord = "NA",
            response_success = False,
            response_message = post_data["activation_warning"]
        )
        response_obj.save()
        response_obj.activation.add(Activation_Message.objects.get(verify_id=verify_id))
    ## Generate Reponse_Message object that will link to Activation_Message object
    return redirect("/activation/dashboard")

def send_activation(request):
    post_data = dict(request.POST.items())
    subject = "ACTIVATION ALERT"
    region = post_data["region"]
    content = post_data["content"]

    activation_id = random.randrange(10000)
    verify_id = generate_verify_id()
    ## Register new Activation object to database
    activation_obj = Activation_Message.objects.create(
        msg_id = activation_id,
        subject = subject,
        region = post_data["region"],
        content = content,
        sent_date = timezone.now(), ## Current time which activation was sent
        sent_success = False,
        verify_id = verify_id,
        escalation_level = 0
    )
    activation_obj.save()

    ## Fetch on-call nurses
    on_call_emails = get_sms_email(get_on_call_nurses())
    ## Create link for nurses to follow to respond to activation
    response_link = "<http://{}/activation/respond/{}/{}>".format(get_ip_address(), activation_id, verify_id)

    for email in on_call_emails:
        packet = {
            "email":email,
            "subject":content,
            "body":"Region: {}\n Content: {} \n To respond, follow link: {}".format(region, content, response_link)
        }
        print("Sent to email: {}".format(email))
        send_email(packet)
    return redirect("/activation/actions/")



def logout_user(request):
    logout(request)
    return redirect("/activation/login")
