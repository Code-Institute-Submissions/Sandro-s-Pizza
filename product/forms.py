from django import forms
from .models import Item
from .widgets import CustomClearableFileInput


class ProductForm(forms.ModelForm):
    """Form for Item model"""
    class Meta:
        """Defines model, fileds and widgets for form"""
        model = Item
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Product name'}),
            'ingredients': forms.TextInput(
                attrs={'placeholder': '(Ingredients)'}),
            'price': forms.TextInput(
                attrs={'placeholder': 'price'}),
        }
    image = forms.ImageField(
        label='Image', required=False, widget=CustomClearableFileInput)
