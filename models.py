from cms.models.pluginmodel import CMSPlugin
from django.db import models


class NewsFilter(CMSPlugin):
    """Saves the settings for the News."""
    # the number of articles that should be displayed.
    number = models.IntegerField(default=5)
