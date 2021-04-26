import pygame
pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode((800, 600))
ballvy,ballvyx = 5,5
j, t = 0,0
font = pygame.font.Font('freesansbold.ttf', 32)
pygame.display.set_caption("Pong")
pygame.display.set_icon(pygame.image.load("pong.png"))

mainPaddle = pygame.transform.scale(pygame.image.load("padpad.png"),(100,20))
mainPaddle_rect = mainPaddle.get_rect(topleft = [350,20])
AIPaddle = pygame.transform.scale(pygame.image.load("padpad.png"),(100,20))
AIPaddle_rect = AIPaddle.get_rect(topleft = [350,550])
pongBall = pygame.transform.scale(pygame.image.load("pong ball.png"),(20,25))
pongBall_rect = pongBall.get_rect(topleft = [400,300])

def player():
    screen.blit(mainPaddle, mainPaddle_rect)
    screen.blit(AIPaddle, AIPaddle_rect)
    screen.blit(pongBall,pongBall_rect)

def score():
    text1 = font.render(str(j), True, (0, 0, 0))
    text2 = font.render(str(t), True, (0, 0, 0))
    screen.blit(text1,(750,550))
    screen.blit(text2,(50,20))

def play():
    global ballvy, ballvyx, j, t
    pongBall_rect.y+=ballvy
    pongBall_rect.x+=ballvyx
    if pongBall_rect.y >= 580:
        t+=1
        pongBall_rect.x = 400
        pongBall_rect.y = 300
    if pongBall_rect.y <= 0:
        j+=1
        pongBall_rect.x = 400
        pongBall_rect.y = 300
    if pongBall_rect.x >= 780 or pongBall_rect.x <= 0:
        ballvyx*=-1
    if pongBall_rect.colliderect(AIPaddle_rect) and ballvy > 0:
        if pongBall_rect.bottom - AIPaddle_rect.top < 1 or pongBall_rect.top - AIPaddle_rect.bottom < 1:
            ballvy *= -1
        if pongBall_rect.right-AIPaddle_rect.left < 5 and pongBall_rect.left-AIPaddle_rect.right > 5 :
            ballvyx*=-1
        elif pongBall_rect.left-AIPaddle_rect.right < 5 and pongBall_rect.right-AIPaddle_rect.left < 5:
            ballvyx*=-1
    if pongBall_rect.colliderect(mainPaddle_rect) and ballvy < 0:
        if pongBall_rect.top - mainPaddle_rect.bottom < 1 or pongBall_rect.bottom - mainPaddle_rect.top < 1:
            ballvy *= -1
        if pongBall_rect.right-mainPaddle_rect.left < 5 and pongBall_rect.left-mainPaddle_rect.right < 5:
            ballvyx*=-1
        elif pongBall_rect.left-mainPaddle_rect.right < 5 and pongBall_rect.right-mainPaddle_rect.left < 5:
            ballvyx*=-1


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    velX = 6
    userInput = pygame.key.get_pressed()
    if userInput[pygame.K_LEFT] and mainPaddle_rect.x >= 0:
        mainPaddle_rect.x-=velX
    if userInput[pygame.K_RIGHT] and mainPaddle_rect.x <= 700:
        mainPaddle_rect.x+=velX
    if userInput[pygame.K_a] and AIPaddle_rect.x >= 0:
        AIPaddle_rect.x-=velX
    if userInput[pygame.K_d] and AIPaddle_rect.x <= 700:
        AIPaddle_rect.x+=velX

    screen.fill((255, 253, 208))
    player()
    score()
    play()
    pygame.display.update()
    clock.tick(60)

