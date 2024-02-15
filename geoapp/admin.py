from django.contrib import admin
from .models import MunDetail, StaffDetail, WardDetail, Demographic, Education, Occupation, DangPop
#for adding leaflet map on django admin
from leaflet.admin import LeafletGeoAdmin

# Register your models here.
admin.site.register(MunDetail)
admin.site.register(StaffDetail)
admin.site.register(WardDetail)
admin.site.register(Demographic)
admin.site.register(Education)
admin.site.register(Occupation)
admin.site.register(DangPop, LeafletGeoAdmin)