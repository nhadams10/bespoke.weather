# commute_time = input("How long is your commute? (in minutes) ")

# print(
# '''
#  ––––––––––––––––––––––––––––––––––––––––––
# |Enter the letter for your means of transit|
# | - - - - - - - - - - - - - - - - - - - - -|
# |w - walk                                  |
# |b - bicycle                               |
# |p - public transit                        |
# |c - car                                   |
#  ––––––––––––––––––––––––––––––––––––––––––
# '''
# )
#
#commute_method = input("How are you getting to your destination? ")
location = "Seoul"
weather = "Good"

#Eventually, it might become worthwhile to upgrade to a custom feels like temperature calcuation based on the user's personal preferences. For now, the program will simply uses the feels like temp from Dark Sky's API for ease of building the first prototype.
feels_like_temp = 72

clothing_rec = "Test"

#Need to add functionality to check for rain
def clothing_rec_engine():
    if feels_like_temp < -20:
        clothing_rec = "Stay inside!"
    elif -20 <= feels_like_temp <= 20:
        clothing_rec + "Sweater & Winter Jacket"
    elif 20 < feels_like_temp <= 40:
        clothing_rec + "Winter Jacket"
    elif 40 < feels_like_temp <= 65: 
        clothing_rec + "Sweater"
    elif 65 < feels_like_temp <= 100:
        clothing_rec = clothing_rec + "No Jacket"
    else:
        clothing_rec = "Stay Inside"
    print(clothing_rec)

print(clothing_rec)