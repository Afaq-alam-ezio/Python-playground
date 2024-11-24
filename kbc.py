def game1():
    answer = input("1. what is national animal of india ?\n\t1.ant\t2.deer\n\t3.tiger\t4.eagle\nEnter answer = ")
    if answer == '3':
        print("Congrats! you won Rs 1000")
        return game2()
    else:
        print("Oops !! wrong answer .. you are out.")
        # return False


def game2():
    answer = input("2. Who is owner of lamborghini ?\n1. Volkswagen\t2. Ferrari\n3. Tata\t\t\t4. Nissan\nEnter answer = ")
    if answer == '1':
        print("Congrats! you won Rs 2000")
        return game3()
    else:
        print("Opps !! wrong answer .. you are out.")
        # return False


def game3():
    answer = input("3. What is the capital of India ?\n1. Delhi\t2. Kerala\n3. Ranchi\t4. Mumbai\nEnter answer = ")
    if answer == '1':
        print("Congrats! you won Rs 3000")
        return game4()
    else:
        print("Opps !! wrong answer .. you are out.")
        # return False


def game4():
    answer = input("4. What is the color of apple ?\n1. Red\t2. Orange\n3. Purple\t4. Yellow\nEnter answer = ")
    if answer == '1':
        print("Congrats! you won Rs 4000")
        return game5()
    else:
        print("Opps !! wrong answer .. you are out.")
        # return False


def game5():
    answer = input("5. What is chemical formula of water ?\n1. H2O\t2. HCl\n3. NaCl\t4. KOh\nEnter answer = ")
    if answer == '1':
        print("Congrats! you won Rs 5000")
        return game6()
    else:
        print("Opps !! wrong answer .. you are out.")
        # return False


def game6():
    answer = input("6. Full form of CD ?\n1. co disk\t2. Compact disk\n3. Card dot\t4. Call dat\nEnter answer = ")
    if answer == '2':
        print("Congrats! you won Rs 6000")
        return game7()
    else:
        print("Opps !! wrong answer .. you are out.")
        # return False


def game7():
    answer = input("7. How many zeros are there in One million ?\n1. 9\t2. 20\n3. 6\t4. 4\n Enter answer = ")
    if answer == '3':
        print("Congrats! you won Rs 7000")
        return game8()
    else:
        print("Opps !! wrong answer .. you are out.")
        # return False


def game8():
    answer = input("8. Who is Code with harry ?\n1. Youtuber\t2. Pilot\n3. Engineer\t4. Watchman\n Enter answer = ")
    if answer == '1':
        print("Congrats! you won Rs 8000")
        return game9()
    else:
        print("Opps !! wrong answer .. you are out.")
        # return False


def game9():
    answer = input("9. When was Windows 11 launched ?\n1. 2003\t2. 2022\n3. 1810\t4. 2023\n Enter answer = ")
    if answer == '2':
        print("Congrats! you won Rs 9000")
        return game10()
    else:
        print("Opps !! wrong answer .. you are out.")
        # return False


def game10():
    answer = input("10. What is configuration of AND Gate ?\n1. a+a\t2. a*a\n3. a/a\t4. a-a\n Enter answer = ")
    if answer == '2':
        print("VERY MUCH CONGRATULATIONS!", name, "you won Rs 10000")
    else:
        print("Opps !! wrong answer .. you are out.")
        # return False


ready = input("Are you ready ?\ny = yes\nn = no\nEnter the status = ")
if ready == 'y':
    name = input("Welcome to the Game \nplease enter your name : ")
    print("The game will consist of 10 questions each\none incorrect answer will lead to disqualification.")
    game1()
elif ready == 'n':
    print("Okay visit us again once ready.")
else:
    print("Invalid input")
