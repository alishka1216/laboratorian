from django.shortcuts import render, get_object_or_404, redirect
from webapp.models import Product, category_choices

from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.urls import reverse
from webapp.forms import ProductForm


# Create your views here.

def index_view(request):
    products = Product.objects.all()
    return render(request, 'index.html', context={'products': products})


def product_view(request, pk):
    product = get_object_or_404(Product, id=pk)
    return render(request, 'product_view.html', context={'product': product})


def product_create_view(request):
    if request.method == "GET":
        form = ProductForm()
        return render(request, 'product_create.html', context={'form': form})
    elif request.method == "POST":
        form = ProductForm(data=request.POST)
        if form.is_valid():
            product = Product.objects.create(
                title=form.cleaned_data.get('title'),
                category=form.cleaned_data.get('category'),
                description=form.cleaned_data.get('description'),
                reminder=form.cleaned_data.get('reminder'),
                price=form.cleaned_data.get('price')
            )


        else:
            return render(request, 'product_create.html', context={'form': form})

        return redirect('product-view', pk=product.id)


def product_update_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'GET':
        form = ProductForm(initial={
            'title': product.title,
            'description': product.description,
            'category': product.category,
            'reminder': product.reminder,
            'price': product.price
        })
        return render(request, 'product_update.html', context={'form': form, 'product': product})
    elif request.method == 'POST':
        form = ProductForm(data=request.POST)
        if form.is_valid():
            product.title = form.cleaned_data['title']
            product.description = form.cleaned_data['description']
            product.category = form.cleaned_data['category']
            product.reminder = form.cleaned_data['reminder']
            product.price = form.cleaned_data['price']
            product.save()
            return redirect('product-view', pk=product.pk)
        else:
            return render(request, 'update.html', context={'form': form, 'product': product})


def product_delete_view(request, pk):
    product = get_object_or_404(Product, id=pk)
    if request.method == 'GET':
        return render(request, 'product_delete.html', context={'product': product})
    elif request.method == 'POST':
        product.delete()
    return redirect('product-list')
