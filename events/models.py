from django.db import models

class Country(models.Model):
    abbr = models.CharField(max_length=3)
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

class Athlete(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name="country")
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    gender = models.CharField(max_length=1)
    age = models.IntegerField()

    #def is_valid_athlete(self):
        #return (condition1) and (condition2)

    def __str__(self):
        return self.first_name

class Event(models.Model):
    name = models.CharField(max_length=64)
    stadium = models.CharField(max_length=64)
    area = models.CharField(max_length=64)
    athletes = models.ManyToManyField(Athlete, blank=True, related_name="participants")

    def __str__(self):
        return self.name
