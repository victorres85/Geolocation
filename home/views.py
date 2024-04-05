from django.shortcuts import render
from django.http import JsonResponse
from .models import *
from geopy.distance import great_circle

# Create your views here.
def home(request):
    return render(request, 'home.html')


def api(request):
    """
    API endpoint to retrieve nearby restaurants based on user's pincode and radius (in kilometers).

    This view function takes optional GET parameters:

    * pincode: User's postal code to determine location.
    * km: Radius in kilometers to search for restaurants around the user's location.

    The view retrieves all restaurants from the database and iterates through them. 
    For each restaurant, it calculates the distance from the user's location (if provided) 
    using the `geopy.distance.great_circle` function.

    The response is a JSON object containing a list of dictionaries, each representing a restaurant. 
    The dictionary includes details like:

        * name: Restaurant name (from model field)
        * image: Restaurant image URL (from model field)
        * description: Restaurant description (from model field)
        * pincode: Restaurant's pincode (from model field)
        * distance: Distance (in kilometers) between the user and the restaurant (if pincode provided)

    If the 'km' parameter is provided, restaurants further than the specified radius are filtered out 
    from the final response payload.

    Returns:
        A JsonResponse containing a list of dictionaries representing nearby restaurants.
    """
    restaurants_objs = Restaurant.objects.all()
    pincode = request.GET.get('pincode')
    km = request.GET.get('km')
    user_lat = None
    user_long = None
    if pincode:
        geolocator = Nominatim(user_agent="home")
        location = geolocator.geocode(pincode)
        user_lat = location.latitude
        user_long = location.longitude

    payload = []
    for rest in restaurants_objs:
        result={}
        result['name'] = rest.name
        result['image'] = rest.image
        result['description'] = rest.description
        result['pincode'] = rest.pincode
        if pincode:
            first = (float(user_lat), float(user_long))
            second = (float(rest.lat), float(rest.long))
            result['distance'] = int(great_circle(first, second).miles)
  
        payload.append(result)
    
        if km != 'any':
            if result['distance'] > int(km):
                payload.pop()
             
    return JsonResponse(payload, safe=False)