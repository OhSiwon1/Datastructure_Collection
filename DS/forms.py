from django import forms
from DS.models import Project, Comment, Year


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project  # 사용할 모델
        fields = ['title', 'content','video','year','imgfile','uploadedFile','abstract','hashtag']
        label={
            'title': '제목',
            'content': '내용',
            'video': '영상링크',
            'year':'제작연도',
            'imgfile':'이미지',
            'uploadedFile':'프로그램파일',
            'abstract': '짧은설명',
            'hashtag':'해시태그',
        } 

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        labels = {
            'content': '답변내용',
        }
