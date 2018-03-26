from django.contrib import admin
from django.contrib.auth.models import User
from .models import Costumer
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

#UserAdmin.list_display = ('username', 'email', 'is_staff')

#admin.site.unregister(User)
#admin.site.register(User, UserAdmin)
admin.site.register(Costumer, CostumerAdmin)
