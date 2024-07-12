import getpass

def game():
    choices = {1: "rock", 2: "paper", 3: "scissors"}
    player1_score = 0
    player2_score = 0

    while True:
        print("\nRock, Paper, Scissors Game")
        print("----------------------------")
        print("Player 1, enter 1 for rock, 2 for paper, or 3 for scissors to play.")
        print("Enter 'quit' to stop playing.")

        player1_choice = getpass.getpass("Player 1: ")

        if player1_choice.lower() == "quit":
            break

        try:
            player1_choice = int(player1_choice)
        except ValueError:
            print("Invalid choice. Please enter 1, 2, or 3.")
            continue

        if player1_choice not in choices:
            print("Invalid choice. Please enter 1, 2, or 3.")
            continue

        print("\nPlayer 2, enter 1 for rock, 2 for paper, or 3 for scissors to play.")

        player2_choice = input("Player 2: ")

        try:
            player2_choice = int(player2_choice)
        except ValueError:
            print("Invalid choice. Please enter 1, 2, or 3.")
            continue

        if player2_choice not in choices:
            print("Invalid choice. Please enter 1, 2, or 3.")
            continue

        print(f"\nPlayer 1 choice: {choices[player1_choice]}")
        print(f"Player 2 choice: {choices[player2_choice]}")

        if player1_choice == player2_choice:
            print("It's a tie!")
        elif (player1_choice == 1 and player2_choice == 3) or \
             (player1_choice == 2 and player2_choice == 1) or \
             (player1_choice == 3 and player2_choice == 2):
            print("Player 1 wins!")
            player1_score += 1
        else:
            print("Player 2 wins!")
            player2_score += 1

        print(f"\nScore - Player 1: {player1_score}, Player 2: {player2_score}\n")

    print("Thanks for playing!")

if __name__ == "__main__":
    game()