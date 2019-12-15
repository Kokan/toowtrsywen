from django.db import models
from datetime import datetime
# Create your models here.
class HomeOfficeRequest(models.Model):
    name = models.CharField(max_length=200,default = "",verbose_name="Name", blank=False)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    approval_status = models.CharField(max_length=100,choices = [('pending','Request pending'),('approved','Request approved'),('declined','Request declined')],verbose_name="Approval Status")
    def __str__(self):
        return  self.name + " " + self.start_time.strftime("%m/%d/%Y, %H:%M:%S") + " " + self.end_time.strftime("%m/%d/%Y, %H:%M:%S") + " " + self.approval_status