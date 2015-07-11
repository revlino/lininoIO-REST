#REST API for LininoIO
This is a REST API for controlling an Arduino Yun, Linino One, or similar device.

Requirements:
---
- LininoOS v1.2 or higher
- LininoIO and bathos sketch
- Python
- Webpy

Setup:
---
- Unpack the package in /opt
- Start the server with the following command:
```
  python /opt/lininoIO_REST/app.py
```
- Access the API:
```
  http://arduino.local:8080/
```
Examples:
---
- GPIO
```
http://arduino.local:8080/gpio/export/13 (export pin D13)
http://arduino.local:8080/gpio/direction/out (change pin direction to out)
http://arduino.local:8080/gpio/13/1 (send HIGH to pin D13)
http://arduino.local:8080/gpio/13/ (read value of pin D13)
http://arduino.local:8080/gpio/unexport/13 (unexport pin D13)
```
- A/D Converter
```
http://arduino.local:8080/adc/export (export analog pins)
http://arduino.local:8080/adc/scale/5 (read scale of pin A5)
http://arduino.local:8080/adc/voltage/5 (read voltage of pin A5 in microVolts)
http://arduino.local:8080/adc/5 (read value of pin A5, 0 - 1024)
```
