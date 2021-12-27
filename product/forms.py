from django import forms
from product import models

class OrderForm(forms.ModelForm):
    class Meta:
        model = models.Order
        fields = '__all__'

class CustomerForm(forms.ModelForm):
    class Meta:
        model = models.Customer
        fields = '__all__'

