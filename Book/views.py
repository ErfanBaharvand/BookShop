from django.shortcuts import render ,render_to_response

from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import RequestContext, loader

from Book.models import Book, Category


def home(request):
    chosen_books = Book.objects.filter(chosen=True)[10]
    new_books = Book.objects.get().order_by('publication_date')[10]
    listMenu = Category.objects.get()
    slider = Category.objects.get()[5]
    return request, 'index.html', {'chosenBook': chosen_books
                                   , 'newBook': new_books
                                   , 'listMenu': listMenu
                                   , 'contentSlider': slider
                                   }


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


