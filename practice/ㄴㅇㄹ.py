import pygame

pygame.init()
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE= (0,0,255)
GREEN = (0,255,0)
RED= (255,0,0)
size = [400, 300]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Drawing Rectangle")
done = False
clock = pygame.time.Clock()

while not done:
    clock.tick(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done=True
    screen.fill(WHITE)
    
    pygame.draw.rect(screen, BLACK, [75, 10, 50, 20], 0)
    pygame.draw.rect(screen, BLACK, [150, 10, 50, 20])
    pygame.display.flip()
