from uk_covid19 import Cov19API
import json
import requests
from helper_functions import *


def local_covid_data():
    """
    Function local_covid_data , save manipulated APi data into a .json folder
    """
    local_only = [
        'areaName={}'.format(get_current_location())
    ]
    cases_and_deaths = {
        "date": "date",
        "areaName": "areaName",
        "areaCode": "areaCode",
        "newCasesByPublishDate": "newCasesByPublishDate",
    }
    # Api Setup
    api = Cov19API(filters=local_only, structure=cases_and_deaths)
    uk_covid_data = api.get_json()

    covid_data =[]

    # Diference between cases
    daily_cases_update =int(uk_covid_data["data"][0]['newCasesByPublishDate']) - int(uk_covid_data["data"][1]['newCasesByPublishDate']) 

    if daily_cases_update > 0 :
            percentage = (daily_cases_update / int(uk_covid_data["data"][1]["newCasesByPublishDate"]))
            covid_data.append({'title' : "Covid daily brifing in {}.\n Date : {}".format(get_current_location(),uk_covid_data["data"][0]["date"]),'content' : "New cases: {} , New covid cases in {} were increased by {} since yesterday by {}%"\
            .format(uk_covid_data['data'][0]['newCasesByPublishDate'],uk_covid_data['data'][0]['areaName'],uk_covid_data['data'][0]['areaName'],percentage)})
    elif daily_cases_update < 0 :
            percentage = (abs(daily_cases_update) / int(uk_covid_data["data"][1]["newCasesByPublishDate"]))
            covid_data.append({'title' : "Covid daily brifing in {}.\n Date : {}".format(get_current_location(),uk_covid_data["data"][0]["date"]),'content' : "New cases: {}, New covid cases in {} were decreased by {} from yesterday, Percentage of decrease of the new cases in {}: {}%" \
            .format(uk_covid_data['data'][0]['newCasesByPublishDate'],uk_covid_data['data'][0]['areaName'],uk_covid_data['data'][0]['areaName'],percentage)})
    else :
        covid_data.append({'title' : "Covid daily brifing in {}.\n Date : {}".format(get_current_location(),uk_covid_data["data"][0]["date"]),'content' : "New cases: {}, New covid cases in {} are the same as yesterday's ones"\
        .format(uk_covid_data['data'][0]['newCasesByPublishDate'],uk_covid_data['data'][0]['areaName'])})
    
    
    with open("api_data/JSON/uk_covid_19.json","w") as uk_covid_file :
        json.dump(covid_data,uk_covid_file)
