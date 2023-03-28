from django import forms
from .models import Product,Diary

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        
class DiaryForm(forms.ModelForm):
    date=forms.DateField(widget=forms.widgets.DateInput(attrs={'type':'date'}))
    
    class Meta:
        model = Diary
        fields = '__all__'