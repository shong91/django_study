# from django import forms
from django.forms import ModelForm
from second.models import Post
from django.utils.translation import gettext_lazy as _

# class PostForm(forms.Form):
#     title = forms.CharField(label='제목', max_length=5)
#     content = forms.CharField(label='내용', widget=forms.Textarea)
#     checkbox = forms.BooleanField(required=False)
#     radiobutton = forms.ChoiceField(choices=(('A', 1), ('B', 2)))


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
        labels = {
            'title': _('제목'),
            'content': _('내용')
        }
        help_texts = {
            'title': _('제목을 입력해주세요. '),
            'content': _('내용을 입력해주세요. ')
        }
        error_messages = {
            'name': {
                'max_length': _('제목이 너무 깁니다. (최대 30자)'),

            }
        }
