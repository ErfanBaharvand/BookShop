from django.shortcuts import render


from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader


def home(request):
    page = loader.get_template('index.html')
    return HttpResponse(page.render())


def about(request):
    page = loader.get_template('about.html')
    return HttpResponse(page.render())


def basket(request):
    page = loader.get_template('basket.html')
    return HttpResponse(page.render())


def contact(request):
    page = loader.get_template('contact.html')
    return HttpResponse(page.render())
