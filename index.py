# importing required modules.
from email import message
import serial # Reading to and writing from the serial stream
import requests # Sending web requests

# contants
# TODO: Modify based on your settings. 
PORT_NAME = '/dev/ttyUSB0'
BAUDRATE  = 9600
TIMEOUT = .1
WEBHOOK_URL = "https://test-twi-server.herokuapp.com/messages"

# Simple method for sending the web request to the IFTTT webhook. 
def handleRawData(data: str) -> None:
    message_text, message_stream_id = data.strip().split("#")
    print(message_text, message_stream_id)
    payload = {
        "message_text": message_text,
        "message_stream_id": message_stream_id
    }

    response = requests.post(WEBHOOK_URL, json=payload)
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
