from django import forms
from DS.models import Project, Comment, Year


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project  # 사용할 모델
        fields = ['title', 'content','video','year']
        label={
            'title': '제목',
            'content': '내용',
            'video': '영상링크',
            'year':'제작연도'
        } 

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        labels = {
            'content': '답변내용',
        }
