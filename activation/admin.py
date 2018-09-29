from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(User)
admin.site.register(Activation_Message)
admin.site.register(Response_Message)
admin.site.register(Nurse)
admin.site.register(Coordinator)
admin.site.register(Schedule)
