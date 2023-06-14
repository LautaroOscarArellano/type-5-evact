import pygame
import sys
import random

from config import *
from nave import Nave
from asteroide import Asteroide


def generar_asteroides(grupo_asteroides, grupo_sprites, cantidad):
    if len(grupo_asteroides) == 0:
        for i in range(cantidad):
            posicion = (random.randrange(20, WIDTH - 20),
                        random.randrange(-500, HEIGHT // 2))
            asteroide = Asteroide("./images/asteroide.png",
                                  SIZE_ASTERIOD, posicion, SPEED_ASTEROIDE)
            grupo_asteroides.add(asteroide)
            grupo_sprites.add(asteroide)


pygame.init()
#
reloj = pygame.time.Clock()

sonido = pygame.mixer.Sound("./sounds/laser.mp3")

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sprites")

fondo = pygame.image.load("./images/background.jpg").convert()
fondo = pygame.transform.scale(fondo, (WIDTH, HEIGHT))

sprites = pygame.sprite.Group()
asteroides = pygame.sprite.Group()
lasers = pygame.sprite.Group()


nave = Nave("./images/nave.png", SIZE_SHIP,
            (screen.get_width() // 2, screen.get_height() - 20))

sprites.add(nave)


while True:
    reloj.tick(FPS)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                nave.velocidad_x = -SPEED_SHIP
                print(nave.velocidad_x)
            if evento.key == pygame.K_RIGHT:
                nave.velocidad_x = SPEED_SHIP
            if evento.key == pygame.K_UP:
                nave.velocidad_y = -SPEED_SHIP
            if evento.key == pygame.K_DOWN:
                nave.velocidad_y = SPEED_SHIP
            if evento.key == pygame.K_SPACE:
                nave.disparar(sonido, SPEED_LASER, sprites, lasers)
                
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT:
                nave.velocidad_x = 0
            elif evento.key == pygame.K_RIGHT:
                nave.velocidad_x = 0
            elif evento.key == pygame.K_UP:
                nave.velocidad_y = 0
            elif evento.key == pygame.K_DOWN:
                nave.velocidad_y = 0

    generar_asteroides(asteroides, sprites, MAX_ASTEROIDES)

    sprites.update()

    if nave.rect.left <= 0:
        nave.rect.left = 0
    elif nave.rect.right >= WIDTH:
        nave.rect.right = WIDTH
    if nave.rect.top <= 0:
        nave.rect.top = 0
    elif nave.rect.bottom >= HEIGHT:
        nave.rect.bottom = HEIGHT

    for asteroide in asteroides:
        if asteroide.rect.bottom >= HEIGHT:
            asteroide.kill()
        lista = pygame.sprite.spritecollide(nave, asteroides, True)


    for laser in lasers:
      if laser.rect.top <= 0:
        laser.kill()
        
      lista = pygame.sprite.spritecollide(laser, asteroides, True)
      if len(lista):
        laser.kill()

    screen.blit(fondo, ORIGIN)

    sprites.draw(screen)

    pygame.display.flip()
