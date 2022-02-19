"""temp_assign URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from unicodedata import name
from django.contrib import admin
from django.urls import path,include
from doctor import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/',include('blog.urls')),
    path('',views.home,name='home'),
    path('register',views.userform,name='register'),
    path('dashboard/',views.dashb,name='dashboard'),
    path('appoint/',views.doc_list,name='appointment'),
    path('book/<id>/',views.book,name='book'),
    path('login/',auth_views.LoginView.as_view(template_name='doctor/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='doctor/logout.html'),name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
