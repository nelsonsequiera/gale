from django.shortcuts import render
from ver1.models import Article
from sqlite3 import Date
import random


# index function
# is invoked when the first page is loadeed
def index(request):
    startdate = '1970-01-01'
    enddate = Date.today()
    # retrieves all articles from the db in ascending order of publication date
    all_articles = Article.objects.filter(pub_date__range = [startdate, enddate]).order_by('-pub_date')
    
    # selects a random article from the list
    random_article = random.choice(all_articles)
    # gets the day of the article published
    day = random_article.pub_date.strftime("%A")
    
    # gets the top three articles from all articles
    topThree_articles = all_articles[:5]
    
    # retrieves 4 articles from the db in random order
    random_four = Article.objects.filter(pub_date__range = [startdate, enddate]).order_by('?')[:4]
    
    # adding contents to the dictionary
    context_dict = {}
    context_dict[ 'random_article' ] = random_article
    context_dict[ 'topThree_articles' ] = topThree_articles
    context_dict['day'] = day
    context_dict['random_four'] = random_four
    
    return render(request, 'ver1/index.html', context_dict) 
    
    
# invoked when a user selects an article 
def page(request, id_num):
    startdate = '1970-01-01'
    enddate = Date.today()
    
    # gets the article based on the id recieved
    article = Article.objects.get(id = id_num)
    
    # gets the day of the article published
    day = article.pub_date.strftime("%A")
    
    # retrieves 4 articles from the db in random order
    random_four = Article.objects.filter(pub_date__range = [startdate, enddate]).order_by('?')[:4]
   
    # adding contents to the dictionary
    context_dict = {}
    context_dict['random_four'] = random_four
    context_dict['article'] = article
    context_dict['day'] = day
     
    return render(request, 'ver1/page.html', context_dict)
