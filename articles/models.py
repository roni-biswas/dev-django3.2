from typing import Iterable, Optional
from django.db import models
from django.utils.text import slugify

# Create your models here.

class Article(models.Model):
    title = models.TextField()
    content = models.TextField()