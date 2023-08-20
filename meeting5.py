#Function
def check_guess(user_input,answer):
    global score
    still guessing = True 
    attempt = 0
    while still_guessing and attempt<3:
        if user_input.upper() == answer.upper():
            print("Correct Answer! Pandai")
            score += 1
            still_guessing = False
        else: 
            if attempt<2:
                user_input = input("Sorry wrong answer. Please try again\n")
            attempt += 1
    if attempt == 3:
        print(f"The correct answer is:{answer}")
# Main program
score = 0 # global variable
print("Guess the Country!")

guess1 = input("By size, what is the largest country in the world?\n")
check_guess(guess1, "russia")
guess2 = input("Which country has a unicorn as its national animal?\n")
check_guess(guess2, "scotland")
guess3 = input("In which country would you find the currency Baht?\n")
check_guess(guess3, "thailand")

print(f"Your score is: {score}")