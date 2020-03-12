"""mysite URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include, reverse_lazy
from django.contrib.auth import views as auth_views
from allauth.account.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('accounts/', include('allauth.urls')),
    # path('accounts/login/', auth_views.LoginView.as_view(),name='log'),
    # path('accounts/logout/',auth_views.LogoutView.as_view(),name='logout'),
    path('accounts/password_change',auth_views.PasswordChangeView.as_view(),name='change_password'),
    path('accounts/password_change/done/',auth_views.PasswordChangeDoneView.as_view(template_name='registration/change_password_done.html'),name='password_change_done'),
    path('admin/', admin.site.urls),
    path('blog/',include('blog.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)