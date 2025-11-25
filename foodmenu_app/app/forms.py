from django import forms
from .models import Item
class Itemform(forms.ModelForm):
    class Meta:
        model=Item
        fields = ['Item_Name','Item_desc','Item_price','Item_image']