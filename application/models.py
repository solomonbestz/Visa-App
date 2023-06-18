from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Application(models.Model):
    passport_number = models.CharField(max_length=20, null=True)
    passport_photo = models.ImageField(upload_to='passports/', 
                                       max_length=100)
    application_country = models.CharField(max_length=50)
    nigeria_embassy = models.CharField(max_length=50)
    nationality = models.CharField(max_length=50)
    date_of_birth = models.DateField(null=True)
    email = models.EmailField(_('Email Address'), unique=True)
    date_of_entry = models.DateField(null=True)
    visa_type = models.CharField(max_length=20, null=True)
