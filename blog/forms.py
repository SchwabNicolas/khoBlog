from django import forms

from .models import Post, Comment, Category


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'categories', 'description', 'body', 'post_image')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'bg-dark text-light'}),
            'categories': forms.SelectMultiple(attrs={'class': 'bg-dark text-light'}),
            'description': forms.Textarea(attrs={'class': 'bg-dark text-light'}),
            'body': forms.Textarea(attrs={'class': 'bg-dark text-light'}),
        }


class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'categories', 'description',
                  'body', 'post_image', 'slug', 'private',)

        widgets = {
            'title': forms.TextInput(attrs={'class': 'bg-dark text-light'}),
            'categories': forms.SelectMultiple(attrs={'class': 'bg-dark text-light'}),
            'description': forms.Textarea(attrs={'class': 'bg-dark text-light'}),
            'body': forms.Textarea(attrs={'class': 'bg-dark text-light'}),
            'slug': forms.TextInput(attrs={'class': 'bg-dark text-light'}),
        }


class CategoryAddForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name', 'description', 'private')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'bg-dark text-light'}),
            'description': forms.Textarea(attrs={'class': 'bg-dark text-light'}),
            'private': forms.CheckboxInput(attrs={'class': 'bg-dark text-light'}),
        }


class CategoryEditForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name', 'description', 'slug', 'private')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'bg-dark text-light'}),
            'description': forms.Textarea(attrs={'class': 'bg-dark text-light'}),
            'slug': forms.TextInput(attrs={'class': 'bg-dark text-light'}),
            'private': forms.CheckboxInput(attrs={'class': 'bg-dark text-light'}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'message')

        widgets = {
            'author': forms.TextInput(attrs={'class': 'bg-dark text-light'}),
            'message': forms.Textarea(attrs={'class': 'bg-dark text-light'}),
        }
