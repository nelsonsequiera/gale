from django.shortcuts import render
from ver1.models import Article
from sqlite3 import Date
import random

# Create your views here.
def index(request):
    
    startdate = '1970-01-01'
    enddate = Date.today()
    articles = Article.objects.filter(pub_date__range = [startdate, enddate]).order_by('pub_date')[:10]
    context_dict = {'articles' : articles}
    
    articles_list =  Article.objects.filter(pub_date__range = [startdate, enddate]).order_by('pub_date')
    id_list = articles_list.values_list('id', flat = True)
    rid = random.choice(id_list)
    random_article = Article.objects.get(id = rid)
    context_dict['rand_article'] = random_article
    
    return render(request, 'ver1/index.html', context_dict) 

def page(request, id_num):
    article = Article.objects.get(id = id_num)
    return render(request, 'ver1/page.html', {'article' : article})