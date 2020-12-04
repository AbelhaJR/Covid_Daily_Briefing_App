"""
Main.py
"""

#Import Modules and Library
from flask import Flask , request, render_template
import json
import time,sched,logging,random
import pyttsx3
import uk_covid_19
from helper_functions import *
import uk_covid_19 weather_update , news_filter



# Global Variables

schedular_module = sched.scheduler(time.time, time.sleep)
app = Flask(__name__)
current_time = datetime.now().strftime("%Y-%m-%dT%H:%M")

# Set general file path form config file 
with open('config.json','r') as config_file : 
    config_data = json.load(config_file)
general_file_path = config_data["file_path"][0]["general_file_path"]



@app.route('/')
def main():
    """
    Function Main , return the template and data from alarms , notifications , title and image
    """
    
    # Reference to load_data() from helper_functions
    alarm_data,notification_data = load_data()
    
    # Every 1 hour the api data update
    update_api()
    return render_template('index.html', title = 'Covid_App' , image = 'favicon.svg' , alarms = alarm_data["active_alarms"] , notifications = notification_data["notification"])



@app.route('/index')
def index():
    """
    Function Index , return the template and data from alarms , notifications , title and image
    """
    
    
    # Reference to load_data() from helper_functions
   
    schedular_module.run(blocking=False)
    logging.basicConfig(filename = "main.log")
    # Set flags to notification and alarm remover
    notification_remove = request.args.get('notif')
    alarm_remove = request.args.get('alarm_item')
    
    if notification_remove:
        close_notification(notification_remove)
    if alarm_remove : 
        cancel_alarm(alarm_remove)
    
    # Get data from the labels alarm and two (Alarm time / Alarm name)
    alarm_date_label = request.args.get("alarm")
    alarm_name_label = request.args.get("two")     
    alarm_data,notification_data = load_data() 
    if alarm_date_label and alarm_name_label:
        
        # Check if user input an invalid date
        if date_to_seconds(alarm_date_label) <= date_to_seconds(current_time) :
            logging.info(alarm_date_label)
            alarm_voice("The date inserted does not correspond to a actual valid date. Insert again!")
        else :
            # Set flags to include news and weather notifications
            news_option = request.args.get("news")
            weather_option = request.args.get("weather")

            date_formatted = alarm_date_label.replace("T"," ")
        
            include_news = False
            include_weather = False
        
            # Check if the user want to include news and/or weather notifications
            if news_option: 
                include_news = True
            if weather_option:
                include_weather = True

        
          
            alarm_data["active_alarms"].append({ "title" : date_formatted , "content" : alarm_name_label})
        
            with open(general_file_path + "alarm.json",'w') as alarms_file:
                json.dump(alarm_data,alarms_file)

        
            set_alarm(alarm_date_label,alarm_name_label,news_option,weather_option)
        
    return render_template('index.html', title='Daily update', image = "favicon.svg", alarms = alarm_data["active_alarms"], notifications = notification_data["notification"])


 


def show_notifications(alarm_date,alarm_name,news_option,weather_option):
    """
    Function show_notifications , output notifications about news , covid daily cases and weather 
    """
    
    # Reference to load_data() from helper_functions
    alarm_data,notification_data = load_data()
    
    
    
    # Create Covid notification 
    with open(general_file_path + "uk_covid_19.json", "r") as covid_file:
        covid_data = json.load(covid_file)

    last_covid_data = covid_data[0]
    
    notification_data["notification"].append({ "title": last_covid_data["title"] , "content": last_covid_data["content"] })
    
  
      
    # Create News notification
    if news_option:
        with open(general_file_path + "news_filter.json", "r") as news_filter_file:
            news_data = json.load(news_filter_file)
    
        article_details = news_data["articles"][random.randint(0,len(news_data["articles"]))]
        notification_data["notification"].append({"title" : article_details["source"]["name"] + " - " + current_time.replace("T"," ") , "content": article_details["title"]})
   
   
    # Create Weather notification
    if weather_option:
        with open(general_file_path + "weather_update.json", 'r') as weather_update_file:
            weather_data = json.load(weather_update_file)
        
        kelvin_to_celsius = weather_data["main"]["temp"] - 273,16
        
        notification_data["notification"].append({"title": current_time.replace("T"," ") + " " + get_current_location(), "content": "Today , you can count with " + weather_data["weather"][0]["description"]})
      
    
    # Insert Notifications in .json file
    with open(general_file_path + "notification.json", "w") as notifications_file:
        json.dump(notification_data, notifications_file)

    for alarm_details in alarm_data["active_alarms"] :
        print(alarm_date.replace("T"," "))
        print(alarm_name)
        if alarm_details["title"] == alarm_date.replace("T"," ") and alarm_details["content"] == alarm_name : 
            alarm_voice(alarm_details["title"])
            alarm_voice(alarm_details["content"])
            alarm_data["active_alarms"].remove(alarm_details)
    
    with open(general_file_path + "alarm.json" , "w") as alarm_file :
        json.dump(alarm_data,alarm_file)








# Cancel/Close Events

# Cancel 
def cancel_alarm(alarm):
    """
    Function cancel_alarm , allow user to cancel alarm before they get activated
    """
    with open('api_data/JSON/alarm.json', 'r') as alarm_file:
        alarm_data = json.load(alarm_file)
    
    for alarm_details in alarm_data["active_alarms"]:
        if alarm_details["title"] == alarm :
            index = alarm_data["active_alarms"].index(alarm_details)
            schedular_module.cancel(schedular_module.queue[index])
            alarm_data["active_alarms"].remove(alarm_details)
            break
    # Confirmation Message
    alarm_voice("Alarm cancelled . Thank you!")
    with open(general_file_path + "alarm.json", 'w') as alarms_file:
        json.dump(alarm_data, alarms_file)

# Close
def close_notification(notification_remove):
    """
    Function close_notification , allow user to close the chosen notification
    """
    with open(general_file_path + "notification.json", 'r') as notifications_file:
        notification_data = json.load(notifications_file)
    for notification_details in notification_data["notification"]:
        if notification_details["title"] == notification_remove:
            
            notification_data["notification"].remove(notification_details)
            break
    
    with open(general_file_path + "notification.json", 'w') as notifications_file:
        json.dump(notification_data,notifications_file)


# Set Alarms 
def set_alarm(alarm_date,alarm_name,news_option,weather_option):
    """
    Function set_alarm , helps setting user alarms 
    """
    schedule_delay = date_to_seconds(alarm_date) - date_to_seconds(current_time)
    print(schedule_delay)
    schedular_module.enter(schedule_delay, 1, show_notifications,[alarm_date,alarm_name,news_option,weather_option])

    # Alarm Voice
    alarm_voice("Alarm " + alarm_name + " schedule for " + alarm_date)


# Alarm Voices (pyttsx3) 
def alarm_voice(current_message):
    """
    Function alarm_voice , activate text-to-speech
    """
    engine = pyttsx3.init()
    engine.say(current_message)
    engine.runAndWait()
    engine.stop()

# Update api_data
def update_api() :
    """
    Function update_api , check if api are updates by using config file 
    """
    with open('config.json','r') as config_file :      
        config_data = json.load(config_file)
        
    update_date = config_data["updates_api"][0]["last_update_time"]
    
    # If the api never was updated
    if update_date == "empty" :
        news_filter.get_news()
        weather_update.get_weather()
        uk_covid_19.local_covid_data()
        config_data["updates"][0]["last_update_time"] = current_time
        
    else :
        # If the update date is expired ( more than 1 hour)
        if date_to_seconds(current_time) - date_to_seconds(update_date) >= 3600 :
            news_filter.get_news()
            weather_update.get_weather()
            uk_covid_19.local_covid_data()
            config_data["updates"][0]["last_update_time"] = current_time
    with open('config.json','w') as config_file : 
        json.dump(config_data,config_file)


if __name__ == '__main__':
    app.run()
    
    

    