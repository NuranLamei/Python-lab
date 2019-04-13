from django import forms

class AddBookForm(forms.Form):
    title = forms.CharField(label='Title', max_length=100)
    email = forms.CharField(label='Email', max_length=100)
