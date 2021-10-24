"""reflector URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import include, path

from account import views as views_account
from journal import views as views_journal


urlpatterns = [
    path('', views_journal.index, name='index'),
    path('admin/', admin.site.urls),
    path('journal/', include('journal.urls')),
    path('account/', include('account.urls')),
    path('accounts/profile/', views_account.profile, name="profile"),
    path('accounts/login/', views_account.redirect_login, name="login_redirect"),
    path('register/', views_account.register, name="register"),
    path('usage/', views_journal.usage, name="usage"),
    path('significance/', views_journal.significance, name="significance"),
]
