#!/usr/bin/python

import sys
import web
import lininoIO.gpio

urls = (
	'/gpio(.*)', 'GPIO'
)
app = web.application(urls, globals())

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
					return lininoIO.gpio.pinMode(*args[1:])
					
				except:
					return sys.exc_info()[1]
					
			if len(args) == 2:
				
				try:
					return lininoIO.gpio.read_direction(*args[1:])
					
				except:
					return sys.exc_info()[1]

			return self.manual
			
		elif args[0].lower() == 'export':
			
			if len(args) == 2:
				
				try:
					return lininoIO.gpio.export(*args[1:])
					
				except:
					return sys.exc_info()[1]

			return self.manual

		elif args[0].lower() == 'unexport':
			
			if len(args) == 2:
				
				try:
					return lininoIO.gpio.unexport(*args[1:])
					
				except:
					return sys.exc_info()[1]

			return self.manual
			
		elif args[0].lower() == 'direction':
			
			if len(args) == 3:
				
				try:
					return lininoIO.gpio.write_direction(*args[1:])
					
				except:
					return sys.exc_info()[1]
					
			if len(args) == 2:
				
				try:
					return lininoIO.gpio.read_direction(*args[1:])
					
				except:
					return sys.exc_info()[1]

			return self.manual			
			
		else:
			
			if len(args) == 2:

				try:
					return lininoIO.gpio.write_value(*args)
					
				except:
					return sys.exc_info()[1]				
				
			if len(args) == 1:

				try:
					return lininoIO.gpio.read_value(*args)
					
				except:
					return sys.exc_info()[1]
					
			return self.manual


if __name__ == "__main__":
	app.run()
