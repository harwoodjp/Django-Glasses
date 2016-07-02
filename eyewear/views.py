from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.forms import ModelForm, modelformset_factory
import csv
from .models import Item, Cart2, CartItem, Glasses


# Create your views here.



def index(request):
    item_list = Item.objects.all()
    cart_list = Cart2.objects.all()
    template = loader.get_template('eyewear/index.html')
    context = RequestContext(request, {
        'item_list': item_list,
        'cart_list': cart_list,
    })
    return HttpResponse(template.render(context))

def show_glasses(request):
    glasses_list = Glasses.objects.all()
    template = loader.get_template('eyewear/show_glasses.html')
    context = RequestContext(request, {
        'glasses_list': glasses_list,
    })
    return HttpResponse(template.render(context))

def import_csv(request):
    FILE_PATH = 'glasses_csv.csv'
    f = open(FILE_PATH)
    next(f)
    with f as open_csv_file:
        csv_reader = csv.reader(open_csv_file, delimiter=',')
        for row in csv_reader:

            frame_name = (row[4]).strip()
            brand = (row[6]).strip()
            product_group_type = (row[9]).strip()
            frame_color_type = (row[10]).strip()
            gender_type = (row[25]).strip()
            material_type = (row[27]).strip()

            Glasses(frame_name=frame_name, brand=brand, product_group_type=product_group_type,
                    frame_color_type=frame_color_type, gender_type=gender_type,
                    material_type=material_type).save()

    return redirect('/eyewear/show_glasses')




def detail(request, id):
    item = Item.objects.get(pk=id)
    return render(request, 'eyewear/detail.html', {'item': item})

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


def delete_item(request, id):
    Item.objects.filter(pk=id).delete()
    returnURL = '/eyewear/'
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

