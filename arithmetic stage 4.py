# write your code here
import random

computer_answer = None

def level():
    global computer_answer
    user_level = int(input("Which level do you want? Enter a number: \n"
                       "1 - simple operations with numbers 2-9\n"
                       "2 - integral squares of 11-29"))
    counter = 0
    correct_answers = 0
    while counter < 5:
        if user_level != 1 and user_level != 2:
            print("Incorrect Format!")
            continue

        if user_level == 2:
            x = random.randint(11, 29)
            print(x)
            computer_answer = x ** 2
        elif user_level == 1:
            equation()

        noerror = True
        while noerror:
            try:
                user_answer = int(input())
            except ValueError:
                print("Wrong Format! Try again.")
                continue
            break
        if user_answer == computer_answer:
            print("Right")
            correct_answers += 1
            counter += 1

        else:
            print("Wrong!")
            counter += 1


    yes_no = input(f"Your mark is {correct_answers}/5. Would you like to save the result? Enter yes or no.")
    if yes_no not in ["Yes", "yes", "y", "YES"]:
        pass
    else:
        name = input("What is your name?")
        results = open("results.txt", "a")
        if user_level == 1:
            results.write(f"{name}: {correct_answers}/5 in level 1 (simple operations with numbers 2-9).")
        else:
            results.write(f"{name}: {correct_answers}/5 in level 2 (integral squares of 11-29).")
        print('The results are saved in "results.txt".')
        results.close()





def equation():
    global computer_answer
    operator = random.randint(1, 3)
    x = random.randint(2, 9)
    y = random.randint(2, 9)
    if operator == 1:
        computer_answer = x + y
        print(x, "+", y)
    elif operator == 2:
        computer_answer = x - y
        print(x, "-", y)
    elif operator == 3:
        computer_answer = x * y
        print(x, "*", y)
    # return answer


level()


