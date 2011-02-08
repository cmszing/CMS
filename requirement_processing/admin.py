from django.contrib import admin
from django.contrib.auth.models  import User

from job.util.admin import AuditAdmin, AuditInlineAdmin

from job.requirement_processing.models import RequirementCandidatesAssignment

#class RequirementEmployeesAssignmentAdmin(AuditAdmin):
#    list_display = ('requirement', 'employee', 'status', 'assigned_at', 'assigned_by',)   + AuditAdmin.list_display
    
class RequirementCandidatesAssignmentAdmin(AuditAdmin):
    list_display = ('requirement', 'candidate', 'status', 'assigned_at', 'assigned_by', 'interview_date', 'remarks',)  + AuditAdmin.list_display

#admin.site.register(RequirementEmployeesAssignment,RequirementEmployeesAssignmentAdmin)
admin.site.register(RequirementCandidatesAssignment, RequirementCandidatesAssignmentAdmin)
