from django.contrib import admin
from django.contrib.auth.models  import User

from job.util.admin import AuditAdmin, AuditInlineAdmin

from job.client.models import Client

class ClientAdmin(AuditAdmin):
    list_display = ('name', 'address', 'contact_name', 'contact_email', 'contact_number', 'active', )   + AuditAdmin.list_display

admin.site.register(Client, ClientAdmin)
