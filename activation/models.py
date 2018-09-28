from django.db import models

# Create your models here.
class User(models.Model):
    USER_TYPE_CHOICES = (
        (1, "Nurse"),
        (2, "Coordinator"),
    )
    user_id = models.CharField(max_length=50)
    user_type = models.PositiveSmallIntegerField(choices = USER_TYPE_CHOICES)

    def __str__(self):
        return str(user_id)+"-"+str(user_type)

class Activation_Message(models.Model):
    msg_id = models.IntegerField()
    subject = models.CharField(max_length=200)
    region = models.CharField(max_length=200)
    content = models.CharField(max_length=200)
    sent_date = models.DateTimeField("Time sent")
    sent_success = models.BooleanField("Sent Success", default=False)
    
    verify_id = models.CharField(max_length=50)
    escalation_level = models.IntegerField()

    def __str__(self):
        return str(msg_id)+"-"+str(sent_date)

class Response_Message(models.Model):
    response_id = models.IntegerField()
    sent_date = models.DateTimeField("Time sent")
    location_coord = models.CharField(max_length=60)

    def __str__(self):
        return str(response_id)+"-"+str(sent_date)

class Nurse(models.Model):
    nurse_id = models.IntegerField()
    first_name = models.CharField(max_length=200, default="", null=True, blank=True)
    last_name = models.CharField(max_length=200, default="", null=True, blank=True)
    
    associated_activations = models.ManyToManyField(Activation_Message, related_name="assoc_activations")
    associated_responses = models.ManyToManyField(Response_Message, related_name="assoc_responses")
                                        
    def __str__(self):
        return str(nurse_id)+"-"+str(first_name)+"-"+str(last_name)

class Coordinator(models.Model):
    coordinator_id = models.IntegerField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return "msg"
