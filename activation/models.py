from django.db import models

# Create your models here.
class Activation_Message(models.Model):
    ESCALATION_LEVELS = (
        (0, "No escalation"),
        (1, "Repeat activation"),
        (2, "Contact coordinator"),
        (3, "Repeat coordinator"),
        (4, "Contact all regions")
    )
    
    msg_id = models.IntegerField()
    subject = models.CharField(max_length=200)
    region = models.CharField(max_length=200)
    content = models.CharField(max_length=200)
    sent_date = models.DateTimeField("Time sent")
    responded = models.BooleanField("Responded Success", default=False)
    
    verify_id = models.CharField(max_length=50)
    escalation_level = models.PositiveSmallIntegerField(choices = ESCALATION_LEVELS)

    def __str__(self):
        return str(self.msg_id)+"-"+str(self.sent_date)

class Response_Message(models.Model):
    response_id = models.IntegerField()
    activation = models.ManyToManyField(Activation_Message, related_name="activation")
    sent_date = models.DateTimeField("Time sent")
    location_coord = models.CharField(max_length=60)
    response_success = models.BooleanField("Response Success", default=False)
    response_message = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return str(self.response_id)+"-"+str(self.sent_date)

class Nurse(models.Model):
    CARRIER_CHOICES = (
        (1, "Telus"),
        (2, "Rogers"),
        (3, "Bell"),
        (4, "Fido"),
        (5, "Koodo"),
        (6, "Virgin"),
        (7, "Chatr")
    )

    REGION = (
        (1, "A - Port Hardy"),
        (2, "B - Campbell River"),
        (3, "C - Nanaimo"),
        (4, "D - Victoria")
    )
    
    nurse_id = models.IntegerField()
    user_id = models.CharField(max_length=50)
    first_name = models.CharField(max_length=200, default="", null=True, blank=True)
    last_name = models.CharField(max_length=200, default="", null=True, blank=True)
    phone_num = models.CharField(max_length=12)
    phone_carrier = models.PositiveSmallIntegerField(choices = CARRIER_CHOICES)
    region = models.PositiveSmallIntegerField(choices = REGION, null=True)
    
    associated_activations = models.ManyToManyField(Activation_Message, related_name="assoc_activations", blank=True)
    associated_responses = models.ManyToManyField(Response_Message, related_name="assoc_responses", blank=True)
                                        
    def __str__(self):
        return str(self.nurse_id)+"-"+str(self.first_name)+"-"+str(self.last_name)+"-"+str(self.

class Schedule(models.Model):
    shift_id = models.IntegerField()
    nurse = models.ManyToManyField(Nurse, related_name="nurse")
    start_time = models.DateTimeField("Shift start")
    end_time = models.DateTimeField("Shift end")

    def __str__(self):
        return str(self.shift_id)+"-"+str(list(self.nurse.all())[0])+"-"+str(self.start_time)+"-"+str(self.end_time)
