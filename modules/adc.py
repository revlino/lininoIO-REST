# Python module for controlling Arduino Yun Analog pins

class LininoIOError(Exception):
	pass

class DeviceError(LininoIOError):
	pass

class PinError(LininoIOError):
	pass


def pin_map():

	map = {
		0: {'id': 0, 'name': 'A0'},
		1: {'id': 1, 'name': 'A1'},
		2: {'id': 2, 'name': 'A2'},
		3: {'id': 3, 'name': 'A3'},
		4: {'id': 4, 'name': 'A4'},
		5: {'id': 5, 'name': 'A5'},
	}
	
	return map


def get_pin(pin):
	
	# vars
	pins = pin_map()
	
	if isinstance(pin,basestring):
		
		pin = pin.lower().replace('a','')
		
		if not pin.isdigit():
			
			raise PinError("Pin '%s' is not an analog pin." % pin)
			
		pin = int(pin)
	
	if isinstance(pin,int):
		
		if not pin in pins:
	
			raise PinError("Pin '%d' is not an analog pin." % pin)
			
		return pin
			
	else:
		
		raise PinError("'%s' is not an analog pin." % str(pin))


def export():
	
	try:
		f = open('/sys/bus/iio/devices/iio:device0/enable', 'w')
		f.write('1')
		f.close()
	
	except IOError:
		
		raise DeviceError("Device not found.")	
	
	return None

	
def read_value(pin):

	# vars
	pins = pin_map()
	pin = get_pin(pin)
	
	try:
	
		# read value
		f = open('/sys/bus/iio/devices/iio:device0/in_voltage_%s_raw' % pins[pin]['name'],'r')
		value = int(f.read().strip())
		f.close()
		
	except IOError:
		
		raise PinError("Analog pins are not enabled.")

	return value


def read_scale(pin):

	# vars
	pins = pin_map()
	pin = get_pin(pin)
	
	try:
	
		# read value
		f = open('/sys/bus/iio/devices/iio:device0/in_voltage_%s_scale' % pins[pin]['name'],'r')
		value = int(f.read().strip())
		f.close()
		
	except IOError:
		
		raise PinError("Analog pins are not enabled.")

	return value
	
	
def read_voltage(pin):
	
	return read_value(pin) * read_scale(pin)



''' These methods emulate native Arduino C functions
'''	
	
def analogRead(pin):
	
	return read_value(pin)
