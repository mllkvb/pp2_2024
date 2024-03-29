import pygame
import sys
import datetime

pygame.init()

W = 800
H= 600

screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Niggamaus Clock")

current_time = datetime.datetime.now().time()
minute = current_time.minute
second = current_time.second

image = pygame.image.load("mainclock.png").convert()

image = pygame.transform.scale(image, (W, H))

rarm = pygame.image.load('right_arm.png')
rarm = pygame.transform.scale(rarm, (700, 603))


right_arm_rect = rarm.get_rect()
right_arm_rect.bottom = 610
right_arm_rect.centerx = 400
right_rotation_speed = -0.1
angle_right = -(minute * 6) - 36



larm = pygame.image.load('left_arm.png')
larm = pygame.transform.scale(larm, (50,603))
                                  
left_arm_rect = larm.get_rect()
left_arm_rect.bottom = 610
left_arm_rect.centerx = 400
clock = pygame.time.Clock()
left_rotation_speed = -6
angle_left = -(second * 6) 






pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    screen.blit(image,(0, 0))
    
    
    rotated_left = pygame.transform.rotate(larm, angle_left)
    rotated_rect_left = rotated_left.get_rect(center=left_arm_rect.center)
    screen.blit(rotated_left, rotated_rect_left)
    angle_left += left_rotation_speed * clock.get_time() / 1000.0
    angle_left %= 360

    rotated_right = pygame.transform.rotate(rarm, angle_right)
    rotated_rect_right = rotated_right.get_rect(center=right_arm_rect.center)
    screen.blit(rotated_right, rotated_rect_right)
    angle_right += right_rotation_speed * clock.get_time() / 1000.0
    angle_right %= 360
    pygame.display.update()
    clock.tick(60)