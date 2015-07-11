# Python module for controlling Arduino Yun GPIO pins

class LininoIOError(Exception):
	pass

class PinError(LininoIOError):
	pass

class ModeError(LininoIOError):
	pass
	
class ValueError(LininoIOError):
	pass


def pin_map():

	map = {
		0: {'id': 0, 'name': 'D0'},
		1: {'id': 0, 'name': 'D1'},
		2: {'id': 117, 'name': 'D2'},
		3: {'id': 116, 'name': 'D3'},
		4: {'id': 120, 'name': 'D4'},
		5: {'id': 114, 'name': 'D5'},
		6: {'id': 123, 'name': 'D6'},
		7: {'id': 0, 'name': 'D7'},
		8: {'id': 104, 'name': 'D8'},
		9: {'id': 105, 'name': 'D9'},
		10: {'id': 106, 'name': 'D10'},
		11: {'id': 107, 'name': 'D11'},
		12: {'id': 122, 'name': 'D12'},
		13: {'id': 115, 'name': 'D13'},
	}
	
	return map


def get_pin(pin):
	
	# vars
	pins = pin_map()
	
	if isinstance(pin,basestring):
		
		pin = pin.lower().replace('d','')
		
		if not pin.isdigit():
			
			raise PinError("Pin '%s' is not a gpio pin." % pin)
			
		pin = int(pin)
	
	if isinstance(pin,int):
		
		if not pins[pin]['id']:
	
			raise PinError("Pin '%d' is not a supported gpio pin." % pin)
			
		return pin
			
	else:
		
		raise PinError("'%s' is not a gpio pin." % str(pin))


def read_direction(pin):
	
	# vars
	pins = pin_map()
	pin = get_pin(pin)
	
	modes = {
		'in': 'INPUT',
		'out': 'OUTPUT',
	}
	
	try:
		f = open('/sys/class/gpio/%s/direction'% pins[pin]['name'],'r')
		mode = f.read().strip()
		f.close()
		
		return modes[mode]
		
	except:
		
		raise ModeError("Pin '%d' is not set." % pin)


def write_direction(pin,mode):
	
	# vars
	pins = pin_map()
	pin = get_pin(pin)	
	
	modes = {
		'input': 'in',
		'output': 'out',
		
		'in': 'in',
		'out': 'out',
		
		#'INPUT_PULLUP': 'NOT AVAILABLE',
	}

	if mode.lower() not in modes:
		
		raise ModeError("Mode '%s' is not a supported gpio mode." % str(mode))

	# set pin direction
	f = open('/sys/class/gpio/%s/direction'% pins[pin]['name'],'w')
	f.write(modes[mode.lower()])
	f.close()
	
	return None


def read_value(pin):

	# vars
	pins = pin_map()
	pin = get_pin(pin)
	
	# check if pin is set
	read_direction(pin)
	
	# read value
	f = open('/sys/class/gpio/%s/value' % pins[pin]['name'],'r')
	value = int(f.read().strip())
	f.close()

	return value


def write_value(pin,value):
	
	# vars
	pins = pin_map()
	pin = get_pin(pin)
	
	values = {
		False: '0',
		True: '1',
		0: '0',
		1: '1',
		'0': '0',
		'1': '1',		
		
	}
	
	# check if pin is set to Output
	if read_direction(pin) != 'OUTPUT':
		
		raise ModeError("Pin '%d' mode is not set to 'OUTPUT'." % pin)
		
	# check to see is value exists
	if value not in values:
		
		raise ValueError("Value '%s' is not a supported gpio value." % str(value))
	
	# write value
	f = open('/sys/class/gpio/%s/value' % pins[pin]['name'],'w')
	f.write(values[value])
	f.close()	
	
	return None


def export(pin):
	
	# vars
	pins = pin_map()
	pin = get_pin(pin)
	
	try:
		# is the pin already exported?
		read_direction(pin)
		
		raise PinError("Pin '%d' has already been exported." % pin)
		
	except ModeError:
		
		# no,  export pin
		f = open('/sys/class/gpio/export','w')
		f.write(str(pins[pin]['id']))
		f.close()
	
	return None


def unexport(pin):
	
	# vars
	pins = pin_map()
	pin = get_pin(pin)
	
	# is the pin exported?
	if read_direction(pin) == "OUTPUT":
		
		# turn off pin
		write_value(pin,0)

	# unexport pin
	f = open('/sys/class/gpio/unexport','w')
	f.write(str(pins[pin]['id']))
	f.close()
	
	return None

	
''' These methods emulate native Arduino C functions
'''

def pinMode(pin, mode):

	export(pin)
	write_direction(pin,mode)
	
	return None


def digitalWrite(pin, value):
	
	return write_value(pin,value)

	
def digitalRead(pin):
	
	return read_value(pin)
