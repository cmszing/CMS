from django.db import models
from job.util.models import Audit

from job.data_management.models import City, Qualification, SkillSet, Company

class Candidate(Audit):
    name = models.CharField(max_length = 40, help_text = 'As per the Passport')
    reference = models.CharField(max_length = 40)
    sex = models.CharField(max_length = 5, choices = (('M', 'MALE'),('F','FEMALE')))
    total_experience = models.IntegerField(verbose_name = 'Total Experience (in years)')
    current_location = models.ForeignKey(City, related_name='current_city_%(class)s_set')
    current_job_type = models.CharField(max_length = 20, choices = (('P', 'Permanent'),('C','Contract')))
    current_ctc = models.BigIntegerField()
    expected_ctc = models.BigIntegerField()
    notice_period = models.IntegerField()
    cob = models.DateField(verbose_name='COB')
    cab = models.DateField(verbose_name='CAB')
    contract_interest = models.BooleanField(default = False)
    onsite_interest = models.BooleanField(default = False)
    passport_validity = models.DateField()
    native = models.CharField(max_length = 40)
    willing_to_relocate = models.BooleanField(default = False)
    where_to_relocate = models.ForeignKey(City, related_name='where_to_relocate_%(class)s_set')
    mobile_number = models.CharField(max_length = 20)
    alternate_contact_number = models.CharField(max_length = 20)
    email = models.EmailField()
    remarks = models.TextField()
    keywords = models.CharField(max_length = 100)
    placement_status = models.CharField(max_length = 25, choices = (('PLACED', 'PLACED'),('NOT PLACED','NOT PLACED')))
    
    def __unicode__(self):
        return self.name

class CandidateQualification(Audit):
    candidate = models.ForeignKey(Candidate)
    qualification = models.ForeignKey(Qualification)
    year_of_completion = models.IntegerField(help_text = "yyyy")
    percentage = models.DecimalField(decimal_places = 2, max_digits = 5)
    remarks = models.CharField(max_length = 200)
    
    def __unicode__(self):
        return self.qualification.name

    class Meta:
        verbose_name = 'Candidate Qualification'
        verbose_name_plural = 'Candidate Qualifications'        
        #db_table = 'app_mgmt_delivery_mode'    


class CandidateSkillSet(Audit):
    candidate = models.ForeignKey(Candidate)
    skillset =  models.ForeignKey(SkillSet)
    exp_in_years = models.IntegerField()
    exp_in_months = models.IntegerField()

    def __unicode__(self):
        return self.skillset.name
    
    class Meta:
        verbose_name = 'Candidate Skill Set'
        verbose_name_plural = 'Candidate Skill Sets'        
    
class CandidateHistory(Audit):
    candidate = models.ForeignKey(Candidate)
    company = models.ForeignKey(Company)
    join_date = models.DateField(null = True , blank = True)
    end_date = models.DateField(null = True , blank = True)
    current_employer = models.BooleanField()
    
    def __unicode__(self):
        return self.company.name
    
    class Meta:
        verbose_name = 'Candidate History'
        verbose_name_plural = 'Candidate Histories'        
    