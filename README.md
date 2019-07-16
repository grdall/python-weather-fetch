# python-weather-fetch

A simple python program that fetches data from [MET Weather API](https://api.met.no/weatherapi) and returns current temp, temp for rest of the day, and temp for next 24 hours.

## Usage (Windows)
1. [Install Python](https://www.python.org/downloads/)
2. Make sure Python is defined on PATH
3. Navigate to folder in CLI
4. Install Googlemaps with PiP: $ python -m pip install googlemaps
5. $ python weather.py [arguments...]

Optional: [Define coordinates](https://www.latlong.net) for custom location
- $ python weather.py 59.91 10.75
Optional: Enter placename for custom location (remember quotes for multiple words)
- $ python weather.py "Henrik Ibsens gate 1"

## TODO:
- classes and more structure
- prog arguments
- Add more detailed info, weather forecast
- tomorrow/week ahead/just weekend/vaiable number of days instead fo next 24 etc

### My Thoughts

I wanted to begin to learn Python as I've seen some buzz around it but never got much information though education, also wanting to monitor the weather with more ease I decided to make a small commandline program to fetch some info from an API and print it.

The more I used the program the more I felt it could be improved and give more and more detailed information to give a better overview of the weather and for longer.