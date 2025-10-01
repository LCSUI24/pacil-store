# pacil-store
**Tugas 2**

*pertanyaan satu*

- membuat repository pada github desktop
- publish repository tersebut ke github
- membuat virtual environment pada repository tersebut dengan command "python -m venv env"
- menjalankan virtual environment dengan command "env\Scripts\activate"
- membuat file requirements.txt untuk dependencies yang dibutuhkan untuk menjalankan projek
- menginstall requirements yang dibutuhkan dengan menjalankan command "pip install -r requirements.txt"
- membuat projek dengan menjalankan command "django-admin startproject pacil_store .
- membuat file .env dan diisi dengan konfigurasi "PRODUCTION=False"
- membuat file .env.prod untuk konfigurasi pada saat deployment diisi dengan 
~~~   
    DB_NAME=<nama database>
    DB_HOST=<host database>
    DB_PORT=<port database>
    DB_USER=<username database>
    DB_PASSWORD=<password database>
    SCHEMA=tugas_individu
    PRODUCTION=True
~~~
- menambahkan kode berikut pada file settings.py 
~~~
    import os
    from dotenv import load_dotenv
    
    load_dotenv()

    tambahkan atribut "localhost", "127.0.0.1" pada array ALLOWED_HOST 

    tambahkan PRODUCTION = os.getenv('PRODUCTION', 'False').lower() == 'true' di atas code DEBUG

    dan mengganti kode DATABASES menjadi 
    if PRODUCTION:
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.postgresql',
                'NAME': os.getenv('DB_NAME'),
                'USER': os.getenv('DB_USER'),
                'PASSWORD': os.getenv('DB_PASSWORD'),
                'HOST': os.getenv('DB_HOST'),
                'PORT': os.getenv('DB_PORT'),
                'OPTIONS': {
                    'options': f"-c search_path={os.getenv('SCHEMA', 'public')}"
                }
            }
        }
    else:
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': BASE_DIR / 'db.sqlite3',
            }
        }
~~~
- jalankan command berikut untuk migration "python manage.py migrate"
- buat file git ignore diisi dengan file-file yang tidak mau di push
~~~
# Django
*.log
*.pot
*.pyc
**pycache**
db.sqlite3
media
# Backup files
*.bak
# If you are using PyCharm
# User-specific stuff
.idea/**/workspace.xml
.idea/**/tasks.xml
.idea/**/usage.statistics.xml
.idea/**/dictionaries
.idea/**/shelf
# AWS User-specific
.idea/**/aws.xml
# Generated files
.idea/**/contentModel.xml
.DS_Store
# Sensitive or high-churn files
.idea/**/dataSources/
.idea/**/dataSources.ids
.idea/**/dataSources.local.xml
.idea/**/sqlDataSources.xml
.idea/**/dynamic.xml
.idea/**/uiDesigner.xml
.idea/**/dbnavigator.xml
# Gradle
.idea/**/gradle.xml
.idea/**/libraries
# File-based project format
*.iws
# IntelliJ
out/
# JIRA plugin
atlassian-ide-plugin.xml
# Python
*.py[cod]
*$py.class
# Distribution / packaging
.Python build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg
*.manifest
*.spec
# Installer logs
pip-log.txt
pip-delete-this-directory.txt
# Unit test / coverage reports
htmlcov/
.tox/
.coverage
.coverage.*
.cache
.pytest_cache/
nosetests.xml
coverage.xml
*.cover
.hypothesis/
# Jupyter Notebook
.ipynb_checkpoints
# pyenv
.python-version
# celery
celerybeat-schedule.*
# SageMath parsed files
*.sage.py
# Environments
.env*
!.env.example*
.venv
env/
venv/
ENV/
env.bak/
venv.bak/
# mkdocs documentation
/site
# mypy
.mypy_cache/
# Sublime Text
*.tmlanguage.cache
*.tmPreferences.cache
*.stTheme.cache
*.sublime-workspace
*.sublime-project
# sftp configuration file
sftp-config.json
# Package control specific files Package
Control.last-run
Control.ca-list
Control.ca-bundle
Control.system-ca-bundle
GitHub.sublime-settings
# Visual Studio Code
.vscode/*
!.vscode/settings.json
!.vscode/tasks.json
!.vscode/launch.json
!.vscode/extensions.json
.history
~~~
- buat aplikasi bernama main dengan command "python manage.py startapp main"
- tambahkan atribut 'main' pada INSTALLED-APPS di settings.py yang ada di folder pacil_store
- mengubah file models.py pada folder main dan diisi dengan 
~~~
    import uuid
    from django.db import models

    class Product(models.Model):
        CATEGORY_CHOICES = [
            ('baju', 'Baju'),
            ('update', 'Update'),
            ('exclusive', 'Exclusive'),
            ('laptop', 'Laptop'),
            ('domain', 'Domain'),
            ('trend', 'Trend'),
        ]
        
        id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
        name = models.CharField(max_length=255)
        price = models.IntegerField()
        description = models.TextField()
        thumbnail = models.URLField(blank=True, null=True)
        category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='update')
        is_featured = models.BooleanField(default=False)
    
        def __str__(self):
            return self.name
~~~
- jalankan command berikut "python manage.py makemigrations | python manage.py migrate" untuk melakukan migrasi model
- tambahkan kode berikut pada views.py di folder main
~~~
    from django.shortcuts import render

    def show_main(request):
        context = {
            'app' : 'Pacil Store',
            'name': 'Cyrillo Praditya Soeharto',
            'class': 'PBP B'
        }

        return render(request, "main.html", context)
~~~
- pada folder main buat folder templates dan buat file "main.html" lalu diisi dengan kode berikut
~~~
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Pacil Store</title>
        <style>
            body{
                text-align: center;
            }
            h1{
                font-size: 50px;
            }
        </style>
    </head>
    <body>
        <h1>{{ app }}</h1>
        <h5>Name: {{ name }}</h5>
        <h5>Class: {{ class }}</h5>
    </body>
    </html>
~~~
- buat file utls.py pada folder main lalu diisi denga kode 
~~~
    from django.urls import path
    from main.views import show_main

    app_name = 'main'

    urlpatterns = [
        path('', show_main, name='show_main'),
    ]
~~~
- tambahkan kode berikut pada file urls.py di folder pacil_store
~~~
    from django.urls import path, include

    dan tambahkan kode ini pada urlpatterns "path('', include('main.urls')),"
~~~
- buka laman "https://pbp.cs.ui.ac.id" dan lakukan login denga sso 
- create new project dan namai pacilstore
- save credential dan command yang diberikan
- pada tab environs pilih raw editor dan masukkan isi dari file.env.prod 
- tambahkan URL deployment pws di ALLOWED_HOSTS pada file settings.py di folder pacil_store
- commit dan push ke github
- jalankan command yang diberikan pws lalu push ke pws

*pertanyaan dua*

<img width="611" height="231" alt="image" src="https://github.com/user-attachments/assets/cba3a838-4a72-4b48-b6d4-a3d34f0cc291" />

untuk flowchart ada pada nomor2.drawio.png

penjelasan:
- Client Request: Saat user mengirim request ke Django, lalu browser mengirim request tersebut ke server
- urls.py: request diterima oleh urls.py dan dicocokkan dengan yang ada di dalam file, lalu meneruskan ke views.py yang cocok
- views.py: memproses data, memanggil model, dan mempersiapkan data untuk ditampilkan pada html
- models.py: berinteraksi dengan database dan menghubungkan aplikasi dengan data dan mengambil informasi yang dibutuhkan
- HTML: proses tadi dikirm ke HTML untuk menunjukkan user interface bagi data yang sudah siap
- Response: Server mengirimkan response kembali ke client, yang berisi halaman HTML yang telah diproses.

*pertanyaan tiga*

settings.py berfungsi sebagai pengaturan untuk projek, seperti INSTALLED_APPS untuk mengetahui aplikasi mana yang aktif, DATABASES untuk mengatur database yang akan digunakan, TEMPLATES untuk memberi tahu file templates kita, SECRET_KEY, DEBUG, DAN ALLOWED_HOSTS agar projek aman.

*pertanyaan empat*

python manage.py makemigrations akan membuat Django memeriksa setiap perubahan pada model dan menghasilkan file migrasi di dalam direktori migrations/ aplikasi. Berkas migrasi ini diberi nomor secara otomatis (misalnya, 0001_initial.py, 0002_auto_...) dan mewakili perubahan inkremental yang dibuat pada skema basis data.

python manage.py migrate akan membuat perintah migrasi memeriksa berkas migrasi yang dihasilkan oleh makemigrations dan menerapkan perubahan dalam urutan yang benar. Perintah ini menangani pembuatan tabel, modifikasi kolom, penambahan indeks, dan pelaksanaan operasi terkait basis data lainnya. Perintah ini memastikan bahwa dependensi antar migrasi dihormati, sehingga migrasi diterapkan dalam urutan yang benar.

*pertanyaan lima*

Karena Django merupakan salah satu framework yang paling populer dan kuat saat ini, Django juga memiliki keamanan yang bagus, juga memiliki banyak templates dan library yang bisa digunakan. Django juga menggunakan bahasa pemrograman python yang dimana bahasa tersebut sudah pernah dipelajari oleh mahasiswa Fasilkom UI pada semester 1.

*pertanyaan enam*

ada beberapa typo pada dokumen tutorial yang sempat bikin bingun, sama kalo bisa tambahin link referensi supaya bisa lebih mengerti saat mengerjakan tutorial.

**Tugas 3**

*pertanyaan satu*

Data delivery melibatkan pemindahan data dari satu tempat ke tempat lain. Data delivery memastikan bahwa informasi yang tepat sampai ke orang yang tepat pada waktu yang tepat. Proses ini mencakup beberapa komponen utama, seperti data sources dan data destinations. Hal ini penting untuk memastikan akurasi data, mendeteksi error, validasi data, meningkatkan pengambilan keputusan, akses data real-time, dan Data-driven insight.

*pertanyaan dua*

Menurut saya JSON lebih baik, karena JSON lebih compact dan mudah di muat di javascript. JSON juga dapat menjadi objek javascript dengan mudah, lebih pendek, tidak menggunakan tag penutup, lebih cepat dibaca dan ditulis, dan dapat menggunakan array.

*pertanyaan tiga*

Method is_valid() pada form Django berfungsi untuk validasi data yang diinput melalui formulir agar memastikan seluruh field mematuhi aturan validasi (misal required, tipe data, pola input). Kita membutuhkan is_valid() agar data yang akan diproses atau disimpan ke database telah lolos pemeriksaan validasi sesuai logika yang kita maksud/inginkan.

*pertanyaan empat*

CSRF token diperlukan untuk melindungi aplikasi dari serangan Cross-Site Request Forgery (CSRF) atau serangan yang di mana penyerang memalsukan permintaan. Jika token ini tidak ada penyerang bisa membuat program yang secara otomatis mengirimkan permintaan ke endpoint Django menggunakan identitas pengguna yang sedang login tanpa sepengetahuannya dengan begitu penyeran dapat mengubah password dan melakukan sesuatu atas nama target yang diserang, data orang yang diserang juga dapat mengalami kebocoran.

*pertanyaan lima*

- membuat folder templates pada root dan membuat base.html di dalamnya
~~~
{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    {% block meta %} {% endblock meta %}
</head>

<body>
    {% block content %} {% endblock content %}
</body>
</html>
~~~
- ubah settingan 'DIRS' pada settings.py pada folder pacil_store
~~~
'DIRS': [BASE_DIR / 'templates']
~~~
- buat file forms.py pada folder main dan diisi dengan 
~~~
from django.forms import ModelForm
from main.models import Product

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "description", "category", "thumbnail", "is_featured"]
~~~
- mengubah file models.py di folder main dengan
~~~
class Product(models.Model):
    CATEGORY_CHOICES = [
        ('pakaian', 'Pakaian'),
        ('exclusive', 'Exclusive'),
        ('elektronik', 'Elektronik'),
        ('makanan', 'Makanan'),
        ('minuman', 'Minuman'),
        ('aksesoris', 'Aksesoris'),
        ('trend', 'Trend'),

    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='update')
    product_views = models.PositiveIntegerField(default=0)
    is_featured = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
    
    def increment_views(self):
        self.product_views += 1
        self.save()
~~~
- lakukan migrasi dengan menjalankan command
~~~ 
python manage.py makemigrations | python manage.py migrate 
~~~
- ubah views.py pada folder main dengan 
~~~
from django.shortcuts import render, redirect, get_object_or_404
from main.forms import ProductForm
from main.models import Product
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_main(request):
    product_list = Product.objects.all()
    context = {
        'app1' : 'Pacil',
        'app2' : '/',
        'app3' : 'Store',
        'name': 'Cyrillo Praditya Soeharto',
        'class': 'PBP B',
        'product_list': product_list,
    }

    return render(request, "main.html", context)

def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product.html", context)

def show_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product.increment_views()

    context = {
        'product': product
    }

    return render(request, "product_detail.html", context)
~~~
- update folder main.html
~~~
{% extends 'base.html' %}
{% block content %}
    <h1 class="app-detail">
        <span class="app1">{{ app1 }}</span> 
        <span class="app2">{{ app2 }}</span> 
        <span class="app3">{{ app3 }}</span>
    </h1>
    <h5 class="app-detail identity">Name: {{ name }}</h5>
    <h5 class="app-detail identity">Class: {{ class }}</h5>

    <a href="{% url 'main:create_product' %}">
    <button class="add">+ Add Product</button>
    </a>

    <hr>

    <div class="product-list">
    {% if not product_list %}
    <p class="empty-list">Belum ada barang pada pacil store.</p>
    {% else %}

    {% for product in product_list %}
    <div class="product-item">
    {% if product.thumbnail %}
    <img src="{{ product.thumbnail }}" alt="ini thumbnail" width="150" height="100">
    {% else %}
    <img src="https://picsum.photos/200" alt="Lorem Picsum" width="150" height="100">
    <br />
    {% endif %}

    <h2><a href="{% url 'main:show_product' product.id %}">{{ product.name }}</a></h2>

    <p><b>{{ product.get_category_display }}</b>{% if product.is_featured %} | 
        <b>Featured</b>{% endif %} | <i>{{ product.created_at|date:"d M Y H:i" }}</i> 
        | Views: {{ product.product_views }}</p>


    <p>{{ product.description|truncatewords:25 }}...</p>

    <p><a href="{% url 'main:show_product' product.id %}"><button>Read More</button></a></p>
    </div>

    
    {% endfor %}

    {% endif %}
    </div>
{% endblock content %}
~~~
- lalu buat file create_product.html pada folder yang sama denga main.html dan diisi dengan
~~~
{% extends 'base.html' %} 
{% block content %}
<h1>Add Product</h1>

<form method="POST">
  {% csrf_token %}
  <table>
    {{ form.as_table }}
    <tr>
      <td></td>
      <td>
        <input type="submit" value="Add Product" />
      </td>
    </tr>
  </table>
</form>

{% endblock %}
~~~
- selanjutnya buat file product_detail.html pada folder yang sama denga main.html dan diisi dengan
~~~
{% extends 'base.html' %}
{% block content %}
<p><a href="{% url 'main:show_main' %}"><button>← Back to Product List</button></a></p>

<h1>{{ product.name }}</h1>
<p><b>{{ product.get_category_display }}</b>{% if product.is_featured %} | 
    <b>Featured</b>{% endif %} | <i>{{ product.created_at|date:"d M Y, H:i" }}</i> 
    | Views: {{ product.product_views }}</p>

{% if product.thumbnail %}
<img src="{{ product.thumbnail }}" alt="Product thumbnail" width="300">
<br /><br />
{% endif %}

<p>{{ product.description }}</p>

{% endblock content %}
~~~
- tambahkan kode berikut pada file settings.py di folder pacil_store
~~~
CSRF_TRUSTED_ORIGINS = ["<url-deployment-pws-kamu>"]
~~~
- tambahkan method berikut pada views.py di folder main
~~~
def show_xml(request):
     product_list = Product.objects.all()
     xml_data = serializers.serialize("xml", product_list)
     return HttpResponse(xml_data, content_type="application/xml")

def show_xml_by_id(request, news_id):
   try:
       product_item = Product.objects.filter(pk=news_id)
       xml_data = serializers.serialize("xml", product_item)
       return HttpResponse(xml_data, content_type="application/xml")
   except Product.DoesNotExist:
       return HttpResponse(status=404)

def show_json(request):
    product_list = Product.objects.all()
    json_data = serializers.serialize("json", product_list)
    return HttpResponse(json_data, content_type="application/json")

def show_json_by_id(request, news_id):
   try:
       product_item = Product.objects.get(pk=news_id)
       json_data = serializers.serialize("json", [product_item])
       return HttpResponse(json_data, content_type="application/json")
   except Product.DoesNotExist:
       return HttpResponse(status=404)
~~~
- ubah kode di dalam urls.py di folder main dengan 
~~~
from main.views import show_main, create_product, show_product, show_xml, show_json, show_xml_by_id, show_json_by_id

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-product/', create_product, name='create_product'),
    path('product/<str:id>', show_product, name='show_product'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:news_id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:news_id>/', show_json_by_id, name='show_json_by_id'),
]
~~~
- menambahkan kode berikut pada bagian header di file base.html
~~~
<style>

        .app-detail {
            font-family: Arial, sans-serif;
            text-align: center;
            font-size: 40px;
            display: inline-block;
            border: 5px solid black;
            margin-left: 41%;
            padding: 10px 20px;
            border-radius: 8px;
        }

        .app1 {
            color: blue;
            font-weight: bold;
        }

        .app2 {
            font-weight: bold;
        }

        .app3 {
            color: red;
            font-weight: bold;
        }

        .identity {
            color: gray;
            font-weight: normal;
            margin-top: -10px;
            margin-bottom: 10px;
            margin-left: 0px;
            font-size: 10px;
            border: none;
            display: block;
            padding-bottom: 0px;
        }

        .add {
            border-radius: 8px;
            background-color: purple;
            color: white;
            font-weight: bold;
            border: 3px solid black;
        }

        .empty-list {
            font-style: italic;
            color: gray;
            text-align: center;
            margin-top: 14%;
            font-size: 20px;
        }

        button {
            border-radius: 8px;
            background-color: lightgray;
            border: 2px solid black;
            cursor: pointer;
        }

        .product-list {
            display: flex;
            flex-wrap: wrap;
            justify-content: flex-start;
            margin-top: 20px;
        }

        .product-item {
            width: 18%;
            display: flex;
            flex-direction: column;
            margin: 20px;
            padding: 10px;
            padding-left: 60px;
            border: 3px solid black;
            border-radius: 10px;
            box-sizing: border-box;
        }

        .product-item img {
            max-width: 100%;
            padding: 0;
            padding-top: 10%;
            margin:0;
        }

        .product-item button:hover {
            background-color: #ffff00;
        }

    </style>
~~~
- lakukan push ke github dengan github desktop dan ke pws dengan command 
~~~
git push pws master
~~~
- uji coba pada lokal
~~~
python manage.py runserver 
~~~

*pertanyaan enam*

ada kode yang diulang di tutorial yang kadang bikin bingung

*Screenshot postman*

<img width="1915" height="953" alt="image" src="https://github.com/user-attachments/assets/d73b113c-1a7d-43e3-9a78-3b232e8313a0" />
<img width="1916" height="953" alt="image" src="https://github.com/user-attachments/assets/230c1960-4f45-41fd-888f-cb2897749a40" />
<img width="1603" height="953" alt="image" src="https://github.com/user-attachments/assets/6f82d21d-b915-41e7-9a4f-3aee854a20a2" />
<img width="1916" height="954" alt="image" src="https://github.com/user-attachments/assets/acedcb94-95eb-4ea0-861e-eca13194b33e" />


**Tugas 4**

*pertanyaan satu*

AuthenticationForm adalah sebuah class yang disediakan oleh Django buat autentikasi pengguna. Form ini dapat menerima input berupa username dan password dari user dan memverifikasi identitas user.
Kelebihan:
- Sudah siap pakai dan terintegrasi dengan django
- Dapat dimodifikasi
- Built-in password hashing dan validasi

Kekurangan:
- Autentifikasi yang sudah template, tidak bisa selalu sesuai kebutuhan

*pertanyaan dua*

Autentikasi adalah proses untuk memastikan bahwa pengguna adalah pemilik sah credential yang dipakai. Django menggunakan AuthenticationForm.
Otorisasi adalah proses untuk menentukan apa saja yang dapat dilakukan oleh pengguna yang telah terautentikasi. Django menggunkana @login_required.

*pertanyaan tiga*

Session:
    Kelebihan:
    - Data disimpan di server.
    - Session ID disimpan di client.

    Kekurangan:
    - Sesi cepat selesai, terutama saat keluar aplikasi atau menutup browser

Cookies:
    Kelebihan:
    - Data disimpan di browser
    - Bertahan lama sesuai tanggal kadaluarsa (biasanya 90 hari) jadi bisa masuk tanpa login

    Kekurangan:
    - Mudah diserang
    - Size terbatas

*pertanyaan empat*

Ada resiko serangan, seperti XSS (Cross-Site Scripting) dan CSRF (Cross-Site Request Forgery).
Django menangani masalah tersebut dengan salah satunya CSRF token.

*pertanyaan lima*
- tambahkan kode berikut di models.py
~~~
from django.contrib.auth.models import User
user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
~~~
- jalankan command berikut "python manage.py makemigrations | python manage.py migrate" untuk melakukan migrasi model
- Menambahkan beberapa import di views.py pada folder main
~~~
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
~~~
- Tambahkan method register, login, dan logout pada file tersebut juga
~~~
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response
~~~
- tambahkan kode berikut di atas show_main dan show_news
~~~
@login_required(login_url='/login')
~~~
- tambahkan kode berikut di dalam context di method show_main
~~~
'last_login': request.COOKIES.get('last_login', 'Never')
~~~
- ubah kode di urls.py menjadi seperti ini
~~~
from django.urls import path
from main.views import show_main, create_product, show_product, show_xml, show_json, show_xml_by_id, show_json_by_id, register, login_user, logout_user 

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-product/', create_product, name='create_product'),
    path('product/<str:id>', show_product, name='show_product'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:news_id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:news_id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),

]
~~~
- buat file register.html di folder templates dalam main dan isi dengan kode berikut
~~~
{% extends 'base.html' %}

{% block meta %}
<title>Register</title>
{% endblock meta %}

{% block content %}

<div>
  <h1>Register</h1>

  <form method="POST">
    {% csrf_token %}
    <table>
      {{ form.as_table }}
      <tr>
        <td></td>
        <td><input type="submit" name="submit" value="Daftar" /></td>
      </tr>
    </table>
  </form>

  {% if messages %}
  <ul>
    {% for message in messages %}
    <li>{{ message }}</li>
    {% endfor %}
  </ul>
  {% endif %}
</div>

{% endblock content %}
~~~
- buat file login.html di folder templates dalam main dan isi dengan kode berikut
~~~
{% extends 'base.html' %}

{% block meta %}
<title>Login</title>
{% endblock meta %}

{% block content %}
<div class="login">
  <h1>Login</h1>

  <form method="POST" action="">
    {% csrf_token %}
    <table>
      {{ form.as_table }}
      <tr>
        <td></td>
        <td><input class="btn login_btn" type="submit" value="Login" /></td>
      </tr>
    </table>
  </form>

  {% if messages %}
  <ul>
    {% for message in messages %}
    <li>{{ message }}</li>
    {% endfor %}
  </ul>
  {% endif %} Don't have an account yet?
  <a href="{% url 'main:register' %}">Register Now</a>
</div>

{% endblock content %}
~~~
- tambahkan kode berikut pada main.html setelah tombol add product
~~~
    <a href="{% url 'main:logout' %}">
    <button class="logout">Logout</button>
    </a>

    <h5>Sesi terakhir login: {{ last_login }}</h5>

    <hr>

    <a href="?filter=all">
    <button type="button">All Articles</button>
    </a>
    <a href="?filter=my">
        <button type="button">My Articles</button>
    </a> 
~~~
- tambahkan kode berikut pada product_detail.html di bawah product.description
~~~
{% if product.user %}
    <p>Author: {{ product.user.username }}</p>
{% else %}
    <p>Author: Anonymous</p>
{% endif %}
~~~
- terakhir tambahkan kode berikut di bagian head pada base.html
~~~
<a href="{% url 'main:logout' %}"></a>
~~~
- dan ubah kode pada bagian style dengan kode berikut
~~~
        .app-detail {
            font-family: Arial, sans-serif;
            text-align: center;
            font-size: 40px;
            display: inline-block;
            border: 5px solid black;
            margin-left: 41%;
            padding: 10px 20px;
            border-radius: 8px;
        }

        .app1 {
            color: blue;
            font-weight: bold;
        }

        .app2 {
            font-weight: bold;
        }

        .app3 {
            color: red;
            font-weight: bold;
        }

        .identity {
            color: gray;
            font-weight: normal;
            margin-top: -10px;
            margin-bottom: 10px;
            margin-left: 0px;
            font-size: 10px;
            border: none;
            display: block;
            padding-bottom: 0px;
        }

        .add {
            border-radius: 8px;
            background-color: red;
            color: white;
            font-weight: bold;
            border: 3px solid black;
        }

        .add:hover {
            background-color: blue;
        }

        .empty-list {
            font-style: italic;
            color: gray;
            text-align: center;
            margin-top: 11%;
            font-size: 20px;
            margin-left: 41%;
        }

        button {
            border-radius: 8px;
            background-color: lightgray;
            border: 2px solid black;
            cursor: pointer;
        }

        .logout {
            border-radius: 8px;
            background-color: blue;
            color: white;
            font-weight: bold;
            border: 3px solid black;
            float: right;
        }
        
        .logout:hover {
            background-color: red;
        }

        .product-list {
            display: flex;
            flex-wrap: wrap;
            justify-content: flex-start;
            margin-top: 20px;
        }

        .product-item {
            width: 18%;
            display: flex;
            flex-direction: column;
            margin: 15px;
            padding: 10px;
            padding-left: 60px;
            border: 3px solid black;
            border-radius: 10px;
            box-sizing: border-box;
        }

        .product-item img {
            max-width: 100%;
            padding: 0;
            padding-top: 10%;
            margin:0;
        }

        .product-item button:hover {
            color: white;
            background-color: #bf00ff;
        }
~~~

*screenshot akun1*
<img width="1911" height="866" alt="Screenshot 2025-09-23 210333" src="https://github.com/user-attachments/assets/fdbf1266-1904-4420-9a39-b1bec493635a" />

*screenshot akun2*
<img width="1910" height="868" alt="Screenshot 2025-09-23 210426" src="https://github.com/user-attachments/assets/c0137e3e-461e-4382-9964-4f95ee81c272" />

**Tugas 5**

*pertanyaan satu*

urutan dengan prioritas tertinggi:
- inline, style langsung diterapkan pada tag html
- ID selector, lebih memprioritaskan yang menunjuk id daripada tipe tag
- class, karena class tidak unique seperti id maka class ada dibawah prioritas id
- tag, mengubah style pada tag yang dituju

*pertanyaan dua*

karena responsive design memungkinkan aplikasi kita dapat terlihat nyaman di ukuran apapun dan menyesuaikan layout dan kebutuhan
contoh website yang tidak responsive adalah https://arngren.net/ karena tidak menyesuaikan layout untuk ukuran-ukuran tertentu sehingga sulit untuk dilihat dan contoh yang responsive adalah siakNG karena dapat menyesuaikan ukuran layout, seperti mobile, table, desktop, dll.

*pertanyaan tiga*

margin adalah jarak dari antara satu elemen ke elemen lainnya (border ke border). Sedangkan padding adalah jarak dari elemen ke border. Terakhir border adalah pembatas yang berada disekitar elemen (seperti frame atau bingkai foto).

*pertanyaan empat*

flexbox mode display css untuk mengatur dalam sebuah container yang lebih flexibel sesuai namanya fexbile box
grid mode display css untuk mengatur dalam sebuah container dalam dua dimensi yang lebih flexibel dari flexbox

*pertanyaan lima*

- checklist 1: menambahkan fungsi edit_product dan delete_product pada views.py. Lalu tambahkan endpoint pada urls.py. Lalu tambahkan file edit.html pada folder templates di main

- checklist 2,3,4,5,6,7,8: menambahkan tailwind ke file base.html dan membuat card.html untuk mengkustomisasi per-produk. Buat static folder yang diisi folder css dan folder image. Lalu tambahkan png pada image folder dan rename menjadi no-product.png. Buat golbal.css pada file css untuk kustomisasi form. Ubah juga file html yang sudah dikerjakan pada tugas sebelumnya dengan menammbahkan styling pada tag html yang ingin di kustomisasi. Buat file navbar.html pada folder templates di root dan tambahkan stying juga.