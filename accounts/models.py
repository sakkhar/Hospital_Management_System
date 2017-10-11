#from cProfile import Profile

#from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Account(models.Model):
    ACCOUNT_UNKNOWN = 0
    ACCOUNT_PATIENT = 10
    ACCOUNT_NURSE = 20
    ACCOUNT_DOCTOR = 30
    ACCOUNT_ADMIN = 40
    ACCOUNT_TYPES = (
        (ACCOUNT_UNKNOWN, "Unknown"),
        (ACCOUNT_PATIENT, "Patient"),
        (ACCOUNT_NURSE, "Nurse"),
        (ACCOUNT_DOCTOR, "Doctor"),
        (ACCOUNT_ADMIN, "Admin"),
    )
    EMPLOYEE_TYPES = (
        (ACCOUNT_NURSE, "Nurse"),
        (ACCOUNT_DOCTOR, "Doctor"),
        (ACCOUNT_ADMIN, "Admin"),
    )

    @staticmethod
    def to_name(key):
        """
        Parses an integer value to a string representing an account role.
        :param key: The account role as a int
        :return: The string representation of the name for the account role
        """
        for item in Account.ACCOUNT_TYPES:
            if item[0] == key:
                return item[1]
        return "None"

    @staticmethod
    def to_value(key):
        """
        Parses an string to a integer representing an account role.
        :param key: The account role as a string
        :return: The integer representation of the account role
        """
        key = key.lower()
        for item in Account.ACCOUNT_TYPES:
            if item[1].lower() == key:
                return item[0]
        return 0

    role = models.IntegerField(default=0, choices=ACCOUNT_TYPES)
    #profile = models.OneToOneField(Profile)
    #user = models.OneToOneField(User)

    def __str__(self):
        if self.role == 30:
            return "Dr. " + self.profile.__str__()
        elif self.role == 20:
            return "Nurse " + self.profile.__str__()
        else:
            return self.profile.__str__()

    class Admin:
        list_display = (
            'role',
            'profile',
            'user'
        )
