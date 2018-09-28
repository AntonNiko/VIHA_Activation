from .models import User, Activation_Message, Response_Message, Nurse, Coordinator
from django.db.models import Q
from django.core.mail import EmailMessage, BadHeaderError, send_mail


def load_user(request):
    if not request.user.is_authenticated:
        return redirect("/activation/login")

def send_email(packet):
    email_addr = packet["email"]
    subject = packet["subject"]
    body = packet["body"]

    email = EmailMessage(subject, body, to=[email_addr])
    email.send()
