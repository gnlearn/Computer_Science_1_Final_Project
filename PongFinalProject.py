#Nico Gonnela
#4/26/23
#Final Project: pong :)

from graphics import *
from PongFinalObjects import *


win = GraphWin("Pong Game",800,500, autoflush=False)
click = 0
changed_speed = False
    
def entire_program(counter_p1, counter_p2, player_scores_list):
    """
    Purpose: This runs one round of pong when called
    Parameters: It takes in the counter for player 1 and player 2 and the player_scores_list which has the scores of the last round and who scored last.
    Return: after running the game it returns a list of the two counters which is triggered by if the ball touched either wall and a one if player 1 was scored on so the ball starts the other direction for the next round. 
    """
    background_rect = Rectangle(Point(0,0), Point(800, 500))
    background_rect.setFill("white")
    background_rect.setOutline("white")
    background_rect.draw(win)

    ball = Ball(6)
    ball.draw(win)
    

    starting_text = Text(Point(400,100), "Press the space bar to start!")
    starting_text.draw(win)
    
    player1_text = Text(Point(75,20), "Player 1 Points: " + str(counter_p1))  #Adding the plus came from chatGPT I couldn't figure out how to not have a comma because it is too many parameters 
    player1_text.setFill("red")
    player1_text.draw(win)

    player2_text = Text(Point(725,20), "Player 2 Points: " + str(counter_p2))   
    player2_text.setFill("blue")
    player2_text.draw(win)

    p1_rect = Rectangle(Point(10,200), Point(20, 300))
    p1_rect.setFill("red")
    p1_rect.setOutline("red")
    p1_rect.draw(win)
    
    p2_rect = Rectangle(Point(780,200), Point(790, 300))
    p2_rect.setFill("blue")
    p2_rect.setOutline("blue")
    p2_rect.draw(win)
    
    start = 0
    collision = False
    while start == 0:
        key = win.checkKey()
             
        
        
        if key == 'space':
            ball.x_speed += 4
            ball.y_speed += 4
            
            starting_text.setText("")
            start = 1
            changed_speed = False
    while win.isOpen() and collision == False:
        
        ball.move()
        
        
        if player_scores_list[len(player_scores_list)-3] == 1 and changed_speed == False:
            ball.x_speed = - ball.x_speed
            changed_speed = True
        
        
        key = win.checkKey()
        if key == 'w' and p1_rect.getCenter().getY() - 50 >= 0:  #Future Nico, this randomly worked because it made sure that the top of the rectangle was above the 0 point which is the top boundary. 
            p1_rect.move(0,-6)
            
        elif key == 's' and p1_rect.getCenter().getY() + 50 <= 500:
            p1_rect.move(0,6)
        
        if key == 'Up' and p2_rect.getCenter().getY() - 50 >= 0:       #Future Nico, this must be capitalized
            p2_rect.move(0,-6)
            
        elif key == 'Down' and p2_rect.getCenter().getY() + 50 <= 500:
            p2_rect.move(0,6)
        
        if ball.top() > 500 or ball.bottom() < 0:
            ball.y_speed = - ball.y_speed
            
        player1_rectangle = p1_rect.getCenter().getY()
        player2_rectangle = p2_rect.getCenter().getY()
        
        if ball.left_side() <= 20 and ball.y_center() <= player1_rectangle + 50 and ball.y_center() >= player1_rectangle - 50:
            ball.x_speed = - ball.x_speed
            ball.change_color()
            
        if ball.right_side() >= 780 and ball.y_center() <= player2_rectangle + 50 and ball.y_center() >= player2_rectangle - 50:
            ball.x_speed = - ball.x_speed
            ball.change_color()
        
        if ball.top() <= player2_rectangle + 50 and 780 <= ball.x_center() <= 790 and ball.y_center() >= player2_rectangle:   #Future Nico, look hard at the parenthesis when debugging. Which value needs to be bigger and smaller and this is in reference to values increasing as you approach the right corner. 
            ball.y_speed = - ball.y_speed
            ball.change_color()
        
        if ball.top() <= player1_rectangle + 50 and 10 <= ball.x_center() <= 20 and ball.y_center() >= player1_rectangle:
            ball.y_speed = - ball.y_speed
            ball.change_color()
        
        if ball.bottom() >= player2_rectangle - 50 and 780 <= ball.x_center() <= 790 and ball.y_center() <= player2_rectangle:   
            ball.y_speed = - ball.y_speed
            ball.change_color()
        
        if ball.bottom() >= player1_rectangle - 50 and 10 <= ball.x_center() <= 20 and ball.y_center() <= player1_rectangle:   
            ball.y_speed = - ball.y_speed
            ball.change_color()
            
            
        send_to_p1 = 0
        
        if ball.right_side() >= 800 and collision == False:  #I couldn't stop it from continuously adding points, chatGPT told me I should add a variable to check if it had already executed this chunk
            ball.x_speed = 0                                 #I didn't use the chatGPT code and stopped it while it was generating the code because I wanted to try and do the idea myself, but it gave me the idea.
            ball.y_speed = 0
            counter_p1 +=1
            send_to_p1 = 1
            collision = True
            player1_text.setText("Player 1 Points: " + str(counter_p1))   #use setText rather than pasting a white rectangle!!!
            
            
        if ball.left_side() <= 0 and collision == False:  
            ball.x_speed = 0
            ball.y_speed = 0
            counter_p2 +=1
            send_to_p1 = 0
            collision = True
            player2_text.setText("Player 2 Points: " + str(counter_p2))
        
        
        
        update(60)
    
    player_scores_list.append(send_to_p1)
    player_scores_list.append(counter_p1)
    player_scores_list.append(counter_p2)
    
    return player_scores_list

player_scores_list = [0,0]
counter_p1 = 0
counter_p2 = 0

button_clicked = False

intro_background_rect = Rectangle(Point(0,0), Point(800, 500))
intro_background_rect.setFill("white")
intro_background_rect.setOutline("white")
intro_background_rect.draw(win)

play_button_rect = Rectangle(Point(300,275), Point(500, 325))
play_button_rect.setFill("red")
play_button_rect.setOutline("black")
play_button_rect.draw(win)

press_play = Text(Point(400,300), "Play")
press_play.draw(win)

Title = Text(Point(400,200), "PONG")
Title.setSize(30)
Title.draw(win)

print("Welcome to my game of Pong! Player one uses w and s to move up and down while player two uses the up and down arrow keys to move. Press\nplay to start the game. When your fingers are on the keys, press the spacebar to make the ball move. The objective is to bounce the ball\noff your paddle without it touching your side. Each time it touches a side the other player scores a point. The first player to 3 points wins!")

while button_clicked == False:    
    
    click = win.getMouse()  #chat GPT helped me identify what this is and how to use it. Also, acknowledged that I can use getX and Y functions with the click
        
    if click is not None and 500 >= click.getX() >= 300:
        if 325 >= click.getY() >= 275:              #could use and also
            button_clicked = True  #for some reason this variable was not working especially when I clicked multiple times, but it randomly started working.
    else:
        print("Press Play!")
           

while counter_p1 != 3 and counter_p2 != 3:
    player_scores_list = entire_program(counter_p1, counter_p2, player_scores_list)
    counter_p1 = player_scores_list[len(player_scores_list)-2]
    counter_p2 = player_scores_list[len(player_scores_list)-1]
    
background_rect = Rectangle(Point(0,0), Point(800, 500))
background_rect.setFill("white")
background_rect.setOutline("white")
background_rect.draw(win)


if counter_p1 > counter_p2:
    p1_win = Text(Point(400,250), "Player 1 WINS!!!")
    p1_win.setFill("red")
    p1_win.setSize(30)
    p1_win.draw(win)

if counter_p1 < counter_p2:
    p2_win = Text(Point(400,250), "Player 2 WINS!!!")
    p2_win.setFill("blue")
    p2_win.setSize(30)
    p2_win.draw(win)

win.mainloop()    #for some reason the player winning text stopped appearing. I found this command from chatGPT for something else and tried it here and it randomly worked. 
