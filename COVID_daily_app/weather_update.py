import requests
import json
from helper_functions import *


def get_weather() :
    """
    Function get_weather , save APi data into .json file
    """
    
    # Reference to get_current_location() from helper_functions
    current_city = get_current_location()
    
        
    complete_url = get_complete_url("OpenWeather")
    

    response = requests.get(complete_url)
    
    #Error
    if response.status_code >= 400  :
        print('Error : Weather request failed')
    
    with open('api_data/JSON/weather_update.json','w') as file :
        json.dump(response.json() , file)


        
        