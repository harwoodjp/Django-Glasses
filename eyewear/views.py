from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.forms import ModelForm, modelformset_factory

from .models import Item, Cart2, CartItem


# Create your views here.

def index(request):
    item_list = Item.objects.all()
    cart_list = Cart2.objects.all()
    clSize = len(cart_list)
    template = loader.get_template('eyewear/index.html')
    context = RequestContext(request, {
        'item_list': item_list,
        'cart_list': cart_list,
        'clSize' : clSize,
    })
    return HttpResponse(template.render(context))

def detail(request, id):
    thisItem = Item.objects.get(pk=id)
    return render(request, 'eyewear/detail.html', {'item': thisItem})

def add_item(request):

    addForm = modelformset_factory(Item, fields=("name", "description","price"))
    formset = addForm()
    if request.method == 'POST':
        formset = addForm(request.POST)
        formset.save()
        return redirect('/eyewear/')

    return render_to_response("eyewear/add.html", {"formset": formset,} )


def edit_item(request, id):

    class ItemForm(ModelForm):
        class Meta:
            model = Item
            fields = ['name','description','price']

    thisItem = Item.objects.get(pk=id)
    form = ItemForm(instance=thisItem)
    print("request = " + str(dir(request)))
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=thisItem)
        form.save()
        return redirect('/eyewear/')

    return render_to_response("eyewear/edit_item.html", {"form": form,})


      #               Cart re-do:

def all_carts(request):
    cart_list = Cart2.objects.all()
    template = loader.get_template('eyewear/all_carts.html')
    context = RequestContext(request, {
        'cart_list': cart_list,
    })
    return HttpResponse(template.render(context))


def cart2_show(request, cart_id):
    #cartitem_list = CartItem.objects.filter(cart = id)
    cart = Cart2.objects.get(pk=cart_id)
    template = loader.get_template('eyewear/cart2_show.html')
    context = RequestContext(request, {
        'cart': cart,
    })
    return HttpResponse(template.render(context))

def add_cart(request):

    addForm = modelformset_factory(Cart2, fields=("owner", "name"))
    formset = addForm()
    if request.method == 'POST':
        formset = addForm(request.POST)
        formset.save()
        return redirect('/eyewear/all_carts.html')

    return render_to_response("eyewear/add_cart.html", {"formset": formset,} )


def select_item(request, cart_id):
    cart = Cart2.objects.get(pk=cart_id)
    item_list = Item.objects.all()
    template = loader.get_template('eyewear/select_item.html')
    context = RequestContext(request, {
        'item_list': item_list,
        'cart': cart,
    })
    return HttpResponse(template.render(context))

def add_to_cart(request, cart_id, item_id):
    cart = Cart2.objects.get(pk=cart_id)
    item = Item.objects.get(pk=item_id)
    CartItem(cart=cart, item=item).save()
    returnURL = '/eyewear/cart2_show/' + str(cart_id) + '/select_item/'
    return redirect(returnURL)

def cartitem_remove(request, cart_id, item_id):
    cart = Cart2.objects.get(pk=cart_id)
    item = Item.objects.get(pk=item_id)
    CartItem.objects.filter(cart=cart, item=item).delete()
    returnURL = '/eyewear/cart2_show/' + str(cart_id) + '/select_item/'
    return redirect(returnURL)


  #        OLD CART views
# def cart_add(request, id):
#     thisItem = Item.objects.get(pk=id).__str__()
#     toAdd = Cart(item = thisItem)
#     toAdd.save()
#     return redirect('/eyewear/cart_show')
#
# def cart_remove(request, pk):
#     Cart.objects.get(pk = pk).delete()
#     return redirect('/eyewear/cart_show')
#
# def cart_show(request):
#     cart_list = Cart.objects.all()
#     template = loader.get_template('eyewear/cart_show.html')
#     context = RequestContext(request, {
#         'cart_list': cart_list,
#     })
#     return HttpResponse(template.render(context))
#

 #         ------------->

