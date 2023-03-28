from .models import Product,Diary
from rest_framework import viewsets
from .serializer import ProductSerializer,DiarySerializer
from django.shortcuts import render, get_object_or_404, redirect
from .forms import ProductForm, DiaryForm

class ProductViewSet(viewsets.ModelViewSet):
    queryset=Product.objects.all()
    serializer_class = ProductSerializer
    
class DiaryViewSet(viewsets.ModelViewSet):
    queryset=Diary.objects.all()
    serializer_class  = DiarySerializer
    
def product_list(request):
    products = Product.objects.all()
    return render(request,'product_list.html',{'products':products})

def add_product(request):
    if request.method =='POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request,'add_product.html',{'form':form})

def remove_product(request, product_id):
    product=get_object_or_404(Product,pk=product_id)
    if request.method=='POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'product_list.html', {'product': product})

def update_product(request,product_id):
    product=get_object_or_404(Product,id=product_id)
    if request.method=='POST':
        form = ProductForm(request.POST,instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    
    else:
        form = ProductForm(instance=product)
    return render(request,'update_product.html',{'form':form})

def add_diary(request):
    if request.method=="POST":
        form = DiaryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('diary_list')
    else:
        form=DiaryForm()
    return render(request,'add_diary.html',{'form':form})


def diary_list(request):
    diary=Diary.objects.all()
    return render(request,'diary_list.html',{'diarys':diary})

def diary_detail(request,diary_id):
    diary = get_object_or_404(Diary,pk=diary_id)
    products=diary.products.all()
    total_calories=diary.calories()
    return render(request, 'diary_detail.html', {'diary': diary, 'products': products, 'total_calories': total_calories})

def diary_remove_product(request,diary_id,product_id):
    diary=get_object_or_404(Diary,pk=diary_id)
    product=get_object_or_404(Product,pk=product_id)
    diary.products.remove(product)
    return redirect('diary_detail',diary_id=diary_id)

def diary_add_product(request,diary_id):
    diary=get_object_or_404(Diary,pk=diary_id)
    if request.method=='POST':
        product_id=request.POST.get('product')
        product=get_object_or_404(Product,pk=product_id)
        if product not in diary.products.all():
            diary.products.add(product)
        return redirect('diary_detail',diary_id=diary_id)

    all_products = Product.objects.all()
    return render(request, 'diary_add_product.html', {'diary': diary, 'all_products': all_products})



 

 