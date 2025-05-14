import pygame
class Hrana:
    def __init__(self, izgled, velicina, pozicija):
        self.izgled = izgled
        self.velicina = velicina
        self.pozicija = pozicija
        self.slika = pygame.image.load("assets/slike/slika_hrane.png").convert_alpha()
        self.slika = pygame.transform.scale(self.slika, (20, 20))
        
    def crtaj_hranu(self, ekran):
        ekran.blit(self.slika, self.pozicija)
