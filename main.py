import weather_analyzer as wa
import forecast_data as fd
import csv

def main():
    forecastToday = fd.read_forecast()
    weatherToday = wa.Daily_Weather(forecastToday)

def weather_report(daily_weather):
    if(not daily_weather.isPrecip()):
        print("There is not projected to be rain, sleet, or snow today. Have a great day!")
    else:
        if(daily_weather.willRain()):
            rainStr = ""
            rain_times = daily_weather.getPrecipTimes()
            prev_time = -1
            counter = 0
            for time in rain_times:
                if(prev_time + 1 != time && prev_time != -1):
                    if(counter > 1):
                        rainStr += " to " + prev_time + ", at "
                        counter = 0
                    System.
                elif(prev_time + 1 == time):
                    counter += 1
                else:
                    rainStr = ("It will rain today at " + time + " ")
                    prev_time = time



main()

