from django.shortcuts import render

def index(request):
    return render(request, 'index.html',locals())

def homepage_2(request):
    return render(request, 'index-2.html',locals())

    