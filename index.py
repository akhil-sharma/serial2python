# importing required modules.
import serial # Reading to and writing from the serial stream
import requests # Sending web requests

# contants
# TODO: Modify based on your settings. 
PORT_NAME = 'COM3'
BAUDRATE  = 9600
TIMEOUT = .1
WEBHOOK_URL = "https://maker.ifttt.com/trigger/soil_moisture_changed/json/with/key/pTWdShVd6Lx8Bg6SDh8Wo7gApQ3wR1achlY-ke1oYUT"

# Simple method for sending the web request to the IFTTT webhook. 
def handleRawData(data: str) -> None:
    number, name = data.strip().split(" ")
    payload = {
        "number": number,
        "name": name 
    }
    response = requests.post(WEBHOOK_URL, payload)
    print(response.text)
    
# Open the serial port.
arduino = serial.Serial(port=PORT_NAME, baudrate=BAUDRATE, timeout=TIMEOUT)

# Clear the input and output streams. 
arduino.flushInput()
arduino.flushOutput()

# Continuously read the data stream on the serial port.
while True:
  data_raw = arduino.readline()
  if data_raw:
      handleRawData(data_raw.decode('ascii'))
