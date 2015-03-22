from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from snippets.models import Snippet, User, Credit_Card, Driver, Pending_Ride, User_Ride
from snippets.serializers import SnippetSerializer, UserSerializer, CreditCardSerializer, DriverSerializer, PendingRideSerializer, UserRideSerializer
import requests
import json
from datetime import datetime
from django.utils import timezone

class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

def snippet_list(request):
    if request.method == 'GET':
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)

def snippet_detail(request, pk):
    try:
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = SnippetSerializer(snippet)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        snippet.delete()
        return HttpResponse(status=204)

def user_list(request):
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return JSONResponse(serializer.data)
        
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)
        
def user_register(request):
    serializer = UserSerializer(data = request.GET)
    if serializer.is_valid():
        serializer.save()
        return JSONResponse(serializer.data, status=201)
    return JSONResponse(serializer.errors, status=400)
    
def user_login(request):
    get = request.GET
    email = get.__getitem__('email')
    password = get.__getitem__('password')
    user = User.objects.filter(email = email)
    if user.count() == 1:
        user = User.objects.filter(email = email, password = password)
        if user.count() == 1:
            userserializer = UserSerializer(user[0])
            creditcards = Credit_Card.objects.filter(email = email)
            ccserializer = CreditCardSerializer(creditcards, many=True)
            return JSONResponse({'userdata':userserializer.data,'creditcards':ccserializer.data}, status = 201)
        else:
            return HttpResponse('incorrect password', status = 401)
    else:
        return HttpResponse('non existing email', status = 402)
        
def user_add_home(request):
    get = request.GET
    email = get.__getitem__('email')
    home = get.__getitem__('home')
    user = User.objects.get(email = email)
    if home == 'null':
        user.home = ''
        user.home_lat = ''
        user.home_long = ''
        user.save()
        return HttpResponse('home removed successfully', 201)
    else:
        homelat = get.__getitem__('homelat')
        homelong = get.__getitem__('homelong')
        user.home = home
        user.home_lat = homelat
        user.home_long = homelong
        user.save()
        return HttpResponse('home added successfully', 201)

def user_add_work(request):
    get = request.GET
    email = get.__getitem__('email')
    work = get.__getitem__('work')
    user = User.objects.get(email = email)
    if work == 'null':
        user.work = ''
        user.work_lat = ''
        user.work_long = ''
        user.save()
        return HttpResponse('work removed successfully', 201)
    else:
        worklat = get.__getitem__('worklat')
        worklong = get.__getitem__('worklong')
        user.work = work
        user.work_lat = worklat
        user.work_long = worklong
        user.save()
        return HttpResponse('work added successfully', 201)
   
def credit_card_list(request):
    if request.method == 'GET':
        creditcards = Credit_Card.objects.all()
        serializer = CreditCardSerializer(creditcards, many=True)
        return JSONResponse(serializer.data)
        
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CreditCardSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)
    
def credit_card_register(request):
    serializer = CreditCardSerializer(data = request.GET)
    if serializer.is_valid():
        serializer.save()
        return JSONResponse(serializer.data, status=201)
    return JSONResponse(serializer.errors, status=400)

def driver_list(request):
    if request.method == 'GET':
        drivers = Driver.objects.all()
        serializer = DriverSerializer(drivers, many=True)
        return JSONResponse(serializer.data)
        
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = DriverSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)

def driver_login(request):
    get = request.GET
    driverid = get.__getitem__('id')
    lat = get.__getitem__('latitude')
    lon = get.__getitem__('longitude')
    driver = Driver.objects.filter(driver_id = driverid)
    if driver.count() == 1:
        drivers = Driver.objects.get(driver_id = driverid)
        drivers.pos_lat = lat
        drivers.pos_long = lon
        drivers.save()
        serializer = DriverSerializer(driver[0])
        return JSONResponse(serializer.data, status = 201)        
    else:
        return HttpResponse('id not valid',status = 401)
        
def driver_register(request):
    serializer = DriverSerializer(data = request.GET)
    if serializer.is_valid():
        serializer.save()
        return JSONResponse(serializer.data, status=201)
    return JSONResponse(serializer.errors, status=400)
    
def driver_get_nearby(request):
    get = request.GET
    radius = float(get.__getitem__('radius'))
    latitude = float(get.__getitem__('latitude'))
    longitude = float(get.__getitem__('longitude'))
    longmax = longitude + radius
    longmin = longitude - radius
    latmax = latitude + radius
    latmin = latitude - radius
    drivers = Driver.objects.all().filter(pos_lat__gte=latmin, pos_lat__lte=latmax,pos_long__gte=longmin, pos_long__lte=longmax)
    serializer = DriverSerializer(drivers, many=True)
    return JSONResponse(serializer.data, status = 201)

def driver_update_position(request):
    get = request.GET
    driverid = get.__getitem__('driverid')
    lat = float(get.__getitem__('latitude'))
    lng = float(get.__getitem__('longitude'))
    driver = Driver.objects.get(driver_id = driverid)
    driver.pos_lat = lat
    driver.pos_long = lng
    driver.save()
    return HttpResponse('Location updated', status=201)
    
def send_uber_request(request):
    serializer = PendingRideSerializer(data = request.GET)
    if serializer.is_valid():
        serializer.save()
        return JSONResponse(serializer.data, status=201)
    return JSONResponse(serializer.errors, status=400)
    
def get_uber_request(request):
    get = request.GET
    latitude = float(get.__getitem__('latitude'))
    longitude = float(get.__getitem__('longitude'))
    radius = float(get.__getitem__('radius'))
    longmax = longitude + radius
    longmin = longitude - radius
    latmax = latitude + radius
    latmin = latitude - radius
    pendingrides = Pending_Ride.objects.all().filter(user_lat__gte=latmin, user_lat__lte=latmax, user_lon__gte=longmin, user_lon__lte=longmax)
    serializer = PendingRideSerializer(pendingrides, many=True)
    return JSONResponse(serializer.data, status = 201)
    
def list_uber_request(request):
    if request.method == 'GET':
        pendingrides = Pending_Ride.objects.all()
        serializer = PendingRideSerializer(pendingrides, many=True)
        return JSONResponse(serializer.data)
        
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PendingRideSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)
        
def accept_uber_request(request):
    get = request.GET
    driverid = get.__getitem__('driverid')
    pendingrequestid = get.__getitem__('pendingrequestid')
    pendingride = Pending_Ride.objects.filter(pending_ride_id = pendingrequestid)
    if pendingride.count() == 1:
        pendingride = Pending_Ride.objects.get(pending_ride_id = pendingrequestid)
        useremail = pendingride.user_id.email
        creditcard = Credit_Card.objects.get(email = useremail, mail = True)
        data = {'user_id':useremail, 'driver_id': driverid, 'credit_card_number':creditcard.credit_card_number, 'pending_ride_id':pendingrequestid}
        serializer = UserRideSerializer(data = data)
        if serializer.is_valid():
            pendingride.delete()
            serializer.save()
            return JSONResponse(serializer.data, status= 201)
        return JSONResponse(serializer.errors, status=400)
    else:
        return HttpResponse("request id not found", status = 401)

def pending_uber_request(request):
    get = request.GET
    pendingrideid = get.__getitem__('pendingrideid')
    pendingride = Pending_Ride.objects.filter(pending_ride_id = pendingrideid)
    if pendingride.count() == 1:
        return HttpResponse('Waiting', status=201)
    else:
        ride = User_Ride.objects.get(pending_ride_id = pendingrideid)
        data = {'driver_id':ride.driver_id.driver_id, 'driver_name':ride.driver_id.name, 'driver_last_name':ride.driver_id.last_name, 'vehicle':ride.driver_id.vehicle, 'license_plate': ride.driver_id.license_plate, 'rideid':ride.ride_id}
        return JSONResponse(data, status=202)
        
def ride_list(request):
    if request.method == 'GET':
        ride = User_Ride.objects.all()
        serializer = UserRideSerializer(ride, many=True)
        return JSONResponse(serializer.data)
        
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserRideSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)
        
def begin_ride(request):
    get = request.GET
    rideid = get.__getitem__('rideid')
    lat = float(get.__getitem__('latitude'))
    lng = float(get.__getitem__('longitude'))
    ride = User_Ride.objects.get(ride_id = rideid)
    ride.initial_lat = lat
    ride.initial_long = lng
    ride.date = timezone.now()
    ride.save()
    return HttpResponse('Ride begun', status= 201)
    
def end_ride(request):
    get = request.GET
    rideid = get.__getitem__('rideid')
    lat = float(get.__getitem__('latitude'))
    lng = float(get.__getitem__('longitude'))
    distance = float(get.__getitem__('distance'))
    distance = distance/1000
    ride = User_Ride.objects.get(ride_id = rideid)
    ride.final_lat = lat
    ride.final_long = lng
    ride.distance = distance
    
    initialtime = ride.date
    finaltime = timezone.now()
    time = finaltime - initialtime
    minutes = time.seconds / 60
    
    fee = (minutes * 2) + (distance * 3.5) + 7.5
    ride.fee = fee
    
    if fee < 40:
        fee = 40
    
    ride.final_fee = fee
    ride.date = timezone.now()
    ride.time = minutes
    
    ride.save()
    return HttpResponse('Ride finished', status= 201)
    
def track_ride(request):
    get = request.GET
    rideid = get.__getitem__('rideid')
    ride = User_Ride.objects.get(ride_id = rideid)
    fee = ride.fee
    if fee == None:
        driver = ride.driver_id
        lat = driver.pos_lat
        lng = driver.pos_long
        data = {'latitude':lat, 'longitude':lng}
        return JSONResponse(data, status = 201)
    else:
        initial_lat = ride.initial_lat
        initial_lng = ride.initial_long
        final_lat = ride.final_lat
        final_lng = ride.final_long
        distance = ride.distance
        time = ride.time
        final_fee = ride.final_fee
        data = {'initial_lat':initial_lat, 'initial_lng':initial_lng, 'final_lat':final_lat, 'final_lng':final_lng, 'distance':distance, 'time':time, 'fee':fee, 'final_fee':final_fee}
        return JSONResponse(data, status = 202)
        
def rating_user_ride(request):
    get = request.GET
    rideid = get.__getitem__('rideid')
    rating = int(get.__getitem__('rating'))
    ride = User_Ride.objects.get(ride_id = rideid)
    ride.user_rating = rating
    ride.save()
    return HttpResponse('Rating sent', status= 201)
    
def rating_driver_ride(request):
    get = request.GET
    rideid = get.__getitem__('rideid')
    rating = int(get.__getitem__('rating'))
    ride = User_Ride.objects.get(ride_id = rideid)
    ride.driver_rating = rating
    ride.save()
    return HttpResponse('Rating sent', status= 201)