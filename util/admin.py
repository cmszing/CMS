from django.contrib import admin
from reversion.admin import  VersionAdmin
from django.core.mail import mail_managers
from django.contrib.admin.models import LogEntry, ADDITION, CHANGE, DELETION
from django.contrib.contenttypes.models import ContentType
from django.utils.encoding import force_unicode
from datetime import datetime

def save_model(self, request, obj, form, change):
    instance = form.save(commit = False)
    if not instance.created_at and not instance.modified_at:
        instance.created_by = request.user
    instance.modified_by = request.user
    instance.save()        
    form.save_m2m()
    return instance
    
def log_common(self, request, object, message, action_flag): 
    LogEntry.objects.log_action(
            user_id         = request.user.pk,
            content_type_id = ContentType.objects.get_for_model(object).pk,
            object_id       = object.pk,
            object_repr     = force_unicode(object),
            action_flag     = action_flag,
            change_message  = message
        )
    
    if object.send_notification_mail():
        if action_flag == ADDITION:
            action_message = ' created'
        if action_flag == CHANGE:
            if message.startswith('No'):
                return
            else:
                action_message = ' updated [%s]' % (message)
        if action_flag == DELETION:
            action_message = ' deleted'
                
        subject = "%s : '%s'  has been %s " % (str(ContentType.objects.get_for_model(object)).title(), force_unicode(object), action_message)
        body = " %s by '%s' at %s " % (subject, request.user, datetime.now())
        mail_managers(subject, body, fail_silently = False)


class AuditAdmin(VersionAdmin):   
    list_display = ('created_by', 'modified_by', 'created_at', 'modified_at',)
    exclude = ('created_by', 'modified_by',)
    save_on_top = True
    
    def save_model(self, request, obj, form, change):
        save_model(self, request, obj, form, change)
    
    def log_addition(self, request, object):
        log_common(self, request, object, "", ADDITION)

    def log_change(self, request, object, message):
        log_common(self, request, object, message, CHANGE)

    def log_deletion(self, request, object, object_repr):
        log_common(self, request, object, "", DELETION)
        

class AuditInlineAdmin(admin.TabularInline):
    exclude = ('created_by', 'modified_by',)
    extra = 0

    def save_model(self, request, obj, form, change):
        save_model(self, request, obj, form, change)

    def log_addition(self, request, object):
        log_common(self, request, object, "", ADDITION)

    def log_change(self, request, object, message):
        log_common(self, request, object, message, CHANGE)

    def log_deletion(self, request, object, object_repr):
        log_common(self, request, object, "", DELETION)
