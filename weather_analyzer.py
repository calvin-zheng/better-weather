from datetime import datetime

class Daily_Weather(object):
    def __init__(self,forecast): #from forecast_data
        self.forecast = forecast
        self.currentHour = datetime.now().hour
        self.precipTypes = {"rain": [], "snow": [], "sleet": []}
        self.initNextHalfDayPrecip()

    def initNextHalfDayPrecip(self):
        #goes through the next 12 hours, adding relevant data points in regards to the type of precip
        #only precip probability greater than 20% is considered
        for i in range(0,12):
            if(self.forecast.hourly.data[i].precip_probability >= 0.2):
                self.precipTypes[self.forecast.hourly.data[i].precip_type].append(self.currentHour + i)
                #print(i)

    def getPrecipTimes(self, precipType):
        return self.precipTypes[precipType]

    def precipTypesToStr(self):
        precipStr = "Rain: "
        for time in self.getPrecipTimes("rain"):
            precipStr += time + ", "
        precipStr += "\nSnow: "
        for time in self.getPrecipTimes("snow"):
            precipStr += time + ", "
        precipStr += "\nSleet: "
        for time in self.getPrecipTimes("sleet"):
            precipStr += time
        return precipStr

    def willPrecip(self):
        return self.willRain() or self.willSnow() or self.willSleet()

    def willRain(self):
        return not (len(self.precipTypes["rain"]) == 0)

    def willSleet(self):
        return not (len(self.precipTypes["sleet"]) == 0)

    def willSnow(self):
        return not (len(self.precipTypes["snow"]) == 0)




