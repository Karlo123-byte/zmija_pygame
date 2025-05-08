import pygame

class Zmija:
    def __init__(self, boja, duzina, pozicija): # Definira zmiju kao objekt
        self.boja = boja
        self.duzina = duzina
        self.pozicija = pozicija

    def crtaj_zmiju(self, ekran): # Prolazi kroz elemente zmije u svakom trenutku
        for element in self.pozicija:
            pygame.draw.rect(ekran, (255, 0, 0), (*element, 10, 10))
    
    def rast_zmije(self):
        zadnji_element = self.pozicija[-1]
        self.pozicija.append(zadnji_element)
        self.duzina += 1
    
    def pomakni_gore(self, brzina):
        # Kretanje prema gore
        head_x, head_y = self.pozicija[0]
        self.pozicija.insert(0, (head_x, head_y - brzina))  
        self.pozicija.pop() 
    
    def pomakni_dolje(self, brzina):
        # Kretanje prema dolje
        head_x, head_y = self.pozicija[0]
        self.pozicija.insert(0, (head_x, head_y + brzina))  
        self.pozicija.pop()  

    def pomakni_desno(self, brzina):
        # Kretanje prema desno
        head_x, head_y = self.pozicija[0]
        self.pozicija.insert(0, (head_x + brzina, head_y))  
        self.pozicija.pop()  
    
    def pomakni_lijevo(self, brzina):
        # Kretanje prema lijevo
        head_x, head_y = self.pozicija[0]
        self.pozicija.insert(0, (head_x - brzina, head_y))  
        self.pozicija.pop()  

