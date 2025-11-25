from django.contrib import admin
from django.contrib.auth.models import Group

from .models import Donation, User

admin.sites.AdminSite.site_title = 'مدیریت سایت'
admin.sites.AdminSite.site_header = 'مدیریت سایت'
admin.sites.AdminSite.index_title = 'وبلاگ'

admin.site.unregister(Group)
admin.site.register(User)

@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    list_display = ['user', 'donation_type', 'donation_amount']
    list_display_links = ['user', 'donation_type']
    ordering = ("-time_created", "time_update")
    list_filter = ("time_created",)
    search_fields = ("user", "donation_amount")