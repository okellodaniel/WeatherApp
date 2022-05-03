from django.db import models

# Create your models here.

class City(models.Model):
    name = models.CharField(max_length=25)

    # show actual name of the city on the dashboard
    
    def __str__(self):
        return self.name
    
    # Show the name of the city in plural form
    class Meta:
        verbose_name_plural = 'Cities'