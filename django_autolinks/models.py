from django.db import models
from django.utils.translation import ugettext_lazy as _

class Link(models.Model):
    slug = models.CharField(_('Slug'), max_length = 80, unique = True)
    url = models.URLField(_('URL'))
