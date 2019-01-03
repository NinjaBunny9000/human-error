from engine import MyFirstGameEngine
import pygame


def main():
    
    # pygame setup
    pygame.init()
    pygame.display.set_caption("human-error")

    # Initialize the Engine
    game = MyFirstGameEngine()
    game.main_loop() 


if __name__ == "__main__":
    main()