
import pygame
import sys
import random

from config import *
from nave import Nave
from asteroide import Asteroide

class Juego:
    def __init__(self) :
        pygame.init()
        pygame.display.set_caption("Sprites")
        self.reloj = pygame.time.Clock()
        self.sonido = pygame.mixer.Sound("./sounds/laser.mp3")
        self.sonido = pygame.mixer.Sound("./sounds/laser.mp3")
        self.score=0
        self.jugando=False
        self.screen=pygame.display.set_mode((WIDTH, HEIGHT))

        self.fondo = pygame.image.load("./images/background.jpg").convert()
        self.fondo = pygame.transform.scale(self.fondo, (WIDTH, HEIGHT))

        self.sprites = pygame.sprite.Group()
        self.asteroides = pygame.sprite.Group()
        self.lasers = pygame.sprite.Group()

        self.nave = Nave("./images/nave.png", SIZE_SHIP,
            (self.screen.get_width() // 2, self.screen.get_height() - 20))
        


    def agregar_sprite(self , sprite):
        self.sprites.add(sprite)
    def agregar_asteroide(self, asteroide):
        self.asteroides.add(asteroide)
    def  agregar_laser(self , laser):
        self.lasers.add(laser)

    def start(self):
        self.jugando = True
        while self.jugando:
            self.reloj.tick(FPS)

            self.manejar_eventos()
            self.actualizar_elementos(self)
            self.sprites.update()

            for asteroide in self.asteroides:
                if asteroide.rect.bottom >= HEIGHT:
                    asteroide.kill()
                lista = pygame.sprite.spritecollide(self.nave, self.asteroides, True)


            for laser in self.lasers:
                if laser.rect.top <= 0:
                    laser.kill()
                
            lista = pygame.sprite.spritecollide(laser, self.asteroides, True)
            if len(lista):
                laser.kill()

            

    pygame.display.flip()


    #EVENTOS
    def manejar_eventos(self):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                self.salir()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    self.nave.velocidad_x = -SPEED_SHIP
                    print(self.nave.velocidad_x)
                elif evento.key == pygame.K_RIGHT:
                    self.nave.velocidad_x = SPEED_SHIP
                elif evento.key == pygame.K_UP:
                   self.nave.velocidad_y = -SPEED_SHIP
                elif evento.key == pygame.K_DOWN:
                    self.nave.velocidad_y = SPEED_SHIP
                elif evento.key == pygame.K_SPACE:
                    self.nave.disparar(self.sonido, SPEED_LASER,self.sprites, self.lasers)
                elif evento.key==pygame.K_ESCAPE:
                    self.terminar()


            elif evento.type == pygame.KEYUP:
                if evento.key == pygame.K_LEFT:
                    self.nave.velocidad_x = 0
                elif evento.key == pygame.K_RIGHT:
                    self.nave.velocidad_x = 0
                elif evento.key == pygame.K_UP:
                    self.nave.velocidad_y = 0
                elif evento.key == pygame.K_DOWN:
                    self.nave.velocidad_y = 0


    def actualizar_elementos(self):
        self.generar_asteroides(MAX_ASTEROIDES)
        self.sprites.update()

    def renderizar_pantalla(self):
        self.renderizar_pantalla()
        self.screen.blit(self.fondo, ORIGIN)
        self.sprites.draw(self.screen)


    def salir(self):
        pygame.quit()
        sys.exit()

    def terminar(self):
        self.jugando = False
        pass

    def generar_asteroides(self, cantidad):
        if len(self.asteroides) == 0:
            for i in range(cantidad):
                posicion = (random.randrange(20, WIDTH - 20),
                            random.randrange(-500, HEIGHT // 2))
                asteroide = Asteroide("./images/asteroide.png",
                                    SIZE_ASTERIOD, posicion, SPEED_ASTEROIDE)
                
                self.agregar_asteroide(asteroide)
                self.agregar_sprite.add(asteroide)
juego=Juego()
juego.start()



