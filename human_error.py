# Step 1: Getting graphics rendering to the console

class Renderator:
    'Draw lines or characters - modifies the text buffer'

    def draw_aussie_char(self):
        pass

    def draw_line(self):
        pass

    def render(self):
        'called once per update/frame/tick. draws text buffer to the console'
        # clear screan
        # prints each line of the text buffer
        # clear the text buffer to spaces (blank it out)
        pass


class GameObject:
    ''
    
    # Constructure
    def __init__(self):
        pass

    def update(self):
        print('dicks')

    def render(self):
        pass


class Engine:
    'Change this'
    
    # Constructor
    def __init__(self):
        self.renderator = Renderator()
        self.objects = [GameObject()] # TODO needs to be populated with GameObject(s)

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
        
game = Engine()

game.main_loop()