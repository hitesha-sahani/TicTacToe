import tkinter as tk            
from tkinter import messagebox    #messagebox is a module within tkinter
'''0,0      0,1      0,2
   1,0      1,1      1,2
   2,0      2,1      2,2'''

def check_winner():                #to determine if a player has won the game
    for row in board:             #iterates through each row
        if len(set(row)) == 1 and row[0] != 0:        #checks if all elements in row are equal and first element in a row is not empty,indicating a winner in that row
            return True

    for col in range(3):               #iterates through each column 
        if board[0][col] == board[1][col] == board[2][col] != 0:            #checks if all elements in column are filled,indicating a winner in that row
            return True

    if board[0][0] == board[1][1] == board[2][2] != 0 or board[0][2] == board[1][1] == board[2][0] != 0:     #checks if there is a winner in both diagonals
        return True

    return False             #returns false if no winner is found

def check_draw():
    return all(cell != 0 for row in board for cell in row)    #checks if clicked cell is empty and there is no winner yet,here all function check if condition holds for all cells

def on_click(row, col):     #this function is called when a button on game grid is clicked
    global current_player

    if board[row][col] == 0 and not winner:       
        board[row][col] = current_player              #updates the board with the current player's move
        buttons[row][col].config(text=players[current_player], state=tk.DISABLED)    #updates button text to display player's symbol and disables the button after the move

        if check_winner():
            messagebox.showinfo("Tic Tac Toe", f"Player {players[current_player]} wins!")
            reset_game()
        elif check_draw():
            messagebox.showinfo("Tic Tac Toe", "It's a draw!")
            reset_game()
        else:
            current_player = 1 if current_player == 2 else 2       #switches the current player

def reset_game():              #to reset game variable and button states
    global board, winner, current_player
    board = [[0, 0, 0] for _ in range(3)]           #initialize the game board as 3*3 matrix filled with zeroes
    winner = False
    current_player = 1
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(text="", state=tk.NORMAL)      #configures each button on grid with default setting

# Initialize the game
board = [[0, 0, 0] for _ in range(3)]   #re-initialize the board after resetting
winner = False
current_player = 1
players = {1: "X", 2: "O"}   #dictionary mapping player number to their symbols

# Create the main window
root = tk.Tk()
root.title("Tic Tac Toe")

# Create buttons for the game grid
buttons = [[tk.Button(root, text="", font=("Helvetica", 24), width=5, height=2, command=lambda i=i, j=j: on_click(i, j)) for j in range(3)] for i in range(3)]

# Place buttons on the grid
for i in range(3):
    for j in range(3):
        buttons[i][j].grid(row=i, column=j)    #place each button on grid

# Create a Reset button
reset_button = tk.Button(root, text="Reset", command=reset_game)   #here root means we are saying that put this button in a main window
reset_button.grid(row=3, column=1)      #place the reset button on grid

# Run the Tkinter event loop
root.mainloop()
