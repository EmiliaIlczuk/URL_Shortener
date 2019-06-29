from django.db import models


class Urls(models.Model):
    url_input = models.URLField(max_length=200)
    short_code = models.SlugField(max_length=15, unique=True, blank=True)
    timestamp = models.DateTimeField(auto_now=True, editable=False, verbose_name='Creation date')

    def __str__(self):
        return self.url_input
