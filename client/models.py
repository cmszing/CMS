from django.db import models

from job.util.models import Audit

# Create your models here.
class Client(Audit):
    name = models.CharField(max_length = 50)
    address = models.TextField(null = True, blank = True)
    contact_name = models.CharField(max_length = 50)
    contact_email = models.EmailField()
    contact_number = models.CharField(max_length = 15)
    active = models.BooleanField(default = True)
    
    def __unicode__(self):
        return self.name