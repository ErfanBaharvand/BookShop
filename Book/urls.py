from django.conf.urls import url
from django.conf.urls.static import static

from BookShop import settings
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^book/(\d+)$', views.book_detail, name='book_detail'),
    url(r'^about$', views.about, name='about'),
    url(r'^contact$', views.contact, name='contact'),
    url(r'^category/(\d+)', views.category, name='category'),
    url(r'^update/userRegister/$' ,views.register ,name='register')

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

