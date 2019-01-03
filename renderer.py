import os

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