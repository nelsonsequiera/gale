from django.db import models
from django.utils import timezone
# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length = 255, unique = True)
    author = models.CharField(max_length = 255)
    pub_date = models.DateField(default = timezone.now)
    category = models.CharField(max_length = 200)
    image = models.ImageField()
    optional_image = models.ImageField(blank = True)
    body = models.TextField()
    
    def __unicode__(self):
        return self.title