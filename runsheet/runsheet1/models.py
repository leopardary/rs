from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone
import datetime

# Create your models here.

class DepChamber(models.Model):
    name=models.CharField(max_length=200)
    starttime=models.DateTimeField('Configuration change time')
    #the HW configuration change time
    S1GasBox=models.CharField(max_length=200)
    S2GasBox=models.CharField(max_length=200)
    #including name, discription, serial numbers etc. Should be changed to customized class, which contains name, description, and serial number.
