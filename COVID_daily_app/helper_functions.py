"""
helper_functions.py.py
"""
import json ,requests
from logging import critical
import geocoder ,time
from datetime import datetime



current_time = datetime.now().strftime("%Y-%m-%dT%H:%M")

# Set general file path form config file 
with open('config.json','r') as config_file : 
    config_data = json.load(config_file)
general_file_path = config_data["file_path"][0]["general_file_path"]

#Current Location
def get_current_location():
    """
    Function get_current_location , return user current location with ip address 
    """
    current_location_data = geocoder.ip('me')
    
    return current_location_data.city


#Load data from notifications and alarm
def load_data(): 
    """
    Function load , return all data available in notification.json and alarm.json
    """
    with open(general_file_path + "notification.json", "r") as notification_file : 
        notification_data = json.load(notification_file)
    
    with open(general_file_path + "alarm.json","r") as alarm_file :
        alarm_data = json.load(alarm_file)
    
    return alarm_data,notification_data




# Complete APi URL
def get_complete_url(api_name : str):
    """
    Function get_complete_url , return APi complete url 
    """
    with open('config.json','r') as config_file :
        config_data = json.load(config_file)
        for api_details in config_data["api_config"] :
            if api_name == api_details["name"] :
                # Swich Python
                return {
                    'News API' : api_details["base_url"] +  "country=" + api_details["country"] + "&apiKey=" + api_details["key"] ,
                    'OpenWeather' : api_details["base_url"] +  "appid=" + api_details["key"] + "&q=" + get_current_location()
                }.get(api_name,'Not found Api')






# Convert date to seconds
def date_to_seconds(date_format):
    """
    Function date_to_seconds , return the date in seconds(int)
    """
    default_date_format = datetime.strptime(date_format,"%Y-%m-%dT%H:%M")
    return time.mktime(default_date_format.timetuple())            

