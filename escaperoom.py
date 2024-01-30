import random
import sys
def rusty_main():
    def rusty_room1():
            
            rusty_junk = [
            "cables",
            "wires",
            "pipes",
            "life ring",
            "old car"

        ]
            junk_string = ", ".join(rusty_junk)
            rusty_junk = input("You enter what apears to be an old run down warehouse. There are piles of broken and abandoned items left in a heap. do you want to inspect the items or read the riddle? (items/riddle)")
            if rusty_junk == "riddle":
                riddle=input("what five letter word written in all caps can be read the same upside down?").upper()
                if riddle == "swims":
                    print("You got the riddle correct!")
                    rusty_room2()
                elif riddle == "SWIMS":
                    print("You got the riddle correct!")
                    rusty_room2()
                else:
                    print("Incorrect")
                    rusty_room1()
            elif rusty_junk == "items":
                print(junk_string)
                print("type back to go back")
            grab_junk = input("What do you want to inspect")
            if grab_junk == "life ring":
                print("a life ring... someone would probably use this to help them to SWIM...")
                rusty_room1()
            elif grab_junk == "cables":
                print("the cables dont seem to do much")
                rusty_room1()
            elif grab_junk == "wires":
                print("the wires dont seem to do much")
                rusty_room1()
            elif grab_junk == "pipes":
                print("the pipes dont seem to do much")
                rusty_room1()
            elif grab_junk == "old car":
                print("you try to start the car, unfortunately it blows up")
                game_over()
            elif grab_junk == "back":
                rusty_room1()

    
    
    ### ^^^ farwa and sara + added extra from dominic

    def rusty_room2():
        print( "Before you lies an empty swimming pool,\n sever through the junk and see what you find.")
        pool_items = ["bin bags", "plastic bags", "a beer bottle",
            "a bike tire", "scrap metal pieces", "a light fixture"]
        while True:
            for item in pool_items:
                scrambled_items = ''.join(random.sample(item, len(item)))
                print(scrambled_items)
            print("Come near, never fear, truth's here, crystal clear.")

            closer_look = input("Would you like to come closer?(yes/no)")
        
            if closer_look == "no":
                 print("remain confused")
            elif closer_look == "yes":
                print("Wise choice, now you see:")
                for x in pool_items:
                    print(x)
                correct_item = input("Out of these items, what has a neck but no head?")
                if correct_item == "a beer bottle":
                    print("Good work, you have selected the right item")
                    rusty_room3()
            else:
               print("Try again")
    ### ^^^ reuben 

    def rusty_room3():
        print("You have entered another room. it looks like an old saloon,\nthere are lots of paintings on the wall which all seem very similar.\nEach scene has a number of people who just seem to be stood talking to each other.\nAt the other side of the bar there is a door with some letters on a keypad.\nYou approach and notice a question is painted on the door\n ")

        print("I'm found in a bar, buzzing with life.\nSome come alone, others with husband or wife.\nI'm key to connections, laughter and cheer.\nAmidst clinking glasses you’ll find me near.\n\nWhat am I?")
        Answer = input("What is your answer?:").lower()
        if Answer == "conversation": 
            rusty_room4()
        else:
            print("You're not looking at the clues")
            rusty_room1()

### ^^^ mark + joseph

    def rusty_room4():

        choice = input("would you like to answer the riddle or sit to think? (riddle/think)")
        if choice == "think":
            print("You have a little sit down, you contemplate your journey and you feel the wind on your face and the sunlight barely warms your skin\nthe air is crisp as you stand as all you can hear is the gentle breeze flowing through the town...")
            rusty_room4()
        elif choice == "riddle":
            answer=input("I touch your face. I'm in your words. I'm the lack of space loved by birds... what am I?").lower()
            if answer == "air":
                print("congrats...")
                rusty_escape()
        else:
           print('unfortunately...')
           rusty_room1()

### ^^^ reuben

    rusty_room1()
    rusty_room2()
    rusty_room3()
    rusty_room4()

def rusty_escape():
        while True:
            print("you have successfully escaped the race against time and successfully stopped yourself from joining the withering away rooms! Congratulations")
            end=input("do you want to try again? Y/N").lower()
            if end == "y":
                start()
            elif end == "n":
                print("We hope you had fun!")
                sys.exit()
            else:
                print("we dont know what you mean")


def future_escape():
        while True:
            print("You beat the clock and escaped just in time to keep living your life before it ran away from you! Congratulations")
            end=input("do you want to try again? Y/N").lower()
            if end == "y":
                start()
            elif end == "n":
                print("We hope you had fun!")
                sys.exit()
            else:
                print("we dont know what you mean")

def game_over():
    while True:
        death=input("You made the wrong choice... you lost your brain.... or your life.... do you want to try again? Y/N")
        if death == "Y":
            start()
        elif death =="N":
            print("We hope you had fun anyway!")
            sys.exit
        else:
            print("we dont know what you mean")

def future_main(Name):
    def future_room1():
        Answer = "four"

        print('You enter the first futuristic room, you see a tv screen which reads: ')

        print('What number contains the same amount of characters as its own number')

        print('Use the keypad to write your answer')

        Answer = input('What is your answer')

        if Answer == "4" or Answer == "four":

                print("That is correct you can move to the next room")
                future_room2()

        else:

                print('Try again')
                future_room1()

### ^^ farwa and sara

    def future_room2():
 
        print ("You're driving an empty bus, you pick up 10 people from Manchester you pick up 5 more people from Bolton, you drop off 11 people at Wigan, you pick up 8 more people in Salford ")
        Answer = input("What is the name of the driver?")
        if Answer.lower() == Name.lower():
            print ("Correct")
            future_room3()
        else:
            print ("Incorrect, go back a room!")
            future_room2()

### ^^^ joseph

    def future_room3():
        print("In front of you there is a set of scales")
        print("One one side is a kilogramme of feathers, and the other has a kilogramme of steel")
        scale=input("which one is heavier?")
        if scale in ["neither", "none", "both"]:
            future_room4()
        elif scale in ["feathers", "steel"]:
            print("you're going back to the start!")
            future_room1()
### ^^ dominic and reuben

    def future_room4():
        print("As you enter the next room, you see two pound coins on the table.")
        examine_coins = input("Do you wish to examine them? (Y/N): ").lower()

        if examine_coins == "y":
            print("Upon examination, both coins look very similar but have different dates.")
        else:
            print("What are you going to do? Sit there for three days until you die of dehydration?")

        riddle_notice = input("You then notice a riddle written on the table. Are 1999 pound coins more valuable than 1993 pound coins? (Y/N): ").lower()

        if riddle_notice == "y":
            print("Move on to the next room.")
            future_room5()
        else:
            print("Looks like you're going to be here for a while.")
            future_room4()
### ^^ mark

    def future_room5():
        print('You are greeted with a screen that says, oe question to go')

        print('I am the beginning of the end and the end of time and space. I am essential to creation, and I surround every place. What am I?')
### reuben^^^
    

        answer=input('What is your answer')
        if answer == "e":
            print('You completed the escape room.')
            future_escape()
        else:
            print("you failed to understand the riddle, because of this you are sucked out into the vaccuum of space never to be seen again.")
            game_over()

    future_room1()
    future_room2()
    future_room3()
    future_room4()
    future_room5()

    





def start():
    Name = input("please enter your name").lower()
    global rusty_key
    global future_key
    rusty_key = 0
    future_key = 0
    while True:
        start = input(f"Hello {Name}, in front of you are two keys, one of them is rusty and the other is new, which key do you want to pick up")
        if start == "rusty" and rusty_key == 0:
            rusty_key += 1
            print("You picked up the rusty key.")
        elif start == "rusty" and rusty_key == 1:
            print("You already picked up this key.")
        elif start == "new" and future_key == 0:
            future_key += 1
            print("You picked up the future key.")
        elif start == "new" and future_key == 1:
            print("You already picked up this key.")
        else:
            print("I don't know what you mean.")

        if rusty_key == 1 and future_key == 1:
            door_choice = input("you notice that two doors reveal themself, which one do you wanter to enter? the rusty door or the door of light")
            if door_choice == "rusty":
                rusty_main()
            if door_choice == "light":
                future_main(Name)


start()