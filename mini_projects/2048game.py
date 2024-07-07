import pygame
import math
import  random

pygame.init()
fps = 60
width,height= 800,600
rows,cols=4,4
rect_height =height//rows
rect_width = width//cols
outline_color=(187,173,160)
outline_thickness=20
background_color=(205,192,180)
font_color=(119,110,101)

font=pygame.font.SysFont("camicsan",60,bold=True)
move_velocity=20

window=pygame.display.set_mode((width,height))
pygame.display.set_caption('2048')

def draw_grid(Window):
    pygame.draw.rect(Window,outline_color,(0,0,width,height),outline_thickness)
    
def draw(Window):
    window.fill(background_color)
    pygame.display.update()
    draw_grid(Window)    
    
def main(Window):
    clock=pygame.time.Clock()
    run= True
    
    while run:
        clock.tick(fps)
        
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
                break
        draw(window)
    pygame.quit()
if __name__ == "__main__":
    main(window)