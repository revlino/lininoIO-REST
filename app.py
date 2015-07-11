#!/usr/bin/python

import os
import sys
import web
import modules.gpio
import modules.adc

urls = (
	'/gpio(.*)', 'GPIO',
	'/adc(.*)', 'ADC',
	'/(.*)', 'Docs',
	
)
app = web.application(urls, globals())

class Docs:
	
	def __init__(self,directory='/opt/lininoIO-REST/manual'):
		
		self.manual = ''
		
		items = os.listdir(directory)

		for item in items:
			
			if os.path.isdir("%s/%s" % (directory,item)):
				self.__init__(directory+"/"+item)
			
			if item.endswith(".txt"):
				
				f = open(directory+"/"+item,'r')
				self.manual += f.read()
				f.close()
		
		return 
	
	
	def GET(self, args):
		
		return self.manual
		
		
class GPIO:

	def __init__(self):
		
		f = open('/opt/lininoIO-REST/manual/gpio.txt', 'r')
		self.manual = f.read()
		f.close()

	
	def GET(self, args):
		
		args = args.split("/")
		
		tmp_args = []
		for arg in args:
			
			if arg.strip():
				
				tmp_args.append(arg)
		
		args = tmp_args

		if not args:
			
			return self.manual

		if args[0].lower() == 'mode':
			
			if len(args) == 3:
				
				try:
					return modules.gpio.pinMode(*args[1:])
					
				except:
					return sys.exc_info()[1]
					
			if len(args) == 2:
				
				try:
					return modules.gpio.read_direction(*args[1:])
					
				except:
					return sys.exc_info()[1]

			return self.manual
			
		elif args[0].lower() == 'export':
			
			if len(args) == 2:
				
				try:
					return modules.gpio.export(*args[1:])
					
				except:
					return sys.exc_info()[1]

			return self.manual

		elif args[0].lower() == 'unexport':
			
			if len(args) == 2:
				
				try:
					return modules.gpio.unexport(*args[1:])
					
				except:
					return sys.exc_info()[1]

			return self.manual
			
		elif args[0].lower() == 'direction':
			
			if len(args) == 3:
				
				try:
					return modules.gpio.write_direction(*args[1:])
					
				except:
					return sys.exc_info()[1]
					
			if len(args) == 2:
				
				try:
					return modules.gpio.read_direction(*args[1:])
					
				except:
					return sys.exc_info()[1]

			return self.manual			
			
		else:
			
			if len(args) == 2:

				try:
					return modules.gpio.write_value(*args)
					
				except:
					return sys.exc_info()[1]				
				
			if len(args) == 1:

				try:
					return modules.gpio.read_value(*args)
					
				except:
					return sys.exc_info()[1]
					
			return self.manual


class ADC:

	def __init__(self):
		
		f = open('/opt/lininoIO-REST/manual/adc.txt', 'r')
		self.manual = f.read()
		f.close()

	
	def GET(self, args):
		
		args = args.split("/")
		
		tmp_args = []
		for arg in args:
			
			if arg.strip():
				
				tmp_args.append(arg)
		
		args = tmp_args

		if not args:
			
			return self.manual
		
		if args[0].lower() == 'export':
			
			if len(args) == 1:
				
				try:
					return modules.adc.export()
					
				except:
					return sys.exc_info()[1]
			
			return self.manual		
			
		elif args[0].lower() == 'scale':
			
			if len(args) == 2:
				
				try:
					return modules.adc.read_scale(*args[1:])
					
				except:
					return sys.exc_info()[1]
			
			return self.manual	
			
		elif args[0].lower() == 'voltage':
			
			if len(args) == 2:
				
				try:
					return modules.adc.read_voltage(*args[1:])
					
				except:
					return sys.exc_info()[1]
			
			return self.manual	
			
		else:
			
			if len(args) == 1:
				
				try:
					return modules.adc.read_value(*args)
					
				except:
					return sys.exc_info()[1]
					
			return self.manual


if __name__ == "__main__":
	app.run()
