import random
while True:
    user_action =input("Enter a choice (rock,paper,scissor): ")
    possible_action =["rock","paper","scissors"]
    computer_action =random.choice(possible_action)
    print("\n You choose {user_action}, computer choose {computer_action}.\n")
    if user_action == computer_action:
        print(f"Both platers selected {user_action} . It is a tie")
    elif user_action =="rock":
        if(computer_action =="scissors"):
            print("Rock smashes the scissors ! YOu win")
        else:
            print("Paper covers the rock ! You Lose")
    elif user_action =="paper":
        if computer_action =="rock":
            print("Paper covers rock  ! You win")
        else:
            print("Scissors cut the paper ! You lose")
    elif user_action =="scissors":
        if(computer_action =="paper"):
            print("Scissors cuts the paper ! you win")
        else:
            print("Rock smashes scissors ! You lose")
    play_again = input("Play again ? (y/n):")
    if play_again.lower() !="y":
        break