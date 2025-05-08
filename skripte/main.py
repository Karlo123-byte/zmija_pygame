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
zmija = Zmija((255, 0, 0), 3, [(100, 100),(100,90),(100,80)])
hrana = Hrana((200,250,135), 10,(pozicija_hrane_x, pozicija_hrane_y))

brzina = 4

while True: #glavna petlja
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    zaslon.blit(skalirana_slika,(0, 0))


    tipka = pygame.key.get_pressed()


    if tipka[pygame.K_w]: #ide ka gore
        zmija.pomakni_gore(brzina)
    if tipka[pygame.K_s]:
        zmija.pomakni_dolje(brzina)
    if tipka[pygame.K_d]:
        zmija.pomakni_desno(brzina)
    if tipka[pygame.K_a]:
        zmija.pomakni_lijevo(brzina)

    hrana.crtaj_hranu(zaslon)


    zmija.crtaj_zmiju(zaslon)
    pygame.display.update()
    sat.tick(60)