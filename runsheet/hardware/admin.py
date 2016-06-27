from django.contrib import admin

# Register your models here. You can manage the classes at http://127.0.0.1:8000/admin/

#username: admin
# email: wenjiao.wang1@gmail.com
#password: leopardary

from .models import DepChamber
from .models import FacePlate
from .models import UpperBlockerPlate
from .models import LowerBlockerPlate
from .models import PedestalHeater
from .models import TopTuner
from .models import BottomTuner
from .models import GasBox
from .models import OtherParts
##from .models import Wafer
##from .models import Foup_slot

class DepChamberAdmin(admin.ModelAdmin):
    list_display=["name","configure_start_time","configure_end_time"] #here you can add the attribute that you want to display on the admin page
    list_display_links=["configure_end_time"]   #add a link to a certain field, so that it can be updated by clicking and edit
    list_filter=["name","configure_start_time"] #filter for the content that you want to display on the page
    search_fields=["name","configure_start_time"]   #search for the objects according to fields
    list_editable=["name"]
    class Meta:
        model=DepChamber


admin.site.register(DepChamber,DepChamberAdmin)
admin.site.register(FacePlate)
admin.site.register(UpperBlockerPlate)
admin.site.register(LowerBlockerPlate)
admin.site.register(PedestalHeater)
admin.site.register(TopTuner)
admin.site.register(BottomTuner)
admin.site.register(GasBox)
admin.site.register(OtherParts)
##admin.site.register(Wafer)
##admin.site.register(Foup_slot)

