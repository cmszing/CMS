from django.db import models

from job.util.models import Audit

class SkillSetCategory(Audit):
    name = models.CharField(max_length = 30)
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Skill Set Category'        
        verbose_name_plural = 'Skill Set Categories'

    
class SkillSet(Audit):
    category = models.ForeignKey(SkillSetCategory)
    name = models.CharField(max_length = 30)
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Skill Set'        
        verbose_name_plural = 'Skill Sets'


    
class Qualification(Audit):
    name = models.CharField(max_length = 20)
    
    def __unicode__(self):
        return self.name    
    
class City(Audit):
    name = models.CharField(max_length = 20)
    
    def __unicode__(self):
        return self.name    
    
    class Meta:
        verbose_name_plural = 'Cities'        
    
    
class Company(Audit):
    name = models.CharField(max_length = 20)
    
    def __unicode__(self):
        return self.name    
    
    class Meta:
        verbose_name_plural = 'Companies'        
    