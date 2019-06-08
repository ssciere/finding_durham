from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import RatingsForm
import random
from .models import Businesses


def takeUserInputView(request):
    form = RatingsForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, "take_user_input.html", context)
   
"""The 'findBestMatchView' function pulls data from the database and assigns each business a compadibility rating
    based on how well the locations ratings match the customers ratings.  The best location and it's rating
    is stored in variables.  In the event that two businesses are tied for best rating, a  random number
    generator is used to break the tie"""

def findBestMatchView(request):
    
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
    y = Businesses.objects.get(name=best_location) #pulls all data for chosen location 
    best_business_address = y.address #the following lines assign variables to be sent to the template
    best_business_zip = y.zipCode
    best_business_phone = y.phoneNumber
    best_business_url = y.link
    #the remaining likes pass the info for the best business to the 'announce_business' template
    return render(request, "./announce_business.html", {'dict': best_loc_dict, 'address': best_business_address,
     'zip':best_business_zip, 'phone':best_business_phone, 'url':best_business_url })
    


      