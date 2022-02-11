from django.contrib import admin
from activate.models import Activate

class ActivateAdmin(admin.ModelAdmin):
  pass

admin.site.register(Activate,ActivateAdmin)
