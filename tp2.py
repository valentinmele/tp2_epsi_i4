import sys

from flask import Flask
from flask import render_template
import Adafruit_DHT

app = Flask(__name__)

@app.route('/', methods=['POST','POST'])
def calcul():
    humidity, temperature = Adafruit_DHT.read_retry(11, 4)

    hum_qa = 'Humidity OK'
    if humidity < 15 :
        hum_qa = 'Too dry'
    elif humidity > 45 : 
        hum_qa = 'Too wet'


    temp_qa = 'Temperature OK'
    if temperature < 16 :
        temp_qa = 'Too cold'
    elif temperature > 24 : 
        temp_qa = 'Too hot'

    temp = [str(temperature),  temp_qa]
    hum = [str(humidity), hum_qa]

    data = {
        'temp': temp,
        'hum': hum
    }
    return render_template('home.html', data=data)


