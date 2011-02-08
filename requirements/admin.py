from django.contrib import admin
from django.contrib.auth.models  import User

from job.util.admin import AuditAdmin, AuditInlineAdmin

from job.data_management.models import Qualification, SkillSet, SkillSetCategory, City, Company
from job.requirements.models import Requirement, RequirementsSkillSet, RequirementsQualification, RequirementUserAssignment

class RequirementsQualificationInline(AuditInlineAdmin):
    model = RequirementsQualification
    extra = 0
    max_num = len(Qualification.objects.all())

class RequirementsSkillSetInline(AuditInlineAdmin):
    model = RequirementsSkillSet
    extra = 0
    max_num = len(SkillSet.objects.all())

class RequirementUserAssignmentInline(AuditInlineAdmin):
    model = RequirementUserAssignment
    extra = 0
    max_num = len(User.objects.all())

class RequirementAdmin(AuditAdmin):
    list_display = ('title', 'client', 'active', 'expires_at', 'status', 'remarks',)   + AuditAdmin.list_display
    inlines = [RequirementsQualificationInline, RequirementsSkillSetInline, RequirementUserAssignmentInline] 

class RequirementsSkillSetAdmin(AuditAdmin):
    list_display = ('requirements', 'skillset', 'min_exp_in_years', 'min_exp_in_months', 'max_exp_in_years', 'max_exp_in_months',)   + AuditAdmin.list_display

class RequirementsQualificationAdmin(AuditAdmin):
    list_display = ('requirements', 'qualification',)  + AuditAdmin.list_display
                     
class RequirementUserAssignmentAdmin(AuditAdmin):
    list_display = ('requirement', 'user',)   + AuditAdmin.list_display
    
admin.site.register(Requirement, RequirementAdmin)
admin.site.register(RequirementsSkillSet, RequirementsSkillSetAdmin)
admin.site.register(RequirementsQualification, RequirementsQualificationAdmin)
admin.site. register(RequirementUserAssignment, RequirementUserAssignmentAdmin)
