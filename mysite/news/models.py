from tokenize import blank_re
from xml.etree.ElementInclude import default_loader
from django.db import models

class News(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # пока не работает (news.News.photo: (fields.E210) Cannot use ImageField because Pillow is not installed.)
    # photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    is_publushed = models.BooleanField(default=True)


