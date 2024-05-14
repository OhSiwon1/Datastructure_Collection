from django.db import models
from common.models import User
import os

# Create your models here.
class Year(models.Model):
    year=models.CharField(max_length=10)
    def __str__(self):
        return self.year


class Project(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_project')
    year=models.ForeignKey(Year,on_delete=models.CASCADE)
    uploadedFile = models.FileField(upload_to="zipfile/",null=True, blank=True)
    harts = models.ManyToManyField(User, related_name='hart_project')  # 추천인 추가
    video=models.URLField()
    imgfile = models.ImageField(null=True, upload_to="", blank=True) # 이미지 컬럼 추가
    abstract=models.CharField(max_length=100)


    def __str__(self):
        return self.title
    
        # 첨부 파일명 반환
    def get_file_name(self):
        return os.path.basename(self.uploadedFile.name)
    

class Comment(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    #harts=??

