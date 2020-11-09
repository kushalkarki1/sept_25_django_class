from django import forms
from home.models import Book

# class BookForm(forms.Form):
#     name = forms.CharField()
#     isbn = forms.CharField()
#     price = forms.CharField()

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ("name", "isbn", "price", "book_image", "author")