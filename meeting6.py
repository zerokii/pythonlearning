import random
print("""Winning Rules of the Rock Paper Scissors Game are:
          Rock Vs Paper => Paper
          Rock Vs Scissors => Rock
          Paper Vs Scissors  => Scissors""")

def pick_winner  (user_choice, AI_choice, user_choice_name, AI_choice_name):
    #user is the winner
    if ((user_choice==1 and AI_choice==2) or (user_choice==2 and AI_choice==3) or (user_choice==3 and AI_choice==1)):
        print(f"{user_choice_name} defeats {AI_choice_name}")
        print("<==User WINS!==>")

    #AI is the winner
    elif ((AI_choice==1 and user_choice==2) or (AI_choice==2 and user_choice==3) or (AI_choice==3 and user_choice==1)):
        print(f"{AI_choice_name} defeats {user_choice_name}")
        print("<== AI's reign has begun ==>")

    #stalemate
    else:
        print(f"{user_choice_name} --- {AI_choice_name}")
        print("<== It is a STALEMATE ==>")

while True:
    print("""Enter choice:
          1 ==> Rock
          2 ==> Scissors
          3 ==> Paper) """)
    choice = int(input("User turn: "))
    while choice > 3 or choice < 1:
        choice= int(input("Enter Valid Input: "))
    if choice == 1:
        choice_name = "Rock"
    elif choice == 2:
        choice_name = "Scissors"
    else:
        choice_name = "Paper"

    print(f"User choice is: {choice_name}")
    print("\n Now it's AI's turn")
    comp_choice = random.randit(1,3)

    if comp_choice == 1:
        comp_choice_name = "Rock"
    elif comp_choice == 2:
        comp_choice_name = "Scissors"
    else:
        comp_choice_name = "Paper"
    print(f"Computer choice is: {comp_choice_name}")

    print(f"\n {choice_name} VS {comp_choice_name}")

    pick_winner(choice, comp_choice, choice_name, comp_choice_name)
    response = input("\nDo you want to play again? (Y/N):")
    if response.upper() == "N":
        break

print("Thanks for playing")