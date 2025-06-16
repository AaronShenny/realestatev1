from django.shortcuts import render
from .models import Property

# Create your views here.
def home(request):
    # Fetch all properties from the database
    properties = Property.objects.all()
    # Pass the properties to the template context
    for property in properties:
        property.image = property.images.first() if property.images.exists() else None
        #print(property.image.img_id)
    context = {
        'properties': properties
    }
    # Render the home template with the context
    return render(request, 'aoo/home.html', context)
def property_detail(request, property_id):  
    # Fetch the property by its ID
    property = Property.objects.get(id=property_id)
    # Pass the property to the template context
    context = {
        'property': property
    }
    # Render the property detail template with the context
    return render(request, 'aoo/property_detail.html', context)