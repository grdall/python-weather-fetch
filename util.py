class Util:
    def praseForecast(post):
        d = dict()
        location = post.find("location")

        d["time"] = post.get("from")

        # Main posts
        temperature = location.find("temperature")
        if(location.findall("temperature")):
            d["temperature"] = temperature.get("value")
            d["temperatureUnit"] = temperature.get("unit")

        windDirection = location.find("windDirection")
        if(location.findall("windDirection")):
            d["windDirectionDeg"] = windDirection.get("deg")
            d["windDirectionName"] = windDirection.get("name")
            
        windSpeed = location.find("windSpeed")
        if(location.findall("windSpeed")):
            d["windSpeedMps"] = windSpeed.get("mps")
            d["windSpeedBeaufort"] = windSpeed.get("beaufort")
            d["windSpeedName"] = windSpeed.get("name")

        if(location.findall("windGust")):
            d["windGust"] = location.find("windGust").get("mps")

        if(location.findall("areaMaxWindSpeed")):
            d["areaMaxWindSpeed"] = location.find("areaMaxWindSpeed").get("mps")

        humidity = location.find("humidity")
        if(location.findall("humidity")):
            d["humidity"] = humidity.get("value")
            d["humidityUnit"] = humidity.get("unit")

        pressure = location.find("pressure")
        if(location.findall("pressure")):
            d["pressure"] = pressure.get("value")
            d["pressureUnit"] = pressure.get("unit")

        if(location.findall("cloudiness")):
            d["cloudiness"] = location.find("cloudiness").get("percent")

        if(location.findall("fog")):
            d["fog"] = location.find("fog").get("percent")

        if(location.findall("lowClouds")):
            d["lowClouds"] = location.find("lowClouds").get("percent")

        if(location.findall("mediumClouds")):
            d["mediumClouds"] = location.find("mediumClouds").get("percent")

        if(location.findall("highClouds")):
            d["highClouds"] = location.find("highClouds").get("percent")

        dewpointTemperature = location.find("dewpointTemperature")
        if(location.findall("dewpointTemperature")):
            d["dewpointTemperature"] = dewpointTemperature.get("value")
            d["dewpointTemperatureUnit"] = dewpointTemperature.get("unit")

        # Minor posts
        precipitation = location.find("precipitation")
        if(location.findall("precipitation")):
            d["precipitationMin"] = precipitation.get("minvalue")
            d["precipitationMax"] = precipitation.get("maxvalue")
            d["precipitationUnit"] = precipitation.get("unit")

        symbol = location.find("symbol")
        if(location.findall("symbol")):
            d["symbolId"] = symbol.get("id")
            d["symbolNumber"] = symbol.get("number")
            
        minTemperature = location.find("minTemperature")
        if(location.findall("minTemperature")):
            d["minTemperature"] = minTemperature.get("value")
            d["minTemperatureUnit"] = minTemperature.get("unit")

        maxTemperature = location.find("maxTemperature")
        if(location.findall("maxTemperature")):
            d["maxTemperature"] = maxTemperature.get("value")
            d["maxTemperatureUnit"] = maxTemperature.get("unit")

        return d

    def printForecast(forecast, logId):
        fromTime = forecast["time"].replace("T", ", ")
        fromTime = fromTime.replace("Z", "")
        mps = " meters per second "

        print("\nFrom: \t\t" + fromTime)

        if("temperature" in forecast):
            print("Temperature: \t" + forecast["temperature"] + " " + forecast["temperatureUnit"])
            
        if("minTemperature" in forecast and logId > 0):
            print("\tMinimum: \t" + forecast["minTemperature"] + " " + forecast["minTemperatureUnit"])
            print("\tMaximum: \t" + forecast["maxTemperature"] + " " + forecast["maxTemperatureUnit"])
            
        # Not using forecast["windSpeedBeaufort"] or forecast["areaMaxWindSpeed"]
        if("windSpeedName" in forecast):
            print("Wind: \t\t" + forecast["windSpeedName"] + ": " + forecast["windSpeedMps"] + mps + "from " + forecast["windDirectionDeg"] + " degrees (" + forecast["windDirectionName"] + ")")

        if("windSpeedName" in forecast and logId > 0):
            print("Gusts: \t\t" + forecast["windGust"] + mps)
    
        if("humidity" in forecast and logId > 0):
            print("Humidity: \t" + forecast["humidity"] + " " + forecast["humidityUnit"])
            
        if("dewpointTemperature" in forecast and logId > 1):
            print("Dewpoint: \t" + forecast["dewpointTemperature"] + " " + forecast["dewpointTemperatureUnit"])
            
        if("pressure" in forecast and logId > 1):
            print("Pressure: \t" + forecast["pressure"] + " " + forecast["pressureUnit"])
            
        if("fog" in forecast and logId > 1):
            print("Fog: \t\t" + forecast["fog"] + " %")
            
        if("cloudiness" in forecast and logId > 0):
            print("Cloudiness: \t" + forecast["cloudiness"] + " %")

        if("lowClouds" in forecast and logId > 1): 
            print("Low clouds: \t" + forecast["lowClouds"] + " %")

        if("mediumClouds" in forecast and logId > 1): 
            print("Medium clouds: \t" + forecast["mediumClouds"] + " %")

        if("highClouds" in forecast and logId > 1): 
            print("High clouds: \t" + forecast["highClouds"] + " %")
            
        if("precipitationMin" in forecast and logId > 0):
            print("Precipitation: \t" + forecast["precipitationMin"] + " " + forecast["precipitationUnit"] + " - " + forecast["precipitationMax"] + " " + forecast["precipitationUnit"])
            
        if("symbolId" in forecast and logId > 0):
            print("Symbol: \t" + forecast["symbolId"] + ": " + forecast["symbolNumber"])