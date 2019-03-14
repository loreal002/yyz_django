from django.contrib import admin
from .models import Event,Guest

import os
print(os.getcwd())
# Register your models here.
class EventAdmin(admin.ModelAdmin):
    list_display = ['name', 'status', 'start_time','id']
    search_fields = ['name'] #搜索栏
    list_filter = ['status'] #过滤器

class GuestAdmin(admin.ModelAdmin):
    list_display = ['realname', 'phone','email','sign','create_time','event']
    search_fields = ['realname','phone'] #搜索栏
    list_filter = ['sign'] #过滤器

# admin.site.register(Event)
#
# admin.site.register(Guest)

admin.site.register(Event,EventAdmin)
admin.site.register(Guest,GuestAdmin)