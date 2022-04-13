import pygame
from gtts import gTTS
  
# This module is imported so that we can 
# play the converted audio
pygame.mixer.init()
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

pygame.mixer.music.load("./sounds/hola.mp3")
pygame.mixer.music.play()
MUSIC_END = pygame.USEREVENT+1
pygame.mixer.music.set_endevent(MUSIC_END)

while running:
    #screen.fill((255, 255, 255))
    screen.blit(background, (0, 0))
    clock.tick(7)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == MUSIC_END:
            ana_talking_moving = False
        if event.type == pygame.KEYDOWN:
            ana_talking_moving = True
            if event.key == pygame.K_1:
                pygame.mixer.music.load("./sounds./como_llamas.mp3")
                pygame.mixer.music.play()
            elif event.key == pygame.K_q:
                pygame.mixer.music.load("./sounds./gusta_nombre.mp3")
                pygame.mixer.music.play()
            elif event.key == pygame.K_2:
                pygame.mixer.music.load("./sounds./donde_eres.mp3")
                pygame.mixer.music.play()
            elif event.key == pygame.K_w:
                pygame.mixer.music.load("./sounds./nunca_visitado.mp3")
                pygame.mixer.music.play()
            elif event.key == pygame.K_s:
                pygame.mixer.music.load("./sounds./soy_de.mp3")
                pygame.mixer.music.play()
            elif event.key == pygame.K_3:
                pygame.mixer.music.load("./sounds./que_tal.mp3")
                pygame.mixer.music.play()
            elif event.key == pygame.K_e:
                pygame.mixer.music.load("./sounds./que_bueno.mp3")
                pygame.mixer.music.play()
            elif event.key == pygame.K_d:
                pygame.mixer.music.load("./sounds./estoy_feliz.mp3")
                pygame.mixer.music.play()
            elif event.key == pygame.K_4:
                pygame.mixer.music.load("./sounds./que_haces.mp3")
                pygame.mixer.music.play()
            elif event.key == pygame.K_r:
                pygame.mixer.music.load("./sounds./interesante.mp3")
                pygame.mixer.music.play()
            elif event.key == pygame.K_f:
                pygame.mixer.music.load("./sounds./trabajo_como.mp3")
                pygame.mixer.music.play()
            elif event.key == pygame.K_5:
                pygame.mixer.music.load("./sounds./cuantos_años.mp3")
                pygame.mixer.music.play()
            elif event.key == pygame.K_t:
                pygame.mixer.music.load("./sounds./viejisima.mp3")
                pygame.mixer.music.play()
            elif event.key == pygame.K_g:
                pygame.mixer.music.load("./sounds./tengo_semanas.mp3")
                pygame.mixer.music.play()
            elif event.key == pygame.K_6:
                pygame.mixer.music.load("./sounds./que_estudias.mp3")
                pygame.mixer.music.play()
            elif event.key == pygame.K_y:
                pygame.mixer.music.load("./sounds./interesante.mp3")
                pygame.mixer.music.play()
            elif event.key == pygame.K_h:
                pygame.mixer.music.load("./sounds./soy_maquina.mp3")
                pygame.mixer.music.play()
            elif event.key == pygame.K_a:
                pygame.mixer.music.load("./sounds/hola.mp3")
                pygame.mixer.music.play()
            elif event.key == pygame.K_0:
                pygame.mixer.music.load("./sounds/no_entiendo.mp3")
                pygame.mixer.music.play()


    if ana_talking_moving:
        ana_talking_val += 1
    else:
        ana_talking_val = 0
    if ana_talking_val >= len(ana_talking):
        ana_talking_val = 0

    image = ana_talking[ana_talking_val]
    image = pygame.transform.scale(image, (500, 500))

    screen.blit(image, (300, 106))
    pygame.display.update()

pygame.quit()