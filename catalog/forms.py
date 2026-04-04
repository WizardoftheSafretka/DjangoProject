from django.forms.models import ModelForm

from catalog.models import Product

class StyleFormMixin

class ProductForm(ModelForm):
    class Meta:
        model = Product
        exclude = ('created_at', 'updated_at',)





