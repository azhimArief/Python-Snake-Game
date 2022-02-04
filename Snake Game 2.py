import pygame
import time
import random

pygame.init()#initialization

#colour inititialization
white = (255,255,255)
yellow = (255,255,102)
pink = (255,55,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

dis_width = 1080
dis_height = 700

dis = pygame.display.set_mode((dis_width,dis_height)) #Takes a tuple or a list as its parameter to create a surface
pygame.display.set_caption("Snake Game by Azhim Arief") #To set Title name

clock = pygame.time.Clock()

snake_block = 10
snake_speed = 15

font_style = pygame.font.SysFont("bahnschrift", 27)#font for you lose
score_font = pygame.font.SysFont("comicsansms", 25)#font for your score

def Your_score(score):
    value = score_font.render("Your Score :" + str(score), True, yellow)
    dis.blit(value, [0,0])

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis,black,[x[0], x[1], snake_block,snake_block])

def message(msg,color):
    message = font_style.render(msg,True,color)
    dis.blit(message, [dis_width/3, dis_height/2]) #to display surfave on screen

def gameLoop():
    game_over = False
    game_close = False

    x1 = dis_width/2
    y1 = dis_height/2

    x1_change = 0
    y1_change = 0

    snake_List =[]
    Length_of_snake = 1

    #food random position
    foodx = round(random.randrange(0,dis_width - snake_block)/10.0) * 10.0
    foody = round(random.randrange(0,dis_width - snake_block)/10.0) * 10.0

    while not game_over:
        while game_close == True:#if lose
            dis.fill(blue)
            message("You Lost!Press Q-quit or C-Play Again", red) #call function message
            Your_score(Length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()       

        for event in pygame.event.get(): #event.get() Returns list of all events
            #print(event) #prints all the action that take place on the screen
            if event.type == pygame.QUIT:
                game_over=True #to allow the user to exit the game
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change= -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    x1_change = 0
                    y1_change = -snake_block
                elif event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change = snake_block
    
        if x1 >= dis_width or x1 <0 or y1 >= dis_height or y1 <0: #if out of border
            game_close = True

        x1 += x1_change
        y1 += y1_change
        dis.fill(pink) #change the colour background
        pygame.draw.rect(dis,green,[foodx,foody,snake_block,snake_block])
        snake_Head = [] #initialize list name snake
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block,snake_List)
        Your_score(Length_of_snake - 1)
        
        pygame.display.update() #Updates the screen

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0,dis_width - snake_block)/10.0) * 10.0
            foody = round(random.randrange(0,dis_width - snake_block)/10.0) * 10.0
            Length_of_snake +=1
        clock.tick(snake_speed)

    pygame.quit()
    quit()#Used to uninitialize everything

gameLoop()