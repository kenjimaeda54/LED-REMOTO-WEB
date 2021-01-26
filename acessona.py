from flask import Flask,render_template
import datetime
import RPi.GPIO as GPIO
app = Flask(__name__)
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

estado={'LED': False}

LED=20

GPIO.setup(LED,GPIO.OUT)
GPIO.output(LED,0)
@app.route("/")
def inicio():
    return mostra_estado()

@app.route('/LED/1')
def ligar_led():
     GPIO.output(LED,1)
     return mostra_estado()
@app.route('/LED/0')
def desliga_led():
    GPIO.output(LED,0)
    return mostra_estado()
	
def mostra_estado():
    estado={'LED':GPIO.input(LED)}
    return render_template('controles-led.html',**estado)
app.run(host='0.0.0.0',debug=True)
				


