from django.db import models
import string
import random
from multiselectfield import MultiSelectField

AMENITY_CHOICES = [
    ('swimming_pool', 'Swimming Pool'),
    ('gym', 'Gym'),
    ('garden', 'Garden'),
    ('parking', 'Parking'),
    ('security', 'Security'),
    ('wifi', 'Wi-Fi'),
    ('air_conditioning', 'Air Conditioning'),
    ('heating', 'Heating'),
    ('furnished', 'Furnished'),
    ('balcony', 'Balcony'),
]


def generate_unique_id(length=5):
    characters = string.ascii_uppercase + string.digits  # A-Z and 0-9
    return ''.join(random.choices(characters, k=length))




class Property(models.Model):
    id = models.CharField(
        max_length=5,
        unique=True,
        primary_key=True,
        editable=False,
        default=generate_unique_id
    )

    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    bathrooms = models.IntegerField()
    age_of_property = models.IntegerField(help_text="Age of the property in years")
    sale_type = models.CharField(max_length=50, choices=[
        ('sale', 'For Sale'),
        ('rent', 'For Rent'),
        ('sold', 'Sold')
    ])
    build_area = models.DecimalField(max_digits=10, decimal_places=2, help_text="Area in square feet")
    plot_area = models.DecimalField(max_digits=10, decimal_places=2, help_text="Plot area in square feet")
    amenities = MultiSelectField(choices=AMENITY_CHOICES, blank=True, null=True)
    balcony_no = models.IntegerField(default=0, help_text="Number of balconies")
    parking_no = models.IntegerField(default=0, help_text="Number of parking spaces")
    property_type = models.CharField(max_length=50, choices=[
        ('apartment', 'Apartment'),
        ('house', 'House'),
        ('condo', 'Condo'),
        ('land', 'Land'),
        ('commercial', 'Commercial')
    ])
    
    bedrooms = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

from django_mongodb_backend.fields import ObjectIdAutoField

class PropertyImage(models.Model):
    id = ObjectIdAutoField(primary_key=True)
    property = models.ForeignKey(Property, related_name='images', on_delete=models.CASCADE)
    image_id = models.CharField(max_length=300)

    def __str__(self):
        return f"Image for {self.property.id}"
