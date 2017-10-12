from cProfile import Profile

from django.db import models

# Create your models here.
class DoctorProfile(models.Model):
    GENDER = (
        ('M', "Male"),
        ('F', "Female"),
    )
    Department=(
        ('N', "Neurology"),
        ('E', "ENT (Ear, Nose & Throat)"),
        ('C', "Cardiovascular"),
        ('NE', "Nephrology"),
        ('O', "Orthopaediatrics"),
    )

    @staticmethod
    def to_gender(key):
        for item in Profile.GENDER:
            if item[0] == key:
                return item[1]
        return "None"

    @staticmethod
    def to_department(key):
        for item in Profile.Departmet:
            if item[0] == key:
                return item[1]
        return "None"

    first_name = models.CharField(blank=True, max_length=50)
    last_name = models.CharField(blank=True, max_length=50)
    address    =models.TextField()
    email   =models.EmailField(null=True, blank=True)
    emergency_Contact_Number = models.CharField(blank=True, max_length=50)
    sex = models.CharField(blank=True, max_length=1, choices=GENDER)
    department = models.CharField(blank=True, max_length=1, choices=Department)
    birthday = models.DateField()
    phone = models.CharField(blank=True, max_length=20)
    created = models.DateTimeField(auto_now_add=True)
    image =models.ImageField(upload_to=None, width_field=None, height_field=None)

    def get_populated_fields(self):
        """
        This is used by the form to collect the data.
        """
        fields = {}
        if self.first_name is not None:
            fields['first_name'] = self.first_name
        if self.last_name is not None:
            fields['lastname'] = self.last_name
        if self.address is not None:
            fields['address'] = self.address
        if self.email is not None:
            fields['email'] = self.email
        if self.sex is not None:
            fields['sex'] = self.sex
        if self.Department is not None:
            fields['department'] = self.department
        if not self.birthday.year == 1000:
            fields['birthday'] = self.birthday
        if self.phone is not None:
            fields['phone'] = self.phone
        if self.emergency_Contact_Number is not None:
            fields['emergency_Contact_Number'] = self.emergency_Contact_Number
        if self.created is not None:
            fields['created'] = self.created
        if self.image is not None:
            fields['image'] = self.image



    def __str__(self):
        return self.first_name + " " + self.last_name


class Hospital(models.Model):
    pass


class Administrator(models.Model):
    first_Name = models.CharField(max_length=50, default='')
    last_Name = models.CharField(max_length=50, default='')
    user_name = models.CharField(max_length=30, default='')
    workplace = models.ForeignKey(Hospital)

    def __str__(self):
        return self.first_Name + " " + self.last_Name

    def getWorkplace(self, admin):
        return admin.workplace