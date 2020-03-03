from django.db import models

# Create your models here.
class App(models.Model):
    appname=models.CharField(max_length=250)
    Description=models.CharField(max_length=400)
    Developer=models.CharField(max_length=500)
    Size=models.CharField(max_length=20)

    def __str__(self):
        return self.appname


class User(models.Model):
    Name=models.CharField(max_length=150)
    email=models.CharField(max_length=250)
    username=models.CharField(max_length=150)
    password=models.CharField(max_length=100)

    def __str__(self):
       return self.Name

class review(models.Model):
    appname=models.ForeignKey(App,related_name='app',on_delete=models.CASCADE)
    username=models.ForeignKey(User,related_name='uname',on_delete=models.CASCADE)
    review=models.CharField(max_length=500)


    
