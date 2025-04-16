from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True,null=True)
    city = models.CharField(max_length=100)
    address = models.TextField(blank=True,null=True)

    def __str__(self):
        return self.name
    

class Vacancy(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True,null=True)
    salary = models.FloatField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='vacancies', default=1)
    
    def __str__(self):
        return self.name
    
    