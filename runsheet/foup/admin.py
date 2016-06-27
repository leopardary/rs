from django.contrib import admin

# Register your models here.

from .models import Wafer
from .models import Foup_slot

admin.site.register(Wafer)
admin.site.register(Foup_slot)