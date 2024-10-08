from django import forms
from pybo.models import Menu

class MenuSearchForm(forms.Form):
    TYPE_CHOICES = [
        ('', '고르지 않음'),
        ('한식', '한식'),
        ('양식', '양식'),
        ('중식', '중식'),
        ('일식', '일식'),
        ('기타', '기타'),
    ]
    location_CHOICES = [
        ('', '고르지 않음'),
        ('충정로', '충정로'),
        ('아현동', '아현동'),
        ('풍산빌딩 지하', '풍산빌딩 지하'),
        ('서대문', '서대문'),
    ]

    type = forms.ChoiceField(choices=TYPE_CHOICES, required=False, widget=forms.RadioSelect, label='음식 종류')
    location = forms.ChoiceField(choices=location_CHOICES, required=False, widget=forms.RadioSelect, label='지역')

class MenuCreateForm(forms.ModelForm):
    class Meta:
        model = Menu  # 사용할 모델
        fields = ['name', 'type','distance','location','price','menu_detail']
        labels = {
            'name': '식당이름',
            'type': '종류',
            'distance': '거리',
            'location': '위치',
            'price': '가격',
            'menu_detail': '메뉴들',
        }
        # QuestionForm에서 사용할 Question 모델의 속성
