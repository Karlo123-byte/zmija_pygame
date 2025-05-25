#Moram dodati score kada god zmija pojede jabuku dobije score +5 
#Score pocinje sa 0
#Score se prkazuje u gornjem desnom kutu dok korisnik igra

import pygame

# Inicijalizacija fonta
pygame.font.init()
font = pygame.font.SysFont('Arial', 16)

def prikazi_score(screen, score):
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    # Prikaz u gornjem desnom kutu (prilagodite širinu ekrana po potrebi)
    screen_width = screen.get_width()
    screen.blit(score_text, (screen_width - score_text.get_width() - 10, 10))