from django.contrib import admin
from django.http import Http404

class MyAdminSite(admin.AdminSite):
    site_header = 'Store Administration'

    def login(self, request, extra_context=None):
        if request.user.is_authenticated:
            if not request.user.is_staff and not request.user.is_superuser:
                raise Http404
        else:
            raise Http404
        return AdminSite.login(self, request)