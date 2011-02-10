from django.db import models
from django.contrib.auth.models import User

from job.util.models import Audit

from job.client.models import Client
from job.data_management.models import SkillSet, Qualification

REQUIREMENTS_STATUS = (
    ('NEW', 'NEW'),
    ('ASSIGNED', 'ASSIGNED'),
    ('IN PROGRESS', 'IN PROGRESS'),
    ('PENDING', 'PENDING'),
    ('COMPLETED', 'COMPLETED'),
    ('CLOSED', 'CLOSED'),
)

class Requirement(Audit):
    title = models.CharField(max_length = 100)
    client = models.ForeignKey(Client)
    active = models.BooleanField(default = True)
    expires_at = models.DateField()
    status = models.CharField(max_length = 100, choices = REQUIREMENTS_STATUS, default = 'NEW')
    remarks = models.TextField()
    any_keywords = models.CharField(max_length = 100)
    all_keywords = models.CharField(max_length = 100)
    exclue_keywords = models.CharField(max_length = 100)
    total_experience_in_years = models.IntegerField()
    total_experience_in_months = models.IntegerField()
    annual_salary_lakhs_from  = models.IntegerField()
    annual_salary_thouands_to    = models.IntegerField()    
    annual_salary_lakhs_from  = models.IntegerField()
    annual_salary_thouands_to    = models.IntegerField()
    current_location = models.CharField(max_length = 50)    
    current_employer = models.CharField(max_length = 50)
    exclude_employer = models.CharField(max_length = 50)
    current_designation = models.CharField(max_length = 50)
    
    def __unicode__(self):
        return self.title
    
class RequirementsQualification(Audit):
    requirements = models.ForeignKey(Requirement)   
    qualification = models.ForeignKey(Qualification)

    def __unicode__(self):
        return self.qualification.name
    
    class Meta:
        verbose_name = 'Requirement Qualification'
        verbose_name_plural = 'Requirement Qualifications'        

    
class RequirementsSkillSet(Audit):
    requirements = models.ForeignKey(Requirement)
    skillset = models.ForeignKey(SkillSet)
    min_exp_in_years = models.IntegerField()
    min_exp_in_months = models.IntegerField()
    max_exp_in_years = models.IntegerField()
    max_exp_in_months = models.IntegerField()
    mandatory = models.BooleanField(default=True)
    
    def __unicode__(self):
        return self.skillset.name

    class Meta:
        verbose_name = 'Requirement Skill Set'
        verbose_name_plural = 'Requirement Skill Sets'        


class RequirementUserAssignment(Audit):
    requirement = models.ForeignKey(Requirement)
    user = models.ForeignKey(User)
    
    def __unicode__(self):
        return self.user.first_name
    
    class Meta:
        verbose_name = 'Requirement User Assignment'
        verbose_name_plural = 'Requirement User Assignments'        

    