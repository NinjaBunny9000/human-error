import os

# Step 1: Getting graphics rendering to the console

class Renderator:
	'Draw lines or characters - modifies the text buffer'

	# constructor
	def __init__(self):
		# 2d array of characters
		# 1d array of strings that's sliced to be the width of the map via indexes
		self.screen = [' '] * 100


	def draw_aussie_char(self, char, x_pos, y_pos):
		buffer_pos = y_pos * 10 + x_pos
		self.screen[buffer_pos] = char

	def draw_line(self):
		pass

	def render(self):
		'called once per update/frame/tick. draws text buffer to the console'
				
		# clear screan
		os.system('cls')

		# prints each line of the text buffer
		index = 0
		while index < 100: # REVIEW  (for i in range?)
			print(self.screen[index : index+10])
			index += 10

		# clear the text buffer to spaces (blank it out)
		self.screen = [' '] * 100


class GameObject:
	''
	
	# Constructure
	def __init__(self, engine):
		self.engine = engine

	def update(self):
		pass

	def render(self):
		pass


class MyFirstGameEngine:
	'Change this'
	
	# Constructor
	def __init__(self):
		self.renderator = Renderator()
		# TODO needs to be populated with GameObject(s) (and not dicks)
		self.objects = [DickObject(self), NipsObject(self)] # (dependancy injection)

	def update(self):
		"""
		Calls render and other classes and tells it to update it's infos 
		to the screen
		"""
		# iterate through list of objects & call that object's update method
		for thing in self.objects:
			thing.update()

	def render(self):
		'Wut do?'
		# iterate through list of objects & call that object's update method
		for thing in self.objects:
			thing.render()

		# Prints to the screen
		self.renderator.render()

	def main_loop(self):
		while(True):
			self.update()
			self.render()

class DickObject(GameObject):
	
	def update(self):
		pass

	def render(self):
		self.engine.renderator.draw_aussie_char('D',3,3)

	
class NipsObject(GameObject):
	
	def update(self):
		pass

	def render(self):
		self.engine.renderator.draw_aussie_char('@',0,0)


		
game = MyFirstGameEngine()

game.main_loop()