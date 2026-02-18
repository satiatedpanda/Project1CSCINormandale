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

startval = 1 #this changes the starting number in MainScore. This is for us to tinker with to adjust difficulty/game length

#person1Questions = {"question": [["answer1", score, checkpoint1, 'otherFriendEffects'], ["answer2", score2, checkpoint2, 'otherFriendEffects2'] ["answers3", score3, checkpoint3, 'otherFriendEffects3']] <- example 
person1 = {} #Cameron - av Joe
person1keys = list(person1.keys()) # this is for the quesiton indexes. This is so the questions and answers dont get mixed up

#DONT convert questions into an f-string. We format the name into it later.
person2 = {"Dawn: {player_name}, I got a funny text from Cameron. He said you’re not\n going to the party tonight. I told him that was a pretty good joke but he\n says he’s serious, so how about you set the record straight for the both of us.": 
           [["1) Ugh… He’s right?", 3], 
            ["2) Okay first, you’re at an 11 when this should be a 4 conversation, and\n   second, yeah I’m staying in tonight.", 2], 
            ["3) I’m just not really feeling it tonight.", 1]], 
            "Dawn: Pretty sure the last time you hung out with all of us was at the beginning\nof the month. We all tried making breakfast with Cameron’s grandma’s prehistoric\nwaffle pan and it almost burned a hole in the counter.": 
            [["1) That only happened because Cameron’s an idiot.", 2], 
             ["2) Y’know, I think waffles are an acceptable reason to cause a house \"fire.\"", 1], 
             ["3) That wasn’t our best idea.", 3]]
             } #meek
    #intended answer weights: 1 = high impact, 2 = light, 3 = medium
person2keys = list(person2.keys())
person2questions = {"Phone Rings": [["What's Up", 2], ["Hello?", 2]], 
                    "Are you coming to Johnny's party tonight": [["Yes", 1000], ["Probably not", 2], ["Fuck no", 1]], #I put 1000 as the score for "yes" because it ends the game, change it to whatever you want 
                    "C'mon dude, It would be so fun": [["I have a stomach ache", 2], ["You think I can't entertain myself? I'm not your circus monkey", 1]],
                    "{player_name}, that is sooooooo lame, just come over": [["Please no, any more pointless conversation is going to send me over the edge of insanity", 2], ["Wow, I didn't know my personal calendar needed your approval. Again, no.", 3]],
                    "Wow, such big words. You can use plenty of those at the party tonight if you come. All of your friends are here. Just stay for like 30 minutes and then you can leave": [["Absolutely not, Especially if Don is there. He's been getting on my nerves recently", 1],["Again, dicating my already made schedule. Not cool, man", 3], ["I'm sorry, I just can't go. I have a frozen pizza in the oven that is calling my name", 2]], 
                    "You woke up on the wrong side of the bed, didn't you? This is your last chance to accept my invite to the party.": [["Yes, I am sure", 2], ["Dude, stop asking, You know the answer", 3], ["Just hang up already", 1]], #this one and the one below it have the same answers because they are mean't for different responses to the question above 
                    "Just throw it back into the freezer and come to the party. Are you really sure you dont want to go?": [["Yes, I am sure", 2], ["Dude, stop asking, You know the answer", 3], ["Just hang up already", 1]], #this is for the response: "I'm sorry, I just can't go. I have a frozen pizza in the oven that is calling my name"
                    "Ok, fine. just don't blame me if you feel bad for not going later": [["I'll go next time you call for sure", 2], ["Don't worry, I won't", 3], ["Piss off", 1]], 
                    }

#Below are the three possible opinion messages at the end of the call. 

#print("He will probably not ask you to any more parties")
#print("he is bummed you aren't going to the party but will definitely invite you to the next one")
#print("He will probably invite you to another party in the future")

person3 = {} #Sock - meek
person3keys = list(person3.keys())

#how to call
# person1[person1keys[0]][2][1]  =  #question=idx (does not get the question itself) > answer#=idx > score=1,answerstr=0
# person1keys[0] = #how to get the question itself

MainScore = [] #idx+1 equals person number. will be in form [pers1, pers2,...,persX]
scorecard = []




#helper functions
def ScoreAnswer(answer, score):
    result = 0
    result += sum(scorecard) #add scores to get result
    if result > 15: #placeholder value is 15 - median
        pass
    else:
        pass
    return(result)
 
def NextQuestion(score, questionNum):
    question = ""
    answers = []
    question = question + str(person2keys[questionNum]) #temporarry
    answers = person2[person2keys[questionNum]] #temporary


    return(question, answers)

def friendsCnt(numpep, startvalue):
    startloop = "apples"
    while True: #asks for input to do tutorial or not
        try: #this is for input validation
            if startloop == "apples":
                print("Default is set to 2 people. Difficulty scales on number of people. 1= Easy, 2= Medium, 3= Hard")
                numpep = int(input(f"Enter number of friends: 1,2 or 3. Current value is: {numpep}\n->")) #sets number of people for game
                startloop = "pears" #first loop check, this will make it not happen again
            else:
                numpep = int(input("-> "))                
            peoplelist = [1,2,3]
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
    #victory conditions are in the docstring for endinggame()
    #scores larger than 100 are victory conditions
    return Endgametype

def Updatelog():
    pass
    #next submission



#game functions
def StartGame(name):
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
    this time you’re going by {name}.

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
    MainGame(name) #this goes into the main game
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

def MainGame(name):
    numquestions = len(person1keys) + len(person2keys) + len(person3keys)
    score = 0
    questionnumber = 0
    VictoryCond = 0
    player_name = name
    bugcondition = 0 #for exiting loop if got stuck
    while VictoryCond == 0: #main loop for the game
        bugcondition += 1
        if numquestions == 0:
            VictoryCond = 1
            break
        anslenlist = []
        anslenstr = ""
        curquestion, curanswers = NextQuestion(score, questionnumber)
        curquestion = curquestion.format(player_name = player_name)
        print(f"{curquestion}\n")
        for i in range(len(curanswers)):
            print(curanswers[i][0])
            anslenlist.append(i+1)
        for i in range(len(anslenlist)):
            anslenstr = anslenstr + str(anslenlist[i]) + ", "
        anslenstr = anslenstr[:-3] + f"or {anslenlist[-1]}"
        while True:
            try: #this is for input validation
                choice = input(f"Pick Answers {anslenstr} by typing that number (ex to exit if stuck)\n-> ")
                if choice.isdigit() == True:
                    choice = int(choice)
                    if choice not in anslenlist:
                        raise ValueError
                    break
                else:
                    if "ex" in choice.lower():
                        print("exiting game ... ")
                        exit()
                    raise ValueError
            except ValueError:
                print("Invalid input, please type exactly one of the numbers shown")
            print()

        CurAnswScore = ScoreAnswer(choice, curanswers[choice-1])
        score += CurAnswScore
        questionnumber += 1
        numquestions -= 1 #this prevents endless loops
        if bugcondition > 500:
            print("bugged code, exiting function ....")
            exit()
        VictoryCond = VictoryConditions(score)            
        
    EndingGame(VictoryCond)
    

def EndingGame(victory):
    """
    victory condition 0: not possible, 0 means game is running

    victory condition 1: out of questions. This is good, and can lead into winning flawlessly
        victory condition 1.2: Flawless victory, all friends dont come and dont hate you
        victory condition 1.3: Atleast 1 friend died
        victory condition 1.4: All survived, but at least 1 hates you 
    victory condition 2: All eaten - all friends get eaten
    victory condition 3: All hate you - all friends hate you


    specicial conditions
        these are to figure out later, and will depend on special peramaters like certain answers chosen
        these will start at 100


    """
    if victory == 1:
        print("\nran out of questions")
        sleep(2)
    elif victory == 2:
        pass
    elif victory == 3:
        pass
    else:
        print("unknown ending...\n...\n..")
        print("bugged code srry")

    print("Game end\n...\n...\n...") #placeholder for checking if this will be called
    sleep(2)
    exitgame = input("Do you want to play again or exit? \"Y\" for yes, anything else for no\n-> ")
    if exitgame != "Y":
        print("Thank you for playing")
        exit()



def Menuscreen(): #unsure about the function input, this could be wrong
    player_name = ""
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
                        StartGame(player_name)
                    else:
                        print("Please set a name first")
                        nonamechecknum -= 1
                else:
                    StartGame(player_name)
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
        except KeyError:
            exit()






if __name__ == '__main__':
    # Write all functions in here that will be called when running the program

    Menuscreen()
