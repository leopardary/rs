from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone
import datetime

#####################################################################################
#Chamber configuration and HW parts:

'''
HW module functions:
    1. Record Chamber configuration as a function of time. Every time there is any change of HW in the chamber, the DepChamber will have a new record, with the new configuration starting time, and also update the ending time for the original configuration record.
    2. Record the chamber parts (as an abstract class), with
        -its name (currently having the parts for ON precision chamber, including faceplate, upperblockerplate, lowerblockerplate, pedestalheater, gasbox, toptuner, bottomtuner, and other parts. Other parts is for some special parts that does not belong to any category of the list above.)
        -brief discription
        -serial number
    3. For each individual part category (inheritance from the abstract ChamParts model), custom field can be added.
    4. Functionwise, each time there is any change in the HW configuration, it will create a new entry according to the updated configurations, and record the starting time. At the same time, record the ending time of the previous configuration entry.

'''

class ChamParts(models.Model):
    Parts=(
        ('FP','FacePlate'),
        ('UBP','Upper BlockerPlate'),
        ('LBP', 'Lower BlockerPlate'),
        ('HTR', 'Pedestal Heater'),
        ('GB', 'GasBox'),
        ('TT', 'Top Tuner'),
        ('BT', 'Bottom Tuner'),
        ('OTH', 'Other'),
    )
    category=models.CharField(max_length=3, choices=Parts)
    discription=models.CharField(max_length=300)
    serial_number=models.CharField(max_length=50)
    entry_time=models.DateTimeField(default=timezone.localtime(timezone.now()))
    #same as models.DateTimeField(auto_now=True,auto_now_add=False)
    class Meta:
        abstract=True

class FacePlate(ChamParts):
    name=models.CharField(max_length=20,default="BKM FacePlate")
    def save(self, *args, **kwargs):
        if self.category=='FP':
            self.entry_time=timezone.now()
            super(FacePlate,self).save(*args,**kwargs)

        else:
            print("Wrong Parts category. Should be \'FP\', instead of \'%s\'." % self.category)
            return
    def __str__(self):
        return self.name

class UpperBlockerPlate(ChamParts):
    name=models.CharField(max_length=20,default="BKM UpperBlockerPlate")
    def save(self, *args, **kwargs):
        if self.category=='UBP':
            self.entry_time=timezone.now()
            super(UpperBlockerPlate,self).save(*args,**kwargs)

        else:
            print("Wrong Parts category. Should be \'UBP\', instead of \'%s\'." % self.category)
            return
    def __str__(self):
        return self.name

class LowerBlockerPlate(ChamParts):
    name=models.CharField(max_length=20,default="BKM LowerBlockerPlate")
    def save(self, *args, **kwargs):
        if self.category=='LBP':
            self.entry_time=timezone.now()
            super(LowerBlockerPlate,self).save(*args,**kwargs)

        else:
            print("Wrong Parts category. Should be \'LBP\', instead of \'%s\'." % self.category)
            return
    def __str__(self):
        return self.name

class PedestalHeater(ChamParts):
    name=models.CharField(max_length=20,default="BKM PedestalHeater")
    def save(self, *args, **kwargs):
        if self.category=='HTR':
            self.entry_time=timezone.now()
            super(PedestalHeater,self).save(*args,**kwargs)

        else:
            print("Wrong Parts category. Should be \'HTR\', instead of \'%s\'." % self.category)
            return
    def __str__(self):
        return self.name

class GasBox(ChamParts):
    name=models.CharField(max_length=20,default="BKM GasBox")
    def save(self, *args, **kwargs):
        if self.category=='GB':
            self.entry_time=timezone.now()
            super(GasBox,self).save(*args,**kwargs)

        else:
            print("Wrong Parts category. Should be \'GB\', instead of \'%s\'." % self.category)
            return
    def __str__(self):
        return self.name

class TopTuner(ChamParts):
    name=models.CharField(max_length=20,default="BKM TopTuner") #this is the shown name of the part, eg. CIP TopTuner
    def save(self, *args, **kwargs):
        if self.category=='TT':
            self.entry_time=timezone.now()
            super(TopTuner,self).save(*args,**kwargs)

        else:
            print("Wrong Parts category. Should be \'TT\', instead of \'%s\'." % self.category)
            return
    def __str__(self):
        return self.name

class BottomTuner(ChamParts):
    name=models.CharField(max_length=20,default="BKM BottomTuner")
    def save(self, *args, **kwargs):
        if self.category=='BT':
            self.entry_time=timezone.now()
            super(BottomTuner,self).save(*args,**kwargs)

        else:
            print("Wrong Parts category. Should be \'BT\', instead of \'%s\'." % self.category)
            return
    def __str__(self):
        return self.name

class OtherParts(ChamParts):
    name=models.CharField(max_length=20,default="BKM OtherParts")
    def save(self, *args, **kwargs):
        if self.category=='OTH':
            self.entry_time=timezone.now()
            super(OtherParts,self).save(*args,**kwargs)

        else:
            print("Wrong Parts category. Should be \'OTH\', instead of \'%s\'." % self.category)
            return
    def __str__(self):
        return self.name

class DepChamber(models.Model):
    #one chamber is only one side, eg. GT7A1 and GT7A2 are seperate instances.
    name=models.CharField(max_length=200)
    configure_start_time=models.DateTimeField('Configuration starting time', default=timezone.now())
    configure_end_time=models.DateTimeField('Configuration end time',blank=True,null=True)
    #the HW configuration change time
    fp=models.ForeignKey(FacePlate, on_delete=models.CASCADE,verbose_name="the installed FacePlate") # the relation is 1-to-1, as one chamber has only one of each part, and each part
    ubp=models.ForeignKey(UpperBlockerPlate, on_delete=models.CASCADE,verbose_name="the installed Upper BlockerPlate")
    lbp=models.ForeignKey(LowerBlockerPlate, on_delete=models.CASCADE,verbose_name="the installed Lower BlockerPlate")
    htr=models.ForeignKey(PedestalHeater,on_delete=models.CASCADE,verbose_name="the installed PedestalHeater")
    gb=models.ForeignKey(GasBox,on_delete=models.CASCADE,verbose_name="the installed GasBox")
    tt=models.ForeignKey(TopTuner,on_delete=models.CASCADE,verbose_name="the installed TopTuner")
    bt=models.ForeignKey(BottomTuner,on_delete=models.CASCADE,verbose_name="the installed BottomTuner")
    #one chamber can have multiple other parts, so this is a foreign key relationship.
    oth=models.ForeignKey(OtherParts,on_delete=models.CASCADE,verbose_name="the installed other parts")

    # for initial chamber configuration, the first entry, just save.
    def save_first_record(self, *args, **kwargs):
        super(DepChamber, self).save(*args, **kwargs)

    def has_previous_record(self, *args, **kwargs):
        chamhistory=DepChamber.objects.filter(name=self.name)
        if len(chamhistory)==0:
            return False
        else:
            return True

    def most_recent_entry(self):
        chamhistory=DepChamber.objects.filter(name=self.name).order_by('-configure_start_time')
        return chamhistory[0]

    def save(self, *args, **kwargs):
        if self.has_previous_record():
            self.configure_start_time=timezone.now()
            most_recent=self.most_recent_entry()
            most_recent.configure_end_time=timezone.now()
            super(DepChamber,most_recent).save(*args,**kwargs)
            super(DepChamber,self).save(*args,**kwargs)

        else:
            self.configure_start_time=timezone.now()
            self.save_first_record()
    def __str__(self):
        return self.name







