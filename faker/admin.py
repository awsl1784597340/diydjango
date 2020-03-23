from django.contrib import admin

# Register your models here.
from django.contrib import admin


from django.contrib import admin
from .models import Servant


class ServantAdmin(admin.ModelAdmin):
    list_display = ('No', 'name', 'classname', 'nickname', 'gender')
    list_display_links = ('No',)


admin.site.register(Servant, ServantAdmin)