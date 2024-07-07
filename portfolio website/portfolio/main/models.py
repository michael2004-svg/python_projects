from django.db import models

class tag(models.Model):
    name=models.CharField(max_length=200,unique=True)
    
    def __str__(self):
        return self.name
    

# Create your models here.
class Project(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField()
    tags=models.ManyToManyField(tag,related_name="projects")
    links=models.URLField(max_length=200,blank=True)
    
    def __str__(self):
        return self.title
class projectImage(models.Model):
    project=models.ForeignKey(Project,related_name="images",on_delete=models.CASCADE)
    IMAGE =models.ImageField(upload_to="project_images/")
    
    def __str__(self):
        return f"{self.project.title} image"