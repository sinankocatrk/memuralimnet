from django.contrib import admin

from kontenjan.models import *
from import_export.admin import ImportExportModelAdmin

@admin.register(S2021)

class VievAdmin(ImportExportModelAdmin):
    
    pass

