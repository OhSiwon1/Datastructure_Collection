from django.db import models
from common.models import User
import os

# Create your models here.
class Year(models.Model):
    year=models.CharField(max_length=10)
    def __str__(self):
        return self.year

class Hashtag(models.Model):
    content = models.TextField(unique=True)
    def __str__(self):
        return self.content


class Project(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField(blank=True,default="")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_project')
    year=models.ForeignKey(Year,on_delete=models.CASCADE)
    uploadedFile = models.FileField(upload_to="zipfile/",null=True)
    harts = models.ManyToManyField(User, related_name='hart_project',blank=True)
    video=models.URLField()
    imgfile = models.ImageField(null=True, upload_to="")
    abstract=models.CharField(max_length=100,blank=True,default="")
    hashtag=models.ManyToManyField(Hashtag,related_name='project_hashtag',blank=True)
    member=models.CharField(max_length=100)
    poster=models.FileField(upload_to="paperfile/",null=True)
    repoter=models.FileField(upload_to="repoter/",null=True)

    def __str__(self):
        return self.title
    
        # 첨부 파일명 반환
    def get_file_name(self):
        return os.path.basename(self.uploadedFile.name)
    def get_file_names(self):
        return os.path.basename(self.repoter.name)
    

class Comment(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)


def year_lists(request):
    years = Year.objects.all()  # 필요한 데이터를 쿼리합니다
    return {'year_lists': years}
