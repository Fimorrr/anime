"""
Definition of urls for anime.
"""

from datetime import datetime
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
import django.contrib.auth.views

import app.forms
import app.views

# Uncomment the next lines to enable the admin:
from django.conf.urls import include
from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    # Examples:
    url(r'^$', app.views.news, name='news'),
    url(r'^news$', app.views.news, name='news'),
    url(r'^news/(?P<num>\d+)/$', app.views.news_page, name='news'),
    url(r'^projects/(?P<id>\d+)/$', app.views.project, name='project'),
    url(r'^comments/(?P<id>\d+)/$', app.views.comment, name='comments'),
    url(r'^projects/search$', app.views.projects_search, name='projects'),
    url(r'^projects$', app.views.projects, name='projects'),
    url(r'^contact$', app.views.contact, name='contact'),
    url(r'^about', app.views.about, name='about'),
    url(r'^captcha/', include('captcha.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)