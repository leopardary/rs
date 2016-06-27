from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone
import datetime

#Wafer class contains foreign key to "pre-measurement" and "post_measurement"
class Wafer(models.Model):
	Types=(
		('RCL', 'Reclaimed Wafer'),
		('MEC', 'Mechanical Grade Wafer'),
		('PTC', 'Particle Grade Wafer'),
		('LRP', 'Low-Resistivity Particle Grade Wafer')
	)
	wafer_type=models.CharField(max_length=3,choices=Types)
	is_used=models.BooleanField(default=False)
	foup_slot=models.ForeignKey('Foup_slot',on_delete=models.SET_NULL,blank=True,null=True)
	def set_foup_slot_null(self):
		self.foup_slot=None
		self.save()
		return
	def set_foup_slot(self, foup_slot):
		self.foup_slot=foup_slot
		self.save()
		return
	def set_used(self):
		self.is_used=True
		self.save()
		return
	def __str__(self):
		if self.is_used:
			return self.wafer_type+'\t'+'used'
		else:
			return self.wafer_type+'\t'+'new'
			
			
class Foup_slot(models.Model):
	foup=models.CharField(max_length=100)
	Slots=(
		('1', 'Slot 1'),
		('2', 'Slot 2'),
		('3', 'Slot 3'),
		('4', 'Slot 4'),
		('5', 'Slot 5'),
		('6', 'Slot 6'),
		('7', 'Slot 7'),
		('8', 'Slot 8'),
		('9', 'Slot 9'),
		('10', 'Slot 10'),
		('11', 'Slot 11'),
		('12', 'Slot 12'),
		('13', 'Slot 13'),
		('14', 'Slot 14'),
		('15', 'Slot 15'),
		('16', 'Slot 16'),
		('17', 'Slot 17'),
		('18', 'Slot 18'),
		('19', 'Slot 19'),
		('20', 'Slot 20'),
		('21', 'Slot 21'),
		('22', 'Slot 22'),
		('23', 'Slot 23'),
		('24', 'Slot 24'),
		('25', 'Slot 25'),
	)
	slot=models.CharField(max_length=2,choices=Slots)
	def __str__(self):
		return (self.foup +" Slot "+self.slot)
	def all_slots_inFoup(self):
		#return all slots in the same foup with the self slot
		return Foup_slot.objects.filter(foup=self.foup)
	def corresponding_wafer(self):
		return self.wafer_set.all()
	
	def reclaim(self):
		corresponding_wafer=self.corresponding_wafer()
		if len(corresponding_wafer)==0:
			print ("No wafer in this slot %s" %(self.foup+'  S'+self.slot))
			return
		else:
			if len(corresponding_wafer)>1:
				print ("ERROR: multiple wafers set to this slot: %s" %(self.foup + ' S'+self.slot))
				return
			else:
				corresponding_wafer[0].set_foup_slot_null()
				print ("%s wafer is successfully reclaimed. Now the slot is vacant." %(self.foup + ' S'+self.slot))
				return
	def load_new_wafer(self,wafer_type):
		corresponding_wafer=self.corresponding_wafer()
		if len(corresponding_wafer)!=0:
			print ("There is wafer in this slot: %s. Please reclaim it firstly." %(self.foup + ' S'+self.slot))
			return
		else:
			wafer=Wafer(wafer_type=wafer_type)
			wafer.set_foup_slot(self)
			return
			
			#Foup_slot.wafer_set.all()	retrieve the wafer at this slot.
	@classmethod
	def all_slots(cls,foup_name):
		#return all slots in the foup given in the foup_name
		return cls.objects.filter(foup=foup_name)
	@classmethod
	def all_available_slots(cls):
		return cls.objects.filter(wafer__is_used=False)
	@classmethod
	def all_available_slots_in_foup(cls, foup_name):
	
		return cls.objects.filter(wafer__is_used=False).filter(wafer__foup_slot__foup=foup_name)
	@classmethod
	def all_slots_in_foup(cls, foup_name):
	
		return cls.objects.filter(wafer__foup_slot__foup=foup_name)
	@classmethod
	def num_available_slots_in_foup(cls, foup_name):
		slots=cls.all_available_slots_in_foup(foup_name)
		return len(slots)
	@classmethod	
	def all_slots_used_in_foup(cls, foup_name):
		if cls.num_available_slots_in_foup(foup_name)==0:
			return True
		else:
			return False
	@classmethod
	def reclaim_all_slots_in_foup(cls,foup_name):
		#reclaim all wafers inside the given foup
		slots=cls.all_slots_in_foup(foup_name)
		for slot in slots:
			slot.reclaim()
		return
	@classmethod
	def foup_vacant(cls,foup_name):
		slots=cls.all_slots(foup_name)
		for slot in slots:
			if len(slot.corresponding_wafer())!=0:
				return False
			else:
				return True
	@classmethod			
	def load_all_slots_in_foup(cls,foup_name,wafer_type):
		if not cls.foup_vacant(foup_name):
			print "%s is not vacant" % foup_name
			return
		else:
			for slot in slots:
				slot.load_new_wafer(wafer_type)
			return
			
		
		
	
	
	
	# S1=models.OneToOneField(Wafer, on_delete=models.SET_NULL,blank=True,null=True,verbose_name="Slot 1")
	# S2=models.OneToOneField(Wafer, on_delete=models.SET_NULL,blank=True,null=True,verbose_name="Slot 2")
	# S3=models.OneToOneField(Wafer, on_delete=models.SET_NULL,blank=True,null=True,verbose_name="Slot 3")
	# S4=models.OneToOneField(Wafer, on_delete=models.SET_NULL,blank=True,null=True,verbose_name="Slot 4")
	# S5=models.OneToOneField(Wafer, on_delete=models.SET_NULL,blank=True,null=True,verbose_name="Slot 5")
	# S6=models.OneToOneField(Wafer, on_delete=models.SET_NULL,blank=True,null=True,verbose_name="Slot 6")
	# S7=models.OneToOneField(Wafer, on_delete=models.SET_NULL,blank=True,null=True,verbose_name="Slot 7")
	# S8=models.OneToOneField(Wafer, on_delete=models.SET_NULL,blank=True,null=True,verbose_name="Slot 8")
	# S9=models.OneToOneField(Wafer, on_delete=models.SET_NULL,blank=True,null=True,verbose_name="Slot 9")
	# S10=models.OneToOneField(Wafer, on_delete=models.SET_NULL,blank=True,null=True,verbose_name="Slot 10")
	# S11=models.OneToOneField(Wafer, on_delete=models.SET_NULL,blank=True,null=True,verbose_name="Slot 11")
	# S12=models.OneToOneField(Wafer, on_delete=models.SET_NULL,blank=True,null=True,verbose_name="Slot 12")
	# S13=models.OneToOneField(Wafer, on_delete=models.SET_NULL,blank=True,null=True,verbose_name="Slot 13")
	# S14=models.OneToOneField(Wafer, on_delete=models.SET_NULL,blank=True,null=True,verbose_name="Slot 14")
	# S15=models.OneToOneField(Wafer, on_delete=models.SET_NULL,blank=True,null=True,verbose_name="Slot 15")
	# S16=models.OneToOneField(Wafer, on_delete=models.SET_NULL,blank=True,null=True,verbose_name="Slot 16")
	# S17=models.OneToOneField(Wafer, on_delete=models.SET_NULL,blank=True,null=True,verbose_name="Slot 17")
	# S18=models.OneToOneField(Wafer, on_delete=models.SET_NULL,blank=True,null=True,verbose_name="Slot 18")
	# S19=models.OneToOneField(Wafer, on_delete=models.SET_NULL,blank=True,null=True,verbose_name="Slot 19")
	# S20=models.OneToOneField(Wafer, on_delete=models.SET_NULL,blank=True,null=True,verbose_name="Slot 20")
	# S21=models.OneToOneField(Wafer, on_delete=models.SET_NULL,blank=True,null=True,verbose_name="Slot 21")
	# S22=models.OneToOneField(Wafer, on_delete=models.SET_NULL,blank=True,null=True,verbose_name="Slot 22")
	# S23=models.OneToOneField(Wafer, on_delete=models.SET_NULL,blank=True,null=True,verbose_name="Slot 23")
	# S24=models.OneToOneField(Wafer, on_delete=models.SET_NULL,blank=True,null=True,verbose_name="Slot 24")
	# S25=models.OneToOneField(Wafer, on_delete=models.SET_NULL,blank=True,null=True,verbose_name="Slot 25")



	
	#Foup just stores the current information of the slots and references to the current wafers.
	#wafer just stores the type, and whether the wafer is new or used. Used means it has been deped. Pre-measurement does not change this attribute.
	
	
	#pre_measurement=models.ForeignKey(Measurement, on_delete=models.CASCADE, blank=True, null=True, verbose_name="pre-measurement")
	#post_measurement=models.ForeignKey(Measurement, on_delete=models.CASCADE, blank=True, null=True, verbose_name="post-measurement")
	
# class Measurement(models.Model):
	# wafer=models.ForeignKey(Wafer,on_delete=models.CASCADE)
	
	