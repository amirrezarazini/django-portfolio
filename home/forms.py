from django import forms
from .models import Comment, BlogPostComment, ContactMessage


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']
        widgets = {
            'body': forms.Textarea(attrs={
                'class': 'textarea form-control',
                'rows': 1,
                'placeholder': 'نوشتن دیدگاه ...'
            }),
        }


# forms.py
class BlogPostCommentForm(forms.ModelForm):
    class Meta:
        model = BlogPostComment
        fields = ['body', 'parent']


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'ایمیل'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'پیامت رو بنویس...'}),
        }
