from Book.models import Book
from Book.models import Publisher
from Book.models import Author
from Book.models import Category


def createData():
    publisher1 = Publisher.objects.create(name="موسسه پژوهشی حکمت و فلسفه ایران", address="داخل تهران", city="تهران",
                                          country="ایران", website="a.com")
    publisher2 = Publisher.objects.create(name="انتشارات موسسه آموزشی و پژوهشی امام خمینی (ره)", address="داخل تهران",
                                          city="تهران", country="ایران", website="a.com")
    publisher3 = Publisher.objects.create(name="مسجد مقدس جمکران", address="داخل تهران", city="تهران", country="ایران",
                                          website="a.com")
    publisher4 = Publisher.objects.create(name="بنیاد فرهنگی حضرت مهدی موعود (عج)", address="داخل تهران", city="تهران",
                                          country="ایران", website="a.com")
    publisher5 = Publisher.objects.create(name="سوره مهر", address="داخل تهران", city="تهران", country="ایران",
                                          website="a.com")
    publisher6 = Publisher.objects.create(name="مشهور", address="داخل تهران", city="تهران", country="ایران",
                                          website="a.com")
    publisher7 = Publisher.objects.create(name="حماسه یاران", address="داخل تهران", city="تهران", country="ایران",
                                          website="a.com")
    publisher8 = Publisher.objects.create(name="شهید ابراهیم هادی", address="داخل تهران", city="تهران", country="ایران",
                                          website="a.com")
    publisher9 = Publisher.objects.create(name=" روایت فتح", address="داخل تهران", city="تهران", country="ایران",
                                          website="a.com")
    publisher10 = Publisher.objects.create(name="شرکت چاپ و نشر بین الملل", address="داخل تهران", city="تهران",
                                           country="ایران", website="a.com")
    publisher11 = Publisher.objects.create(name="دانشکده اصول دین", address="داخل تهران", city="تهران", country="ایران",
                                           website="a.com")
    publisher12 = Publisher.objects.create(name="حکمت", address="داخل تهران", city="تهران", country="ایران",
                                           website="a.com")
    publisher13 = Publisher.objects.create(name=" هاجر (وابسته به مرکز مدیریت حوزه های علمیه خواهران)",
                                           address="داخل تهران", city="تهران", country="ایران", website="a.com")
    publisher14 = Publisher.objects.create(name="سمت", address="داخل تهران", city="تهران", country="ایران",
                                           website="a.com")
    publisher15 = Publisher.objects.create(name="بوستان کتاب قم", address="داخل تهران", city="تهران", country="ایران",
                                           website="a.com")
    publisher16 = Publisher.objects.create(name="اسراء", address="داخل تهران", city="تهران", country="ایران",
                                           website="a.com")

    author1 = Author.objects.create(first_name="سید ناصر", last_name=" حسینی پور", email="a@gmail.com")
    author2 = Author.objects.create(first_name="رضا", last_name=" دیلمی", email="a@gmail.com")
    author3 = Author.objects.create(first_name="محمد حسین", last_name=" اشرافی", email="a@gmail.com")
    author4 = Author.objects.create(first_name="مرتضی", last_name=" مطهری", email="a@gmail.com")
    author5 = Author.objects.create(first_name="لطف الله", last_name="صافی گلپایگانی", email="a@gmail.com")
    author6 = Author.objects.create(first_name="حسن", last_name=" محمودی", email="a@gmail.com")
    author7 = Author.objects.create(first_name="پری", last_name=" ریاحی", email="a@gmail.com")
    author8 = Author.objects.create(first_name="محسن", last_name=" قرائتی", email="a@gmail.com")
    author9 = Author.objects.create(first_name="علی اکبر", last_name="صمدی یزدی", email="a@gmail.com")
    author10 = Author.objects.create(first_name="حسین", last_name="کاجی", email="a@gmail.com")
    author11 = Author.objects.create(first_name="گروه فرهنگی شهید ابراهیم هادی", last_name="", email="a@gmail.com")
    author12 = Author.objects.create(first_name="افروز", last_name="مهدیان", email="a@gmail.com")
    author13 = Author.objects.create(first_name="مرضیه", last_name="نظرلو", email="a@gmail.com")
    author14 = Author.objects.create(first_name="سعید", last_name="علامیان", email="a@gmail.com")
    author15 = Author.objects.create(first_name="فاطمه سادات", last_name="موسوی حرمی", email="a@gmail.com")
    author16 = Author.objects.create(first_name="صادق", last_name="محمودی", email="a@gmail.com")
    author17 = Author.objects.create(first_name="راجر", last_name="اسکروتر", email="a@gmail.com")
    author18 = Author.objects.create(first_name="فریبا", last_name="علاسوند", email="a@gmail.com")
    author19 = Author.objects.create(first_name="علی اکبر", last_name="بابایی", email="a@gmail.com")
    author20 = Author.objects.create(first_name="جعفر", last_name="سبحانی تبریزی", email="a@gmail.com")
    author21 = Author.objects.create(first_name="عبد الله", last_name="جوادی آملی", email="a@gmail.com")

    category1 = Category.objects.create(name="مهدویت", en_name="mahdaviyat")
    category2 = Category.objects.create(name="دفاع مقدس", en_name="defa")
    category3 = Category.objects.create(name="معارف", en_name="maaref")
    category4 = Category.objects.create(name="فلسفه", en_name="phalsafe")
    category5 = Category.objects.create(name="داستان", en_name="dastan")

    book1 = Book.objects.create(title="جهت نما (40 پرسش و پاسخ مهدوی)", authors=author8, publisher=publisher4,
                                publication_date="2017-01-16", photo="book_images/3.jpg ", score=5.0,
                                categories=category1, description="", price=36000)
    book2 = Book.objects.create(title="پایی که جا ماند", authors=author1, publisher=publisher5,
                                publication_date="2017-01-16", photo="book_images/1.jpg", score=5.0,
                                categories=category2, description="", price=33000)
    book3 = Book.objects.create(title="چشمه سار حکمت، یا اندرزهای لقمان حکیم در قرآن و حدیث", authors=author9,
                                publisher=publisher3, publication_date="2017-01-16", photo="book_images/14.jpg",
                                score=5.0, categories=category3, description="", price=36000)
    book4 = Book.objects.create(title="آشنایی با علوم حدیثی", authors=author3, publisher=publisher6,
                                publication_date="2017-01-16", photo="", score=5.0, categories=category3,
                                description="book_images/19.jpg", price=24000)
    book5 = Book.objects.create(title="فلسفه مقدماتی: برگرفته از آثار استاد شهید مرتضی مطهری", authors=author4,
                                publisher=publisher2, publication_date="2017-01-16", photo="book_images/2.jpg",
                                score=5.0, categories=category4, description="", price=19000)
    book6 = Book.objects.create(title="پرتوی از عظمت امام حسین علیه السلام", authors=author5, publisher=publisher3,
                                publication_date="2017-01-16", photo="book_images/15.jpg", score=5.0,
                                categories=category3, description="", price=48600)
    book7 = Book.objects.create(title="فریادرس: داستان هایی از کرامات امام زمان (عج)", authors=author6,
                                publisher=publisher3, publication_date="2017-01-16", photo="book_images/16.jpg",
                                score=5.0, categories=category5, description="", price=36000)
    book8 = Book.objects.create(title="عقل از دیدگاه مولانا", authors=author7, publisher=publisher1,
                                publication_date="2017-01-16", photo="book_images/18.jpg", score=5.0,
                                categories=category4, description="", price=13500)
    book9 = Book.objects.create(title="ازدواج به سبک شهدا", authors=author10, publisher=publisher7,
                                publication_date="2017-01-16", photo="book_images/10.jpg", score=5.0,
                                categories=category2, description="", price=4000)
    book10 = Book.objects.create(title="غریب قریب: زندگینامه مهاجر افغانی شهید رجب غلامی", authors=author11,
                                 publisher=publisher8, publication_date="2017-01-16", photo="book_images/17.jpg",
                                 score=5.0, categories=category2, description="", price=6500)
    book11 = Book.objects.create(title="روزگاران 23: کتاب تفحص", authors=author12, publisher=publisher9,
                                 publication_date="2017-01-16", photo="book_images/7.jpg", score=5.0,
                                 categories=category2, description="", price=5500)
    book12 = Book.objects.create(title="از چشم ها 14: ققنوس سوخته (کتاب بهروز فلاحت پور)", authors=author13,
                                 publisher=publisher9, publication_date="2017-01-16", photo="book_images/6.jpg",
                                 score=5.0, categories=category2, description="", price=7000)
    book13 = Book.objects.create(title="در راه (خاطرات آزاده جانبار، سرباز وظیفه علی خسروی نیک)", authors=author14,
                                 publisher=publisher10, publication_date="2017-01-16", photo="book_images/5.jpg",
                                 score=5.0, categories=category2, description="", price=11250)
    book14 = Book.objects.create(title="انسان کامل: پژواکی از کمال عبد و جمال حق در آیین و اندیشه", authors=author15,
                                 publisher=publisher11, publication_date="2017-01-16", photo="book_images/12.jpg",
                                 score=5.0, categories=category4, description="", price=6000)
    book15 = Book.objects.create(title="خاستگاه و جایگاه پیامبر (ص): جستاری در خاستگاه کلامی، فلسفی و عرفانی نبوت",
                                 authors=author16, publisher=publisher11, publication_date="2017-01-16",
                                 photo="book_images/13.jpg", score=5.0, categories=category4, description="",
                                 price=35000)
    book16 = Book.objects.create(title="تاریخ مختصر فلسفه جدید: از دکارت تا ویتگنشتاین)", authors=author17,
                                 publisher=publisher12, publication_date="2017-01-16", photo="book_images/11.jpg",
                                 score=5.0, categories=category4, description="", price=29700)
    book17 = Book.objects.create(title="زن در اسلام: کلیات و مبانی", authors=author18, publisher=publisher13,
                                 publication_date="2017-01-16", photo="book_images/11.jpg", score=5.0,
                                 categories=category3, description="", price=18000)
    book18 = Book.objects.create(title="بررسی مکاتب و روش های تفسیری - جلد دوم", authors=author19,
                                 publisher=publisher14, publication_date="2017-01-16", photo="book_images/8.jpg",
                                 score=5.0, categories=category3, description="", price=5600)
    book19 = Book.objects.create(title="مربی نمونه: تفسیر سوره لقمان", authors=author20, publisher=publisher15,
                                 publication_date="2017-01-16", photo="book_images/4.jpg", score=5.0,
                                 categories=category3, description="", price=11700)
    book19 = Book.objects.create(title="تسنیم: تفسیر قرآن کریم - جلد سی و نهم", authors=author21, publisher=publisher16,
                                 publication_date="2017-01-16", photo="book_images/20.jpg", score=5.0,
                                 categories=category3, description="", price=29000)
