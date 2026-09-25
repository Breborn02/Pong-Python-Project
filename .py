from turtle import width

import pygame 

pygame.init()

WIDTH, HEIGHT = 700, 800
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Pong")

FPS = 60

WHITE = ( 255, 255, 255)
BLACK = (0, 0, 0)

class Paddle:
    def _init_(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        def draw(self, win):
            pygame.draw.rect(win, self.COLOR, (self.x, self.y, self.width, self.height))


def draw(win):
    win.fill(BLACK)
    pygame.display.update()

    

def main():
    run  = True
    clock = pygame.time.Clock()

    left_paddle = Paddle()
    
    while run:
        clock.tick(FPS)
        draw(WIN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break


    pygame.quit()

if __name__ == "__main__" :
     main()