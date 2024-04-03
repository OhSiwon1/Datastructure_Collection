from django.db import models

# Create your models here.
class Project(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()

    #years=models.IntegerField()

    #upload = models.FileField(upload_to='uploads/')
    #harts = ??
    
    video=models.URLField()

class Comment(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    content = models.TextField()
    #harts=??