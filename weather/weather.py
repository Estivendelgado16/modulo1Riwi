import requests


city = input("Ingres el nombre de la cuidad para ver saber e clima: ").strip()
apiKey = "c3ee6b08c3ec79e10e9328084be51fc8"

url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={apiKey}'

data = requests.get(url)

try: 
    if data.status_code == 200:
            data = data.json()

            weatherMain = data['weather'][0]['main']
            weatherDescription = data['weather'][0]['description']
            temp = data['main']['temp']
            humidity = data['main']['humidity']

            print(f"\nClima en {city.title()}:")
            print(f"Estado: {weatherMain}")
            print(f"Descripción: {weatherDescription}")
            print(f"Temperatura: {temp}°C")
            print(f"Humedad: {humidity}%")

            
except ValueError as e:
    print(e)