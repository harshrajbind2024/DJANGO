from django.db import models

from django.utils import timezone
# Create your models here.

# create a model
  # name = models.models.CharField(_(""), max_length=50)
    # name = models.CharField(max_length=50)

# class rajvarity(models.Model):
#     chia_type_choice=[
#         ('pl','plain'),
#         ('el','pelachi'),
#     ]
#     name = models.CharField(max_length=255)
#     image = models.ImageField(upoad_to='raj/')
#     date_added = models.DateTimeField(default=timezone.now)
#     type= models.CharField(max_length=2, choices= chia_type_choice)




class rajvarity(models.Model):
    chia_type_choice=[
        ('pl','plain'),
        ('el','elachi'),
    ]
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='raj/')
    date_added = models.DateTimeField(default=timezone.now)
    type= models.CharField(max_length=2, choices= chia_type_choice)
    description=models.TextField(default='')

    def __str__(self):   #add
        return self.name
    
