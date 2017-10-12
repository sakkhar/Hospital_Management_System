from django.db import models

# Create your models here.
class  Payment_History(models.Model):
    invoice_number=models.CharField(max_length=100)

class Bed_Allotment(models.Model):
    invoice_number=models.CharField(max_length=100)

class Blood_Bank(models.Model):
    blood_group=models.CharField(max_length=100)

class  Blood_Donor(models.Model):
    name = models.CharField(max_length=100)
    address=models.TextField()
    age =models.ImageField(default=0, null=True, blank=True)

    def __str__(self):
        return self.name

class Medicine(models.Model):
    name =models.CharField(max_length=100)

    def __str__(self):
        return self.name

class  Operation_Report(models.Model):
    description=models.TextField(max_length=200)

    def __str__(self):
        return self.description

class birth_report(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class death_report(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

