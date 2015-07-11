REST API for LininoIO
=====
This is a complete REST API for controlling an Arduino Yun, Linino One, or similar device.

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
  python /opt/lininoIO_REST/app.py
- Access the API:
```
  http://arduino.local:8080/
```
Examples:
---
```
http://arduino.local:8080/gpio/export/13 (export pin D13)
http://arduino.local:8080/gpio/direction/out (change pin direction to out)
http://arduino.local:8080/gpio/13/1 (send HIGH to pin D13)
http://arduino.local:8080/gpio/13/ (read vaue of pin D13)
http://arduino.local:8080/gpio/unexport/13 (unexport pin D13)
```
