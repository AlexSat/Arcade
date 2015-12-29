__author__ = 'Alex Sattarov'

import os, sys, pygame
from pygame.locals import *
from PodSixNet.Channel import Channel

#https://github.com/Mekire/pygame-button
#Mekire, Thank you!
from button import Button

from colors import *

class Player:
	def __init__(self, avatar_image, nickname):
		self.avatar = avatar_image
		self.nickname = nickname

#For controlling a drawing graphics information
class GraphicsController:
	def __init__(self, screen, screen_size):
		self.screen = screen
		self.size = screen_size
		self.BUTTON_STYLE = {"hover_color" : BLUE,
		                     "clicked_color" : GREEN,
		                     "clicked_font_color" : BLACK,
		                     "hover_font_color" : ORANGE,
		                     #http://www.freesound.org/people/fins/sounds/146721/
		                     "click_sound" : pygame.mixer.Sound("146721__fins__menu-click.wav")}
		self.startMenu = False
		self.color = WHITE
		#                   Message,             width, height
		self.mconnectbtn = ("Connect to server", 300,   50)
		self.mcreateserver = "Create server"
		self.connectBtn = Button((0, 0, self.mconnectbtn[1], self.mconnectbtn[2]), RED, self.connectToServer, text=self.mconnectbtn[0], font=pygame.font.Font(pygame.font.get_default_font(), 25), **self.BUTTON_STYLE)
		self.connectBtn.rect.center = (self.size[0] // 2, self.size[1] // 2)

	#Change scene state to drawing startMenu
	def setStartMenu(self):
		self.startMenu = True

	#Repaint method to drawing scene depending on status (start menu, game, ... )
	def updateScreen(self):
		if self.startMenu:
			self.screen.fill(self.color)
			self.connectBtn.update(self.screen)

	#Change scene graphics for entering ip of server
	def connectToServer(self):
		pass

	#Processing event depending on state (menu, game, connecting to server...)
	def event(self, event):
		if self.startMenu:
			self.connectBtn.check_event(event)

#Only for controlling a main window
class Window:
	def __init__(self, window_size=(800, 600), flags=0, depth=32, title="Window", icon=None):
		pygame.init()
		self.size = window_size
		self.screen = pygame.display.set_mode(window_size, flags, depth)
		self.screen_rect = self.screen.get_rect()
		self.clock = pygame.time.Clock()
		self.fps = 60.0
		self.color = WHITE
		pygame.display.set_caption(title)
		if type(icon) is pygame.SurfaceType:
			pygame.display.set_icon(pygame.transform.scale(icon, (32, 32)))
		self.graphics = GraphicsController(self.screen, window_size)
		self.graphics.setStartMenu()

	def event_loop(self):
		for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.mainLoop = False
				else:
					self.graphics.event(event)

	def mainLoop(self):
		self.mainLoop = True
		while self.mainLoop:
			self.event_loop()
			self.graphics.updateScreen()
			pygame.display.update()
			self.clock.tick(self.fps)



def main(args):
	game = Window((800, 600), 0, 32, "Group WAR", pygame.image.load("icon.png"))
	game.mainLoop()
	pygame.quit()
	sys.exit()

if __name__ == '__main__':
	#place python-window in center of screen
	os.environ["SDL_VIDEO_CENTERED"] = '1'
	main(sys.argv)