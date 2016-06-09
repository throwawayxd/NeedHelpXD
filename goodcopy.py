import pygame
import time
from random import randint

pygame.init()

#Get the width and height of the screen
screenw=800
screenh=600
screen=pygame.display.set_mode((screenw,screenh))

#Colour codes for use later on
white=(255,255,255)
black=(0,0,0)
red=(255,0,0)

#Get the background
background=(white)

#Loads the person image, then scales it 
personw=50
personh=75
person=pygame.image.load("person.jpg")
person=pygame.transform.scale(person, (personw, personh))

#Loads the trump image, then scales it
trumpw=40
trumph=40
trump=pygame.image.load("trump.jpg")
trump=pygame.transform.scale(trump, (trumpw, trumph))

#Loads the wall image, then scales it
wallw=50
wallh=50
wall=pygame.image.load("wall.jpg")
wall=pygame.transform.scale(wall, (wallw, wallh))

#Loads the flag image, then scales it
flagw=60
flagh=60
flag=pygame.image.load("flag.png")
flag=pygame.transform.scale(flag, (flagw, flagh))

#Loads the great image, then scales it
sloganw=70
sloganh=70
slogan=pygame.image.load("makeamericagreatagain.jpg")
slogan=pygame.transform.scale(slogan, (sloganw, sloganh))

#Change the title
pygame.display.set_caption("Run From Trump")

#Define the person's starting position
def personpos(personx, persony):
    screen.blit(person, (personx, persony))

#Define trump's starting position
def trumppos(trumpx, trumpy):
    screen.blit(trump, (trumpx, trumpy))
    
#Define wall's starting position
def wallpos(wallx, wally):
    screen.blit(wall, (wallx, wally))

#Define flag's starting position
def flagpos(flagx, flagy):
    screen.blit(flag, (flagx, flagy))

#Define great's starting position
def sloganpos(sloganx, slogany):
    screen.blit(slogan, (sloganx, slogany))

#Set points to 0                          
points=0

#Position of the person
personx=(screenw * 0.5)
persony=520
personmovement=0

#Position of Trump
trumpx=randint(0,800)
trumpy=-100
trumpmovement=10

#Position of wall
wallx=randint(0,800)
wally=-100
wallmovement=15

#Position of flag
flagx=randint(0,800)
flagy=-100
flagmovement=20

#positionofslogan
sloganx=randint(0,800)
slogany=-100
sloganmovement=20

contact=False

while not contact:
        
        events=pygame.event.get()
        for event in events:
            
            #Quit Option
            if event.type == pygame.QUIT:
                contact = True

            #Move the person left or right
            if event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_LEFT:
                    personmovement = -10
                elif event.key == pygame.K_RIGHT:
                    personmovement = 10

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    personmovement=0
                        

        #Changes the positions 
        personx += personmovement
        trumpy += trumpmovement

        #Fill the background
        screen.fill(background)

        #Puts the person, trump, flag, wall, and slogan on the screen
        screen.blit(person, (personx, persony))
        trumppos(trumpx, trumpy)
        wallpos(wallx, wally)
        flagpos(flagx, flagy)
        sloganpos(sloganx, slogany)

        #Set the boundaries for the person, so the person can't go off the screen
        if personx > screenw - personw:
           personx = screenw - personw
           personpos(personx, persony)
        elif personx < 0:
           personx = 0
           personpos(personx, persony)

        #Make trump come back when it goes off screen
        if trumpy > screenh:
           trumpy=-100
           trumpx=randint(40,760)

        #Make the wall come back when it goes off screen
        if wally > screenh:
           wally=-100
           wallx=randint(50,750)

        #Make the flag come back when it goes off screen
        if flagy > screenh:
           flagy=-100
           flagx=randint(60,740)

        #Make the slogan come back when it goes off screen
        if slogany > screenh:
           slogaly=-100
           sloganx=randint(70,730)

        #Add 1 point for every trump avoided, if trump hits the person reset the points counter to 0, then game resets
        if trumpy == persony + 80:
            if trumpx > personx + 20 or trumpx < personx -20:
                points = points + 1
        else:
            points = 0
                    
            contact = False
                    
            personx=(screenw * 0.5)
            persony=520
            personmovement=0

            trumpx=randint(40,760)
            trumpy=-200
            trumpmovement=10

            wallx=randint(50,750)
            wally=-200
            wallmovement=15

            flagx=randint(60,740)
            flagy=-200
            flagmovement=20

            sloganx=randint(70,730)
            slogany=-200
            sloganmovement=20
                    
        #Add 1 point for every wall avoided, if trump hits the person reset the points counter to 0, then game resets
        if wally == persony + 80:
            if wallx > personx + 20 or wallx < personx -20:
                points = points + 1
            else:
                points = 0
                        
                contact = False
                        
                personx=(screenw * 0.5)
                persony=520
                personmovement=0

                trumpx=randint(40,760)
                trumpy=-200
                trumpmovement=10

                wallx=randint(50,750)
                wally=-200
                wallmovement=15

                flagx=randint(60,740)
                flagy=-200
                flagmovement=20

                sloganx=randint(70,730)
                slogany=-200
                sloganmovement=20

        #Add 1 point for every wall avoided, if trump hits the person reset the points counter to 0, then game resets       
        if flagy == persony + 80:
            if flagx > personx + 20 or flagx < personx -20:
                points = points + 1
            else:
                points = 0
                        
                contact = False
                        
                personx=(screenw * 0.5)
                persony=520
                personmovement=0

                trumpx=randint(40,760)
                trumpy=-200
                trumpmovement=10

                wallx=randint(50,750)
                wally=-200
                wallmovement=15

                flagx=randint(60,740)
                flagy=-200
                flagmovement=20

                sloganx=randint(70,730)
                slogany=-200
                sloganmovement=20
                  
        #Add 1 point for every wall avoided, if trump hits the person reset the points counter to 0, then game resets       
        if slogany == persony + 80:
            if sloganx > personx + 20 or sloganx < personx -20:
                points = points + 1
            else:
                points = 0
                        
                contact = False
                        
                personx=(screenw * 0.5)
                persony=520
                personmovement=0

                trumpx=randint(40,760)
                trumpy=-200
                trumpmovement=10

                wallx=randint(50,750)
                wally=-200
                wallmovement=15

                flagx=randint(60,740)
                flagy=-200
                flagmovement=20

                sloganx=randint(70,730)
                slogany=-200
                sloganmovement=20
                    
        #Display the points counter
        scoretext=pygame.font.SysFont(None, 40)
        score=scoretext.render("Points:" + str(points), True, red)
        screen.blit(score, (30,20))

        #When you have more the 5 points, trumpmovement increases to 10
        if points > 5:
            trumpmovement=12
                
        #When you have more than 15 points, the walls start to fall
        if points > 15:
            wally+=wallmovement
            wallpos(wallx, wally)
                
        #When you have more than 45 points, the flags start to fall
        if points > 45:
            flagy+=flagmovement
            flagpos(flagx,flagy)
                
        #When you have more than 75 points, the slogans start to fall
        if points > 75:
            slogany+=sloganmovement
            sloganpos(sloganx, slogany)
                
        #When you reach 150 points, displays a "Congratulations, You WON!!!"
        if points == 150:
            wintext = pygame.font.SysFont(None, 60)
            winlabel = wintext.render("Congratulations!!!", True, black)
            screen.blit(winlabel, (200, 200))
            time.sleep(5)
            contact = True
                
                
        pygame.display.update()
        pygame.time.delay(50)

pygame.quit()
quit()




        

        

        
        
        
    




        

        

        
        
        
    
