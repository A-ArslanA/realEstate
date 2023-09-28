from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Property, RentHistory, Review, FAQ
from django.forms import ModelForm, TextInput, Textarea, NumberInput, DateInput, EmailInput

class NewUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')


class AddPropertyForm(ModelForm):
    class Meta:
        model = Property
        fields = ('name', 'description', 'price', 'address', 'bedrooms', 'bathrooms', 'squareArea', 'repairQuality', 'photo', 'status', 'isRent', 'isBuy', 'owner')

        owner = forms.ModelChoiceField(
            widget=forms.HiddenInput,
            queryset=User.objects.all(),
            initial=lambda request: request.user
        )

        widgets = {
            "name": TextInput(attrs={
                "placeholder": "Name: "
            }),
            "description": Textarea(attrs={
                "placeholder": "Description: "
            }),
            "price": NumberInput(attrs={
                "placeholder": "Price: "
            }),
            "address": TextInput(attrs={
                "placeholder": "Address: "
            }),
            "bedrooms": NumberInput(attrs={
                "placeholder": "Bedrooms: "
            }),
            "bathrooms": NumberInput(attrs={
                "placeholder": "Bathrooms: "
            }),
            "squareArea": NumberInput(attrs={
                "placeholder": "SquareArea: "
            }),
            "repairQuality": TextInput(attrs={
                "placeholder": "RepairQuality: "
            }),
            "photo": TextInput(attrs={
                "placeholder": "Photo: "
            }),
        }


# class RentForm(forms.ModelForm):
#     class Meta:
#         model = RentHistory
#         fields = ['rental_start_date', 'rental_end_date']
#
#         widgets = {
#             "rental_start_date": DateInput(),
#             "rental_end_date": DateInput(),
#         }


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['text']

        widgets = {
            "text": TextInput(attrs={
                "placeholder": "Rewiew",
            })
        }


class FAQForm(forms.ModelForm):
    class Meta:
        model = FAQ
        fields = ['email']

        widgets = {
            "email": EmailInput(attrs={
                "placeholder": "Your Email",
                "class": "input_field",
                "id": "email",

            })
        }