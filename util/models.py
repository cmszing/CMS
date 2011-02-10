from django.db import models
from django.contrib.auth.models import User

class Audit(models.Model):
    created_by = models.ForeignKey(User, related_name='created_%(class)s_set', null=True, blank=True, verbose_name = "Created By")
    modified_by = models.ForeignKey(User, related_name='updated_%(class)s_set', null=True, blank=True, verbose_name = "Modified By")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name = "Created At", null=True, blank=True)
    modified_at = models.DateTimeField(auto_now=True, verbose_name = "Last Modified At", null=True, blank=True)
  
    def send_notification_mail(self):
        return False; 

    class Meta:
        abstract = True
        
