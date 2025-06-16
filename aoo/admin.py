from django.contrib import admin
from .models import Property,PropertyImage  # make sure it's 'models', not 'model'

admin.site.register(Property)
admin.site.register(PropertyImage)  # Register the PropertyImage model
# This will allow you to manage Property and PropertyImage models in the Django admin interface.