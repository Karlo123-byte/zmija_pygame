import pygame

class Zmija:
    def __init__(self, pozicija, sirina, visina):
        self.pozicija = pozicija  
        self.segment_sirina = sirina
        self.segment_visina = visina

        self.glava = pygame.image.load("assets/slike/glava_zmije.png").convert_alpha()
        self.tijelo = pygame.image.load("assets/slike/slika_tijela.png").convert_alpha()
        self.rep = pygame.image.load("assets/slike/slika_repa.png").convert_alpha()

        self.glava = pygame.transform.scale(self.glava, (self.segment_sirina * 2, self.segment_visina * 2))
        self.tijelo = pygame.transform.scale(self.tijelo, (self.segment_sirina, self.segment_visina))
        self.rep = pygame.transform.scale(self.rep, (self.segment_sirina, self.segment_visina))

        self.smjerovi = [(1, 0)] * len(self.pozicija)

    def rotiraj_sliku(self, slika, smjer):
        if smjer == (0, -1):
            return pygame.transform.rotate(slika, 180)
        elif smjer == (1, 0):
            return pygame.transform.rotate(slika, 90)
        elif smjer == (0, 1):
            return pygame.transform.rotate(slika, 0)
        elif smjer == (-1, 0):
            return pygame.transform.rotate(slika, 270)
        return slika

    def crtaj_zmiju(self, ekran):
        glava_smjer = self.smjerovi[0]
        glava_slika = self.rotiraj_sliku(self.glava, glava_smjer)
        glava_rect = glava_slika.get_rect(center=(self.pozicija[0][0] + self.segment_sirina // 2,self.pozicija[0][1] + self.segment_visina // 2))
                                           
        ekran.blit(glava_slika, glava_rect)

        for i in range(1, len(self.pozicija) - 1):
            smjer = self.smjerovi[i]
            tijelo_slika = self.rotiraj_sliku(self.tijelo, smjer)
            ekran.blit(tijelo_slika, self.pozicija[i])

        rep_smjer = self.smjerovi[-1]
        rep_slika = self.rotiraj_sliku(self.rep, rep_smjer)
        ekran.blit(rep_slika, self.pozicija[-1])

    def pomakni(self, dx, dy):
        nova_glava = (self.pozicija[0][0] + dx, self.pozicija[0][1] + dy)
        self.pozicija = [nova_glava] + self.pozicija[:-1]

        if dx > 0:
            normirani_dx = 1
        elif dx < 0:
            normirani_dx = -1
        else:
            normirani_dx = 0

        if dy > 0:
            normirani_dy = 1
        elif dy < 0:
            normirani_dy = -1
        else:
            normirani_dy = 0

        novi_smjer = (normirani_dx, normirani_dy)
        stari_smjerovi = self.smjerovi[:-1]
        self.smjerovi = [novi_smjer] + stari_smjerovi


    def rast_zmije(self, broj):
        for i in range(broj):
            self.pozicija.append(self.pozicija[-1])
            self.smjerovi.append(self.smjerovi[-1])

    def pomakni_gore(self, brzina):
        self.pomakni(0, -brzina)

    def pomakni_dolje(self, brzina):
        self.pomakni(0, brzina)

    def pomakni_desno(self, brzina):
        self.pomakni(brzina, 0)

    def pomakni_lijevo(self, brzina):
        self.pomakni(-brzina, 0)
    
    
        
    def game_over(self, zmija, pozicija):
        glava = zmija.pozicija[0]

        
        if glava in zmija.pozicija[1:]:
            return True

        
        x, y = glava
        if x < 0 or x >= 800 or y < 0 or y >= 400:
            return True

        return False

        