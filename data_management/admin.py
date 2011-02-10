from django.contrib import admin
from django.contrib.auth.models  import User

from job.util.admin import AuditAdmin, AuditInlineAdmin

from job.data_management.models import Qualification, SkillSet, SkillSetCategory, City, Company


class QualificationAdmin(AuditAdmin):
    list_display = ('name',)   + AuditAdmin.list_display

class SkillSetCategoryAdmin(AuditAdmin):
    list_display = ('name',)   + AuditAdmin.list_display

class SkillSetAdmin(AuditAdmin):
    list_display = ('name', 'category',)   + AuditAdmin.list_display
    
class CityAdmin(AuditAdmin):
    list_display = ('name',)   + AuditAdmin.list_display
                        
class CompanyAdmin(AuditAdmin):    
    list_display = ('name',)  + AuditAdmin.list_display                        

admin.site.register(Qualification, QualificationAdmin)
admin.site.register(SkillSetCategory, SkillSetCategoryAdmin)
admin.site.register(SkillSet, SkillSetAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Company, CompanyAdmin)

