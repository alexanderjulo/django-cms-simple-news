from cms.models import Page
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import ugettext_lazy as _
from .models import NewsFilter, SmallNewsFilter


class NewsFilterPlugin(CMSPluginBase):
    """Renders an overview of all children of this page that use the
    news.html template."""
    model = NewsFilter
    name = _("News Filter")
    render_template = "news_overview.html"

    def render(self, context, instance, placeholder):
        pages = Page.objects.all()
        lang = context.get('current_language', None)
        if not lang:
            return context
        news = []
        for page in pages:
            # make sure that we only load as many items as we are supposed to.
            if len(news) == instance.number:
                break
            # only load items that are published, available in the right
            # language and using the right template.
            if page.template == 'news.html' and lang in page.get_languages() \
                    and page.published:
                news.append(page)
        # sort the object, showing the newest first
        news = sorted(news, key=lambda x: x.publication_date, reverse=True)
        # add our news to the context so that we can render it
        context['news'] = news
        return context


class SmallNewsFilterPlugin(CMSPluginBase):
    """Renders an overview of all children of this page that use the
    news.html template (small version)."""
    model = SmallNewsFilter
    name = _("Small News Filter")
    render_template = "news_overview_small.html"

    def render(self, context, instance, placeholder):
        pages = Page.objects.all()
        lang = context.get('current_language', None)
        if not lang:
            return context
        news = []
        for page in pages:
            # make sure that we only load as many items as we are supposed to.
            if len(news) == instance.number:
                break
            # only load items that are published, available in the right
            # language and using the right template.
            if page.template == 'news.html' and lang in page.get_languages() \
                    and page.published:
                news.append(page)
        # sort the object, showing the newest first
        news = sorted(news, key=lambda x: x.publication_date, reverse=True)
        # add our news to the context so that we can render it
        context['smallnews'] = news
        return context

plugin_pool.register_plugin(NewsFilterPlugin)
plugin_pool.register_plugin(SmallNewsFilterPlugin)
