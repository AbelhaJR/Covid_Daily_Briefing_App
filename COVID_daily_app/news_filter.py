import requests
import json
from helper_functions import *




def get_news() :
    """
    Function get_news , save APi data into a .json folder
    """
    complete_url = get_complete_url('News API')
    
    response = requests.get(complete_url,timeout=10)
    
    # Error 
    if response.status_code >= 400  :
        print('Error : News request failded')
    
    with open('api_data/JSON/news_filter.json','w') as news_filter_file :
        json.dump(response.json(),news_filter_file)


       