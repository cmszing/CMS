from django.utils.translation import ugettext_lazy as _
from admin_tools.dashboard import modules, Dashboard, AppIndexDashboard
from job.portal.models import News
from datetime import datetime
from job.settings import ADMIN_TOOLS_INDEX_DASHBOARD_COLUMNS
from dashboardmods import get_memcache_dash_modules, get_rss_dash_modules, get_varnish_dash_modules

# to activate your index dashboard add the following to your settings.py:
#
# ADMIN_TOOLS_INDEX_DASHBOARD = 'myproj.dashboard.CustomIndexDashboard'

class CustomIndexDashboard(Dashboard):
    """
    Custom index dashboard for myproj.
    """
    def __init__(self, **kwargs):
        Dashboard.__init__(self, **kwargs)
#        display="tabs",
        self.columns = ADMIN_TOOLS_INDEX_DASHBOARD_COLUMNS
        self.children.append(modules.Group(
            title="",
            display="tabs",
            children=[
                
                modules.AppList(
                    title='Requirements',
                    include_list=('requirements', 'requirement_processing',)
                ),

                modules.AppList(
                    title='Data Management',
                    include_list=('client', 'candidate', 'job.data_management',)
                ),

                modules.AppList(
                    title='Portal Administration',
                    include_list=('django.contrib.sites', 'dashboardmods', 'portal',)
                ),
                
                modules.AppList(
                    title='User Management',
                    include_list=('django.contrib.auth',)
                ),
                
                modules.AppList(
                    title='All Applications',
                    exclude_list=('django.contrib', )
                )
                
            ]
        ))

        

#        # append an app list module for "Applications"
#        self.children.append(modules.AppList(
#            title=_('Applications'),
#            exclude_list=('django.contrib',),
#        ))
#
#        # append an app list module for "Administration"
#        self.children.append(modules.AppList(
#            title=_('Administration'),
#            include_list=('django.contrib',),
#        ))


        # append a recent actions module
        self.children.append(modules.RecentActions(
            title=_('Recent Actions'),
            limit=5
        ))

#        # append a feed module
#        self.children.append(modules.Feed(
#            title=_('Latest Django News'),
#            feed_url='http://www.djangoproject.com/rss/weblog/',
#            limit=5
#        ))

#        # append another link list module for "support".
#        self.children.append(modules.LinkList(
#            title=_('Support'),
#            children=[
#                {
#                    'title': _('Django documentation'),
#                    'url': 'http://docs.djangoproject.com/',
#                    'external': True,
#                },
#                {
#                    'title': _('Django "django-users" mailing list'),
#                    'url': 'http://groups.google.com/group/django-users',
#                    'external': True,
#                },
#                {
#                    'title': _('Django irc channel'),
#                    'url': 'irc://irc.freenode.net/django',
#                    'external': True,
#                },
#            ]
#        ))
        # append another link list module for "support".
        
        news_db_list = News.objects.filter(expires_at__gte = datetime.today(), enabled = True )
        
        news_list = []
        
        for news in news_db_list:
            news_dict = {
                         'title' : news.title,
                         'url' : news.url,
                         'external' : True,
                         }
            news_list.append(news_dict)
        
        self.children.append(modules.LinkList(
            title=_('Latest News'),
            children = news_list 
        ))
        
                # append a link list module for "quick links"
#        self.children.append(modules.LinkList(
#            title=_('Quick links'),
#            layout='inline',
#            draggable=True,
#            deletable=True,
#            collapsible=True,
#            children=[
#                {
#                    'title': _('Return to site'),
#                    'url': '/',
#                },
#                {
#                    'title': _('Change password'),
#                    'url': reverse('admin:password_change'),
#                },
#                {
#                    'title': _('Log out'),
#                    'url': reverse('admin:logout')
#                },
#            ]
#        ))
        self.children.extend(get_memcache_dash_modules())
        self.children.extend(get_varnish_dash_modules())
        self.children.extend(get_rss_dash_modules())

    def init_with_context(self, context):
        """
        Use this method if you need to access the request context.
        """
        print "=========================="
        print context.get('user')
    
        pass


# to activate your app index dashboard add the following to your settings.py:
#
# ADMIN_TOOLS_APP_INDEX_DASHBOARD = 'myproj.dashboard.CustomAppIndexDashboard'

class CustomAppIndexDashboard(AppIndexDashboard):
    """
    Custom app index dashboard for myproj.
    """
    def __init__(self, *args, **kwargs):
        AppIndexDashboard.__init__(self, *args, **kwargs)

        # we disable title because its redundant with the model list module
        self.title = ''

        # append a model list module
        self.children.append(modules.ModelList(
            title=self.app_title,
            include_list=self.models,
        ))

        # append a recent actions module
        self.children.append(modules.RecentActions(
            title=_('Recent Actions'),
            include_list=self.get_app_content_types(),
        ))

    def init_with_context(self, context):
        """
        Use this method if you need to access the request context.
        """
        print context
        pass
