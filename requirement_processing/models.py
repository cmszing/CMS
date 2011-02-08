from django.db import models
from django.contrib.auth.models import User

from job.util.models import Audit
 
from job.requirements.models import Requirement
from job.candidate.models import Candidate

#class RequirementEmployeesAssignment(Audit):
#    requirement = models.ForeignKey(Requirement)
#    employee = models.ForeignKey(User, related_name='employee_%(class)s_set')
#    status = models.CharField(max_length = 25, choices = (('IN PROGRESS', 'IN PROGRESS'),('COMPLETED','COMPLETED')))
#    assigned_at = models.DateField(auto_now_add = True)
#    assigned_by = models.ForeignKey(User)    
#    
#    class Meta:
#        verbose_name = 'Requirement <-> Employees Assignment'
#        verbose_name_plural = 'Requirement <-> Employees Assignments'        
#   
    
class RequirementCandidatesAssignment(Audit):
    requirement = models.ForeignKey(Requirement)
    candidate = models.ForeignKey(Candidate)
    #employee = models.ForeignKey(User, related_name='employee_%(class)s_set')
    status = models.CharField(max_length = 25, choices = (('INTERVIEW SCHEDULED', 'INTERVIEW SCHEDULED'),('COMPLETED','COMPLETED')))
    assigned_at = models.DateField(auto_now_add = True)
    assigned_by = models.ForeignKey(User, related_name='assigned_by_%(class)s_set')
    interview_date = models.DateTimeField()
    remarks = models.TextField()
    
    class Meta:
        verbose_name = 'Requirement <-> Candidates Assignment'
        verbose_name_plural = 'Requirement <-> Candidates Assignments'