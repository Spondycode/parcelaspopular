from django.db import models
from django.contrib.auth.models import User


class Campsite(models.Model):
    name = models.CharField('Campsite Name', max_length=40)
    address = models.CharField(max_length=320)
    postcode = models.CharField('Postal Code', max_length=10)
    w3words = models.CharField(max_length=60)
    phone = models.CharField('Phone', max_length=25)
    web = models.URLField('Website Address')
    email_address = models.EmailField('Email Address')

    def __str__(self):
        return self.name


class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField('Email Address')
    primary_mode = models.CharField('Camper Type', max_length=60)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Sun(models.Model):
    sun = models.CharField('SunOrShadow', max_length=25, default='sun')

    def __str__(self):
        return self.sun


class Group(models.Model):
    name = models.CharField('Group', max_length=25)

    def __str__(self):
        return self.name


class Parcela(models.Model):
    number = models.CharField('Plot Number', max_length=20)
    campsite = models.ForeignKey(Campsite, blank=True, null=True, on_delete=models.CASCADE)
    group = models.ForeignKey('Group', blank=True, null=True, on_delete=models.CASCADE)
    width = models.IntegerField('Size', blank=True)
    length = models.IntegerField('Plot Length', blank=True)
    description = models.TextField('Description')
    sun = models.ForeignKey(Sun, blank=True, null=True, on_delete=models.CASCADE)


    def __str__(self):
        return self.number


