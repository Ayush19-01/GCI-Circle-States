#Made for the sole purpose of GCI 2019
import pygame
white = (255,255,255)
black = (0,0,0)
a=int(input("Enter the radius of the first circle:"))
b=int(input("Enter the  radius of the second cirlce:"))
c=int(input("Distance between the centres of the circle:"))
pygame.init() 
gameDisplay = pygame.display.set_mode((400,300))
gameDisplay.fill(white)
font = pygame.font.Font("LuckiestGuy.ttf", 17)  
if c==0:
    print("The circles are cocentric.")
    pygame.draw.circle(gameDisplay,black, (200,150), a,1)
    pygame.draw.circle(gameDisplay,black, (200,150), b,1)
    pygame.draw.line(gameDisplay, black, (200,150), (200+a,150),2)
    pygame.draw.line(gameDisplay, black, (200,150), (200+b,150),2)
    text=font.render("The circles are cocentric.",True,black)
    textRect=text.get_rect()
    textRect.center=(200,30) 
    gameDisplay.blit(text, textRect) 
elif a+b==c or a+c==b or b+c==a:
    print("The circles are tangent.")
    pygame.draw.circle(gameDisplay,black, (200-c//2,150), a,1)
    pygame.draw.circle(gameDisplay,black, (200+c//2,150), b,1)
    pygame.draw.line(gameDisplay,black, (200-c//2,150), ((200-c//2)+a,150),2)
    pygame.draw.line(gameDisplay,black, (200+c//2,150), ((200+c//2)+b,150),2)
    text = font.render("The circles are tangent.", True,black)
    textRect = text.get_rect()
    textRect.center = (200,30) 
    gameDisplay.blit(text, textRect)
elif a+b<c  or a+c<b or b+c<a:
    print("The circles are not intersecting.")
    pygame.draw.circle(gameDisplay,black, (200-(c//2),150), a,1)
    pygame.draw.circle(gameDisplay,black, (200+(c//2),150), b,1)
    pygame.draw.line(gameDisplay,black, (200-c//2,150), ((200-c//2)+a,150),2)
    pygame.draw.line(gameDisplay,black, (200+c//2,150), ((200+c//2)+b,150),2)
    text = font.render("The circles are not intersecting.", True,black)
    textRect = text.get_rect()
    textRect.center = (200,30) 
    gameDisplay.blit(text, textRect)
elif a+b>c:
    print("The circles are intersecting at two points.")
    pygame.draw.circle(gameDisplay,black, (200-c//2,150), a,1)
    pygame.draw.circle(gameDisplay,black, (200+c//2,150), b,1)
    pygame.draw.line(gameDisplay,black, (200-c//2,150), ((200-c//2)+a,150),2)
    pygame.draw.line(gameDisplay,black, (200+c//2,150), ((200+c//2)+b,150),2)
    text = font.render("The circles are intersecting at two points.", True,black)
    textRect = text.get_rect()
    textRect.center = (200,30) 
    gameDisplay.blit(text, textRect)
    
while True:
    pygame.display.update () 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
            break
