import pygame
import sys
import random
from zmija import Zmija
from hrana import Hrana

#inicijaliziranje pygamea, prozora, fontova
pygame.init()
pygame.display.set_caption("Zmija")
zaslon = pygame.display.set_mode((800, 400))
sat = pygame.time.Clock()
dno_pozadina = pygame.image.load("assets/slike/pozadina.png")
skalirana_slika = pygame.transform.scale(dno_pozadina, (800, 400))
font = pygame.font.SysFont(None, 60)
mali_font = pygame.font.SysFont(None, 30)


SEGMENT_SIRINA = 10
SEGMENT_VISINA = 10
brzina = 4.5
start_x = 300
start_y = 100


CRNA = (0, 0, 0)
SIVA = (50, 50, 50)
BIJELA = (255, 255, 255)
OVERLAY = (0, 0, 0, 180)


def nova_pozicija_hrane():
    x = random.randint(0, 800 - 20)
    y = random.randint(0, 400 - 20)
    return (x, y)


def reset_igre():
    global zmija, hrana, dx, dy, game_over
    pozicija_zmije = [(start_x - i * SEGMENT_SIRINA, start_y) for i in range(15)]
    zmija = Zmija(pozicija_zmije, SEGMENT_SIRINA, SEGMENT_VISINA)
    hrana = Hrana(nova_pozicija_hrane())
    dx, dy = brzina, 0
    game_over = False

reset_igre()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if not game_over and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and dy == 0:
                dx, dy = 0, -brzina
            elif event.key == pygame.K_s and dy == 0:
                dx, dy = 0, brzina
            elif event.key == pygame.K_d and dx == 0:
                dx, dy = brzina, 0
            elif event.key == pygame.K_a and dx == 0:
                dx, dy = -brzina, 0
        if game_over and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                reset_igre()

    if not game_over:
        zmija.pomakni(dx, dy)

        glava_rect = pygame.Rect(zmija.pozicija[0][0], zmija.pozicija[0][1], 10, 10)
        hrana_rect = pygame.Rect(hrana.pozicija[0], hrana.pozicija[1], 15, 15)

        if zmija.game_over(zmija, zmija.pozicija):
            game_over = True

        if glava_rect.colliderect(hrana_rect):
            zmija.rast_zmije(6)
            hrana.pozicija = nova_pozicija_hrane()

    
    zaslon.blit(skalirana_slika, (0, 0))
    hrana.crtaj_hranu(zaslon)
    zmija.crtaj_zmiju(zaslon)
    

    if game_over:
        
        overlay = pygame.Surface((800, 400), pygame.SRCALPHA)
        overlay.fill(OVERLAY)
        zaslon.blit(overlay, (0, 0))

        
        popup = pygame.Rect(200, 80, 400, 240)
        pygame.draw.rect(zaslon, SIVA, popup)
        pygame.draw.rect(zaslon, BIJELA, popup, 5)

        
        tekst = font.render("Game Over", True, BIJELA)
        podtekst = mali_font.render("Pritisni SPACE da pokušaš ponovno!", True, BIJELA)

        zaslon.blit(tekst, (popup.centerx - tekst.get_width() // 2, popup.top + 50))
        zaslon.blit(podtekst, (popup.centerx - podtekst.get_width() // 2, popup.top + 130))

    pygame.display.update()
    sat.tick(60)
