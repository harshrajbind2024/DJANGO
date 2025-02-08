from django.db import models

from django.utils import timezone
from django.contrib.auth.models import User
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
    


# one to many
class rajReview(models.Model):
    chai=models.ForeignKey(rajvarity, on_delete=models.CASCADE,related_name='review')
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    rating=models.IntegerField()
    comment = models.TextField()
    date_added=models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f'{self.user.username} review for {self.chai.name}'
    
    
    
    
    



# many to many 
class store(models.Model):
    name=models.CharField(max_length=200)
    location=models.CharField(max_length=100)
    raj_varieties=models.ManyToManyField(rajvarity , related_name='stores')
    def __str__(self):
        return self.name
    
    
    
    

# one to one


# class   rajCertificate(models.Model):
#     raj  
    
    
    
class rajCertificate(models.Model):
    raj = models.OneToOneField(rajvarity, on_delete=models.CASCADE, related_name='certificate')
    certificate_number = models.CharField(max_length=100)
    issued_date = models.DateTimeField(default=timezone.now)
    valid_untill = models.DateTimeField()

    def _str_(self):
        return f'Certificate for {self.name.raj}'    