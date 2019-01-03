import game_objects
from renderer import Renderator
import pygame

class MyFirstGameEngine:
    'Change this'
        
    # Constructor
    def __init__(self):
        self.renderator = Renderator()
        # TODO needs to be populated with GameObject(s) (and not dicks)
        self.objects = [game_objects.DickObject(self), game_objects.NipsObject(self)] # (dependancy injection)
        self.running = True
        self.screen = pygame.display.set_mode((680,400)) 


    def update(self):
        """
        Calls render and other classes and tells it to update it's infos 
        to the screen
        """
        
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                self.running = False

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
        while(self.running):
            self.update()
            self.render()