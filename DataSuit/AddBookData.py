from django.db.models import ImageField

from Book.models import Book
from Book.models import Publisher
from Book.models import Author
from Book.models import Category


def createData():
    Book.objects.all().delete()
    Publisher.objects.all().delete()
    Author.objects.all().delete()
    Category.objects.all().delete()
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

    book1 = Book(title="جهت نما (40 پرسش و پاسخ مهدوی)",
                 publication_date="2017-01-16", score=5.0,
                 description="", price=36000)
    book1.save()
    book1.categories.add(category1)
    book1.authors.add(author8)
    book1.publisher = publisher4
    book1.save()

    book2 = Book(title="پایی که جا ماند",
                 publication_date="2017-01-16", score=5.0,
                 description="", price=33000)
    book2.save()
    book2.categories.add(category2)
    book2.authors.add(author1)
    book2.publisher = publisher5
    book2.save()

    book3 = Book(title="چشمه سار حکمت، یا اندرزهای لقمان حکیم در قرآن و حدیث",
                 publication_date="2017-01-16",
                 score=5.0, description="", price=36000)
    book3.save()
    book3.categories.add(category3)
    book3.authors.add(author9)
    book3.publisher = publisher3
    book3.save()

    book4 = Book(title="آشنایی با علوم حدیثی",
                 publication_date="2017-01-16", photo="", score=5.0, price=24000)
    book4.save()
    book4.categories.add(category3)
    book4.authors.add(author3)
    book4.publisher = publisher6
    book4.save()

    book5 = Book(title="فلسفه مقدماتی: برگرفته از آثار استاد شهید مرتضی مطهری",
                 publication_date="2017-01-16",
                 score=5.0, description="", price=19000)
    book5.save()
    book5.categories.add(category4)
    book5.authors.add(author4)
    book5.publisher = publisher2
    book5.save()

    book6 = Book(title="پرتوی از عظمت امام حسین علیه السلام",
                 publication_date="2017-01-16", score=5.0, description="", price=48600)

    book6.save()
    book6.categories.add(category3)
    book6.authors.add(author5)
    book6.publisher = publisher3
    book6.save()

    book7 = Book(title="فریادرس: داستان هایی از کرامات امام زمان (عج)", publication_date="2017-01-16",
                 score=5.0, description="", price=36000)

    book7.save()
    book7.categories.add(category5)
    book7.authors.add(author6)
    book7.publisher = publisher3
    book7.save()

    book8 = Book(title="عقل از دیدگاه مولانا",
                 publication_date="2017-01-16", score=5.0,
                 description="", price=13500)
    book8.save()
    book8.categories.add(category4)
    book8.authors.add(author7)
    book8.publisher = publisher1
    book8.save()

    book9 = Book(title="ازدواج به سبک شهدا",
                 publication_date="2017-01-16", score=5.0,
                 description="", price=4000)
    book9.save()
    book9.categories.add(category2)
    book9.authors.add(author10)
    book9.publisher = publisher7
    book9.save()

    book10 = Book(title="غریب قریب: زندگینامه مهاجر افغانی شهید رجب غلامی", publication_date="2017-01-16",
                  score=5.0, description="", price=6500)
    book10.save()
    book10.categories.add(category2)
    book10.authors.add(author11)
    book10.publisher = publisher8
    book10.save()

    book11 = Book(title="روزگاران 23: کتاب تفحص",
                  publication_date="2017-01-16", score=5.0,
                  description="", price=5500)
    book11.save()
    book11.categories.add(category2)
    book11.authors.add(author12)
    book11.publisher = publisher9
    book11.save()

    book12 = Book(title="از چشم ها 14: ققنوس سوخته (کتاب بهروز فلاحت پور)", publication_date="2017-01-16",
                  score=5.0, description="", price=7000)
    book12.save()
    book12.categories.add(category4)
    book12.authors.add(author7)
    book12.publisher = publisher1
    book12.save()

    book13 = Book(title="در راه (خاطرات آزاده جانبار، سرباز وظیفه علی خسروی نیک)", publication_date="2017-01-16",
                  score=5.0, description="", price=11250)
    book13.save()
    book13.categories.add(category2)
    book13.authors.add(author14)
    book13.publisher = publisher10
    book13.save()

    book14 = Book(title="انسان کامل: پژواکی از کمال عبد و جمال حق در آیین و اندیشه",
                  publication_date="2017-01-16",
                  score=5.0, description="", price=6000)
    book14.save()
    book14.categories.add(category4)
    book14.authors.add(author15)
    book14.publisher = publisher11
    book14.save()

    book15 = Book(title="خاستگاه و جایگاه پیامبر (ص): جستاری در خاستگاه کلامی، فلسفی و عرفانی نبوت",
                  publication_date="2017-01-16",
                  score=5.0, description="",
                  price=35000)
    book15.save()
    book15.categories.add(category4)
    book15.authors.add(author16)
    book15.publisher = publisher11
    book15.save()

    book16 = Book(title="تاریخ مختصر فلسفه جدید: از دکارت تا ویتگنشتاین)",
                  publication_date="2017-01-16",
                  score=5.0, description="", price=29700)
    book16.save()
    book16.categories.add(category4)
    book16.authors.add(author17)
    book16.publisher = publisher12
    book16.save()

    book17 = Book(title="زن در اسلام: کلیات و مبانی",
                  publication_date="2017-01-16", score=5.0,
                  description="", price=18000)
    book17.save()
    book17.categories.add(category3)
    book17.authors.add(author18)
    book17.publisher = publisher13
    book17.save()

    book18 = Book(title="بررسی مکاتب و روش های تفسیری - جلد دوم",
                  publication_date="2017-01-16",
                  score=5.0, description="", price=5600)

    book18.save()
    book18.categories.add(category3)
    book18.authors.add(author19)
    book18.publisher = publisher14
    book18.save()

    book19 = Book(title="مربی نمونه: تفسیر سوره لقمان",
                  publication_date="2017-01-16", score=5.0,
                  description="", price=11700)
    book19.save()
    book19.categories.add(category2)
    book19.authors.add(author14)
    book19.publisher = publisher10
    book19.save()

    book20 = Book(title="تسنیم: تفسیر قرآن کریم - جلد سی و نهم",
                  publication_date="2017-01-16", score=5.0,
                  description="", price=29000)
    book20.save()
    book20.categories.add(category3)
    book20.authors.add(author21)
    book20.publisher = publisher16
    book20.save()
