from django.contrib import admin
from .models import CarMake, CarModel

# Register your models here.
# class CarMakeAdmin(admin.ModelAdmin):
#    fields = ['name', 'description']

# class CarModelAdmin(admin.ModelAdmin):
#    fields = ['car_make', 'name']

# Registering models with their respective admins
# admin.site.register(CarMake, CarMakeAdmin)
# admin.site.register(CarModel, CarModelAdmin)
admin.site.register(CarMake)
admin.site.register(CarModel)
# CarModelInline class

# CarModelAdmin class

# CarMakeAdmin class with CarModelInline

# Register models here
