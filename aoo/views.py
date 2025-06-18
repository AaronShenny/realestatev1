from django.shortcuts import render
from .models import Property

# Create your views here.
def home(request):
    # Fetch all properties from the database
    districts = [
        "Alappuzha", "Ernakulam", "Idukki", "Kannur", "Kasaragod",
        "Kollam", "Kottayam", "Kozhikode", "Malappuram", "Palakkad",
        "Pathanamthitta", "Thiruvananthapuram", "Thrissur", "Wayanad"
    ]
    location = request.GET.get('location', '')
    filter_type = request.GET.get('filter_type', '')
    properties = Property.objects.all()
    # Pass the properties to the template context
    for property in properties:
        property.image = property.images.first() if property.images.exists() else None
        #print(property.image.img_id)
    context = {
        'properties': properties,
        'districts': districts,
        'selected_location': location,
        'selected_type': filter_type,
    }
    # Render the home template with the context
    return render(request, 'aoo/home.html', context)


def property_filter(request):
    districts = [
        "Alappuzha", "Ernakulam", "Idukki", "Kannur", "Kasaragod",
        "Kollam", "Kottayam", "Kozhikode", "Malappuram", "Palakkad",
        "Pathanamthitta", "Thiruvananthapuram", "Thrissur", "Wayanad"
    ]
    filter_type = request.GET.get('filter_type', None)
    location = request.GET.get('location', None)
    # Fetch properties based on the filter type
    if filter_type == 'rent' and location:
        properties = Property.objects.filter(sale_type='rent', district=location)
    elif filter_type == 'sale' and location:
        properties = Property.objects.filter(sale_type='sale', district=location)
    elif filter_type == 'sale':
        properties = Property.objects.filter(sale_type='sale')
    elif filter_type == 'rent':
        properties = Property.objects.filter(sale_type='rent')
    elif location:
        properties = Property.objects.filter(district=location)
    else:
        properties = Property.objects.all()
    
    for property in properties:
        property.image = property.images.first() if property.images.exists() else None
       
    # if location:
    #     # If a location is provided, filter properties by location
    #     properties = properties.filter(district=location)
    # Pass the filtered properties to the template context
    context = {
        'properties': properties,
        'districts': districts,
    }
    # Render the property filter template with the context
    return render(request, 'aoo/property_filter.html', context)

def property_detail(request, property_id):  
    # Fetch the property by its ID
    property = Property.objects.get(id=property_id)
    # Pass the property to the template context
    context = {
        'property': property
    }
    # Render the property detail template with the context
    return render(request, 'aoo/property_detail.html', context)