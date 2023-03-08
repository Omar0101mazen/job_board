from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify

# Create your models here.

def photo(inc,file_name):
    img_name,extention = file_name.split(".")
    return "jobs/%s.%s"%(inc.id,extention)
 
 
class job(models.Model): 
    Job_Type = (
        ('full time','full time'),
        ('part time','part time'),
    )
    owner = models.ForeignKey(User,related_name='job_owner',on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    #location
    job_type = models.CharField(max_length = 50,choices =Job_Type)
    description = models.TextField(max_length = 1000)
    published_at = models.DateTimeField(auto_now=True)
    Vacancy = models.IntegerField(default = 1)
    salary = models.IntegerField(default = 0)
    experience =  models.IntegerField(default = 1)
    category = models.ForeignKey('Category',on_delete=models.CASCADE)
    img = models.ImageField(upload_to = photo,blank=True,null=True)
    Country = models.CharField(max_length=50)
    slug = models.SlugField(blank=True,null=True)
    
    
    def save(self,*args, **kwargs):
        self.slug = slugify(self.title)
        super(job,self).save(*args, **kwargs)
        
        
    def __str__(self) :
        return self.title
    
    
class Category(models.Model):
    name = models.CharField(max_length = 50)
    photo_cat = models.ImageField(upload_to='cat_photo/%y/%m')
    def __str__(self) :
        return self.name
    
    
    


class apply(models.Model):
        name = models.CharField(max_length=50)
        email = models.EmailField(max_length=254)
        websit = models.URLField()
        cv = models.FileField(upload_to='aplly/')
        coverletter = models.TextField()
        published_at = models.DateTimeField(auto_now=True)
        titl = models.ForeignKey(job, related_name=("aplly_job"), on_delete=models.CASCADE)
        
        def __str__(self) :
           return self.name
        
        

    