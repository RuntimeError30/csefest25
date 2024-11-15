from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(events)
admin.site.register(announcements)

admin.site.register(timeLine)
admin.site.register(prizeMoney)
admin.site.register(contactInfos)
admin.site.register(guidelines)
