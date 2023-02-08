from django.contrib import admin
from.models import Man_box,Woman_box,School
# Register your models here.
class BoxAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'create_time')
    list_filter = ('name', 'user')
    search_fields = ('name', 'user')
    ordering = ['user']
admin.site.register(Man_box,BoxAdmin)
admin.site.register(Woman_box,BoxAdmin)
admin.site.register(School)