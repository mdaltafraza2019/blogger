from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    cat_title=models.CharField(max_length=200)
    description=models.CharField(max_length=200,default=None, null=True,blank=True)

    def __str__(self):
        return self.cat_title
    
class Post(models.Model):
    title=models.CharField(max_length=100)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    content=models.TextField()
    image=models.ImageField(upload_to='media')
    date_of_pub=models.DateTimeField(auto_now_add=True)
    author=models.ForeignKey(User,on_delete=models.CASCADE ,null=True ,blank=True)


    def __str__(self):
        return self.title +" "+ self.category.cat_title

