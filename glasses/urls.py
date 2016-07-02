"""glasses URL Configuration

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
from django.contrib import admin


urlpatterns = [
    url(r'^eyewear/', include('eyewear.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^eyewear/add_item/', include('eyewear.urls')),
    url(r'^eyewear/delete_item/', include('eyewear.urls')),
    url(r'^eyewear/add_cart/', include('eyewear.urls')),
    url(r'^eyewear/cart_show/', include('eyewear.urls')),
    url(r'^eyewear/cart_remove/(?P<id>[0-9]+)/', include('eyewear.urls')),
    url(r'^edit_item/(?P<id>[0-9]+)/', include('eyewear.urls')),
    url(r'^eyewear/cart2_show/(?P<id>[0-9]+)/$', include('eyewear.urls')),
    url(r'^eyewear/all_carts/', include('eyewear.urls')),
    url(r'^eyewear/cart2_show/(?P<id>[0-9]+)/select_item/$', include('eyewear.urls')),
    url(r'^cart2_show/(?P<cart_id>[0-9]+)/select_item/(?P<item_id>[0-9]+)$', include('eyewear.urls')),
    url(r'^cart2_show/(?P<cart_id>[0-9]+)/select_item/(?P<item_id>[0-9]+)/cartitem_remove/$', include('eyewear.urls')),
    url(r'^show_glasses/', include(admin.site.urls)),
    url(r'^import_csv/', include(admin.site.urls)),



]