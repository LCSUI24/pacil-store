# pacil-store
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
{   
    DB_NAME=<nama database>
    DB_HOST=<host database>
    DB_PORT=<port database>
    DB_USER=<username database>
    DB_PASSWORD=<password database>
    SCHEMA=tugas_individu
    PRODUCTION=True
}
- menambahkan kode berikut pada file settings.py 
{
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
}
- jalankan command berikut untuk migration "python manage.py migrate"
- buat file git ignore diisi dengan 
{
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
}
- buat aplikasi bernama main dengan command "python manage.py startapp main"
- tambahkan atribut 'main' pada INSTALLED-APPS di settings.py yang ada di folder pacil_store
- mengubah file models.py pada folder main dan diisi dengan 
{
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
}
- jalankan command berikut "python manage.py makemigrations | python manage.py migrate" untuk melakukan migrasi model
- tambahkan kode berikut pada views.py di folder main
{
    from django.shortcuts import render

    def show_main(request):
        context = {
            'app' : 'Pacil Store',
            'name': 'Cyrillo Praditya Soeharto',
            'class': 'PBP B'
        }

        return render(request, "main.html", context)
}
- pada folder main buat folder templates dan buat file "main.html" lalu diisi dengan kode berikut
{
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
}
- buat file utls.py pada folder main lalu diisi denga kode 
{
    from django.urls import path
    from main.views import show_main

    app_name = 'main'

    urlpatterns = [
        path('', show_main, name='show_main'),
    ]
}
- tambahkan kode berikut pada file urls.py di folder pacil_store
{
    from django.urls import path, include

    dan tambahkan kode ini pada urlpatterns "path('', include('main.urls')),"
}
- buka laman "https://pbp.cs.ui.ac.id" dan lakukan login denga sso 
- create new project dan namai pacilstore
- save credential dan command yang diberikan
- pada tab environs pilih raw editor dan masukkan isi dari file.env.prod 
- tambahkan URL deployment pws di ALLOWED_HOSTS pada file settings.py di folder pacil_store
- commit dan push ke github
- jalankan command yang diberikan pws lalu push ke pws

*pertanyaan dua*
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