from flask import Flask, render_template, request
import requests

app = Flask(__name__)

def get_weather(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()

    if data['cod'] == 200:
        weather_info = {
            'city': data['name'],
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description'],
            'humidity': data['main']['humidity'],
            'wind_speed': data['wind']['speed']
        }
        return weather_info
    else:
        return None

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        city = request.form['city']
        api_key = "your api key"  # Replace 'YOUR_API_KEY' with your actual OpenWeatherMap API key
        weather_info = get_weather(city, api_key)
        if weather_info:
            return render_template('index.html', weather=weather_info)
        else:
            return render_template('index.html', error=True)
    return render_template('index.html', weather=None, error=False)

if __name__ == '__main__':
    app.run(debug=True)
