using System;
using System.Collections.Generic;
using SDL2;

namespace human_error
{
	class Program
	{
		static void Main(string[] args)
		{
			// Engine init
			Engine game = new Engine();
			
			// Engine loop forever and ever and ever and ever and ever and ever and ever and ever (until it's not)
			game.main_loop();
		}
	}

	class Renderator {

		// 1d array of strings that's sliced to be the width of the map via indexes
		char[] screen = new char[100];

		public IntPtr win;  
		public IntPtr ren;  


		// constructurator
		public Renderator() {
			// Set up stuff
			SDL.SDL_Init(SDL.SDL_INIT_VIDEO | SDL.SDL_INIT_AUDIO);
			win = SDL.SDL_CreateWindow("SDL2 Sharp", 50, 50, 1280, 720, SDL.SDL_WindowFlags.SDL_WINDOW_SHOWN);  
			ren = SDL.SDL_CreateRenderer(win, -1, SDL.SDL_RendererFlags.SDL_RENDERER_ACCELERATED | SDL.SDL_RendererFlags.SDL_RENDERER_PRESENTVSYNC);  
		}

		// spits out thigns
		public void drawAussieChar(char character, int xPos, int yPos) {
			int bufferPos = yPos * 10 + xPos;
			screen[bufferPos] = character;
		}

		// called once per update/frame/tick. draws text buffer to the console'
		public void render() {
			// TODO clear the screen
			// Console.Clear();

			// print each line of the text buffer
			// for ( int i = 0; i < 100 ; i++) {
			// 	Console.Write(screen[i]);
			// 	if ( i % 10 == 9) // xD
			// 		Console.Write("\n");
			// }
			SDL.SDL_RenderPresent(ren);
			// clear the text buffer to spaces (blank it out betch)
			// for (int i = 0; i < screen.Length; i++) {
			// 	screen[i] = ' ';
			// }
		}
	}

	class GameObject {

		protected Engine engine;

		// Constructure
		public GameObject(Engine engine) {
			// inheritance weirdy thing -- self.engine = engine
			this.engine = engine;
		}

		public virtual void update() {
			// pass
		}

		public virtual void render() {
			// pass
		}
	}

	class Engine {

		public Renderator renderator = new Renderator();

		List<GameObject> gameObjects = new List<GameObject>();

		 //go!  
		public bool bRunning = true;  
		

		// Constructurator
		public Engine() {
			// TODO inheritancy thingies????
			// TODO needs to be populated with actual GameObject(s) (and not dicks or nips)
			// (dependancy injection) self.objects = [DickObject(self), NipsObject(self)]
			gameObjects.Add(new DickObject(this));
			gameObjects.Add(new TiddyObject(this));
		}

		// Calls render and other classes and tells it to update it's infos to the screen
		public void update() {
			// iterate through list of objects & call that object's update method
			foreach (GameObject thing in gameObjects) {
				thing.update();
			}
		}

		public void render() {
			// iterate through list of objects & call that object's update method
			foreach (GameObject thing in gameObjects) {
				thing.render();
			}

			// print to the screen
			renderator.render();
		}

		public void main_loop() {
			SDL.SDL_Event systemEvent;  

			while(bRunning) {
				while(SDL.SDL_PollEvent(out systemEvent) != 0)  {  
					//This is an SDL2 escape event  
					if (systemEvent.type == SDL.SDL_EventType.SDL_QUIT) {  
						bRunning = false;  
					}
				}
				this.update();
				// this.render(); 
			}
			 
		}
	}

	class DickObject : GameObject {
		
		// Constructurematurator
		public DickObject(Engine engine) : base(engine) {

		}

		public override void update() {
			// pass
		}

		public override void render() {
			engine.renderator.drawAussieChar('8',3,3);
			engine.renderator.drawAussieChar('=',4,3);
			engine.renderator.drawAussieChar('=',5,3);
			engine.renderator.drawAussieChar('D',6,3);
			engine.renderator.drawAussieChar('~',7,3);
		}
	}

	class TiddyObject : GameObject {
		
		// Constructurematurator
		public TiddyObject(Engine engine) : base(engine) {

		}

		public override void update() {
			// pass
		}

		public override void render() {
			engine.renderator.drawAussieChar('(',0,1);
			engine.renderator.drawAussieChar(' ',1,1);
			engine.renderator.drawAussieChar('o',2,1);
			engine.renderator.drawAussieChar(' ',3,1);
			engine.renderator.drawAussieChar(')',4,1);
			engine.renderator.drawAussieChar('(',5,1);
			engine.renderator.drawAussieChar(' ',6,1);
			engine.renderator.drawAussieChar('o',7,1);
			engine.renderator.drawAussieChar(' ',8,1);
			engine.renderator.drawAussieChar(')',9,1);
		}
	}


}
