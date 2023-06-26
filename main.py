"""
main.py is the executable for the game, run this to play the game!
"""
# - Module imports for the game
import pygame
from assets import Window, test_loop

# - Initialise modules
pygame.font.init()
pygame.display.init()

# - Renderer and flags to boost speed with each
RENDER = "SDL 2"
SDL_FLAGS = 512
OPENGL_FLAGS = 1073741824 | 1

# - Set attributes for the 'Window' class
window_attributes = {
	"dimensions": [1280, 720],
	"fullscreen": False,
	"renderer": RENDER,
	"running": True,
	"paused": False,
	"tex_id": None,
	"flags": OPENGL_FLAGS if RENDER == "OpenGL" else SDL_FLAGS,
	"clock": pygame.time.Clock(),
	"vsync": False,
	"loop": "test environment",
	"tick": "NA",
	"path": "assets/original/",
	"fps": 60
}

# - Create game object
game = Window(window_attributes, False, False)
game.set_game_surface("Blood Summit")

# - Main window loop
if __name__ == "__main__":
    while game.running:
        match game.loop:
            case "test environment":
                test_loop(game)

    pygame.display.quit()
