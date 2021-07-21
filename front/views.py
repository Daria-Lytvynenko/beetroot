import datetime

from django.shortcuts import render

# Create your views here.
from front.models import Page, Menu, News


def index(request):
    return render(request, "index.html",
                  {
                      "page": Page.objects.get(id=1),
                      "menu": Menu.objects.filter(visible=True).order_by("order")
                  })

def one_page(request, id):
    return render(request, "index.html",
                  {
                      "page": Page.objects.get(id=id),
                      "menu": Menu.objects.filter(visible=True).order_by("order")
                  })
def news_list(request):
    return render(request, "news.html", {"newslist":News.objects.filter(time_pub__lte=datetime.datetime.now())})

def one_news(request, id):
    pass