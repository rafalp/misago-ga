from django.conf import settings

class GoogleAnalyticsMiddleware(object):
    def process_context(self, theme, templates, context):
        if 'hook_append_extra' in context:
            context['hook_append_extra'] += theme.render_to_string('ga_script.html',
                                                                   {'GoogleAnalyticsID': settings.GOOGLE_ANALYTICS_ID})
            return context