from django import forms
from . import models


class CreateProductForm(forms.ModelForm):
    class Meta:
        model = models.Product
        fields = (
            "title",
            "profile",
            "content",
            "explanation",
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
            "explanattion": forms.TextInput(attrs={'placeholder': "필요한 설명을 적어주세요"})
            # forms.NumberInput을 사용
        }

        lables = {

        }

    def save(self, *args, **kwargs):
        project = super().save(commit=False)
        repair = self.cleaned_data.get("repair")
        project.repair = repair
        project.save()
        
        return project
