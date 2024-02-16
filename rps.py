import random

ROCK = "rock"
PAPER = "paper"
SCISSORS = "scissors"

rock_img = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

paper_img = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

scissors_img = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

choices = {
    ROCK: rock_img,
    PAPER: paper_img,
    SCISSORS: scissors_img
}


def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "Draw!"
    elif (player_choice == ROCK and computer_choice == SCISSORS) or \
         (player_choice == PAPER and computer_choice == ROCK) or \
         (player_choice == SCISSORS and computer_choice == PAPER):
        return "You Win!"
    else:
        return "You Lose!"


def main():
    playing = True
    while playing:
        print("1. Rock\n2. Paper\n3. Scissors")
        player_selection = input("Enter your choice (1/2/3): ").strip()

        if player_selection not in ["1", "2", "3"]:
            print("Invalid choice. Please enter 1, 2, or 3.")
            continue

        player_choice = ""
        if player_selection == "1":
            player_choice = ROCK
        elif player_selection == "2":
            player_choice = PAPER
        elif player_selection == "3":
            player_choice = SCISSORS

        computer_choice = random.choice([ROCK, PAPER, SCISSORS])

        print("Player chooses:")
        print(choices.get(player_choice, "Invalid choice!"))
        print("Computer chooses:")
        print(choices[computer_choice])

        print(determine_winner(player_choice, computer_choice))

        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != "yes":
            playing = False

if __name__ == "__main__":
    main()
