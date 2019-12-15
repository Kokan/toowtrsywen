from django.db import models

# Create your models here.
class ManagerWorkers(models.Model):
    manager_name = models.CharField(max_length=200,default = "",verbose_name="Manager Name", blank=False)
    worker_name = models.CharField(max_length=200,default = "",verbose_name="Worker Name", blank=False)
    def __str__(self):
        return  self.worker_name + " works for  " + self.manager_name 
