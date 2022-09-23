from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Band(models.Model) :
    
    def __str__(self) -> str:
        return f'{self.name}'
    
    class Genre(models.TextChoices) :
        
        HIP_HOP = "HH"
        ALTERNATIVE_ROCK = "AR"
        SYNTH_POP = "SP"
        
    class Type(models.TextChoices) :
        
        RECORDS = "RC"
        CLOTHINGS = "CH"
        POSTERS = "PT"
        MISCELLANEOUS = "ML"
        
    genre = models.fields.CharField(choices=Genre.choices,max_length=5)
    
    name = models.fields.CharField(max_length=100)
        
    biography = models.fields.CharField(max_length=1000)
    
    year_formed = models.fields.IntegerField(
        validators=[MinValueValidator(1900),MaxValueValidator(2022)]
    )
    
    active = models.fields.BooleanField(default=True)
    
    official_homepage = models.fields.URLField(null=True,blank=True)
    
    # description = models.fields.CharField(max_length=1000)
    
    # sold = models.fields.BooleanField(default=False)
    
    # year = models.fields.IntegerField(null=True)
    
    # type = models.fields.CharField(choices=Type.choices,max_length=10)
    
    
class Listing(models.Model):
    
    def __str__(self) -> str:
        return f'{self.type}'
    
    class Type(models.TextChoices) :
        RECORDS = "RC"
        CLOTHINGS = "CH"
        POSTERS = "PT"
        MISCELLANEOUS = "ML"
        
    description = models.fields.CharField(max_length=1000)
    
    sold = models.fields.BooleanField(default=False)
    
    year = models.fields.IntegerField(null=True)
    
    type = models.fields.CharField(choices=Type.choices,max_length=10)
    
    band = models.ForeignKey(Band,null=True,on_delete=models.SET_NULL)