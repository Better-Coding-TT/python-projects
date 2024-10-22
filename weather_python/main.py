import requests

#Replace with your API key from OpenWeatherMap
api_key = '95ceb5fe2a98b0ba09ed4280dbc57db9' 

city = input('Enter city name: ')

url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    temp = data['main']['temp']
    humidity = data['main']['humidity']
    desc = data['weather'][0]['description']
    print(f'\nTemperature: {round(temp - 273.15)} °C')
    print(f'Humidity: {humidity}%')
    print(f'Description: {desc}')
else:
    print('Error. Try again later.')


    