__author__ = 'Alex Sattarov'

import os, sys, pygame
from pygame.locals import *
from PodSixNet.Channel import Channel

#https://github.com/Mekire/pygame-button
#Mekire, Thank you!
from button import Button

class Player:
	def __init__(self, avatar_image, nickname):
		self.avatar = avatar_image
		self.nickname = nickname

class Window:
	def __init__(self, window_size=(800, 600), flags=0, depth=32, title="Window", icon=None):
		#I dont understand, why it is not work with initializate
		#pygame.init()
		self.screen = pygame.display.set_mode(window_size, flags, depth)
		pygame.display.set_caption(title)
		if type(icon) is pygame.SurfaceType:
			pygame.display.set_icon(pygame.transform.scale(icon, (32, 32)))

	def mainLoop(self):
		self.mainLoop = True
		while self.mainLoop:
			for event in pygame.event.get():
				if event.type == QUIT:
					self.mainLoop = False
			pygame.display.update()

def main(args):
	game = Window((800, 600), 0, 32, "Group WAR", pygame.image.load("icon.png"))
	game.mainLoop()
	pygame.quit()
	sys.exit()

if __name__ == '__main__':
	#place python-window in center of screen
	os.environ["SDL_VIDEO_CENTERED"] = '1'
	main(sys.argv)