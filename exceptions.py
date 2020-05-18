while True: 
    try:
        x = int(input("enter a number"))
    except ValueError:
        print("uh oh")
    else:
        print("good job")
        break 
    finally: 
        print("thanks for playing")