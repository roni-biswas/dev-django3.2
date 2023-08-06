"""
To render HTML web pages
---------------------------------
"""

# from django.http import HttpResponse
from django.shortcuts import render
import random
from articles.models import Article


def home_page(request):

    random_id = random.randint(1, 4)

    # get data from database
    article_obj = Article.objects.get(id=random_id)
    article_queryset = Article.objects.all()

    # context = {
    #     "id" : article_obj.id,
    #     "title": article_obj.title,
    #     "content": article_obj.content,
    # }
    
    # HTML_CONTENT = """
    # <h4><b>Fatch data from database: Article</b></h4>
    # <p>Id: {id} </br> Title: {title} </br> Content: {content}</p>
    # """.format(**context)

    context = {"article_obj":article_obj, "data_list": article_queryset}
    
    return render(request, 'home_page.html', context)
