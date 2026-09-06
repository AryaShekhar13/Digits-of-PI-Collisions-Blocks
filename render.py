import pygame as pg
from config import x1,x2,width1,width2,collisions
from main import vel1,vel2,update
pg.init()

screen = pg.display.set_mode((1000, 600))
pg.display.set_caption("Block Collision")

running = True
color2 = (130,245,229)
color1 = (242,250,250)
color3 = (189,182,174)

font = pg.font.Font(None, 40)

while running:
    screen_x1 = x1
    screen_x2 = x2
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    x1,x2,vel1,vel2,collisions=update(x1,x2,vel1,vel2,collisions)
    screen.fill((0,0,0))
    pg.draw.rect(screen, color1, (screen_x1-width1/2, 500, width1, width1))
    pg.draw.rect(screen, color2, (screen_x2-width2/2, 480, width2, width2))
    pg.draw.line(screen, color3, (-10,530), (1010,530), 3)
    text1 = font.render(f"Digits of PI: {collisions}", True, (255, 0, 0))
    text2 = font.render(f"Digits of PI {collisions}", True, (0, 255, 0))
    screen.blit(text1, (350, 100))
    if vel2 >= vel1 and vel1 >= 0:
        screen.blit(text2, (350, 100))


    pg.display.flip()

pg.quit()
    