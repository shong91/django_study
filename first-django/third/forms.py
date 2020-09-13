from django.forms import ModelForm
from django import forms
from third.models import Restaurant, Review
from django.utils.translation import gettext_lazy as _

REVIEW_POINT_CHOICES = (
    ('1', 1),
    ('2', 2),
    ('3', 3),
    ('4', 4),
    ('5', 5),
)


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['point', 'comment', 'restaurant']
        labels = {
            'point': _('평점'),
            'comment': _('코멘트'),
        }
        help_texts = {
            'point': _('평점을 입력해주세요. '),
            'comment': _('코멘트를 입력해주세요. '),
        }
        widgets = {
            # rendering 시 form 재정의
            'restaurant': forms.HiddenInput(),
            'point': forms.Select(choices=REVIEW_POINT_CHOICES),
        }


class RestaurantForm(ModelForm):
    class Meta:
        model = Restaurant
        fields = ['name', 'address', 'password', 'image']
        labels = {
            'name': _('이름'),
            'addresss': _('주소'),
            'password': _('게시물 비밀번호'),
            'image': _('이미지 url'),

        }
        help_texts = {
            'name': _('이름을 입력해주세요. '),
            'address': _('주소를 입력해주세요. '),
            'password': _('게시물 비밀번호를 입력해주세요. '),
            'image': _('이미지 url을 입력해주세요.'),
        }
        widgets = {
            'password': forms.PasswordInput()
        }
        error_messages = {
            'name': {
                'max_length': _('이름이 너무 깁니다! ')
            },
            'password': {
                'max_length': _('패스워드가 너무 깁니다! ')
            },
            'image': {
                'max_length': _('이미지 주소의 길이가 너무 깁니다! ')
            }
        }


class UpdateRestaurantForm(RestaurantForm):
    class Meta:
        model = Restaurant
        # 이 form 을 사용할 때, password 는 제외하고 update 함
        exclude = ['password']
