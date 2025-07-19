import random

def get_computer_choice():
    return random.choice(["stone", "paper", "scissors"])

def get_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == "stone" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "stone"):
        return "You win!"
    else:
        return "Computer wins!"

print("🎮 Stone, Paper, Scissors Game 🎮")
print("Enter your choice: stone / paper / scissors")

user_choice = input("Your choice: ").lower()
if user_choice not in ["stone", "paper", "scissors"]:
    print("❌ Invalid choice. Please choose stone, paper, or scissors.")
else:
    comp_choice = get_computer_choice()
    print(f"Computer chose: {comp_choice}")
    result = get_winner(user_choice, comp_choice)
    print(result)
