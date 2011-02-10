from django.db import models
from job.util.models import Audit
from job.util import constants
from datetime import date, timedelta

class News(Audit):

    title = models.CharField(max_length = 50, unique = True)
    #slug = models.SlugField(unique=True, help_text="Suggested value automatically generated from title. Must be unique")
    url = models.URLField()
    enabled = models.BooleanField(default = True)
    expires_at = models.DateField(default = date.today() + timedelta(days = constants.DEFAULT_NO_OF_DAYS_TO_SHOW_THE_NEWS))

    def __unicode__(self):
        return self.title

#    @models.permalink
#    def get_absolute_url(self):
#          return ('portal_news', (), {'news_slug' : self.slug} )

    def send_notification_mail(self):
        return constants.NEWS_SEND_MAIL_NOTIFICATION 
 
    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'        
        db_table = 'portal_news'