import os, sys, time
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello boys and girls'

@app.route('/gettemp')
def gettemp():
    temp = readTemp()
    TextStr = "Temperatur: " + str(temp) + " °C"
    return TextStr

@app.route('/gethtmltemp')
def gethtmltemp():
    temp = readTemp()
    return '''
<html>
    <head>
        <meta http-equiv="refresh" content="10">
        <title>My Temperature</title>
    </head>
    <body>
        <h1>Temperatur: ''' + temp + '''°C</h1>
    </body>
</html>'''

def readTemp():
    # 1-wire Slave Datei lesen
    file = open('/sys/bus/w1/devices/28-000005d2e508/w1_slave')
    filecontent = file.read()
    file.close()
 
    # Temperaturwerte auslesen und konvertieren
    stringvalue = filecontent.split("\n")[1].split(" ")[9]
    temperature = float(stringvalue[2:]) / 1000
 
    # Temperatur ausgeben
    rueckgabewert = '%6.2f' % temperature 
    return(rueckgabewert)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')