from .models import Product,Diary
from rest_framework import viewsets
from .serializer import ProductSerializer,DiarySerializer
from django.shortcuts import render, get_object_or_404, redirect
from .forms import ProductForm, DiaryForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth.decorators import user_passes_test



@login_required
def private_place(request):
    return HttpResponse("Shhh, members only!", content_type="text/plain")

@user_passes_test(lambda user: user.is_staff)
def staff_place(request):
    return HttpResponse("Employees must wash hands", content_type="text/plain")

def user_info(request):
    text = f"""
        Selected HttpRequest.user attributes:

        username:     {request.user.username}
        is_anonymous: {request.user.is_anonymous}
        is_staff:     {request.user.is_staff}
        is_superuser: {request.user.is_superuser}
        is_active:    {request.user.is_active}
    """

    return HttpResponse(text, content_type="text/plain")
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
    products = diary.products.all()
    total_calories = diary.calories
    total_carbo = diary.total_carbo
    total_fat = diary.total_fat
    total_protein = diary.total_protein
    context={
        'diary': diary,
        'products': products,
        'total':{
            'calories': total_calories,
            'carbo': total_carbo, 
            'protein': total_protein, 
            'fat': total_fat
        }
    }
    return render(request,'diary_detail.html',context)
     
     
def diary_remove_product(request,diary_id,product_id):
    diary=get_object_or_404(Diary,pk=diary_id)
    product=get_object_or_404(Product,pk=product_id)
    diary.products.remove(product)
    return redirect('diary_detail',diary_id=diary_id)

def add_product_to_diary(request, diary_id):
    diary = Diary.objects.get(pk=diary_id)
    all_products = Product.objects.all()

    if request.method == 'POST':
        product_id = request.POST.get('product')
        product = Product.objects.get(pk=product_id)
        diary.products.add(product)
        return redirect('diary_detail', diary_id=diary.id)

    context = {
        'diary': diary,
        'all_products': all_products,
    }

    return render(request, 'diary_add_product.html', context)

    
def update_product_grams(request, diary_id, product_id):
    diary = get_object_or_404(Diary, pk=diary_id)
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        grams = request.POST.get('grams')
        if grams:
            grams = float(grams)
            factor = grams / product.grams
            product.grams = int(grams)
            product.protein = int(round(product.protein * factor))
            product.fat = int(round(product.fat * factor))
            product.carbo = int(round(product.carbo * factor))
            product.calories = round(product.calories()*factor,2)
            product.save()
        return redirect('diary_detail', diary_id=diary_id)



 

 