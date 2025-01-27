from django.db import models

class Passport(models.Model):
    name = models.CharField(max_length=30)  # name maydoni, maksimal uzunligi 30
    surname = models.CharField(max_length=30)  # surname maydoni, maksimal uzunligi 30
    phone_number = models.CharField(max_length=13)  # telefon raqam, maksimal uzunligi 8
    birth_day = models.DateField()  # tug'ilgan sana, DateField turida
    passport_id = models.CharField(max_length=9, unique=True)  # pasport ID, maksimal uzunligi 7
    address = models.CharField(max_length=50)  # address maydoni, maksimal uzunligi 50

    def __str__(self):
        return f"{self.name} {self.surname} - {self.passport_id}"
