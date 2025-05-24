import pygame

class Hrana:
    def __init__(self, pozicija):
        self.slika = pygame.image.load("assets/slike/slika_hrane.png").convert_alpha()
        self.slika = pygame.transform.scale(self.slika, (12, 12))
        self.pozicija = pozicija

    def crtaj_hranu(self, ekran):
        rect = self.slika.get_rect()
        rect.center = self.pozicija
        ekran.blit(self.slika, rect)
