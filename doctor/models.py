from django.db import models

from account.models import User


class Doctor(models.Model):
    Cardiologist = 'CL'
    Dermatologists = 'DL'
    Emergency_Medicine_Specialists = 'EMC'
    Immunologists = 'IL'
    Anesthesiologists = 'AL'
    Colon_and_Rectal_Surgeons = 'CRS'

    department_choices = [(Cardiologist, 'Cardiologist'),
                          (Dermatologists, 'Dermatologists'),
                          (Emergency_Medicine_Specialists, 'Emergency Medicine Specialists'),
                          (Immunologists, 'Immunologists'),
                          (Anesthesiologists, 'Anesthesiologists'),
                          (Colon_and_Rectal_Surgeons, 'Colon and Rectal Surgeons')
    ]
    department = models.CharField(max_length=3, choices=department_choices, default=Cardiologist)
    address = models.TextField()
    mobile = models.CharField(max_length=20)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name

    @property
    def get_id(self):
        return self.user.id

    def __str__(self):
        return "{} ({})".format(self.user.first_name, self.department)
