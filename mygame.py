__author__ = 'Alex Sattarov'

import sys, pygame
from pygame.locals import *
from PodSixNet.Channel import Channel

class Player:
	def __init__(self, avatar_image, nickname):
		self.avatar = avatar_image
		self.nickname = nickname

def main(args):
	#I dont understand, why it is not work with initializate
	#pygame.init()
	screen = pygame.display.set_mode((800, 600), 0, 32)
	pygame.display.set_caption("Group WAR")
	mainLoop = True
	while mainLoop:
		for event in pygame.event.get():
			if event.type == QUIT:
				mainLoop = False
		pygame.display.update()
	pygame.quit()

if __name__ == '__main__':
	main(sys.argv)