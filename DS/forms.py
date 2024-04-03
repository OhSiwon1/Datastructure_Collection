from django import forms
from DS.models import Project


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project  # 사용할 모델
        fields = ['title', 'content','video']
        label={
            'title': '제목',
            'content': '내용',
            'video': '영상링크',
        } 