from django.conf.urls import include, url

from . import views



urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^add_item', views.add_item, name='add_item'),
   # url(r'^cart_show', views.cart_show, name='cart_show'),
    url(r'^add_cart', views.add_cart, name='add_cart'),
  #  url(r'^cart_add/(?P<id>[0-9]+)', views.cart_add, name='cart_add'),
  #  url(r'^cart_remove/(?P<pk>[0-9]+)', views.cart_remove, name='cart_remove'),
    url(r'^edit_item/(?P<id>[0-9]+)/', views.edit_item, name="edit_item"),
    url(r'^cart2_show/(?P<cart_id>[0-9]+)/$', views.cart2_show, name='cart2_show'),

    url(r'^cart2_show/(?P<cart_id>[0-9]+)/select_item/$', views.select_item, name='select_item'),
    url(r'^cart2_show/(?P<cart_id>[0-9]+)/select_item/(?P<item_id>[0-9]+)$', views.add_to_cart, name='add_to_cart'),
    url(r'^cart2_show/(?P<cart_id>[0-9]+)/select_item/(?P<item_id>[0-9]+)/cartitem_remove/$', views.cartitem_remove, name='cartitem_remove'),
    url(r'^all_carts', views.all_carts, name='cart_show'),


]