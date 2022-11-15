from django.shortcuts import render
from django.http import JsonResponse
from .models import *
from geopy.distance import great_circle

# Create your views here.
def home(request):
    return render(request, 'home.html')


def api(request):
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
    
        if km:
            if result['distance'] > int(km):
                payload.pop()
             
    return JsonResponse(payload, safe=False)