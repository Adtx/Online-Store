from django.contrib import admin
from django.contrib.auth.models import User
from .models import Costumer, Desktop, SmartPhone, Processor, Monitor, Keyboard, SSD, Router
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm

# Register your models here.

class CostumerChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = Costumer

class CostumerAdmin(UserAdmin):
    form = CostumerChangeForm

    fieldsets = (
        (None, {'fields': ('username', 'email', 'telephone', 'street', 'city', 'district', 'zipcode', 'country')}),
    )

class DesktopAdmin(admin.ModelAdmin):

    list_display = ('name','is_on_sale','is_bestseller','is_new','is_featured','price','d_processor', 'gpu', 'ram', 'storage', 'os', 'dimensions', 'weight')

class SmartPhoneAdmin(admin.ModelAdmin):

    list_display = ('name','is_on_sale','is_bestseller','is_new','is_featured','price','os','s_processor','storage','ram','display','camera','mobile_data','dimensions','weight')

class ProcessorAdmin(admin.ModelAdmin):

    list_display = ('name','is_on_sale','is_bestseller','is_new','is_featured','price','base_freq','turbo_freq','num_cores','num_threads','tdp','cache','socket')

class MonitorAdmin(admin.ModelAdmin):

    list_display = ('name','is_on_sale','is_bestseller','is_new','is_featured','price','size','aspect_ratio','resolution','response_time','conectivity','dimensions','weight')

class KeyboardAdmin(admin.ModelAdmin):

    list_display = ('name','is_on_sale','is_bestseller','is_new','is_featured','price','Layout','conectivity','dimensions','weight')

class SSDAdmin(admin.ModelAdmin):

    list_display = ('name','is_on_sale','is_bestseller','is_new','is_featured','price','Capacity','format','interface','seq_read_speed','seq_write_speed','random_read','random_write')

class RouterAdmin(admin.ModelAdmin):

    list_display = ('wireless_norm','is_on_sale','is_bestseller','is_new','is_featured','segment','data_rate','antena','segnal_freq','ports','dimensions')

#UserAdmin.list_display = ('username', 'email', 'is_staff')

#admin.site.unregister(User)
#admin.site.register(User, UserAdmin)
admin.site.register(Costumer, CostumerAdmin)
admin.site.register(Desktop, DesktopAdmin)
admin.site.register(SmartPhone, SmartPhoneAdmin)
admin.site.register(Processor, ProcessorAdmin)
admin.site.register(Monitor, MonitorAdmin)
admin.site.register(Keyboard, KeyboardAdmin)
admin.site.register(SSD, SSDAdmin)
admin.site.register(Router, RouterAdmin)
