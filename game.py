import random 

def play_game():
    lucky_num = random .randint( 1 ,50)
   
    while True:
        num = int(input("Guess a lucky  number between 1 to 50 : "))
        if num == lucky_num:
            print("Congratulations ! ,You found it ",lucky_num)
            break
        elif num < lucky_num:
            print("TO low ")
        elif num > lucky_num:
            print("TO high ")

play_game()
