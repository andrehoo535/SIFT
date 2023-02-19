import tkinter
from tkinter import *
whites_move=True
square1_h = 0
square1_v = 0
button_in_progress=False
def piece_check(col,row):
    #piece check is a prescence check for a piece in a given location. I have made it so it acts
    #differently depending on if it is black or whites move. Only the player currently moving is relevant.
    if whites_move==True:
        if board_status[row][col]>0:
            #0 represent no piece, Black pieces will be represented by negative integers. White by positive.
            print(col)
            print(row)
            global square1_h
            global square1_v
            square1_h=col
            square1_v=row
            return True
        else:
            print("you do not have a piece on this square")
            return False
    else:
        if board_status[row][col]<0:
            print("meh")
            square1_h=col
            square1_v=row
            return True
        else:
            print("you do not have a piece on this square")
            return False        
def attempt_move(square1_h,square1_v,square2_h,square2_v):
    global legal_moves
    global whites_move
    if [square1_h,square1_v,square2_h,square2_v] in legal_moves:
        if whites_move==False:
            whites_move = True
            #commit_move()
            #generate new legal moves
        else:
            whites_move = False
        #change board and image

def button_check(column,row):
    #upon button pressed checked the location of the button in relation to the board
    global button_in_progress
    if button_in_progress==False:
        if piece_check(column,row)==True:
            button_in_progress=True
    #elif button_in_progress==True:
    else:
        global square1_h
        global square1_v 
        print(column)
        print(row)
        if attempt_move(square1_h,square1_v,column,row)==True:
            #image stuff
            #delete image from square1, move to new square
            global whites_move
            if whites_move==False:
                whites_move=True
            else:
                whites_move=False
        else:
            button_in_progress = False
        

        
board_status=[]
def startgame():
    global board_status
    #set board to starting position
    board_status=[[-2,-3,-4,-8,-9,-4,-3,-2],[-1,-1,-1,-1,-1,-1,-1,-1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[1,1,1,1,1,1,1,1],[2,3,4,8,9,4,3,2]]
    #create a tkinter canvas in which i can produce a grid of buttons to represents squares on the board.
    global legal_moves
    legal_moves = [[0,6,0,5],[0,6,0,4],[1,6,1,5],[1,6,1,4],[2,6,2,5],[2,6,2,4],[3,6,3,5],[3,6,3,4],[4,6,4,5],[4,6,4,4],[5,6,5,5],[5,6,5,4],[6,6,6,5],[6,6,6,4],[7,6,7,5],[7,6,7,4],[1,7,0,5],[1,7,2,5],[6,7,5,5],[6,7,7,5]]
    Board_buttons=tkinter.Tk()
    Board_buttons.title("grid() method")
    Board_buttons.geometry("640x680")
    #assign images for pieces

    

    #creating a canvas for img display
    image_canvas = Canvas(Board_buttons,width=640,height=640)
    BRook = PhotoImage(file="C:\SIFT\B_Rook.png")
    B_Rook = image_canvas.create_image(50,50, anchor=NW,image=BRook)
    for i in range(8):
        for j in range(8):
            #small algorithm for chequered board pattern
            if (i+j)%2==1:
                colour="black"
            else:
                colour="white"
            button1=tkinter.Button(Board_buttons,width=10,height=5,bg=colour, command=lambda row=j, column=i:button_check(row,column))
            button1.grid(row=i,column=j)
    Board_buttons.mainloop()
startgame()



