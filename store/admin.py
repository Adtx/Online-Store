from django.contrib import admin
from online_store.admin import MyAdminSite
from django.contrib.admin import sites
from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import GroupAdmin
from .models import Costumer, Desktop, SmartPhone, Processor, Monitor, Keyboard, SSD, Router
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.utils.translation import gettext, gettext_lazy as _

class CostumerChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = Costumer

# class CostumerCreationForm(UserCreationForm):
#     class Meta(UserCreationForm.Meta):
#         model = Costumer
#         fields = '__all__'

class CostumerAdmin(UserAdmin):
    form = CostumerChangeForm
    #add_form = CostumerCreationForm

    # fieldsets = (
    #     (None, {'fields': ('username', 'email', 'telephone', 'street', 'city', 'district', 'zipcode', 'country')}),
    # )

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('email', 'telephone', 'street', 'city', 'district', 'zipcode', 'country')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
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

mysite = MyAdminSite(name='myadmin')
# admin.site = mysite
# sites.site = mysite

mysite.register(Costumer, CostumerAdmin)
mysite.register(Desktop, DesktopAdmin)
mysite.register(SmartPhone, SmartPhoneAdmin)
mysite.register(Processor, ProcessorAdmin)
mysite.register(Monitor, MonitorAdmin)
mysite.register(Keyboard, KeyboardAdmin)
mysite.register(SSD, SSDAdmin)
mysite.register(Router, RouterAdmin)
mysite.register(Group, GroupAdmin)