"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, reverse_lazy
from .views import home_page, contact_page, about_page, login_page, register_page
from django.contrib.auth.views import LoginView, LogoutView
from carts.views import cart_home

urlpatterns = [
	path('', home_page,name='home'),
	path('about/', about_page, name='about'),
	path('contact/', contact_page, name='contact'),
	path('register/', register_page,name='register'),
	path('cart/', include("carts.urls",namespace="cart")),
	path('login/', login_page,name='login'),
	path('logout/', LogoutView.as_view(next_page=reverse_lazy('home')),name='logout'),
	path('products/', include("products.urls",namespace="products")),
	path('search/', include("search.urls",namespace="search")),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
	urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)