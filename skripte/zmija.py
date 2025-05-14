import pygame

class Zmija:
    def __init__(self, duzina, pozicija): # Definira zmiju kao objekt
        self.pozicija = pozicija
        self.duzina = duzina
        self.glava = pygame.image.load("assets/slike/glava_zmije.png").convert_alpha()
        self.tijelo_ravno = pygame.image.load("assets/slike/slika_tijela.png").convert_alpha()
        self.tijelo_zakrivljeno = [
            pygame.image.load(f"assets/slike/tijelo_zakrivljeno_{i}.png").convert_alpha() for i in range(1, 5)
        ]
        self.rep = pygame.image.load("assets/slike/slika_repa.png").convert_alpha()

        # Skaliraj ako treba
        self.glava = pygame.transform.scale(self.glava, (100, 100))
        self.tijelo_ravno = pygame.transform.scale(self.tijelo_ravno, (100, 100))
        self.tijelo_zakrivljeno = [pygame.transform.scale(img, (100, 100)) for img in self.tijelo_zakrivljeno]
        self.rep = pygame.transform.scale(self.rep, (100, 100))

    def crtaj_zmiju(self, ekran):
        for i, segment in enumerate(self.pozicija):
            if i == 0:
                ekran.blit(self.glava, segment)
            elif i == len(self.pozicija) - 1:
                ekran.blit(self.rep, segment)
            else:
                ekran.blit(self.tijelo_ravno, segment) 
    
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

    def pomakni(self, dx, dy):
        glava_x, glava_y = self.pozicija[0]
        nova_pozicija = (glava_x + dx, glava_y + dy)
        self.pozicija = [nova_pozicija] + self.pozicija[:-1]

