from django.shortcuts import render,render_to_response, redirect
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.forms import ModelForm, modelformset_factory

from .models import item, cart



# Create your views here.

def index(request):
    item_list = item.objects.all()
    template = loader.get_template('eyewear/index.html')
    context = RequestContext(request, {
        'item_list': item_list,
    })
    return HttpResponse(template.render(context))

def cart_show(request):
    cart_list = cart.objects.all()
    template = loader.get_template('eyewear/cart_show.html')
    context = RequestContext(request, {
        'cart_list': cart_list,
    })
    return HttpResponse(template.render(context))

def cart_add(request, id):
    thisItem = item.objects.get(pk=id).__str__()
    toAdd = cart(item = thisItem)
    toAdd.save()
    return redirect('/eyewear/cart_show')

def cart_remove(request, pk):
    cart.objects.get(pk = pk).delete()
    return redirect('/eyewear/cart_show')


def detail(request, id):
    thisItem = item.objects.get(pk=id)
    return render(request, 'eyewear/detail.html', {'item': thisItem})

def add_item(request):

    addForm = modelformset_factory(item, fields=("name", "description","price"))
    formset = addForm()
    if request.method == 'POST':
        formset = addForm(request.POST)
        formset.save()
        return redirect('/eyewear/')

    return render_to_response("eyewear/add.html", {"formset": formset,} )


def edit_item(request, id):

    class ItemForm(ModelForm):
        class Meta:
            model = item
            fields = ['name','description','price']

    thisItem = item.objects.get(pk=id)
    form = ItemForm(instance=thisItem)
    print("request = " + str(dir(request)))
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=thisItem)
        form.save()
        return redirect('/eyewear/')

    return render_to_response("eyewear/edit_item.html", {"form": form,})


