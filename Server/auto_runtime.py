from Control import *
# Also need to import ultrasonic module and camera module.
# To do: write voice command class, called "listener" using PocketSphinx
# To do: write face recognizer that takes input from camera module and recognizes a face

class Dog():
	"""
	This is where al of our control code will go.
	"""
	
	def __init__(self);
		# Set attributes here
		self.controller = Control()
		self.is_wall = False
		self.is_face = False
		self.command = None
		
		#self.listener = instance of listener class
		#self.recognizer = ...
		# etc.
	
	def detect(self):
		self.is_face = self.detect_face()
		self.is_wall = self.detect_wall()
		self.command = self.detect_command()
	
	def detect_face(self):
		# if there's a face somewhere in view, then return true. If not, then return false.
		# Use the self.listener to refer to the listener object to help with this function.
		pass
	
	def detect_command(self):
		# if there's a command, then return the word it heard. If not, then return null.
		pass
		
	def detect_wall(self):
		#If the ultrasonic sensor says we're 'too close' to a wall, then return true. If not, return false.
		
	
	def showtime(self):
		# Main runtime loop. The loop is intended to run forever, any other function we make should be called here.
		
		while True:
			self.detect()
			
			if self.wall:
				#avoid the wall
				pass
			
			else if self.command is not None:
				# do the command
				pass
			else if self.face:
				# start moving toward it. 
				pass
			else:
				# do a random action from list of viable actions.
				# actions may include: look up and down, move forward, turn left, turn right, stop moving, etc.
				pass
			
	


if __name__ == '__main__':
	try:
		dog = Dog()
		dog.showtime()
	except KeyboardInterrupt:
        print ("\nEnd of program")
        break
