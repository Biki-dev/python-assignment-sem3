# Rock - Scissors and Lizard - ( 1 beats 3 and 4 )
# Paper - Rock and Spock - ( 2 beats 1 and 5 )
# Scissors - Paper and Lizard - ( 3 beats 2 and 4 )
# Lizard - Paper and Spock - ( 4 beats 2 and 5 )
# Spock - Rock and Scissors - ( 5 beats 1 and 3 )

print("Welcome to the game!")
print("Choose your move:\n1. Rock\n2. Paper\n3. Scissors\n4. Lizard\n5. Spock")
print("------------------------------------------------------")
print("Player 1, please enter your choice (1-5):")
player1_choice = int(input())
print("Player 2, please enter your choice (1-5):")
player2_choice = int(input())

if player1_choice == player2_choice:
    print("It's a tie!")
elif (player1_choice == 1 and (player2_choice == 3 or player2_choice == 4)) or \
     (player1_choice == 2 and (player2_choice == 1 or player2_choice == 5)) or \
     (player1_choice == 3 and (player2_choice == 2 or player2_choice == 4)) or \
     (player1_choice == 4 and (player2_choice == 2 or player2_choice == 5)) or \
     (player1_choice == 5 and (player2_choice == 1 or player2_choice == 3)):
    print("Player 1 wins!") 
else:
    print("Player 2 wins!") 