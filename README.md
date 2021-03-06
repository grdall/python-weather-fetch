# python-weather-fetch

A simple python program that fetches data from [MET Weather API](https://api.met.no/weatherapi) and returns forecast in various forms.

## Usage (Windows)

1. [Install Python](https://www.python.org/downloads/)
2. Make sure Python is defined on PATH
3. Navigate to folder in CLI
4. $ python weather.py [arguments...]

Optional: Add Googlemaps to enter placename for custom location (remember quotes for multiple words)
1. Install Googlemaps with PiP: $ python -m pip install googlemaps
2. [Get your Google Maps API key](https://cloud.google.com/maps-platform/) or check [this guide](https://developers.google.com/maps/documentation/javascript/get-api-key)
3. Make a file to hold the key or paste the key directly into the project in place of "gmap_key_key"
4. $ python weather.py "Henrik Ibsens gate 1"

## Help

- To use Googles Geocoding API you must install it on your computer. This is optional and the guide is in "readme.md"
- Fetch uses Metrologisk Institutt API and can only fetch weather from Norwegian territory. 
- Run by following "Usage" instructions in "readme.md" then enter:
- - $ python weather.py
- Running without any further arguments defaults to getting weather in Oslo, Norway.
- The following are the optional arguments implemented:
- - "-placename" or "-pn" + [string]: uses Google Maps Geocoding API to search for the [string], and fetches the forecast for that place. For multiple words, use quotes ("place name").
- - "-coordinates" or "-c" + [float] [float]: fetches the forecast for the place at [float] [float] coordinates.
- - "-update" or "-u": fetches the current forecast and updates hourly with the respective forecast.
- - "-simple" or "-s" + [int] (optional): prints data in a simplified format: time, temprature, wind, rain. Optional argument for number of data collation sets printed.
- - "-saveLocation" or "-sl" + [string] [float] [float]: saves the [float] [float] coordinates and [string] placename in a file which later can be used similarly to the placename argument (see "-loadLocation" argument)
- - "-loadLocation" or "-ll" + [string]: looks for [string] locations saved in a local file with the aruments above. For changes to the file, simply open it in Vim or Notepad.
- - "-help" or "-h": prints this help text.

## My Thoughts

I wanted to begin to learn Python as I've seen some buzz around it but never got much information though education, also wanting to monitor the weather with more ease I decided to make a small commandline program to fetch some info from an API and print it.

The more I used the program the more I felt it could be improved and give more and more detailed information to give a better overview of the weather and for longer.

## TODO:

- check spelling
- tests
- get location from file path (not working outside root directory)