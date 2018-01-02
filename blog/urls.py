"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.views.static import serve
from article.views import HomepageView
from article.views import secondpage, articlepage, osw_mainpage, osw_articlelist, osw_article, osw_taglist, Contact_function, Comment_function, Search_function, osw_resources, osw_onlinetest
from blog.settings import MEDIA_ROOT



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'ckeditor/', include('ckeditor_uploader.urls')),
    #url(r'^homepage/', homepage),
    url(r'^$', osw_mainpage, name="osw_mainpage"),
    url(r'^media/(?P<path>.*)$',  serve, {"document_root":MEDIA_ROOT}),
    url(r'^articlelist/(?P<leixing>.*)/$', osw_articlelist, name="osw_articlelist"),
    url(r'^taglist/(?P<biaoqian>.*)/$', osw_taglist, name="osw_taglist"),
    url(r'^article/(?P<article_id>.*)/$', osw_article, name="osw_article"),
    url(r'^contact/$', Contact_function, name="contact"),
    url(r'^comment/(?P<article_id>.*)/$', Comment_function, name="comment"),
    url(r'^search/$', Search_function, name="search"),
    url(r'^resources/$', osw_resources, name="osw_resources"),
    url(r'^onlinetest/$', osw_onlinetest, name="osw_onlinetest"),
]






