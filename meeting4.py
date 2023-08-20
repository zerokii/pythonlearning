# BMI checking system
while True:
    weight = float(input("What is your weight in kg?(Enter -1 to exit)==>"))
    if weight == -1:
        break
    height = float(input("What is your height in meters?(Enter -1 to exit)==>"))
    if height == -1:
        break
    bmi = weight/(height*height)
    print(f"Your BMI is: {bmi}")
    if bmi <18.5:
        print("Go eat")
    elif bmi <=24.9:
        print("You good")
    elif bmi <=29.9:
        print("Eat less")
    elif bmi <=34.9:
        print("Stop eating")
    elif bmi <=39.9:
        print("Go to the hospital")
    else:
        print("You dead")