from django.contrib import admin
from django.contrib.auth.models  import User

from job.util.admin import AuditAdmin, AuditInlineAdmin

from job.candidate.models import Candidate, CandidateHistory, CandidateQualification, CandidateSkillSet
from job.data_management.models import Qualification, SkillSet, SkillSetCategory, City, Company

class CandidateHistoryInline(AuditInlineAdmin):
    model = CandidateHistory
    extra = 0

class  CandidateQualificationInline(AuditInlineAdmin):
    model =  CandidateQualification
    extra = 0    
    max_num = len(Qualification.objects.all())


class  CandidateSkillSetInline(AuditInlineAdmin):
    model =  CandidateSkillSet
    extra = 0    
    max_num = len(SkillSet.objects.all())  

class CandidateAdmin(AuditAdmin):
    list_display = ('name', 'total_experience', 'current_location', 'current_job_type', 'current_ctc', 'expected_ctc', 'notice_period','placement_status',) + AuditAdmin.list_display
    inlines = [CandidateHistoryInline, CandidateSkillSetInline, CandidateQualificationInline ]
     

class CandidateQualificationAdmin(AuditAdmin):
    list_display = ('candidate', 'qualification', 'year_of_completion', 'percentage', 'remarks',) + AuditAdmin.list_display


class CandidateSkillSetAdmin(AuditAdmin):
    list_display = ('candidate', 'skillset', 'exp_in_years', 'exp_in_months',)   + AuditAdmin.list_display 
    
class CandidateHistoryAdmin(AuditAdmin):
    list_display = ('candidate', 'company', 'join_date', 'end_date', 'current_employer',)  + AuditAdmin.list_display
    #date_hierarchy = 'join_date'

admin.site.register(Candidate,CandidateAdmin)
admin.site.register(CandidateHistory,CandidateHistoryAdmin)
admin.site.register(CandidateQualification, CandidateQualificationAdmin)
admin.site.register(CandidateSkillSet, CandidateSkillSetAdmin)
