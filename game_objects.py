class GameObject:
	
	# Constructure
	def __init__(self, engine):
		self.engine = engine

	def update(self):
		pass

	def render(self):
		pass


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