import forecast_data

class Current_Weather(object);
    def __init__(self,forecast): #from forecast_data
        self.highLows = []
        self.highLows.append(forecast.daily.data[0].temperature_low)
        self.highLows.append(forecast.daily.data[0].temperature_high)
        self.precipType = forecast.daily.data[0].precip_type
        self.precipPercent = forecast.daily.data[0].precip
        self.windSpeed = forecast.daily.data[0].wind_speed
        self.windGust = forecast.daily.data[0].wind_gust


    #Returns 0 (for rain), 1 (for snow), and 2 (for sleet)
    # -1 reserved for lack of precip (precipProbability is 0) or unlikely
    def analyze_precip(self):
        if(self.precipType == "snow"):
            if(self.precipPercent > 0.5):
                return 1
        elif(self.precipType == "rain"):
            if(self.precipPercent > 0.5):
                return 0
        elif(self.precipType == "sleet"):
            if(self.precipPercent > 0.5):
                return 2
        return -1
