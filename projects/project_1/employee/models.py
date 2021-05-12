from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Company(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(unique=True,
                              blank=False,
                              error_messages={
                                  "unique": "A user with that email already exists.",
                              },)
    contact_number = PhoneNumberField()
    desription = models.TextField(max_length=100, null=True, blank=True)

    
    def __str__(self):
        return self.name
    class Meta:
        ordering = ["name"]
        verbose_name_plural = "Companies"
        
class Employee(models.Model):
    employee_name = models.CharField(max_length=150)
    employee_phone = PhoneNumberField()
    employee_adress = models.TextField(null=True, blank=True)
    employee_id = models.IntegerField(null=False)
    employee_company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.employee_name

    class Meta:
        ordering = ["employee_company"]
        verbose_name_plural = "Employees"

