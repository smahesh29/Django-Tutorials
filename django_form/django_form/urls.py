"""django_form URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views as myapp_views
from model_form import views as model_form_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',myapp_views.get_name, name='name'),
    path('form/',myapp_views.html_form, name='html_form'),
    path('mail/',myapp_views.mail, name='mail_form'),
    path('author/',model_form_views.author, name='author'),
    path('author_1/',model_form_views.author_1, name='author_1'),
    path('author_2/',model_form_views.author_2, name='author_2'),
    path('author_3/',model_form_views.author_3, name='author_3'),
    path('author_4/',model_form_views.author_4, name='author_4'),
    path('author_5/',model_form_views.author_5, name='author_5'),
    path('book/',model_form_views.book, name='book'),
]
