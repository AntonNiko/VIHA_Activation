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
        return str(self.user_id)+"-"+str(self.user_type)

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
        return str(self.msg_id)+"-"+str(self.sent_date)

class Response_Message(models.Model):
    response_id = models.IntegerField()
    sent_date = models.DateTimeField("Time sent")
    location_coord = models.CharField(max_length=60)

    def __str__(self):
        return str(self.response_id)+"-"+str(self.sent_date)

class Nurse(models.Model):
    nurse_id = models.IntegerField()
    first_name = models.CharField(max_length=200, default="", null=True, blank=True)
    last_name = models.CharField(max_length=200, default="", null=True, blank=True)
    phone_num = models.CharField(max_length=12)
    phone_carrier = models.CharField(max_length=12)
    
    associated_activations = models.ManyToManyField(Activation_Message, related_name="assoc_activations")
    associated_responses = models.ManyToManyField(Response_Message, related_name="assoc_responses")
                                        
    def __str__(self):
        return str(self.nurse_id)+"-"+str(self.first_name)+"-"+str(self.last_name)

class Coordinator(models.Model):
    coordinator_id = models.IntegerField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return str(self.coordinator_id)+"-"+str(self.first_name)+"-"+str(self.last_name)
