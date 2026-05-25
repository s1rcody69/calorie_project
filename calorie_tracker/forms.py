from django import forms
from .models import FoodItem

class FoodItemForm(forms.ModelForm):
    """Form for adding and editing food items."""
    class Meta:
        model = FoodItem
        fields = ['name', 'calories']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'e.g. Chicken Rice', 'class': 'input-field'}),
            'calories': forms.NumberInput(attrs={'placeholder': 'e.g. 450', 'class': 'input-field'}),
        }