from django.shortcuts import render ,render_to_response

from django.http import HttpResponse, HttpResponseRedirect, Http404
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


def handler404(request):
    page = loader.get_template('404Page.html')
    return HttpResponse(page.render())