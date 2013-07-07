from django.conf import settings
from misago.utils.plugins import render_to_string

class GoogleAnalyticsMiddleware(object):
    def process_context(self, templates, context):
        if 'hook_append_extra' in context:
            context['hook_append_extra'] += render_to_string('ga_script.html',
                                                             {'GoogleAnalyticsID': settings.GOOGLE_ANALYTICS_ID})
            return context