from django import forms

from .models import Category, Post

choices = Category.objects.all().values_list('name', 'name').order_by('-name')


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'title_tag', 'author',
                  'category', 'body', 'referencia']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title goes here...'}),  # noqa: E501
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'id': 'myuser', 'value': '', 'type': 'hidden'}),  # noqa: E501
            # 'author': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Write author name'}),  # noqa: E501
            'category': forms.Select(choices=choices, attrs={'class': 'form-control', 'placeholder': 'Write category name'}),  # noqa: E501
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write something here'}),  # noqa: E501
            'referencia': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write something here'}),  # noqa: E501

        }


class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'title_tag', 'body', 'referencia']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title goes here...'}),  # noqa: E501
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            # 'author': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Write author name'}),  # noqa: E501
            'author': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Write category name'}),  # noqa: E501
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write something here'}),  # noqa: E501
            'referencia': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write something here'}),  # noqa: E501

        }
