from django.forms import ModelForm, TextInput, Textarea, NumberInput, Select, ClearableFileInput
from .models import Author, Book

class BookForm(ModelForm):
    class Meta:
        model=Book
        fields='__all__'
        widgets={
           "author": Select(attrs={
               "class": "form-select col-md-6"
           }),
           "title": TextInput(attrs={
                "class": "form-control col-md-6",
                "placeholder": "input title"
           }),
           "image": ClearableFileInput(attrs={
               "class": "form-control"
           }),
           "price": NumberInput(attrs={
               "class": "form-control col-12",
               "placeholder": 'input price'
           }),
           "description": Textarea(attrs={
               "class": "form-control col-12",
               "placeholder": "input description",
           })
        }


class AuthorForm(ModelForm):
    class Meta:
        model=Author
        fields='__all__'
        widgets={
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'input name'
            }),
            "bio": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'input bio'
            })
        }