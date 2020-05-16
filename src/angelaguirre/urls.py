"""angelaguirre URL Configuration

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
from django.urls import include, path, re_path

# Imports to make to uploaded files work
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import TemplateView

# Importing the portfolio module
from .static_portfolio import ProjectsView

urlpatterns = [
    path('', TemplateView.as_view(template_name='static_pages/index.html'), name='index'),
    path('about/', TemplateView.as_view(template_name='static_pages/about.html'), name='about'),
    path('portfolio/', ProjectsView.as_view(), name='portfolio'),
    path('blog/', include('blog.urls')),
    path('admin/', admin.site.urls),
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
