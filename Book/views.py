from django.shortcuts import render ,render_to_response

from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import RequestContext, loader

from Book.models import Book, Category, Slider


def home(request):
    chosen_books = Book.objects.filter(chosen=True)
    if len(chosen_books) > 10:
        chosen_books = chosen_books[:10]
    new_books = Book.objects.all().order_by('publication_date')
    if len(new_books) > 10:
        new_books = new_books[:10]
    listMenu = Category.objects.all()
    slider = Slider.objects.all()
    if len(slider) > 5:
        slider = slider[:5]
    return render(request, 'index.html', {'chosenBook': chosen_books
                                   , 'newBook': new_books
                                   , 'listMenu': listMenu
                                   , 'contentSlider': slider
                                   })


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


def book_detail(request, id):
    book = Book.objects.get(pk=id)
    author = book.authors.all()[0]
    key = ['عنوان', 'نویسنده','ناشر', 'تاریخ انتشار', 'امتیاز']
    val = [book.title, author.first_name + " " + author.last_name, book.publisher.name, book.publication_date, book.score]
    detail = []
    for i in range(0, len(key)):
        detail.append(str(key[i]) + ":" +str(val[i]))
    return render(request, 'BookPage.html', {'detail': detail, 'val': val, 'book': book})
