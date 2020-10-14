"""houtai URL Configuration

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
from django.conf.urls import include
from Result import urls as Result_urls
from Bumen import urls as Bumen_urls
from Renyuan import urls as Renyuan_urls
from Fangan import urls as Fangan_urls
from others import urls as others_urls
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('zuzhibu/result/', include(Result_urls)),
    path('zuzhibu/bumen/', include(Bumen_urls)),
    path('zuzhibu/renyuan/', include(Renyuan_urls)),
    path('zuzhibu/fangan/', include(Fangan_urls)),
    path('zuzhibu/others/', include(others_urls))
]
# 允许所有的media文件被访问
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
