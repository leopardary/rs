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

admin.site.register(DepChamber)
admin.site.register(FacePlate)
admin.site.register(UpperBlockerPlate)
admin.site.register(LowerBlockerPlate)
admin.site.register(PedestalHeater)
admin.site.register(TopTuner)
admin.site.register(BottomTuner)
admin.site.register(GasBox)
admin.site.register(OtherParts)


