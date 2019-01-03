import game_objects
from renderer import Renderator

class MyFirstGameEngine:
	'Change this'
	
	# Constructor
	def __init__(self):
		self.renderator = Renderator()
		# TODO needs to be populated with GameObject(s) (and not dicks)
		self.objects = [game_objects.DickObject(self), game_objects.NipsObject(self)] # (dependancy injection)

	def update(self):
		"""
		Calls render and other classes and tells it to update it's infos 
		to the screen
		"""
		# iterate through list of objects & call that object's update method
		for thing in self.objects:
			thing.update()

	def render(self):
		# iterate through list of objects & call that object's update method
		for thing in self.objects:
			thing.render()

		# Prints to the screen
		self.renderator.render()

	def main_loop(self):
		while(True):
			self.update()
			self.render()