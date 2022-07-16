"""mycafe URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from . import views
from mycafe.views import Order
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('admin/',admin.site.urls),
	path('home', views.index , name='name'),
    path('', views.index , name='name'),
	path('reservations',views.reservations,name='name'),
	path('aboutus',views.aboutus,name='name'),
	path('contact',views.contact,name='name'),
	path('menu',views.menu,name='name'),
    path('order',Order.as_view(),name='order'),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)