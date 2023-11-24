# #The code for /celsius-to-fahrenheit/app.py is:

"""
This file is the main file of the application. It contains the Flask application and the routes for the Celsius to Fahrenheit and Fahrenheit to Celsius conversion.
"""

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    temperature = float(request.form['temperature'])
    conversion_type = request.form['conversion_type']
    converted_temperature = 0

    if conversion_type == 'celsius_to_fahrenheit':
        converted_temperature = (temperature * 9/5) + 32
    elif conversion_type == 'fahrenheit_to_celsius':
        converted_temperature = (temperature - 32) * 5/9
    
    return render_template('index.html', converted_temperature=converted_temperature)

if __name__ == '__main__':
    app.run(debug=True)