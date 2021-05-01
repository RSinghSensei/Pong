import pygame

pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode((900, 600))
screen.fill((255, 253, 208))
ballvy,ballvyx = 6.5,2.5
j, t = 0,0
init1,init2 = 0,0
font = pygame.font.Font('Pixeboy-z8XGD.ttf', 64)
pygame.display.set_caption("Pong")
pygame.display.set_icon(pygame.image.load("pong.png"))

font1 = pygame.font.Font("Pixeboy-z8XGD.ttf", 64)
fontB = pygame.font.Font("Pixeboy-z8XGD.ttf",80)


h_1 = pygame.Rect(350, 0, 120, 40)
h_2 = pygame.Rect(350, 550, 120, 40)
h_3 = pygame.Rect(400, 300,20,20)

def line():
    pygame.draw.line(screen, (72,60,50),(0,300),(900,300),5)
    pygame.draw.circle(screen,(72,60,50),(445,300),30,5)


def comingsoon():
    global isitTrue
    text3 = font1.render("COMING SOON", True, (0, 0, 0))
    isitTrue = True
    if isitTrue:
        screen.blit(text3,(295,300))


def menu():
    global running, mainmenu, click, isitTrue, running2

    if isitTrue:
        pygame.time.wait(2000)
        screen.fill((255,253,208))
        isitTrue = False

    pos = pygame.mouse.get_pos()
    mainText = fontB.render("PONG",True,(0,0,0))
    text1 = font1.render("Single Player",True,(0,0,0))
    text2 = font1.render("Double Player",True,(0,0,0))
    sp = pygame.draw.rect(screen,(0,0,0),(260,195,385,50),4)
    dp = pygame.draw.rect(screen,(0,0,0),(260,395,385,50),4)
    screen.blit(mainText,(375,50))
    screen.blit(text1,(268,200))
    screen.blit(text2,(268,400))
    if click:
        if sp.collidepoint(pos):
            mainmenu = False
            running2 = True
        if dp.collidepoint(pos):
            mainmenu = False
            running = True


def score():
    text1 = font.render(str(j), True, (0, 0, 0))
    text2 = font.render(str(t), True, (0, 0, 0))
    screen.blit(text1,(750,550))
    screen.blit(text2,(50,20))

def play():
    global ballvy, ballvyx, j, t, h_1 , h_2, h_3,init1,init2
    h_3.y+=ballvy
    h_3.x+=ballvyx

    if h_3.y >= 600:
        t+=1
        h_3.x = 400
        h_3.y = 300

    if h_3.y <= 0:
        j+=1
        h_3.x = 400
        h_3.y = 300


    if h_3.x >= 880 or h_3.x <= 0:
        ballvyx*=-1

    if h_3.colliderect(h_2):
        if abs(h_2.top - h_3.bottom) < 10 and ballvy > 0:
            h_3.bottom = h_2.top
            ballvy*=-1
        elif abs(h_2.right - h_3.left) < 10 and ballvy > 0:
            # h_3.left = h_2.right + 14
            ballvy *=-1
            ballvyx*=-1
        elif abs(h_2.left - h_3.right) < 10 and ballvy > 0:
            # h_3.right = h_2.left - 14
            ballvy *= -1
            ballvyx*=-1
    if h_3.colliderect(h_1):
        if abs(h_1.bottom - h_3.top) < 10 and ballvy < 0:
            h_3.top = h_1.bottom
            ballvy*=-1
        elif abs(h_1.right - h_3.left) < 10 and ballvy < 0:
            ballvy*=-1
            ballvyx*=-1
        elif abs(h_1.left - h_3.right) < 10 and ballvy < 0:
            ballvy*=-1
            ballvyx*=-1

def ai():
    global h_1,h_3
    if h_1.x <= 780:
        h_1.x+=AIVelX
    if h_1.x >= 0:
        h_1.x-=AIVelX
   


running = False
running2 = False
mainmenu = True
isitTrue = False


while mainmenu:
    click = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mainmenu = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            click = True
    menu()
    pygame.display.update()
    clock.tick(60)

while running2:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running2 = False
    velX = 8
    AIVelX = 7
    userInput = pygame.key.get_pressed()
    if userInput[pygame.K_a] and h_2.x >= 0:
        h_2.x -= velX
    if userInput[pygame.K_d] and h_2.x <= 780:
        h_2.x += velX
    if h_3.centerx > h_1.centerx and h_3.y < 250 and abs(h_3.centerx - h_1.centerx) > 40 :
        h_1.x+=AIVelX
    if h_3.centerx < h_1.centerx and h_3.y < 250 and abs(h_3.centerx - h_1.centerx) > 40:
        h_1.x-=AIVelX
    screen.fill((255, 253, 208))
    pygame.draw.rect(screen, (0, 0, 0), h_1, 4)
    pygame.draw.rect(screen, (0, 0, 0), h_2, 4)
    pygame.draw.rect(screen, (0, 0, 0), h_3, 4)
    line()
    score()
    ai()
    play()
    pygame.display.update()
    clock.tick(60)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    velX = 7
    userInput = pygame.key.get_pressed()
    if userInput[pygame.K_LEFT] and h_1.x >= 0:
        h_1.x-=velX
    if userInput[pygame.K_RIGHT] and h_1.x <= 780:
        h_1.x+=velX
    if userInput[pygame.K_a] and h_2.x >= 0:
        h_2.x-=velX
    if userInput[pygame.K_d] and h_2.x <= 780:
        h_2.x+=velX
   

    screen.fill((255, 253, 208))
    pygame.draw.rect(screen, (0, 0, 0), h_1, 4)
    pygame.draw.rect(screen, (0, 0, 0), h_2, 4)
    pygame.draw.rect(screen, (0, 0, 0), h_3, 4)
    line()
    score()
    play()
    pygame.display.update()
    clock.tick(60)
