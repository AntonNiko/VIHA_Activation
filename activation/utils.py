from .models import User, Activation_Message, Response_Message, Nurse, Coordinator
from django.db.models import Q
from django.core.mail import EmailMessage, BadHeaderError, send_mail
import random
import string
import socket

def load_user(request):
    if not request.user.is_authenticated:
        return redirect("/activation/login")

    print(request.user.username)
    user = User.objects.get(user_id = request.user.username)
    print(user.user_type)
    
def send_email(packet):
    email_addr = packet["email"]
    subject = packet["subject"]
    body = packet["body"]

    email = EmailMessage(subject, body, to=[email_addr])
    email.send()

def generate_verify_id():
    x = "".join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(10))
    return x

def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]
