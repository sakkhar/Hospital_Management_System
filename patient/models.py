from cProfile import Profile

from django.contrib.auth.models import User

from django.db import models

# Create your models here.
class Admission(models.Model):
    ADMISSIONREASON = (
        ('Pneumonia', "Pneumonia"),
        ('Congestive Heart Failure', "Congestive Heart Failure"),
        ('Hardening of the arteries', "Hardening of the arteries"),
        ('Heart Attack', "Heart Attack"),
        ('Chronic Obstruction Lung Disease', "Chronic Obstruction Lung Disease"),
        ('Stroke', "Stroke"),
        ('Irregular Heartbeat', "Irregular Heartbeat"),
        ('Congestive Heart Failure', "Congestive Heart Failure"),
        ('Complications of procedures, devices, implants and grafts', "Complications of procedures, devices, implants and grafts"),
        ('Mood Disorders', "Mood Disorders"),
        ('Fluid and Electrolyte Disorders', "Fluid and Electrolyte Disorders"),
        ('Urinary Infections', "Urinary Infections"),
        ('Asthma', "Asthma"),
        ('Diabetes mellitus with and without complications', "Diabetes mellitus with and without complications"),
        ('Skin Infections', "Skin Infections"),
        ('Gallbladder Disease', "Gallbladder Disease"),
        ('Gastrointestinal Bleeding', "Gastrointestinal Bleeding"),
        ('Hip Fracture', "Hip Fracture"),
        ('Appendicitis', "Appendicitis"),
        ('Other', "Other")
    )
    GENDER = (
        ('M', "Male"),
        ('F', "Female"),
    )

    Blood_Group=(
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

    #account = models.ForeignKey(Account, related_name="admissions_account")
    user =models.ManyToManyField(User)
    first_name    = models.CharField(max_length=100, null=True, blank=True)
    last_name   = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=1000, null=True, blank=True)
    mobile  = models.CharField(max_length=100, null=True, blank=True)
    sex = models.CharField(blank=True, max_length=1, choices=GENDER)
    age =models.IntegerField(default=0, null=True, blank=True)
    blood_group = models.CharField(blank=True, max_length=1, choices=Blood_Group)
    birth_date = models.DateField()
    admission = models.DateTimeField(auto_now_add=True)
    discharged_timestamp = models.DateTimeField(null=True, blank=True)
    reason = models.CharField(max_length=20, choices=ADMISSIONREASON)
    description = models.TextField(blank=True, max_length=1000, help_text='This is parient details')
    #hospital = models.ForeignKey(Hospital)
    active = models.BooleanField(default=True)


    def __str__(self):
        return self.first_name + " " + self.last_name

class Appointment(models.Model):
    #doctor = models.ForeignKey(Account, related_name="appointments_doctor")
    #patient = models.ForeignKey(Account, related_name="appointments_patient")
    description = models.CharField(max_length=200)
    status = models.CharField(max_length=50, default="Active")
   # hospital = models.ForeignKey(Hospital)
    startTime = models.DateTimeField()
    endTime = models.DateTimeField()

    def get_populated_fields(self):
        """
        This is used by the form to collect the data.
        """
        fields = {
            'description': self.description,
            'startTime': self.startTime,
            'endTime': self.endTime,
        }
        return fields

class MedicalTest(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateField()
    #hospital = models.ForeignKey(Hospital)
    description = models.CharField(max_length=200)
    #doctor = models.ForeignKey(Account, related_name="medicaltests_doctor")
    #patient = models.ForeignKey(Account, related_name="medicaltests_patient")
    private = models.BooleanField(default=True)
    completed = models.BooleanField()
    image1 = models.FileField(blank=True, null=True, upload_to='medtests/%Y/%m/%d')
    image2 = models.FileField(blank=True, null=True, upload_to='medtests/%Y/%m/%d')
    image3 = models.FileField(blank=True, null=True, upload_to='medtests/%Y/%m/%d')
    image4 = models.FileField(blank=True, null=True, upload_to='medtests/%Y/%m/%d')
    image5 = models.FileField(blank=True, null=True, upload_to='medtests/%Y/%m/%d')

    def get_populated_fields(self):
        """
        This is used by the form to collect the data.
        """
        fields = {
            'name': self.name,
            'date': self.date,
            #'hospital': self.hospital,
            'description': self.description,
            #'doctor': self.doctor,
            #'patient': self.patient,
            'private': self.private,
            'completed': self.completed,
            'image1': self.image1,
            'image2': self.image2,
            'image3': self.image3,
            'image4': self.image4,
            'image5': self.image5,
        }
        return fields

class Statistics(models.Model):
    startDate = models.DateField()
    endDate = models.DateField()

    def get_populated_fields(self):
        """
        This is used by the form to collect the data.
        """
        fields = {
            'startDate': self.startDate,
            'endDate': self.endDate,
        }
        return fields