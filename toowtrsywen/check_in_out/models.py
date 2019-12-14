from django.db import models
from datetime import datetime

# Create your models here.
class CheckTime(models.Model):
    name_text = models.CharField(max_length=200,default = "",verbose_name="Name", blank=False)
    in_or_out = models.CharField(max_length=20,choices = [('in','checkin'),('out','checkout'),],verbose_name="Check in or out")
    timestamp = models.DateTimeField(auto_now=False,auto_now_add=True)
    def __str__(self):
        return  self.name_text + " " + self.in_or_out + " " + self.timestamp.strftime("%m/%d/%Y, %H:%M:%S")