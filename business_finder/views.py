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

   
"""The 'findBestMatchView' function does the following:
    1-Pulls in the input the end user gave when answering five questions
    2-Pulls in the the name of all businesses in the database along with how well they meet the end users desires in the five questions
    3-Loops through all the businesses and compares their ratings to the end user preferences to assign a compatibility rating to 
    each business.  Right after the rating is assigned to a business, it's compared to the best rated business so far and if it's higher,
    the best rated business is updated.  Ties can occur while looping through the businesses. In that case, a random number generator
    breaks the time.
    4-Once all businesses have been checked, additional details are pulled about the best match and sent to the template to be displayed.
   
Please note, I started to break this function up into smaller functions but it seemed to become less readable so I left it as is.
If I expand this program I will probably go ahead and break it up into smaller functions that can be re-used
"""


def findBestMatchView(request):


#***********************PULL IN PREFERENCES ENTERED BY USER************************
    if request.method == 'POST':
       general = request.POST.get('general')
       car = request.POST.get('car')
       golf = request.POST.get('golf')
       house = request.POST.get('house')
       morning = request.POST.get('morning')
       preferences = [general, car, golf, house, morning]



#*********************PULL IN BUSINESS INFO FROM DATABASE************************
    possible_destinations = {} #This will become a dict with names of business as keys and tuples of category ratings as values
    y = 1
    dbSizeFinder = Businesses.objects.last() #The next two lines find out how many entries are in the Businesses table
    numOfBusinesses = dbSizeFinder.pk
    while y <= numOfBusinesses:   #looping through the database and adding business names and category ratings to the possible_destinations dict      
        x = Businesses.objects.get(pk=y)  
        possible_destinations.update({x.name:(x.general,x.car,x.golf,x.house,x.morning)})
        y += 1

#***********************COMPARE BUSINESS INFO WITH USER PREFERENCES*****************
       
    best_rating = 0  #best_rating, best_business will eventually hold the name and rating for the business that matches the user preferences the most. They are changed each time a new most compatable business is found while cycling trough all businesses. 
    best_business = ""
    for business, ratings in possible_destinations.items():
        x = 0
        compatibility_rating = (len(preferences)) * 10 #compatibility_rating for each business starts as 10 X the number of questions (since each question has a max compatibility of 10)
        while x < len(preferences): #loops through the questions and subracts the difference between user rating and business rating from the overall compatibility rating
            compatibility_rating = compatibility_rating - (abs(int(preferences[x]) - ratings[x]))
            x = x + 1
               
        if compatibility_rating > best_rating: #if the business being examined has a higher rating than the prior best rating, the best rating is replaced with the rating of the business being examined
            best_rating = compatibility_rating
            best_business = business   #best business thus far is also updated if we have a new highest rating
            
        elif compatibility_rating == best_rating:   #if there is a tie, a random number is used to determine which business to make the best thus far
            ran_number = int(random.randint(1, 2))
            if ran_number == 1:   #if ran_number is 1 the best business and rating get changed, if 2 they do not.  this breaks the tie!
                best_rating = compatibility_rating
                best_business = business
                

#*********************PULL ALL DETAILS ABOUT BUSINESS THAT IS BEST MATCH AND SEND IT TO TEMPLATE*************

    y = Businesses.objects.get(name=best_business) #pulls all data for chosen business
    best_business_address = y.address #the following lines assign variables to be sent to the template
    best_business_zip = y.zipCode
    best_business_phone = y.phoneNumber
    best_business_url = y.link
    #the remaining likes pass the info for the best business to the 'announce_business' template
    return render(request, "./announce_business.html", {'business': best_business, 'address': best_business_address,'zip':best_business_zip, 'phone':best_business_phone, 'url':best_business_url })
    


    

      
