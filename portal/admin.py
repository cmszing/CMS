from django.contrib import admin
from job.util.admin import AuditAdmin
from job.portal.models import News 
from job.util.constants import * 
from datetime import datetime
from django.core.mail import mail_managers
from django.contrib.contenttypes.models import ContentType
from django.utils.encoding import force_unicode

model_singular = News._meta.verbose_name.title() #@UndefinedVariable
model_plural = News._meta.verbose_name_plural.title() #@UndefinedVariable

class NewsAdmin(AuditAdmin):
    list_display = ('title', 'url', 'enabled', 'expires_at',) + AuditAdmin.list_display
    search_fields = ['title']
    list_filter = ['enabled', 'expires_at']
    ordering = ['expires_at']
    #prepopulated_fields = {'slug' : ('title',)}


    def update_model(self, request, queryset, enabled):
        update_list = queryset.exclude(enabled__exact = enabled)
        
        for object in update_list:            
            if object.send_notification_mail():
                subject = '%s : %s  has been updated [Changed Status]' % (str(ContentType.objects.get_for_model(object)).title(), force_unicode(object))
                body = ' %s by %s at %s ' % (subject, request.user, datetime.now())
                mail_managers(subject, body, fail_silently = False)
        
        rows_updated = update_list.update(enabled = enabled, modified_at = datetime.now(), modified_by = request.user)

        if rows_updated == 1:
            message_bit = "1 " + model_singular +  " was "
        elif rows_updated > 1:
            message_bit =  "%s %s were" % (rows_updated, model_plural) 
        else:
            message_bit = "No " +  model_singular + " was"
        
        status_message = "%s successfully marked as %s." % (message_bit, "Enabled" if enabled else "Disabled" )
        self.message_user(request, status_message)


    def mark_enabled(self, request, queryset):
        self.update_model(request, queryset, True)

    def mark_disabled(self, request, queryset):
        self.update_model(request, queryset, False)

    mark_enabled.short_description = "Enable Selected " +  model_singular  
    mark_disabled.short_description = "Disable Selected " +  model_singular
        
    actions = [mark_enabled, mark_disabled]

admin.site.register(News, NewsAdmin)
