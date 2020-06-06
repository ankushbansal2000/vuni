from django.db import models

# create your models here.
class UserDetails(models.Model):
    username = models.CharField(max_length=50,unique=True)
    category = models.CharField(max_length=50,default="admin")
    email = models.EmailField(max_length=254,unique = True)
    password = models.CharField(max_length=50)

    def __str__(self):
        return str(self.id)+"__"+self.username+"__"+str(self.category)