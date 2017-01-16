from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader


def home(request):
    page = loader.get_template('404Page.html')
    return HttpResponse(page.render())
