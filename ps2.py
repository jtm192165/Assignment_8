#defining the game table
board = ["0", "0", "0",
         "0", "0", "0",
         "0", "0", "0"]

def display_board():
  print("\n")
  print(board[0] + " | " + board[1] + " | " + board[2] + "     ")
  print(board[3] + " | " + board[4] + " | " + board[5] + "     ")
  print(board[6] + " | " + board[7] + " | " + board[8] + "     ")
  print("\n")         

game_on = True 
winner = None
current_player = "Player1"
used_numbers = ""

def main():

  print("Welcome to the Game!")

  # Loop until the game stops (winner or tie)
  while game_on:

    # Handle a turn
    current_turn(current_player)
    check_if_game_over()
    flip_player()

  if winner == "Player1" or winner == "Player2":
    print(winner + " won.")
  elif winner == None:
    print("Tie.")





def current_turn(player):
  
  # Get data from player
  print(player + "'s turn.")
  position,number = input("Enter the position and number to be entered: ").split()
  
  valid = False
  while not valid:

    # Make sure the input is valid
    while (position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]) or (number not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]) :
      position,number = input("Enter valid position and number: ").split()
 
    # Get correct index
    position = int(position) - 1
    
    global used_numbers
    if (board[position] == "0") and (number not in used_numbers) :
      valid = True
    else:
      print("You have entered already filled position or already used number. Retry ")
      display_board()

  board[position] = number
  used_numbers = used_numbers + number

  display_board()

def check_if_game_over():
  check_for_winner()
  check_for_tie()

def check_for_winner():
  # Set global variables
  global winner
  # Check if there was a winner anywhere
  row_winner = check_rows()
  column_winner = check_columns()
  diagonal_winner = check_diagonals()
  # Get the winner
  if row_winner:
    winner = row_winner
  elif column_winner:
    winner = column_winner
  elif diagonal_winner:
    winner = diagonal_winner
  else:
    winner = None

def check_rows():
  # Set global variables
  global game_on
  # Check if any of the rows have all the same value (and is not empty)
  row_1 = int(board[0]) + int(board[1]) + int(board[2]) >= 15
  row_2 = int(board[3]) + int(board[4]) + int(board[5]) >= 15
  row_3 = int(board[6]) + int(board[7]) + int(board[8]) >= 15

  # If any row does have a match, flag that there is a win
  if row_1 or row_2 or row_3:
    game_on = False
    return current_player
  # Return the winner
  else:
    return None

def check_columns():
  # Set global variables
  global game_on
  # Check if any of the rows have all the same value (and is not empty)
  column_1 = int(board[0]) + int(board[3]) + int(board[6]) >= 15
  column_2 = int(board[1]) + int(board[4]) + int(board[7]) >= 15
  column_3 = int(board[2]) + int(board[5]) + int(board[8]) >= 15

  # If any row does have a match, flag that there is a win
  if column_1 or column_2 or column_3:
    game_on = False
    return current_player
  # Return the winner
  else:
    return None

def check_diagonals():
  # Set global variables
  global game_on
  # Check if any of the rows have all the same value (and is not empty)
  diagonal_1 = int(board[0]) + int(board[4]) + int(board[8]) >= 15
  diagonal_2 = int(board[2]) + int(board[4]) + int(board[6]) >= 15

  # If any row does have a match, flag that there is a win
  if diagonal_1 or diagonal_2:
    game_on = False
    return current_player
  # Return the winner
  else:
    return None

# Check if there is a tie
def check_for_tie():
  # Set global variables
  global game_on
  # If board is full
  if "0" not in board:
    game_on = False
    return True
  # Else there is no tie
  else:
    return False

def flip_player():
  # Global variables we need
  global current_player
  
  if current_player == "Player1":
    current_player = "Player2"
  
  elif current_player == "Player2":
    current_player = "Player1"


main()