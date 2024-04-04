from django.db import models

# Defines a Django model named Users
class Users(models.Model):
    # Defines a field 'username' of type CharField with a maximum length of 20 characters
    username = models.CharField(max_length=20)
    
    # Defines a field 'password' of type CharField with a maximum length of 20 characters
    password = models.CharField(max_length=20)

class warehouse(models.Model):
    email = models.CharField(max_length=50, null=True)
    username = models.CharField(max_length=20, null=True)
    password = models.CharField(max_length=20, null=True)


class acc_details(models.Model):
    email = models.CharField(max_length=50, null=True)
    username = models.CharField(max_length=20, null=True)
    name = models.CharField(max_length=50, default="", blank=True)  # Add default value here
    surname = models.CharField(max_length=50, blank=True)
    dob = models.DateField(null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True) 
    image = models.ImageField(null=True, blank=True,upload_to='images/')