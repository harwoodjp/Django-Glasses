from django.conf.urls import include, url

from . import views



urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^add_item', views.add_item, name='add_item'),
    url(r'^cart_show', views.cart_show, name='cart_show'),
    url(r'^cart_add/(?P<id>[0-9]+)', views.cart_add, name='cart_add'),
    url(r'^cart_remove/(?P<pk>[0-9]+)', views.cart_remove, name='cart_remove'),
    url(r'^edit_item/(?P<id>[0-9]+)/', views.edit_item, name="edit_item"),
]