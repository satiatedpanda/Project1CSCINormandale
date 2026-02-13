import random
import collections
import math
import tkinter

"""
Docstring for project 1
"""



"""
personality types


person x: food obscessed, sarcastic, manipulative, peer-
person y: bully, abrasive
person z: meek, needy lil' guy, 


30 distinct ones, 5-10 variable standard


"""

#global variables

#person1Questions = {"question":str : [["answer1": str, score: int/float], ["answer2", score2] ["answers3", score3]] <- example 
person1 = {} #food guy
person1keys = list(person1.keys) # this is for the quesiton indexes. This is so the questions and answers dont get mixed up

person2 = {} #bully
person2keys = list(person2.keys)

person3 = {} #meek
person3keys = list(person3.keys)
numquestions = len(person1keys) + len(person2keys) + len(person3keys)
#how to call
# person1[person1keys[0]][2][1]  =  #question=idx (does not get the question itself) > answer#=idx > score=1,answerstr=0
# person1keys[0] = #how to get the question itself

MainScore = [] #idx+1 equals person number
numofPeople = int(0)
startval = 1 #this changes the starting number in MainScore 

#functions
def ScoreAnswer(score):
    result = -1



    #MainScore[idx] = int(MainScore * 0.75)
    return(result)
    #



def NextQuestion(score, questionNum):
    question = ""
    answers = []
    return(question, answers)




def EndingGame():
    pass

def StartGame():
    print("   ---\nGame Setup\n   ---\n")
    numpeople = int(input("number of friends: 1,2 or 3\n")) #sets number of people for game
    numofPeople = numpeople 
    for i in range(numofPeople):
        MainScore.append(int(startval))
    while True: #asks for input to do tutorial or not
        try:
            tutorialY = input("Do Tutorial? Y/n\n")
            corlist = ["Y", "n"]
            if tutorialY not in corlist:
                raise ValueError
            if tutorialY == "Y":
                Tutorial()
            break
        except ValueError:
            print("Invalid input, please type exactly \"Y\" or \"n\"\n")
        #block was found in stackoverflow: https://stackoverflow.com/questions/41832613/python-input-validation-how-to-limit-user-input-to-a-specific-range-of-integers
        



def Tutorial():
    Tut_text = """
    Welcome to Stay Home Moon! You’ve found yourself in a bit of a spot, 
    haven’t you? The goal of the game is pretty simple: Don’t Eat Your Friends.

    You will have to navigate a series of phone calls with your friends. 
    You’ll be presented with a series of responses that will shape how your 
    friend reacts to the conversation. You will select your response by typing 
    the correlating number into the command line. There are three things to 
    remember when selecting a response:

    -Your words have weight.
    -Some of your options will have a greater impact than others.
    -The ultimate goal is to not eat your friends, but try not to completely 
     ruin your relationships.

    You should really pick up that phone now, Cameron’s waiting, good luck!"""
    print(Tut_text)


def Intro():
    Intro_text = f"""
    Turns out being a werewolf isn’t what fantasy novels chock it up to be, at 
    least not a modern werewolf anyway. There’s no running through the woods 
    and ‘unleashing your inner wolf’ or any of that nonsense depicted in books 
    with scandalous oil paintings for covers. It’s still just like being any 
    other person that has to make it day to day…. except with the ‘fun’ 
    challenge of turning into a murderous beast once a month. You’ve had to 
    learn first hand the issues that come with that ranging from copious 
    amounts of shedding that your vacuum never seems to fully clean up, to the 
    bloody messes that you need to discreetly clean up when you can’t keep 
    yourself locked up during those pesky full moons. It really is a pain to 
    have to change your name and abandon your entire life every time just one 
    teensy little security measure just doesn’t hold up. 

    It’s been a couple months since the last time you’ve had to jump ship, and 
    this time you’re going by {player_name}.

    You’ve managed to settle in quite nicely. You’ve scored a great job and 
    managed to land a spot in a semi-stable group of friends. You’ve finally 
    found the best way to keep from going on a bloodthirsty rampage during the 
    full moons. Thanks to your new iron clad security, courtesy of ‘Trademarked 
    Hardware and Home Improvement’ store, there’s absolutely no way you’re 
    busting through those locks! So now it’s just you, a movie that you 
    probably won’t finish due to your impending transformation, and a supply 
    of tranquilizer laced meat in the fridge all settled in for a completely 
    uneventful evening.

                            So why is your phone ringing? 

    Looking at the number on display, you see Cameron’s name popping up. Before
    you can think to answer it all rushes in: the party and the plans you made 
    with each of your friends. That was tonight! You scheduled that all on the 
    night of the full moon like some giant idiot!

    You’re gonna have to cancel all of your plans and you just know your 
    friends aren’t going to make that easy. The alternative however is 
    potentially eating them at worst, possibly only mauling them at best. It’s
    what you’ve gotta do.


                                    1) View Tutorial?
                                    2) Answer the call"""
    
    input(Intro_text)
    response = input()
    if response == "1" or "1)":
        Tutorial()
    else:
        #continue

#ascii pattern made from https://www.aestheticsymbols.me/dot.html
def Menuscreen():
    Menu_text = """
                ┌── ⋆⋅☆⋅⋆ ──.·:*¨༺ ☾ ༻¨*:·.── ⋆⋅☆⋅⋆ ──┐


                            Stay Home Moon

                            Play
                            Set Name
                            Friends Count
                            Exit
                
                
                └── ⋆⋅☆⋅⋆ ──•,¸,.·'  '·.,¸,•── ⋆⋅☆⋅⋆ ──┘
        """
    input(Menu_text)
    while response != "exit":
        response = input()
        if response == "name" or "set name":
            name = input("What should we call you?")
            print(f"That's a good name, {name}! Your friends will remember it!")
        
        elif response == "Friends Count"
            numfriends = input("How many friends would you like to talk to?")
            #mechanism for making this work too tired to hash it now

        elif response == "Play"
            StartGame()
        
        else:
            break #exit the program?


def Updatelog():
    pass
    #next submission



def MainFun():
    StartGame()
    while numquestions > 0: #main loop for the game
        curquestion, curanswers = NextQuestion()
        print(f"{curquestion}\n")
        for i in range(len(curanswers)):
            print(curanswers[i])
        print()
        








if __name__ == '__main__':
    # Write all functions in here that will be called when running the program
    MainFun()