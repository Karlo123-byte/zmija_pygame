import pygame
import sys
from zmija import Zmija
from hrana import Hrana
import random

pygame.init()

pygame.display.set_caption("Zmija")
dno_pozadina = pygame.image.load("assets/slike/pozadina.png")
sat = pygame.time.Clock()
zaslon = pygame.display.set_mode((800, 400))
pozicija_hrane_x = random.randint(0, 800)
pozicija_hrane_y = random.randint(0, 400)
skalirana_slika = pygame.transform.scale(dno_pozadina, (800, 400))
zmija = Zmija( 3, [(100, 100),(100,90),(100,80)])
hrana = Hrana((200,250,135), 10,(pozicija_hrane_x, pozicija_hrane_y))

brzina = 4
dx, dy = 0, -brzina
while True: #glavna petlja
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and dy == 0:
                dx, dy = 0, -brzina
            if event.key == pygame.K_s and dy == 0:
                dx, dy = 0, brzina
            if event.key == pygame.K_d and dx == 0:
                dx, dy = brzina, 0
            if event.key == pygame.K_a and dx == 0:
                dx, dy = -brzina, 0


    zaslon.blit(skalirana_slika,(0, 0))


    tipka = pygame.key.get_pressed()
    



    zmija.pomakni(dx, dy)
    hrana.crtaj_hranu(zaslon)


    zmija.crtaj_zmiju(zaslon)
    pygame.display.update()
    sat.tick(60)