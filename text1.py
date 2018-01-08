from pyowm import OWM
API_key = "10d4923cb75c31bfa0a786005f4803db"
owm = OWM(API_key)

def weather(city):
    obs = owm.weather_at_place(city)
    w = obs.get_weather()
    l = obs.get_location()
    print(l.get_name()+'\n최고 기온 :', w.get_temperature(unit='celsius')['temp_max'], '˚C','\n최저 기온 :', w.get_temperature(unit='celsius')['temp_min'], '˚C','\n현재 기온 :',w.get_temperature(unit='celsius')['temp'], '˚C' ,'\n현재 날씨 :', w.get_status())
    
weather('gwangju')
