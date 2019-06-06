from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import RatingsForm
import random
from .models import Businesses


def ratings_create_view(request):
    form = RatingsForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, "ratings_create.html", context)
   


def find_best_match_view(request): #loops through all the locations compares their category ratings to the user input to create compatibility rating
    
    possible_destinations = {"Bull City Ciderworks":(8,9,8,9,2),"Fullsteam Brewery":(4,7,6,7,6),"Durham Distillery":(3,3,3,9,5),
    "Honeygirl Meadery":(1,4,8,3,7),"Hi-Wire Brewing":(4,5,8,3,10),"James Joyce Irish Pub":(7,6,9,5,4),"Bull City Apparel & Customs":(6,9,2,1,5),
    "Boxcar Barcade":(7,7,7,9,4),"Quarter Horse Barcade":(6,2,3,4,6), "Parts and Labor":(5,10,6,2,6),"106 Main":(1,10,8,1,10),
    "Durham Short Run Shirts":(9,10,7,1,2),"Pompieri Pizza":(8,3,5,9,3) }
    possible_destinations = {}
    y = 1
    dbSizeFinder = Businesses.objects.last() #The next two lines find out how many entries are in the Businesses table
    numOfBusinesses = dbSizeFinder.pk
    while y <= numOfBusinesses:
        
        x = Businesses.objects.get(pk=y)  
        possible_destinations.update({x.name:(x.general,x.car,x.golf,x.house,x.morning)})
        y += 1
    if request.method == 'POST':
       general = request.POST.get('general')
       car = request.POST.get('car')
       golf = request.POST.get('golf')
       house = request.POST.get('house')
       morning = request.POST.get('morning')
       preferences = [general, car, golf, house, morning]
       
    best_rating = 0  #best_rating,best_location are changed each time a new most compatable location is found while comparing locations to user preferences
    best_location = ""
    for location, ratings in possible_destinations.items():
        x = 0
        compatibility_rating = (len(preferences)) * 10 #compatibility_rating for each location starts as 10 X the number of questions (since each question has a max compatibility of 10)
        while x < len(preferences): #loops through the number of times that there are questions in the list of questions
            compatibility_rating = compatibility_rating - (abs(int(preferences[x]) - ratings[x]))
            x = x + 1
               
        if compatibility_rating > best_rating: #if the location being examined has a higher rating than the best rating thus far, the best rating is replaced with the current rating
            best_rating = compatibility_rating
            best_location = location   #best location thus far is also updated if we have a new highest rating
            best_loc_dict = {'first':best_location}
        elif compatibility_rating == best_rating:   #if there is a tie, a random number is used to determine which location to make the best thus far
            ran_number = int(random.randint(1, 2))
            if ran_number == 1:   #if ran_number is 1 the best location and rating get changed, if 2 they do not.  this breaks the tie!
                best_rating = compatibility_rating
                best_location = location
                best_loc_dict = {'first':best_location}
    

    return render(request, "./announce_venue.html", {'dict': best_loc_dict})
    return HttpResponse(best_location)


      