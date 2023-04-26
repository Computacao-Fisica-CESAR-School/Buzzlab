from django.contrib import admin
from .models import UserProfile, Address, OpeningHours, Lab, ComponentCategory, Component, LabComponent, Comment

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Address)
admin.site.register(OpeningHours)
admin.site.register(Lab)
admin.site.register(ComponentCategory)
admin.site.register(Component)
admin.site.register(LabComponent)
admin.site.register(Comment)