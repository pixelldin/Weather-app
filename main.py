from flask import Flask, render_template, request
import requests
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file

app = Flask(__name__)

api_key = os.getenv('API_KEY')  # Get API key from environment variable

@app.route('/', methods=['GET', 'POST'])
def weather():
    if request.method == 'POST':
        city = request.form['city']
        weather_data = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=imperial")

        if weather_data.status_code == 404:
            error_msg = "City not found"
            return render_template('weather.html', error=error_msg)
        else:
            data = weather_data.json()
            if data.get('cod') != 200:
                error_msg = f"Error: {data.get('message', 'Unknown error')}"
                return render_template('weather.html', error=error_msg)
            else:
                weather = data['weather'][0]['main']
                temp = round(data['main']['temp'])
                return render_template('weather.html', city=city, weather=weather, temp=temp)

    return render_template('weather.html')

if __name__ == '__main__':
    app.run(debug=True)

