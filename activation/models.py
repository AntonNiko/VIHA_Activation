from django.db import models

# Create your models here.
class User(models.Model):
    USER_TYPE_CHOICES = (
        (1, "Nurse"),
        (2, "Coordinator"),
    )
    user_type = models.PositiveSmallIntegerField(choices = USER_TYPE_CHOICES)


class Nurse(models.Model):
    nurse_id = models.IntegerField()

class Message(models.Model):
    msg_id = models.IntegerField()
    sent_date = models.DateTimeField("Time sent")
    escalation_level = models.IntegerField()

    def __str__(self):
        return "msg"

class Coordinator(models.Model):
    coordinator_id = models.IntegerField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return "msg"

class EscalationLevel(models.Model):
    def __str__(self):
        return "msg"
    
