from django.conf.urls import include, url

from . import views



urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^add_item', views.add_item, name='add_item'),
    url(r'^edit_item/(?P<id>[0-9]+)/', views.edit_item, name="edit_item"),
]