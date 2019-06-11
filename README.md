# finding_durham
findingdurham.com

This is a django project that includes a (largely unscientific) mathematical formula that compares user preferences with data Django pulls from an SQLite database to finda business the user might like. 

The 'findBestMatchView' function does the following:
    1-Pulls in the input the end user gave when answering five questions
    2-Pulls in the the name of all businesses in the database along with how well they meet the end users desires in the five questions
    3-Loops through all the businesses and compares their ratings to the end user preferences to assign a compatibility rating to 
    each business.  Right after the rating is assigned to a business, it's compared to the best rated business so far and if it's higher,
    the best rated business is updated.  Ties can occur while looping through the businesses. In that case, a random number generator
    breaks the time.
    4-Once all businesses have been checked, additional details are pulled about the best match and sent to the template to be displayed.


