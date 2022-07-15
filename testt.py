from pickle import TRUE
import pygame as pg
import sys
import numpy as np
from pygame.locals import *
from math import inf as infinity
import itertools
import time



    
# Initializing Pygame

pg.init()
stop=1
scoreO=0
scoreX=0
p=1


# Pygame Screen

WIDTH=800

HEIGHT=500
width=350
height=250
widthx=int(width/3)
heighty=int(height/3)

# Colors

WHITE = (255, 255, 255)

BLACK = (0, 0, 0)

GRAY = (200, 200, 200)

BLUE = (0, 0, 255)
ORANGE=(255,145,0)

#Tic Tac Toe Board


BOARD = [[' ',' ',' '],
              [' ',' ',' '],
              [' ',' ',' ']]



#Other Global Variables

medium = pg.font.Font("opensans.ttf", 28)
Large = pg.font.Font("opensans.ttf", 40)
small = pg.font.Font("opensans.ttf", 22)

DRAW=False

WINNER=None

XO=None
k=1

main_screen=pg.display.set_mode((WIDTH,HEIGHT))

pg.display.set_caption("Tic Tac Toe Game")

main_screen.fill(BLACK)



def main():
   
    
    global XO
        
    #Main Window and Grids

    def starting_game():
        global stop

        font=pg.font.Font(None,80)

        main_screen.fill(GRAY)

        text=font.render("Let's Play", True,BLUE,(GRAY))

        textRect = text.get_rect()

        textRect.center = (WIDTH // 2, HEIGHT // 2)

        main_screen.blit(text, textRect)

        pg.display.update()
        

        pg.time.wait(1200)

        main_screen.fill(WHITE)
        
        
        while(stop):
            global XO

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    sys.exit()

            main_screen.fill(BLACK)

    # Let user choose a player.
            

            # Draw title
            title = Large.render("Play Tic-Tac-Toe", True, WHITE)
            titleRect = title.get_rect()
            titleRect.center = ((WIDTH / 2), 50)
            main_screen.blit(title, titleRect)

            #write choices message

            title = small.render("Choose which player goes first -X (You - the petty human)", True, ORANGE)
            titleRect = title.get_rect()
            titleRect.center = ((WIDTH / 2), 120)
            main_screen.blit(title, titleRect)
            title1 = small.render("Or O(The mighty AI):", True, ORANGE)
            titleRect1 = title1.get_rect()
            titleRect1.center = ((WIDTH / 2), 160)
            main_screen.blit(title1, titleRect1)


            # Draw buttons
            playXButton = pg.Rect((WIDTH / 8), (HEIGHT / 2), WIDTH / 4, 50)
            playX = medium.render("X first", True, BLACK)
            playXRect = playX.get_rect()
            playXRect.center = playXButton.center
            pg.draw.rect(main_screen, WHITE, playXButton)
            main_screen.blit(playX, playXRect)

            playOButton = pg.Rect(5 * (WIDTH / 8), (HEIGHT / 2), WIDTH / 4, 50)
            playO = medium.render("O first", True, BLACK)
            playORect = playO.get_rect()
            playORect.center = playOButton.center
            pg.draw.rect(main_screen, WHITE, playOButton)
            main_screen.blit(playO, playORect)

            

            click, _, _ = pg.mouse.get_pressed()
            if click == 1:
                stop=0
                mouse = pg.mouse.get_pos()
                if playXButton.collidepoint(mouse):
                    
                    time.sleep(0.3)
                    XO="x"
                    main_screen.fill(BLACK)
                    #Show Player Message turns
                    message= "X's Turn"
                    text1 = Large.render(message, True, WHITE)

                    textRect1 = text1.get_rect()

                    textRect1.center = (WIDTH/2,80)

                    main_screen.blit(text1, textRect1)

                    pg.display.update()  
                    
                     
        
                   

                elif playOButton.collidepoint(mouse):
                    time.sleep(0.3)
                    XO="o"
                    main_screen.fill(BLACK)
                    pg.draw.line(main_screen,WHITE,(225,125),(225,375),5)

                    pg.draw.line(main_screen,WHITE,(575,125),(575,375),5)


                    pg.draw.line(main_screen,WHITE,(341,125),(341,375),5)

                    pg.draw.line(main_screen,WHITE,(457,125),(457,375),5)

                    # Two Horizontal lines

                    pg.draw.line(main_screen,WHITE,(225,125),(575,125),5)
                    

                    pg.draw.line(main_screen,WHITE,(225,208),(575, 208),5)

                    pg.draw.line(main_screen,WHITE,(225,291),(575,291),5)

                    pg.draw.line(main_screen,WHITE,(225,375),(575,375),5)
        
                    
                    draw_figure(0,0)
                
            
                    
            pg.display.flip()
        # score section

        title = Large.render("Score", True, ORANGE)
        titleRect = title.get_rect()
        titleRect.center = (80, 30)
        main_screen.blit(title, titleRect)

        #score for AI
        title = small.render(f"Agent: {scoreO}", True, ORANGE)
        titleRect = title.get_rect()
        titleRect = (40, 60)
        main_screen.blit(title, titleRect)

        #score for Human
        title = small.render(f"Human: {scoreX}", True, ORANGE)
        titleRect = title.get_rect()
        titleRect = (40, 100)
        main_screen.blit(title, titleRect)
             


        # Two Vertical lines


        pg.draw.line(main_screen,WHITE,(225,125),(225,375),5)

        pg.draw.line(main_screen,WHITE,(575,125),(575,375),5)


        pg.draw.line(main_screen,WHITE,(341,125),(341,375),5)

        pg.draw.line(main_screen,WHITE,(457,125),(457,375),5)

        # Two Horizontal lines

        pg.draw.line(main_screen,WHITE,(225,125),(575,125),5)
        

        pg.draw.line(main_screen,WHITE,(225,208),(575, 208),5)

        pg.draw.line(main_screen,WHITE,(225,291),(575,291),5)

        pg.draw.line(main_screen,WHITE,(225,375),(575,375),5)
        


        



    #Getting Mouse x and y coordinates

    def mouse_pointing():

        global row,col
        
    

        x,y = pg.mouse.get_pos()
        

        #  getting width of the box

        if(x<(225+widthx)) and (y<(125+heighty)):

            row=0

            col=0

        elif(x>(225+widthx) and x<(225+widthx*2)) and (y<(125+heighty)):

            row=0

            col=1

        elif(x>(225+widthx*2)) and (y<(125+heighty)):

            row=0

            col=2

        elif(x<(225+widthx)) and (y>(125+heighty) and y<(125+heighty*2)):

            row=1

            col=0

        elif(x>(225+widthx) and x<(225+widthx*2)) and (y>(125+heighty) and y<(125+heighty*2)):

            row=1

            col=1

        elif(x>(225+widthx*2)) and (y>(125+heighty) and y<(125+heighty*2)):

            row=1

            col=2

        elif(x<(225+widthx)) and (y>(125+heighty*2)):

            row=2

            col=0

        elif(x>(225+widthx) and x<(225+widthx*2)) and (y>(125+heighty*2)):

            row=2

            col=1

        elif(x>(225+widthx*2)) and (y>(125+heighty*2)):

            row=2

            col=2

        else:

            row=None

            col=None
        draw_figure(row,col)

    #Drawing X and O on window

    def draw_figure(row,col):
        global XO
        global k
        global p
        if(XO=="o"):
            
            p = ObtainBestMove(BOARD, XO)
            row=int((p-1)/3)
            col=int((p-1)%3)

           

        
        
        
        if(BOARD[row][col] == ' '):
        

            global DRAW
            

            if row==0 and col==0:

                posx = 225+58
                posy = 125+42

            if row==1 and col==1:

                posx = 225+widthx + 58
                posy = 125+heighty+42

            if row==2 and col==2:

                posx = 225+widthx*2 + 58
                posy = 125+heighty*2+42

            if row==0 and col==1:

                posx=225+widthx+58
                posy = 125+42

            if row==0 and col==2:
                posx=225+widthx*2+58
                posy = 125+42

            if row==1 and col==0:


                posx = 225+58
                posy = 125+heighty+42
            if row==1 and col==2:


                posx = 225+widthx*2+58
                posy = 125+heighty+42    
            if row==2 and col==0:


                posx = 225+58
                posy = 125+heighty*2+42 

            if row==2 and col==1:


                posx = 225+widthx+58
                posy = 125+heighty*2+42     

            #Drawing X and O on mainscreen

            if(XO=='o'):
                message="Agent thinking..."
                text = Large.render(message, True, WHITE)

                textRect = text.get_rect()

                textRect.center = (WIDTH/2,80)

                main_screen.blit(text, textRect)
                

                pg.display.update()
                pg.time.wait(400)
                
                text = Large.render(message, True, BLACK)

                textRect = text.get_rect()

                textRect.center = (WIDTH/2,80)

                main_screen.blit(text, textRect)
                pg.draw.circle(main_screen, WHITE, (posx,posy), 25,6)

                BOARD[row][col] = "o"
                


                XO='x'
                k=k+1

            else:

                message= "X's Turn"
                text1 = Large.render(message, True, WHITE)

                textRect1 = text1.get_rect()

                textRect1.center = (WIDTH/2,80)

                main_screen.blit(text1, textRect1)

                pg.display.update()    

                


                pg.draw.line (main_screen,WHITE, (posx - 20, posy - 20),

                            (posx + 20, posy + 20), 8)

                pg.draw.line (main_screen,WHITE, (posx + 20, posy - 20),

                            (posx - 20, posy + 20), 8)

                BOARD[row][col] = "x"
                

                XO='o'
                message= "X's Turn"
                text = Large.render(message, True, BLACK)

                textRect = text.get_rect()

                textRect.center = (WIDTH/2,80)

                main_screen.blit(text, textRect)

                pg.display.update()    


                k=k+1

            pg.display.update()
            check_winner(k)
            if(XO=="o"):
                p = ObtainBestMove(BOARD, XO)
                row=int((p-1)/3)
                col=int((p-1)%3)
               
            
                draw_figure(row,col)

            #Show Player Message turns
            message= "X's Turn"
            text1 = Large.render(message, True, WHITE)

            textRect1 = text1.get_rect()

            textRect1.center = (WIDTH/2,80)

            main_screen.blit(text1, textRect1)

            pg.display.update()
              

            

        else:

            pass


        
    # checking winner 

    def check_winner(k):
        global WINNER
        for row in range(3):
            if ((BOARD [row][0] == BOARD[row][1] == BOARD[row][2]) and(BOARD [row][0] != ' ')):

                # this row won

                WINNER = BOARD[row][0]

                pg.draw.line(main_screen, ORANGE, (230, 125+(row + 1)*heighty -42),(570,125+(row+1)*heighty-42), 8)

                show_winning_message(WINNER)

                break
        # check for winning columns

        for col in range (0, 3):

            if (BOARD[0][col] == BOARD[1][col] == BOARD[2][col]) and (BOARD[0][col] != ' '):

                # this column won

                WINNER = BOARD[0][col]

                #draw winning line

                pg.draw.line (main_screen, ORANGE,(225+(col + 1)* widthx - 58, 130),

                            (225+(col + 1)*widthx  -58, 370), 8)

                show_winning_message(WINNER)

                break    
        # check for diagonal WINNERs

        if (BOARD[0][0] == BOARD[1][1] == BOARD[2][2]) and (BOARD[0][0] != ' '):

            # game won diagonally left to right

            WINNER = BOARD[0][0]

            pg.draw.line (main_screen, ORANGE, (225+20, 125+10), (575-20, 375-10), 8)

            show_winning_message(WINNER)

        



        if (BOARD[0][2] == BOARD[1][1] == BOARD[2][0]) and (BOARD[0][2] != ' '):

            # game won diagonally right to left

            WINNER = BOARD[0][2]

            pg.draw.line (main_screen, ORANGE, (575-20, 125+10), (225+20, 375-10), 8)

            show_winning_message(WINNER)
        if(k==10):
            WINNER="Game Over: Match Draw"
            show_winning_message(WINNER)



    #showing winning message function

    def show_winning_message(winner):


        global scoreO,scoreX

        if winner == "o":

            winner = "Game Over: O wins "
            
            #score for AI updation
            
            title = small.render(f"AI: {scoreO}", True, BLACK)
            titleRect = title.get_rect()
            titleRect = (40, 60)
            main_screen.blit(title, titleRect)

            scoreO=scoreO+1

            title = small.render(f"AI: {scoreO}", True, ORANGE)
            titleRect = title.get_rect()
            titleRect = (40, 60)
            main_screen.blit(title, titleRect)
            

        

        elif winner == "x":

            winner = "Game Over: X wins"
            
            #score for Human updation
            pg.display.update()
            title = small.render(f"Human: {scoreX}", True, BLACK)
            titleRect = title.get_rect()
            titleRect = (40, 100)
            main_screen.blit(title, titleRect)

            scoreX=scoreX+1

            title = small.render(f"Human: {scoreX}", True, ORANGE)
            titleRect = title.get_rect()
            titleRect = (40, 100)
            main_screen.blit(title, titleRect)
            
        else:
            pass

        title = Large.render(winner, True, WHITE)
        titleRect = title.get_rect()
        titleRect.center = ((WIDTH / 2), 80)
        main_screen.blit(title, titleRect)

        pg.display.update()

        pg.time.wait(100)
        
        reset_game()
        

        
    
    #defining a reset function to reset game 
    def reset_game():
        
        while(True):
            for event in pg.event.get():

                if event.type == pg.QUIT:

                    pg.quit()

                    sys.exit()

                
                
                elif event.type==pg.MOUSEBUTTONDOWN:

                    mouse_pointing_reset()


            againButton = pg.Rect(WIDTH / 3, HEIGHT - 90, WIDTH / 3, 50)
            again = medium.render("Play Again", True, BLACK)
            againRect = again.get_rect()
            againRect.center = againButton.center
            pg.draw.rect(main_screen, WHITE, againButton)
            main_screen.blit(again, againRect)
            pg.display.update()
            pg.display.flip()        



    #defining a function to pointing play again button  to get cordinate

    def mouse_pointing_reset():
        global BOARD,WINNER,k,XO,stop1,stop
        x,y = pg.mouse.get_pos()
        if((x>225 and x<550) and (y>375+40 and y<500-40)):
            BOARD =  [[' ',' ',' '],
            [' ',' ',' '],
            [' ',' ',' ']]

            XO=None
            k=1
            WINNER=None
            stop1=0
            stop=1
            main() 

    # Reinforcement learning core functions

    def ObtainBestMove(state, player):
        '''
        Reinforcement Learning Algorithm
        '''    
        moves = []
        CurrentStateValues = []
        Empty_Block = []
        for i in range(3):
            for j in range(3):
                if state[i][j] is ' ':
                    Empty_Block.append(i*3 + (j+1))
        
        for empty_cell in Empty_Block:
            moves.append(empty_cell)
            
            NewState = Intermediate_state(state)
            
            PlayMoveFor_AI(NewState, player, empty_cell)
            
            NextStateIndex = list(State_Dictionery_values.keys())[list(State_Dictionery_values.values()).index(NewState)]
            
            
            CurrentStateValues.append(StateValuesForAI_agent[NextStateIndex])
            
        print('Possible_moves = ' + str(moves))
        print('Move_values = ' + str(CurrentStateValues))    
        BestMoveIndex = np.argmax(CurrentStateValues)
        BestMove = moves[BestMoveIndex]
        print(BestMove)
        return BestMove





    def PlayMoveFor_AI(state, player, block_num):
        if state[int((block_num-1)/3)][(block_num-1)%3] is ' ':
            state[int((block_num-1)/3)][(block_num-1)%3] = player
        else:
            block_num = int(input("Block is not empty, ya blockhead! Choose again: "))
            PlayMoveFor_AI(state, player, block_num)
    
    def Intermediate_state(state):
        NewState = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
        for i in range(3):
            for j in range(3):
                NewState[i][j] = state[i][j]
        return NewState 


    #Main Program starts from this point at First!!
    
    

    
    # Initialize state values
    player = ['x','o',' ']
    State_Dictionery_values = {}
    AllPossibleStates = [[list(i[0:3]),list(i[3:6]),list(i[6:10])] for i in itertools.product(player, repeat = 9)]

    n_states = len(AllPossibleStates) # 2 players, 9 space


    n_actions = 9   # 9 spaces
    StateValuesForAI_agent = np.full((n_states),0.0)
    print("n_states = %i \nn_actions = %i"%(n_states, n_actions))
    for i in range(n_states):
        State_Dictionery_values[i] = AllPossibleStates[i]


    #LOAD TRAINED STATE VALUES    
    StateValuesForAI_agent = np.loadtxt('trained_state_values_O.txt', dtype=np.float64)


    starting_game()

    while(True):
        
        

        for event in pg.event.get():

            if event.type == pg.QUIT:

                pg.quit()

                sys.exit()

            
            
            elif event.type==pg.MOUSEBUTTONDOWN:

                mouse_pointing()

        pg.display.update()

        
 #calling main function at first
main()        