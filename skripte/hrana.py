import pygame
class Hrana:
    def __init__(self, izgled, velicina, pozicija):
        self.izgled = izgled
        self.velicina = velicina
        self.pozicija = pozicija
        
    def crtaj_hranu(self, ekran):
        pygame.draw.rect(ekran, self.izgled, (self.pozicija[0], self.pozicija[1], self.velicina, self.velicina))
