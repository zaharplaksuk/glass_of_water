import pygame

pygame.init()
width = (1600)
height = (900)
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("galaxy")

pygame.mixer.init()
pygame.mixer.music.load('c54cdd246e29178.mp3')
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play(-1)

button_sound = pygame.mixer.Sound('joystick-trigger-button-press_gyyt5ied.mp3')

class Button:
    def __init__(self, width, heitght, inactive_color, active_color):
        self.width = width
        self.heitght = heitght
        self.inactive_clr =  (23, 204, 58)
        self.active_clr = (13, 162, 58)

    def draw(self, x, y, massage, action=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if x < mouse[0] < x + self.width:
            if y < mouse[1] < y + self.heitght:
                pygame.draw.rect(display, self.active_clr, (x, y, self.width, self.heitght))

                if click[0] == 1:
                    pygame.mixer.Sound.play(button_sound)
                    pygame.time.delay(300)
                    if action is not None:
        else:
            pygame.draw.rect(display, self.inactive_clr,  (x, y, self.width, self.heitght))

        print_text(message, x + 10, x + 10, )

        button.draw(20, 100, 'wow')


pygame.display.update()

pygame.quit()
