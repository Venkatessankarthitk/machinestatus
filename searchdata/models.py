import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Question(models.Model):
    dns_name = models.CharField(max_length=200, null=True, unique=True, blank=True)
    ran_date = models.DateTimeField('ran date')
    assimilate_status= models.CharField(max_length=45)
    assimilate_error = models.CharField(max_length=200, null=True, blank=True)
    remeditor_status= models.CharField(max_length=45)
    remeditor_error = models.CharField(max_length=200, null=True, blank=True)
    report_status= models.CharField(max_length=45)
    report_error = models.CharField(max_length=200, null=True, blank=True)
    def __str__(self):
        return self.dns_name
    def __unicode__(self):
        return self.assimilate_status


