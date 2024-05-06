from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context = {
        'title':'Home - Главная',
        'content':'Магазин мебели HOME',
    }
    return render(request,'main/index.html',context)

def about(request):
    context = {
        'title':'О нас',
        'content':'О нас',
        'text_on_page':'Текст о том как хорош и какой классный этот сайт , и как хорош этот товар.'
    }   
    return render(request,'main/about.html',context)
