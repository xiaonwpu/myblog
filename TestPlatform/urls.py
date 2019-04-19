"""TestPlatform URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from testtools import views
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from testtools.views import index, about, tag, list, show, search
from django.views.static import serve

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index, name='index'),
    url(r'^about', views.about),
    url(r'^s/', views.search, name='search'),
    # url(r'^result/$', search, name='result'),
    url(r"^upload/(?P<path>.*)$", "django.views.static.serve", {"document_root": settings.MEDIA_ROOT, }),
    url('^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    url(r'^ueditor/', include('DjangoUeditor.urls')),
    url(r'^list-<int:lid>', views.list, name='list'),#列表页
    url(r'^show-(\d+)', views.show, name='show'),#内容页
    url(r'^tag/<tag>', views.tag, name='tags'),#标签列表页
    url(r'^s/', views.search, name='search'),#搜索列表页

]
