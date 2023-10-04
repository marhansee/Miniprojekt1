#Miniprojekt 1
#Import af biblioteker, der bruges
import pygame
import math
import datetime
#Skærmopløsning defineres samt opstart af pygame. 
screen_size = (800,800)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Analogt ur")
pygame.init()
#while True loop, der gør, at programmet kører indtil den møder en False value. 
while True:
    #Definere baggrundsfarve, farven gold og navyblue, der bruges til at farve uret.
    #Hertil defineres radius og et dynamisk centerpunkt, der ændres, hvis screen_size ærndres.
    screen.fill((0,0,0))
    gold = (255,215,0)
    navyblue = (0,0,128)
    radius = 360
    center = (screen_size[0]//2, screen_size[1]//2)
    
    #Tegner en cirkel i gold samt fylder cirklen med farven navyblue.  
    pygame.draw.circle(screen, gold,center,radius+40,width=8)
    pygame.draw.circle(screen, navyblue,center,radius+35,width=0)
    #Tegner en cirkel i center af uret i farven gold. 
    pygame.draw.circle(screen,gold,center, 10)
    #Tegner timemarkeringer i yderkanten af året ved brug af for loop-
    base_point = (400,400)
    length = 40
    angle = 360/12
    radius_marks = 320
    for i in range(12):
        start_point_x = base_point[0] + radius_marks * math.cos(math.radians(angle*i)) 
        start_point_y = base_point[1] + radius_marks * math.sin(math.radians(angle*i))
        start_point = (start_point_x, start_point_y)

        end_x = start_point[0] + length * math.cos(math.radians(angle *i))
        end_y = start_point[1] + length * math.sin(math.radians(angle *i))
        end_point = (end_x, end_y)
        pygame.draw.line(screen, gold,start_point,end_point,3)

    #Tegner et ur mindre ur inde i uret (venste urskive).
    pygame.draw.circle(screen, gold, (base_point[0]-120,base_point[1]-80),75,1)
    pygame.draw.line(screen,gold,(base_point[0]-120,base_point[1]-80),(base_point[0]-120,base_point[1]-145))
    #Tegner små markeringer inde i det lille venstre ur. 
    base_point_small = (base_point[0]-120,base_point[1]-80)
    radius_small_marks = 60
    angle_small_marks = 360/36
    length_small_marks = 10
    for j in range (36):
        start_point_smallx = base_point_small[0] + radius_small_marks * math.cos(math.radians(angle_small_marks*j))
        start_point_smally = base_point_small[1] + radius_small_marks * math.sin(math.radians(angle_small_marks*j))
        start_pointsmall = (start_point_smallx,start_point_smally)

        end_smallx = start_pointsmall[0] + length_small_marks * math.cos(math.radians(angle_small_marks*j))
        end_smally = start_pointsmall[1] + length_small_marks * math.sin(math.radians(angle_small_marks*j))
        end_pointsmall = (end_smallx,end_smally)
        pygame.draw.line(screen, gold,start_pointsmall,end_pointsmall)
    #Tegner et ur mindre ur inde i uret (højre urskive)
    pygame.draw.circle(screen, gold, (base_point[0]+120,base_point[1]-80),75,1)
    pygame.draw.line(screen,gold,(base_point[0]+120,base_point[1]-80),(base_point[0]+120,base_point[1]-145))
    #Tegner små markeringer inde i det lille højre ur. 
    base_point_small = (520,320)
    radius_small_marks = 60
    angle_small_marks = 360/36
    length_small_marks = 10
    for j in range (36):
        start_point_smallx = base_point_small[0] + radius_small_marks * math.cos(math.radians(angle_small_marks*j))
        start_point_smally = base_point_small[1] + radius_small_marks * math.sin(math.radians(angle_small_marks*j))
        start_pointsmall = (start_point_smallx,start_point_smally)

        end_smallx = start_pointsmall[0] + length_small_marks * math.cos(math.radians(angle_small_marks*j))
        end_smally = start_pointsmall[1] + length_small_marks * math.sin(math.radians(angle_small_marks*j))
        end_pointsmall = (end_smallx,end_smally)
        pygame.draw.line(screen, gold,start_pointsmall,end_pointsmall)
    
    #Laver en lille firkant i bunden af uret
    rect = (360,600,80,100)
    pygame.draw.rect(screen,gold,rect,1)
    #Definere en font og dags dato.
    font = pygame.font.Font(None,70)
    today = datetime.datetime.now().strftime("%d")
    #Definere en surface, hvorpå dags dato bliver dannet på ved brug af render metoden
    text_surface = font.render(today, True, gold)
    text_rect = text_surface.get_rect()
    text_rect.topleft = (375,620)
    #Tegner dags dato som et tal 
    screen.blit(text_surface,text_rect)

    

    #Tegner timeviser
    angle_hour = datetime.datetime.now().hour * (360/12) - 90 
    hour_x = (radius*math.cos(math.radians(angle_hour)))
    hour_y = (radius*math.sin(math.radians(angle_hour)))
    end_hour = (center[0]+hour_x,center[1]+hour_y)
    pygame.draw.line(screen, gold,center,end_hour,5)
    
    #Tegner minutviser 
    angle_minute = datetime.datetime.now().minute *360/60 - 90 
    minute_x = (radius*math.cos(math.radians(angle_minute)))
    minute_y = (radius*math.sin(math.radians(angle_minute)))
    end_minute = (center[0]+minute_x,center[1]+minute_y)
    pygame.draw.line(screen, gold, center,end_minute,8)

    #Tegner sekundviser
    angle_second = datetime.datetime.now().second *360/60 - 90
    second_x = (radius*math.cos(math.radians(angle_second)))
    second_y = (radius*math.sin(math.radians(angle_second)))
    end_second = (center[0]+second_x,center[1]+second_y)
    pygame.draw.line(screen, gold, center, end_second,3)

    #Gør så brugeren kan se hvad pygame har lavet. 
    pygame.display.flip()

    #Afslutter programmer, hvis brugeren trykker på krydset i højre øvre hjørne. 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()