from __future__ import unicode_literals

from django.db import models
from .contributor import Contributor


class Work(models.Model):
    title = models.CharField(max_length=255, null=False)
    iswc = models.CharField(max_length=15, null=False)
    contributors = models.ManyToManyField(Contributor, related_name="works_list")

