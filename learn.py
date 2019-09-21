# Import a library of functions called 'pygame'
import pygame
import random
import os


def draw_text(surf, text, color, size, x, y, pos="midtop"):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    if pos == "midtop":
        text_rect.midtop = (x, y)
    elif pos == "topleft":
        text_rect.topleft = (x, y)
    surf.blit(text_surface, text_rect)


# Center Window on teh screen
os.environ['SDL_VIDEO_CENTERED'] = '1'

# Initialize the game engine
pygame.init()

BLACK = [0, 0, 0]
WHITE = [255, 255, 255]
GREEN = [0, 255, 0]
RED = [255, 0, 0]

# Set the height and width of the screen
SIZE = [1000, 600]

screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Apprends le clavier")

font_name = pygame.font.match_font('courier')

timelapse = 0
bonne_reponse = 0
mauvaise_reponse = 0
liste_lettre = [
    'A', 'B', 'C', 'D', 'E', 'F',
    'G', 'H', 'I', 'J', 'K', 'L',
    'M', 'N', 'O', 'P', 'Q', 'R',
    'S', 'T', 'U', 'V', 'W', 'X',
    'Y', 'Z'
]
scan2char = {
    16: "A", 48: "B", 46: "C", 32: "D", 18: "E",
    33: "F", 34: "G", 35: "H", 23: "I", 36: "J",
    37: "K", 38: "L", 39: "M", 49: "N", 24: "O",
    25: "P", 30: "Q", 19: "R", 31: "S", 20: "T",
    22: "U", 47: "V", 44: "W", 45: "X", 21: "Y",
    17: "Z"
}
trouve_courant = False
lettre_courante = ""

clock = pygame.time.Clock()

# Loop until the user clicks the close button.
done = False

while not done:

    timelapse += 1  # A ajuster si besoin

    for event in pygame.event.get():  # User did something

        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop

        if event.type == pygame.KEYUP:
            try:
                if event.key == pygame.K_ESCAPE:
                    done = True
                elif lettre_courante == scan2char[event.scancode]:
                    bonne_reponse += 1
                else:
                    mauvaise_reponse += 1
            except KeyError:
                mauvaise_reponse += 1

            trouve_courant = False

    # Set the screen background
    screen.fill(BLACK)

    # Affiche une lettre
    if not trouve_courant:
        lettre_courante = random.choice(liste_lettre)
        draw_text(screen, "*", BLACK, 200, SIZE[0] / 2, SIZE[1] / 2 - 100)
        trouve_courant = True

    if trouve_courant:
        draw_text(screen, lettre_courante, WHITE, 200, SIZE[0] / 2, SIZE[1] / 2 - 100)

    # Afficher score
    draw_text(screen, "Bonnes réponses: " + str(bonne_reponse), GREEN, 20, SIZE[0] / 2, 5)
    draw_text(screen, "Mauvaises réponses: " + str(mauvaise_reponse), RED, 20, SIZE[0] / 2, 25)

    # Affiche Timer
    draw_text(screen, "Timer: " + str(timelapse), WHITE, 20, 5, 5, "topleft")

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
