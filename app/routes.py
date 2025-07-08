from flask import render_template, request, jsonify
from app import app
import requests
import pandas as pd
from app.model import predict
from datetime import datetime

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/weather', methods=['GET', 'POST'])
def weather():
    weather_data = None
    if request.method == 'POST':
        city = request.form['city']
        api_key = 'e8865c6728bd4805de801a9b96907b8d'
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
        response = requests.get(url)
        if response.ok:
            data = response.json()
            weather_data = {
                'city': city,
                'temperature': data['main']['temp'],
                'description': data['weather'][0]['description'],
                'humidity': data['main']['humidity'],
                'wind_speed': data['wind']['speed']
            }
            
            # Add an approximate prediction using existing model
            try:
                # Use available data to make a climate prediction
                df = pd.DataFrame({
                    'temperature': [weather_data['temperature']],
                    'humidity': [weather_data['humidity']],
                    # Estimate CO2 level for the model (typical value)
                    'co2': [415]  
                })
                weather_data['prediction'] = round(predict(df), 2)
            except Exception as e:
                # If prediction fails, continue without it
                pass
                
        else:
            weather_data = {'error': 'City not found or API issue'}
    
    # Pass current time to template
    now = datetime.now()
    return render_template('weather.html', weather=weather_data, now=now)

@app.route('/predict', methods=['GET', 'POST'])
def prediction():
    prediction_result = None
    if request.method == 'POST':
        if request.is_json:
            # Handle AJAX requests from script.js
            data = request.get_json()
            df = pd.DataFrame({
                'temperature': [float(data['temperature'])],
                'humidity': [float(data['humidity'])],
                'co2': [float(data['co2'])]
            })
            prediction_value = predict(df)
            return jsonify({'prediction': round(prediction_value, 2)})
        else:
            # Handle form submissions
            try:
                temperature = float(request.form['temperature'])
                humidity = float(request.form['humidity'])
                co2 = float(request.form['co2'])
                
                df = pd.DataFrame({
                    'temperature': [temperature],
                    'humidity': [humidity],
                    'co2': [co2]
                })
                
                prediction_result = round(predict(df), 2)
            except Exception as e:
                prediction_result = f"Error: {str(e)}"
    
    return render_template('prediction.html', prediction=prediction_result)