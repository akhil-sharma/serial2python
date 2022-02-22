import serial
import requests

PORT_NAME = 'COM3'
BAUDRATE  = 9600
TIMEOUT = .1
WEBHOOK_URL = "https://maker.ifttt.com/trigger/soil_moisture_changed/json/with/key/pTWdShVd6Lx8Bg6SDh8Wo7gApQ3wR1achlY-ke1oYUT"

def handleRawData(data: str) -> None:
    number, name = data.strip().split(" ")
    payload = {
        "number": number,
        "name": name 
    }
    response = requests.post(WEBHOOK_URL, payload)
    print(response.text)
    

arduino = serial.Serial(port=PORT_NAME, baudrate=BAUDRATE, timeout=TIMEOUT)
arduino.flushInput()
arduino.flushOutput()

while True:
  data_raw = arduino.readline()
  if data_raw:
      handleRawData(data_raw.decode('ascii'))
