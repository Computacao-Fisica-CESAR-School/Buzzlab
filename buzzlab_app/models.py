from django.db import models
from django.contrib.auth.models import User

class Address(models.Model):
    postal_code = models.CharField(max_length=15)
    city = models.CharField(max_length=63)
    state = models.CharField(max_length=63)
    country = models.CharField(max_length=63)
    district = models.CharField(max_length=63)
    street = models.CharField(max_length=63)
    street_number = models.CharField(max_length=7)
    additional = models.CharField(max_length=63)
    
    def __str__(self):
        return f"{self.street}, {self.street_number} - {self.district}, {self.city} - {self.state}, {self.postal_code}"

class OpeningHours(models.Model):
    class Weekdays(models.TextChoices):
        MONDAY = "Monday"
        TUESDAY = "Tuesday"
        WEDNESDAY = "Wednesday"
        THURSDAY = "Thursday"
        FRIDAY = "Friday"
        SATURDAY = "Saturday"
        SUNDAY = "Sunday"
    
    weekday = models.CharField(max_length=16, choices=Weekdays.choices)
    open_time = models.TimeField()
    close_time = models.TimeField()
    
    def __str__(self):
        return f"{self.weekday}: {self.open_time} - {self.close_time}"

class Lab(models.Model):
    name = models.CharField(max_length=63)
    description = models.TextField(max_length=1023)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)
    opening_hours = models.ManyToManyField(OpeningHours)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=127)
    admins = models.ManyToManyField('UserProfile')
    
    def __str__(self):
        return f"{self.name}"

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    verified = models.BooleanField()
    favorite_labs = models.ManyToManyField(Lab, blank=True)
    
    def __str__(self):
        return f"{self.user.username} | Verified: {self.verified}"

class ComponentCategory(models.Model):
    category = models.CharField(max_length=31)
    
    def __str__(self):
        return f"{self.category}"
    
class Component(models.Model):
    name = models.CharField(max_length=63)
    description = models.TextField(max_length=1023)
    category = models.ForeignKey(ComponentCategory, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.name} ({self.category})"
    
class LabComponent(models.Model):
    component = models.ForeignKey(Component, on_delete=models.CASCADE)
    lab = models.ForeignKey(Lab, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    
    def __str__(self):
        return f"{self.quantity}x {self.component.name} ({self.lab.name})"

class Comment(models.Model):
    content = models.TextField(max_length=1023)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    component = models.ForeignKey(Component, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"[{self.author.username} - {self.component.name}] {self.content}"