import random
def game():
    computer_score = 0
    user_score = 0
    for i in range(5):
        computer_choice = random.choice(("rock", "paper", "scissors"))
        user_choice = input("Enter your choice (rock/paper/scissors): ").strip().lower()
        if user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice! Please choose 'rock', 'paper', or 'scissors'.")
            continue
        print(f"Computer chose: {computer_choice}")

        if (computer_choice == "rock" and user_choice == "scissors") or (computer_choice=="scissors" and user_choice=="paper") or (computer_choice=="paper" and user_choice=="rock"):
            computer_score += 1
            print(f"Computer gets a point.\nComputer points: {computer_score}, Your points: {user_score}")
        elif (computer_choice == "rock" and user_choice == "paper") or (computer_choice=="paper" and user_choice=="scissors") or (computer_choice == "scissors" and user_choice == "rock"):
            user_score += 1
            print(f"You get a point.\nComputer points: {computer_score}, Your points: {user_score}")
        else:
            computer_score += 1
            user_score += 1
            print(f"Both computer and you get a point.\nComputer points: {computer_score}, Your points: {user_score}")
    print("\nFinal Results:")        
    if user_score > computer_score:
        print(f"You are winner! Total points: Computer: {computer_score}, You: {user_score}") 
    elif computer_score > user_score:
        print(f"Computer is winner! Total points: Computer: {computer_score}, You: {user_score}") 
    else:
        print(f"Draw! Total points: Computer: {computer_score}, You: {user_score}") 

game()  