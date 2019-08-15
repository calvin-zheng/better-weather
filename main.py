import weather_analyzer as wa
import forecast_data as fd
import csv

def main():
    forecastToday = fd.read_forecast()
    weatherToday = wa.Daily_Weather(forecastToday)
    weather_report(weatherToday)

def weather_report(daily_weather):
    if(not daily_weather.willPrecip()):
        print("There is not projected to be rain, sleet, or snow today. Have a great day!")
    else:
        if(daily_weather.willRain()):
            rainStr = ""
            rain_times = daily_weather.getPrecipTimes("rain")
            prev_time = -1

            for i in range(len(rain_times)):
                if((prev_time + 1 != rain_times[i] and prev_time != -1)):
                    rainStr += " to " + str(prev_time) + ", at " + str(rain_times[i])
                    prev_time = rain_times[i]
                elif(i + 1 == len(rain_times) and prev_time != -1):
                    rainStr += " to " + str(rain_times[i])
                elif(prev_time + 1 == rain_times[i]):
                    prev_time += 1
                else:
                    rainStr = ("It may rain today at " + str(rain_times[i]))
                    prev_time = rain_times[i]
            rainStr = rainStr[:len(rainStr)] + "."
            print(rainStr)



main()

