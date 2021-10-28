import pygame
import sys
import time

pygame.init()

W = 600
H = 600
white = (255, 255, 255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
grey = (192, 192, 192)
orange = (255, 165, 0)
planepos = [300, 300]
Rpos = [500, 100]
screen = pygame.display.set_mode((W, H))
score = 0
moves = 0

myFont = pygame.font.SysFont("monospace", 45)

bg = pygame.image.load(r'C:\Users\Vaibhav\Desktop\space\space.png')

px = planepos [0]
py = planepos [1]
Rx = Rpos [0] 
Ry = Rpos [1]

bulletpos = [px,py]
bullet2pos = [(px+20),py]

gameover = False
gunon = False

screen.blit(bg, (0,0))

def detectcollision(planepos,Rpos):
    if (Rx >= px and Rx < (px + 30)) or (px >= Rx and px < (Rx + 20)):
        if (Ry >= py and Ry < (py + 30)) or (py >= Ry and py < (Ry + 20)):
            return True
    return False

def detecthit(Rp,bp):
    if (((bp[0] >= Rp[0] and bp[0] < (Rp[0] + 20)) or
         (Rx >= bp[0] and Rx < (bp[0] + 6)))and
        ((bp[1] >= Rp[1] and bp[1] < (Rp[1] + 20)) or
        (Ry >= bp[1] and Ry < (bp[1] + 15)))):
        return True
    return False

while not gameover:
    time.sleep(0.1)
    score += 1
    
    if True:
        if (Rpos[0] >= 600) or (Rpos[0] <= 0):
                    Rpos[0] = 0
        if (Rpos [1] >= 600) or (Rpos[1] <= 0):
                    Rpos[1] = 0
                    
        if abs(px-Rx) > abs(py - Ry):
            if px > Rx:
                Rx += 10
            else:
                Rx -= 10
        else:
            if py > Ry:
                Ry += 10
            else:
                Ry -= 10
        Rpos = [Rx,Ry]

    if score>=100:
        if (Rpos[0] >= 600) or (Rpos[0] <= 0):
                    Rpos[0] = 0
        if (Rpos [1] >= 600) or (Rpos[1] <= 0):
                    Rpos[1] = 0
                    
        if abs(px-Rx) > abs(py - Ry):
            if px > Rx:
                Rx += 15
            else:
                Rx -= 15
        else:
            if py > Ry:
                Ry += 15
            else:
                Ry -= 15
        Rpos = [Rx,Ry]

    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            sys.exit()
            
        if event.type == pygame.KEYDOWN:
            moves +=1

            if (planepos[0] >= 600) or (planepos[0] <= 0):
                    planepos[0] = 0
            if (planepos [1] >= 600) or (planepos[1] <= 0):
                    planepos[1] = 0

            if event.key == pygame.K_LEFT:
                px -= 25
            elif event.key == pygame.K_RIGHT:
                px += 25
            elif event.key == pygame.K_DOWN:
                py += 15
            elif event.key == pygame.K_UP:
                py -= 15
            planepos = [px,py]
            bulletpos = [planepos[0],planepos[1]]
            bullet2pos = [planepos[0]+20,planepos[1]]
            
            if event.key == pygame.K_TAB:
                gunon = not gunon
            bulletpos = [bulletpos[0],bulletpos[1]]
            bullet2pos = [bullet2pos[0],bullet2pos[1]]
            
            pygame.display.update()
        
                
    if True:
        screen.fill((0,0,0))
        screen.blit(bg, (0,0))
        pygame.draw.rect(screen, red, (Rpos[0], Rpos[1], 20, 20))
        pygame.draw.rect(screen, blue, (planepos[0], planepos[1], 30, 30))
        
        if (gunon):
            pygame.draw.rect(screen, orange, (bulletpos[0], bulletpos[1], 6, 15))               
            bulletpos[1] -= 60
            bulletpos[0] += 0
            pygame.draw.rect(screen, orange, (bullet2pos[0], bullet2pos[1], 6, 15))               
            bullet2pos[1] -= 60
            bullet2pos[0] += 0

        print (int(score))
        text  = "Score:" + str(int(score))
        label = myFont.render(text, 1, green)
        screen.blit(label, (W-300, H-40))
        print (moves)
        text  = "Moves:" + str(moves)
        label = myFont.render(text, 1, green)
        screen.blit(label, (W-600, H-40))
        text  = "Press tab to shoot"
        label = myFont.render(text, 20, green)
        screen.blit(label, (W-500, H-550))
        
        pygame.display.update()
        
    if detectcollision(planepos, Rpos):
        text  = "You lose :("
        label = myFont.render(text, 20, orange)
        screen.blit(label, (W-400, H-300))
        pygame.display.update()
        gameover = True
        break
        
    if detecthit(Rpos, bulletpos):
        text  = "You win!"
        label = myFont.render(text, 6, orange)
        screen.blit(label, (W-450, H-300))
        pygame.display.update()
        gameover = True
        break
        
    if detecthit(Rpos, bullet2pos):
        text  = "You win!"
        label = myFont.render(text, 6, orange)
        screen.blit(label, (W-450, H-300))
        pygame.display.update()
        gameover = True
        break
        
    
    
        
        

    
    

    

