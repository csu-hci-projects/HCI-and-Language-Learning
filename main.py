import pygame

pygame.init()

screen = pygame.display.set_mode([1100, 606])
running = True

ana_talking = [
    pygame.image.load("./images/ana-neutral.png"),
    pygame.image.load("./images/ana-neutral-talking.png")
]
background = pygame.image.load("./images/cafe-background.png")

clock = pygame.time.Clock()
ana_talking_val = 0
ana_talking_moving = True
ana_talking_velocity = 12

while running:
    #screen.fill((255, 255, 255))
    screen.blit(background, (0,0))
    clock.tick(5)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    if ana_talking_moving:
        ana_talking_val += 1
    if ana_talking_val >= len(ana_talking):
        ana_talking_val = 0

    image = ana_talking[ana_talking_val]
    image = pygame.transform.scale(image, (500,500))

    screen.blit(image, (300,106))
    pygame.display.update()

    

pygame.quit()