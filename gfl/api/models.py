from django.db import models

# Create your models here.
class Player(models.Model):
    name=models.CharField(max_length=100)
    role=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    image=models.ImageField(upload_to="images/")

    def __str__(self):
        return self.name
   


