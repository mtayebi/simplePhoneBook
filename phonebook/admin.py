from django.contrib import admin
from phonebook.models import Contact


# Register Contact model
class ContactAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'phone_number', 'email']
    search_fields = ['first_name', 'last_name', 'phone_number']


admin.site.register(Contact, ContactAdmin)
