# этот код устроен так чтобы мяч двигался по одному нажатию клавиш:
import pygame

pygame.init()

w=800
h=600

sc=pygame.display.set_mode((w, h))
pygame.display.set_caption("Redball")

white=(255, 255, 255)
Blue=(0, 0, 255)
Green=(0, 255, 0)
Red=(255, 0, 0)

FPS=60

clock=pygame.time.Clock()

radius=25

posx=w//2
posy=h//2

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
        keys=pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            posx+=20
        elif keys[pygame.K_LEFT]:
            posx-=20
        if keys[pygame.K_UP]:
            posy-=20
        elif keys[pygame.K_DOWN]:
            posy+=20

        if posx - radius < 0:  
            posx = radius
        elif posx + radius > 800:  
            posx = 800 - radius
        if posy - radius < 0:  
            posy = radius
        elif posy + radius > 600:  
            posy = 600 - radius
        
        sc.fill(white)

        pygame.draw.circle(sc, Red, (posx, posy), radius)

        pygame.display.update()

        clock.tick(FPS)