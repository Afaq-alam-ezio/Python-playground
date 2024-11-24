def student():
    try:
        a = int(input("Enter the roll num = "))
        print(f"The roll number is {a}")
        return 1   #  on using the return keyword below print won't works else it was working when there was no return keyword

    except:
        print("invalid input")
        return 0  #  on using the return keyword below print won't works

    print("hello there")

    #  below is the code that would have printed the statement inside print() above

    '''finally:
            print("Hello there)    # this would have worked
    '''


student()  #  calling the student function that is mentioned above

