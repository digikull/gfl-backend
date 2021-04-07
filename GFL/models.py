from django.db import models

# Create your models here.
class Tournament(models.Model):
   # tournament_name = models.ForeignKey(User,on_delete=models.CASCADE)
    tournament_name = models.CharField(max_length=100)
    tournament_type = models.BooleanField()
    tournament_class = models.CharField(max_length=100,)
    tournament_total_team = models.CharField(max_length=100,blank=True)
    tournament_template = models.CharField(max_length=100,blank=True)
   # tournament_location = models.(max_length=100,blank=True)
    tournament_detials = models.CharField(max_length=100,blank=True)
    lat= models.DecimalField(max_digits=20,decimal_places=2,blank=True)
    lon= models.DecimalField(max_digits=20,decimal_places=2,blank=True)
    #start_date = models.DateTimeField(auto_now_add=True)
    #end_date =models.DateTimeField(auto_now=True)
    
    
    
    def __str__(self):
        return self.tournament_name