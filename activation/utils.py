from .models import *
from datetime import datetime
from django.db.models import Q
from django.core.mail import EmailMessage, BadHeaderError, send_mail
from django.utils import timezone
import random
import string
import socket

def get_on_call_nurses():
    """
    Function which returns a dicitionary of phone number keys, and carrier values
    """
    on_call = {}
    nurses = Nurse.objects.all()
    schedules = Schedule.objects.all()

    for s in schedules:
        if timezone.now() > s.start_time and timezone.now() < s.end_time:
            nurse = list(s.nurse.all())[0]
            on_call[nurse.phone_num] =  nurse.get_phone_carrier_display()
    return on_call

def get_sms_email(on_call):
    CARRIER_DOMAINS = {
        "Telus" : "msg.telus.com",
        "Rogers": "pcs.rogers.com",
        "Bell": "txt.bell.ca",
        "Fido": "fido.ca",
        "Koodo": "msg.koodomobile.com,",
        "Virgin": "vmobile.ca",
        "Chatr": "pcs.rogers.com"
    }

    emails = []
    for number in on_call:
        emails.append("{}@{}".format(number, CARRIER_DOMAINS[on_call[number]]))
    return emails
    
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
