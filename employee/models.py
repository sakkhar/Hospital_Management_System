from cProfile import Profile

from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Nurse(models.Model):
    GENDER = (
        ('M', "Male"),
        ('F', "Female"),
    )

    Blood_Group = (
        ('O', "O Positive"),
        ('O', "O Negetive)"),
        ('AB', "AB Positive"),
        ('AB', "AB Negetive"),
        ('A', "A Positive"),
        ('A', "A Negetive"),
        ('B', "B Positive"),
        ('B', "B Negetive")
    )

    @staticmethod
    def to_gender(key):
        for item in Profile.GENDER:
            if item[0] == key:
                return item[1]
        return "None"

    @staticmethod
    def to_blood_group(key):
        for item in Profile.BLOOD_GROUP:
            if item[0] == key:
                return item[1]
        return "None"

    user =models.OneToOneField(User)
    first_name    = models.CharField(max_length=100, null=True, blank=True, help_text='This is First Name')
    last_name   = models.CharField(max_length=100, null=True, blank=True,help_text='This is Last Name')
    address = models.CharField(max_length=1000, null=True, blank=True, help_text='This is address')
    mobile  = models.CharField(max_length=100, null=True, blank=True)
    sex = models.CharField(blank=True, max_length=1, choices=GENDER)
    age =models.IntegerField(null=True, blank=True)
    blood_group = models.CharField(blank=True, max_length=1, choices=Blood_Group)
    birth_date = models.DateField()

    image =models.ImageField(upload_to=None, width_field=None, height_field=None)
    active = models.BooleanField(default=True)


    def __str__(self):
        return self.first_name + " " + self.last_name

class Laboratorist(models.Model):
    GENDER = (
        ('M', "Male"),
        ('F', "Female"),
    )

    Blood_Group = (
        ('O', "O Positive"),
        ('O', "O Negetive)"),
        ('AB', "AB Positive"),
        ('AB', "AB Negetive"),
        ('A', "A Positive"),
        ('A', "A Negetive"),
        ('B', "B Positive"),
        ('B', "B Negetive")
    )

    @staticmethod
    def to_gender(key):
        for item in Profile.GENDER:
            if item[0] == key:
                return item[1]
        return "None"

    @staticmethod
    def to_blood_group(key):
        for item in Profile.BLOOD_GROUP:
            if item[0] == key:
                return item[1]
        return "None"

    user =models.OneToOneField(User)
    first_name    = models.CharField(max_length=100, null=True, blank=True)
    last_name   = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=1000, null=True, blank=True)
    mobile  = models.CharField(max_length=100, null=True, blank=True)
    sex = models.CharField(blank=True, max_length=1, choices=GENDER)
    age =models.IntegerField(null=True, blank=True)
    blood_group = models.CharField(blank=True, max_length=1, choices=Blood_Group)
    birth_date = models.DateField()

    image =models.ImageField(upload_to=None, width_field=None, height_field=None)
    active = models.BooleanField(default=True)


    def __str__(self):
        return self.first_name + " " + self.last_name

class Pharmacist(models.Model):
    GENDER = (
        ('M', "Male"),
        ('F', "Female"),
    )

    Blood_Group = (
        ('O', "O Positive"),
        ('O', "O Negetive)"),
        ('AB', "AB Positive"),
        ('AB', "AB Negetive"),
        ('A', "A Positive"),
        ('A', "A Negetive"),
        ('B', "B Positive"),
        ('B', "B Negetive")
    )

    @staticmethod
    def to_gender(key):
        for item in Profile.GENDER:
            if item[0] == key:
                return item[1]
        return "None"

    @staticmethod
    def to_blood_group(key):
        for item in Profile.BLOOD_GROUP:
            if item[0] == key:
                return item[1]
        return "None"

    user =models.OneToOneField(User)
    first_name    = models.CharField(max_length=100, null=True, blank=True)
    last_name   = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=1000, null=True, blank=True)
    mobile  = models.CharField(max_length=100, null=True, blank=True)
    sex = models.CharField(blank=True, max_length=1, choices=GENDER)
    age =models.IntegerField(null=True, blank=True)
    blood_group = models.CharField(blank=True, max_length=1, choices=Blood_Group)
    birth_date = models.DateField()

    image =models.ImageField(upload_to=None, width_field=None, height_field=None)
    active = models.BooleanField(default=True)


    def __str__(self):
        return self.first_name + " " + self.last_name

