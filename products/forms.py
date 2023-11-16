from django import forms
from . import models


class CreateProductForm(forms.ModelForm):
    class Meta:
        model = models.Product
        fields = (
            "title",
            "profile",
            "content",
            "price",
            "department",
            "species",
            "grade",
            "repair",

            "team_number",
            "meet",
            "category",
            "framework"
        )
        widgets = {
            "title": forms.TextInput(attrs={'placeholder': '프로젝트 이름'}),
            "content": forms.TextInput(attrs={'placeholder': '간단한 설명을 적어주세요'}),
            "thumnail_img": forms.FileInput(attrs={'placeholder': '사용할 이미지를 넣어주세요'}),
            # forms.NumberInput을 사용
            "price": forms.NumberInput(attrs={'placeholder': '가격을 입력하세요'}),

        }

        lables = {

        }

    def save(self, *args, **kwargs):
        project = super().save(commit=False)
        return project
