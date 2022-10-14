import random
pencils = input("How many pencils would you like to use: ")

while True:
    if pencils.isdigit():
        pencils = int(pencils)
        if pencils > 0:
            break
        else:
            print("The number of pencils should be positive")
            pencils = input()
    else:
        print("The number of pencils should be numeric")
        pencils = input()


john = "John"
jack = "Jack"
user = input("Who will be the first (John, Jack)?")
user2 = ""

while True:
    if user == john:
        user2 = "Jack"
        break
    elif user == "Jack":
        user2 = "John"
        break
    else:
        print("Choose between 'John' and 'Jack'")
        user = input()
    
print("|" * pencils)
print(user + "'s turn")
player = user

while True:
    if player == "John":
        player_input = input()
        if player_input.isdigit():
            if int(player_input) not in (1, 2, 3):
                print("Possible values: '1', '2' or '3'")
                continue
            if int(player_input) > pencils:
                print("Too many pencils were taken")
                continue
        else:
            print("Possible values: '1', '2' or '3'")
            continue
        if player == "John":
            player = "Jack"
        else: 
            player = "John"
    else:
        if pencils in range(2, 1000, 4):
            player_input = 1
            print(player_input)
        elif pencils in range(3, 1000, 4):
            player_input = 2
            print(player_input)
        elif pencils in range(4, 1000, 4): 
            player_input = 3
            print(player_input)
        else:
            if pencils > 3:
                player_input = random.randint(1,3)
                print(player_input)
            else:
                player_input = random.randint(1, pencils)
                print(player_input)
        if player == "John":
            player = "Jack"
        else: 
            player = "John"
    if int(player_input) == pencils:
        print(player + " won!")
        break
    pencils -= int(player_input)
    print("|" * pencils)
    print(player + "'s turn!")
    continue 
