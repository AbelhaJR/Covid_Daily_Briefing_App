# COVID Daily Breifing App

### Introduction
This COVID Daily Breifing App offer users simple and quick access to information on the weather and current Covid-19 infection rates in their local area, as well as the top news headlines in the UK. It provides an easy and efficient way to stay up to date with the constantly-changing Covid-19 situation and keeps users informed and aware of the infection rates in their local area by displaying scheduled notification updates. 
### App Features
- Automatically find the user location and provide every data from that location. 
- Provides weather, news, and Covid-19 infection rate updates. 
- Precisive setting schedule and cancel alarms at any chosen time. 
- The APi data are update every day , offering the user a better experience 
- Both text-to-speech and silent notifications are displayed.

### Prerequisites
  - Python 3.7+ (I am using version 3.9)
  - An IDE or texteditor (ex. Pycharm or Sublime)
  - [Weather] and [news] API keys
  - Stable internet connection and some programming knowledge:)
  
### Installation
> Packages in the requirement.txt file need to be installed first using pip: 

**flask**, run:
pip install Flask

**requests**, run:
pip install requests

**pyttsx3**, run:
pip install pyttsx3

**geopy**, run:
pip install geopy

**uk-covid19**, run:
pip install uk-covid19

you can activate your virtualenv and run:
pip install -r requirements.txt

### How to use
- After open the App , the should a simple graphic interface
- The user can click on the calendar icon to schedule the date and time of an announcement. 
- The user can also choose whether or not to include a weather and news briefing in the announcement. 
- Once the alarm is scheduled, it will be added to the alarms section :
- The user can cancel scheduled alarms by clicking on the “x” in the top right corner. 
- When the scheduled time is reached, a voice announcement will be made
- Silent notifications will appear in the notifications column
- Silent notifications can be dismissed by clicking the “x” in the top right corner.


### Developer's guide
- Copy all provided files into a new directory 
- First, you will need to get API keys from the [weather] and [news] websites in order to complete the URL and have access to the updates.
- My code is set to provide news and Covid-19 updates in the Uk, and the current weather in Exeter. The region, as well as the news and types of updates extracted from the websites can be changed to fit your preference. 
- There are plenty of different options to customize the updates. For a full guide on how to access and implement these choices, follow the developer's guide on these websites: 
-- Weather: https://openweathermap.org/api
-- News: https://newsapi.org/docs/endpoints/sources
-- Covid-19: https://coronavirus.data.gov.uk/details/developers-guide
- The images displayed on user interface, announcement voice, and frequency of updates is customizable to suit your preference:
Check out https://pypi.org/project/pyttsx3/ for details on how to customize the text-to-speech function.
- The daily briefing can be easily changed to include updates of your choice by editing the the 'notification_dict' commands. 

### Testing 
- 

### Links and Sources
- Requirements.txt guide: https://www.jetbrains.com/help/pycharm/managing-dependencies.html
- Weather API: https://openweathermap.org/api
- Flask guide: https://flask.palletsprojects.com/en/1.1.x/quickstart/
- News API: https://newsapi.org/docs/endpoints/sources
- Covid-19 API: https://coronavirus.data.gov.uk/details/developers-guide
- Requests guide: https://realpython.com/python-requests/
- Pyttsx3 guide: https://pypi.org/project/pyttsx3/ 



### License
----
Copyright (c) [2020] [Henrique Oliveria Abelha]
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files "covid-daily-briefing-app", to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.






   [weather]: <https://openweathermap.orgr>
   [news]: <https://newsapi.org/>
   
