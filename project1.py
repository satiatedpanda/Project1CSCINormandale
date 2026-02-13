import random
import collections
import math
import tkinter
from time import sleep

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

#person1Questions = {"question": [["answer1", score, otherFriendEffects, checkpoint1], ["answer2", score2, otherFriendEffects2, checkpoint2] ["answers3", score3, otherFriendEffects3, checkpoint3]] <- example 
person1 = {} #food guy
person1keys = list(person1.keys()) # this is for the quesiton indexes. This is so the questions and answers dont get mixed up

person2 = {} #bully
person2keys = list(person2.keys())

person3 = {} #meek
person3keys = list(person3.keys())

#how to call
# person1[person1keys[0]][2][1]  =  #question=idx (does not get the question itself) > answer#=idx > score=1,answerstr=0
# person1keys[0] = #how to get the question itself

MainScore = [] #idx+1 equals person number. will be in form [pers1, pers2,...,persX]
scorecard = []

#variables (should be worked on to make these inside functions, not global)
player_name = ""
startval = 1 #this changes the starting number in MainScore 



#helper functions
def ScoreAnswer(answer, score):
    result = 0
    result += sum(scorecard) #add scores to get result
    if result > 15: #placeholder value is 15 - median
        MainScore.append(result) #this will cause errors, ill discuss this tommorow
    else:
        pass
    return(result)
 
def NextQuestion(score, questionNum):
    question = ""
    answers = []
 #   scorecard.append(answers(input()))
    return(question, answers)

def friendsCnt(numpep, startvalue):
    startloop = "apples"
    while True: #asks for input to do tutorial or not
        try: #this is for input validation
            if startloop == "apples":
                print("Default is set to 2 people. Difficulty scales on number of people. 1= Easy, 2= Medium, 3= Hard")
                numpep = int(input(f"Enter number of friends: 1,2 or 3. Current value is: {numpep}\n-> ")) #sets number of people for game
                startloop = "pears" #first loop check, this will make it not happen again
            else:
                numpep = int(input("-> "))                
            peoplelist = [1,2,3] #only things that will be accepted
            if numpep not in peoplelist:
                raise ValueError
            break
        except ValueError:
            print("Invalid input, please type exactly \"1\", \"2\", or \"3\"")
    for idx in range(numpep):
        MainScore.append(startvalue)
    return numpep

def nameSet(person_name):
    while True:
        try:
            person_name = input("What should we call you?\n-> ")     
            if len(person_name) != 0:          
                print(f"That's a good name, {person_name}! Your friends will remember it!")
                break
            else:
                raise ValueError
        except ValueError:
            print("Name cannot be empty. Try again")
    return person_name

def VictoryConditions(score):
    Endgametype = 0
    #victory condition '1' is out of quesitons
    return Endgametype

def ChoiceInput(answerlistlen):
    while True:
        try:
            if answerlistlen == 0:
                #work on this later
            break    
            else:
                raise ValueError
        except ValueError:
            print("Name cannot be empty. Try again")
    return person_name    

def Updatelog():
    pass
    #next submission



#game functions
def StartGame():
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
    what you’ve gotta do."""


    print(Intro_text)
    while True: #asks for input to do tutorial or not
        try: #this is for input validation
            tutorialY = input("""                                   1) View Tutorial?
                                   2) Answer the call\n-> """)
            corlist = ["1", "2"]
            if tutorialY not in corlist:
                raise ValueError
            if "1" in tutorialY:
                Tutorial()
            break
        except ValueError:
            print("Invalid input, please type exactly \"1\" or \"2\"")
    MainGame() #this goes into the main game
        #block was found in stackoverflow: https://stackoverflow.com/questions/41832613/python-input-validation-how-to-limit-user-input-to-a-specific-range-of-integers

def Tutorial():
    Tut_text = """
    Welcome to Stay Home Moon! You’ve found yourself in a bit of a spot,\n 
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

def MainGame():
    numquestions = len(person1keys) + len(person2keys) + len(person3keys)
    score = 0
    questionnumber = 0
    VictoryCond = 0
    while VictoryCond == 0: #main loop for the game
        if numquestions == 0:
            VictoryCond = 1 
            break       
        curquestion, curanswers = NextQuestion(score, questionnumber)
        print(f"{curquestion}\n")
        for i in range(len(curanswers)):
            print(curanswers[i])
        print()
        choice = ChoiceInput(len(curanswers))
        CurAnswScore = ScoreAnswer(choice, curanswers[choice-1])
        score += CurAnswScore
        questionnumber += 1
        numquestions -= 1
        VictoryCond = VictoryConditions(score)
    EndingGame(VictoryCond)




def EndingGame(victory):
    print("Game end\n...\n...\n...") #placeholder for checking if this will be called
    sleep(2)
    exitgame = input("Do you want to play again or exit? \"Y\" for yes, anything else for no\n-> ")
    if exitgame == "Y":
        print("Thank you for playing")
        exit()



def Menuscreen(player_name=player_name): #unsure about the function input, this could be wrong
    nonamechecknum = 2
    numofPeople = 2
    global startval #this is bad form, ill try to fix this later. This was just an easy fix
    
    Menu_text = """
                ┌── ⋆⋅☆⋅⋆ ──.·:*¨༺ ☾ ༻¨*:·.── ⋆⋅☆⋅⋆ ──┐


                            Stay Home Moon

                            Play
                            Set Name
                            Friends Count
                            Exit
                
                
                └── ⋆⋅☆⋅⋆ ──•,¸,.·'  '·.,¸,•── ⋆⋅☆⋅⋆ ──┘
        """
    #ascii pattern made from https://www.aestheticsymbols.me/dot.html
    print(Menu_text)
    while True:
        try: #this is for input validation

            menuinput = input("What do you want to do? Type \"Play\", \"Name\", \"Friends\", or \"Exit\"\n-> ").upper()
            inputcheck = ["PL", "NA", "FR", "EX"] #checking substrings for higher chance of getting right thing
            
            if any(substring in menuinput for substring in inputcheck) == False:
                raise ValueError
            if "PL" in menuinput: #play
                if len(player_name) == 0:
                    if nonamechecknum == 0: #this is a funny easteregg
                        print("Fine, name has been set to 'Billybob'. You win")
                        player_name = "Billybob"
                        sleep(2)
                        StartGame()
                    else:
                        print("Please set a name first")
                        nonamechecknum -= 1
                else:
                    StartGame()
            elif "NA" in menuinput:
                player_name = nameSet(player_name)
            elif "FR" in menuinput: #sets friends
                numofPeople = friendsCnt(numofPeople, startval)
            elif "EX" in menuinput: #exits program
                leaveY = input("Do you really want to leave? Type \"Y\" if you do, or anything else for no\n-> ")
                if leaveY == "Y":    
                    print("Thank you for playing")
                    exit()
            else: #this is for wrong inputs not caught
                print("how did you get here. bad !!@%$@#@#!!!$#@#@#@\n")
                raise KeyError
        except ValueError:
            print("Invalid input, please type one of the four options\n")    






if __name__ == '__main__':
    # Write all functions in here that will be called when running the program
    Menuscreen(player_name)