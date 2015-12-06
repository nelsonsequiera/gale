from django.db import models
from django.utils import timezone
# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length = 255, unique = True)      # title of the article 
    author = models.CharField(max_length = 255)                    # author if the article
    pub_date = models.DateField(default = timezone.now)            # publication date of the article
    category = models.CharField(max_length = 200)                   # category of the article
    image = models.ImageField()                                     # image of the article
    optional_image = models.ImageField(blank = True)    
    body = models.TextField()                                       # body of the article
    
    def __unicode__(self):
        return self.title           # returns the title of the article whenever an artice object is referenced