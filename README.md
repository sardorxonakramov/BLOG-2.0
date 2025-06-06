# Django Project Setup

Follow these steps to set up and run the Django project locally.

## 1. Create and Activate Virtual Environment

Create a virtual environment to manage project dependencies.

For **Mac/Linux**:

```bash

python3 -m venv .venv
source .venv/bin/activate
```
----------
windows
```bash
python -m venv .venv
.venv\Scripts\activate
```

```bash
pip install -r requirements.txt
python manage.py migrate

python manage.py createsuperuser
```

```bash
python manage.py runserver
```

---

Bu **`README.md`** faylida loyiha o'rnatilishi va ishga tushirilishi uchun kerakli barcha qadamlar aniq ko'rsatilgan. Unga loyiha haqida qisqacha ma'lumot, talablarga muvofiq qadamlar va serverni ishga tushirish bo'yicha ko'rsatmalar ham kiritilgan.



----------------------------






# CKEditor 4 ni Django loyihasiga qo'shish

Bu qo'llanma `django-ckeditor` kutubxonasidan foydalanib, `CKEditor 4` ni Django loyihasiga qanday integratsiya qilishni tushuntiradi.

## 1. CKEditor kutubxonasini o'rnatish

Django loyihangizga CKEditor 4 ni qo'shish uchun quyidagi buyruqni ishga tushiring:

```sh
pip install django-ckeditor
```

## 2. Django loyihasiga CKEditor ni qo'shish

### `settings.py` faylini sozlash

`INSTALLED_APPS` ga `ckeditor` va `ckeditor_uploader` ni qo'shing:

```python
INSTALLED_APPS = [
    ...
    'ckeditor',
    'ckeditor_uploader',
]
```

`MEDIA_URL` va `MEDIA_ROOT` ni sozlang:

```python
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

CKEDITOR_UPLOAD_PATH = 'uploads/'
```

### CKEditor sozlamalari

`settings.py` faylida CKEditor sozlamalarini qo'shing:

```python
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
        'height': 300,
        'width': '100%',
    },
}
```

## 3. CKEditor bilan model yaratish

Misol uchun, `Post` modeli uchun CKEditor maydonidan foydalanamiz:

```python
from django.db import models
from ckeditor.fields import RichTextField

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = RichTextField()
    
    def __str__(self):
        return self.title
```

## 4. CKEditor yuklovchisini ishlatish (ixtiyoriy)

Agar CKEditor orqali fayllarni yuklash funksiyasini qo‘shmoqchi bo‘lsangiz, quyidagicha model yaratishingiz kerak:

```python
from ckeditor_uploader.fields import RichTextUploadingField

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = RichTextUploadingField()
```

## 5. `urls.py` sozlash

`urls.py` faylida CKEditor media fayllarini qo'shing:

```python
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
    path('ckeditor/', include('ckeditor_uploader.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

## 6. CKEditor ni `forms.py` ichida ishlatish

Agar CKEditor ni formalar orqali ishlatmoqchi bo‘lsangiz, quyidagi kabi foydalanishingiz mumkin:

```python
from django import forms
from .models import Post
from ckeditor.widgets import CKEditorWidget

class PostForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())
    
    class Meta:
        model = Post
        fields = ['title', 'content']
```

## 7. Admin panelda CKEditor ni faollashtirish

Admin panelda CKEditor ni ishlatish uchun:

```python
from django.contrib import admin
from .models import Post
from ckeditor.widgets import CKEditorWidget
from django.db import models

class PostAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget()},
    }

admin.site.register(Post, PostAdmin)
```

## 8. Django migration va serverni ishga tushirish

Loyihani yangilash va serverni ishga tushirish uchun quyidagi buyruqlarni bajaring:

```sh
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

Endi CKEditor 4 Django loyihangizda ishlaydi! ✅

---
Agar savollaringiz bo'lsa, bemalol so'rashingiz mumkin! 🚀


# ISHLATISH UCHUN COLLECT STATIK QILISH KERAK
