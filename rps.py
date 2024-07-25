import random
def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissor'])
def get_user_choice():
    user_choice = input("Enter your choice (rock/paper/scissor): ").lower()
    while user_choice not in ['rock', 'paper', 'scissor']:
        print("Invalid choice. Please choose rock, paper, or scissor.")
        user_choice = input("Enter your choice (rock/paper/scissor): ").lower()
    return user_choice
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissor') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "Computer win!"
def play_game():
    user_score = 0
    computer_score = 0
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")
        result = determine_winner(user_choice, computer_choice)
        print(result)
        if result == "You win!":
            user_score += 1
        elif result == "Computer win!":
            computer_score += 1
        print(f"Score: You {user_score} - {computer_score} Computer")
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break
if __name__ == "__main__":
    play_game()