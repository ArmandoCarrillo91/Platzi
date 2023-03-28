import pygame

pygame.init()

window_size = (500,500)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption('Juego de Ajedrez')

running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
	screen.fill((255,255,255))
	pygame.draw.rect(screen, (0,0,0), (100,100,50,50))
	pygame.display.update()

pygame.quit()