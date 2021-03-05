from django.shortcuts import render


# Create your views here.

def index_view(request):
    products = Product.objects.all()
    return render(request, 'index.html', context={'products': products})
