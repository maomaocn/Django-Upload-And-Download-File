"""filetransport URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
#from django.contrib import admin

urlpatterns = [
    #url(r'^admin/', include(admin.site.urls)),
	url(r'^login/$','myTransport.views.mylogin'),
	url(r'^login_for_polar/$','myTransport.views.login_for_polar'),
	url(r'^logout/$','myTransport.views.logout'),
	url(r'^index/$','myTransport.views.index'),
	url(r'^transport/(upload|page|file_list)/$','myTransport.views.upload_file'),
	url(r'^transport/(downloadFile|downloadDir)/$','myTransport.views.download_file'),
	url(r'^transport/createDir/$','myTransport.views.createDir'),
	url(r'^transport/removeFile/$','myTransport.views.removeFile'),
	url(r'^transport/user_(get|page|add|del|update)/$','myTransport.views.userOption'),

	url(r'^log/(page|getLogData)/$','myTransport.views.logOption'),
]