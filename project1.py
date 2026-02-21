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
person1 = {f"Hey {player_name}, it's Cam again. Just leaving you a mess-wait a minute... Holy hell, you picked up!": 
                    [["1) Wow, I know, right? Mark the calendar - this is a historic moment. \n I figured I'd keep you on your toes this time", 0],
                     ["2) Obviously, you're one of my best friends", 0],
                     ["3) Suprise. I thought i'd save you the trouble fo finishing that voicemail. What's up?", 0]],
                     "Dude! It's been like... I don't even know actually when the last time we talked was.": 
                     [["1) It has been a while, I do miss our catch-ups.", 0],
                      ["2) It hasn't been that long, has it.", 0],
                      ["Yeah, I was starting to think you joined witness protection or something.", 0]], 
                      "Where have you been? Lemme guess, you also got your life eaten by that really extensive story driven fantasy game that came out a while back?": 
                      [["1) Maybe. but I regret nothing.", 0], 
                       ["2) I plead the fifth. That game had me hooked.", 0],
                       ["3) List... side quests dont't finish themselves, okay?", 0]], 
                       "Ha, nice. I wish I had time for video games. I've had to set it down because work ramped up again.": 
                       [["1) Work really said 'no fun allowed', huh?", 0],
                        ["2) Respect the grind. still, that hurts", 0],
                        ["3) We'll save a quest for when you're free", 0]],
                        "Preparing for the seasonal crap six months ahead of time. I’m already tired of hearing about the holidays. Remember enjoying the holidays?": 
                        [["1) Since 9 to 5's came into play, that is a thing of the past", 0],
                         ["2) It sucks now but makes the holiday's that much better", 0],
                         ["3) I don't know if you need to prepare this early but to each their own", 0]],
                         "You’re still coming to Johnny’s party tonight right? You know it’s gonna be good. The guy always says he’s got a few things and then BOOM, whole fricken buffet of stuff you’ve never even heard of. Some of it you never wanted to hear of.": 
                        [["1) I love his mashed potatoes", 0],
                         ["2) The food is okay, some of his choices are questionable at best", 0],
                         ["3) It's very hit or miss for me", 0]],
                         "Hazelnut spread, banana pizza was a bit weird. I think it would’ve been better with cheese…": 
                        [["1) I missed that one, it sounds like a recipe for stomach sadness", 0],
                         ["2) Hate it say it but I think that might hit on the right night", 0],
                         ["3) I always wonder what is going on in his head when he chooses these things", 0]],
                         "Johnny’s got weird taste but I don’t think he’s a bad guy. Don’t be surprised if you hear from him too.": 
                        [["1) Noted", 0],
                         ["2) I'll have my notecards ready", 0],
                         ["3) I don't know if I'm in the right mood to talk to him but I think I can manage", 0]],
                         "He also got a new cat. Have you seen the pictures in the group chat?": 
                        [["1) Well, I'm not too fond of cats", 0],
                         ["2) I put my phone on Do Not Disturb after the 3rd photo", 0],
                         ["3) I guess I'm happy for him... from a distance", 0]],
                         "Wait, you seriously don’t like cats? That’s messed up man.": 
                        [["1) It's not personal, I would just prefer I leave my feet unattacked", 0],
                         ["2) Hey, I'm not heartless. I just respect them from a safe distance", 0],
                         ["3) listen, someone has to say it", 0]],
                         "Well… we’re gonna have some movies on! He’s got a poll going in the group chat for what we watch.": 
                        [["1) Please tell me it's not a three hour mood film like last time.", 0],
                         ["2) Sounds fun. I've got a super fun night planned, though.", 0],
                         ["3) The groups movie choice are always so good.", 0]],
                         "First spot is at a tie between two old horror movies.": 
                        [["1) You know I love that!", 0],
                         ["2) Sounds spooky", 0],
                         ["3) My favorites", 0]],
                         "There’s a slasher flick and a werewolf movie.": 
                        [["1) Are we talking about modern horrors or classic horrors", 0],
                         ["2) That's what I'm talking about!", 0],
                         ["3) Again? We saw you of those like a week ago", 0]],
                         "Obviously ‘Guy With Knife III’ is the correct choice.": 
                        [["1) Of Course", 0],
                         ["2) Finally, someone with taste.", 0],
                         ["3) How did the other movies even stand a chance with that on the roster.", 0]],
                         "Who’s gonna pick a movie about some overgrown pooch when you’ve got the *classic* horror movie set up that is stupid teenagers get got?": 
                        [["1) Yeah, werewolves are so much cooler.", 0],
                         ["2) Werewolfs and slashers, name a better combination", 0],
                         ["3) You can't compare the folklore of werewolfs and the stupidness of teenagers.", 0]],
                         "Nah dude, werewolves are lame.": 
                        [["1) Sounds like someone who wouldn't survive a full moon", 0],
                         ["2) They are moon powered shapeshifters and you consider them lame?", 0],
                         ["3) You are definitely entitled to your opinion, but it is wrong unfortunatly.", 0]],
                         "Kinda sad about Sock’s recommendation. They were the only one who voted for ‘The Night is Short, Walk on Girl’. I just don’t think anyone is gonna be up for reading subtitles.": 
                        [["1) No one is gonna know what that is", 0],
                         ["2) It is a good movie, maybe not for most though", 0],
                         ["3) If we can deal with our group chat messages, we can read subtitles", 0]],
                         f"Oh, if movies don’t sell it, there’s also gonna be Karaoke! Everyone should be drunk so no one will care how bad you sound {player_name}.": 
                        [["1) My karaoke is legendary!", 0],
                         ["2) Great, if everyone is drunk, I'll sound like Aretha Franklin", 0],
                         ["3) Na, I'd get so embarrassed", 0]],
                         "Nah see the way you get ahead of that is to go all in on the most ridiculous pop song ever. Just give the most hammered performance of your life.": 
                        [["1) This is just know I get immortalized for that thing", 0],
                         ["2) I get what you are aluding to: Weaponized cringe", 0],
                         ["3) I just don't know, I get nervous about that sort of stuff", 0]],
                         "Oh y’know what I was just thinking about? We never finished that board game from last time.": 
                        [["1) It's funny how you remembered you were losing", 0],
                         ["2) Aren't some things better left unfinished?", 0],
                         ["3) Let's be real, I'm gonna win no matter what.", 0]],
                         "No, not that one. The one where you build the house and then someone is a traitor.": 
                        [["1) Good luck, I've been thinking about that one all week.", 0]
                         ["2) That game has been haunting me", 0],
                         ["3) I have a stomach ache, lets do that another time.", 0]],
                         "Pretty sure Dawn got pissy and scattered the pieces after taking a bunch of sanity damage like three times in a row during their turn and then they weren’t the traitor.": 
                        [["1) Shes always getting pissed about something", 0],
                         ["2) To be honest, that was a frustrating game, I don't blame them.", 0],
                         ["3) Well, I would've won that one too though.", 0]],
                         "It could be fun to try it again. We could also play something with a rule book that isn’t 45 pages long though.": 
                        [["1) finally - a game that doesn't require 30 minutes to explain the rules", 0],
                         ["2) Anything under 15 pages seems like a dream right now", 0],
                         ["3) That sounds nice", 0]],
                         "So, do you need me to pick you up?": 
                        [["1) Sure", 1000],
                         ["2) Actually, maybe not tonight, I want to get to bed early", 0],
                         ["3) Well, I have a stomach ache so maybe not tonight.", 0]],
                         "Come on dude, my car finally stopped making that sound!": 
                        [["1) I glad for that but I'm just not feeling it tonight.", 0],
                         ["2) That's not going to fix my stomach ache though", 0],
                         ["3) Finally, I thought that would go on forever", 0]],
                         "Well first I thought maybe a racoon or something got in there with the way the speakers were thumping around. Something about the cold and the wiring to the radio.": 
                        [["1) That makes sense, I know sometimes the cold can mess with the wiring", 0],
                         ["2) Maybe it was a raccon DJ that played the bass way too loud in that death trap.", 0],
                         ["3) That thing is a death trap.", 0]],
                         "I think it’s unfair to keep calling her a death trap. Her engine hadn’t started smoking in a good few months!": 
                        [["1) That car is a chaos magnet.", 0],
                         ["2) She sould keep an eye out; that car is out to get her", 0],
                         ["3) I don't know why she still drives that thing", 0]],
                         "Alright, alright. Enough of these lies and slander. Carlotta is a fantastic machine and she deserves the world.": 
                        [["1) I don't know about that.", 0],
                         ["2) She deserves to be in a junkyard.", 0],
                         ["3) She is more like a rolling paperweight than a car.", 0]],
                         "You’re seriously gonna miss out on the party tonight because of vague tummy troubles?": 
                        [["1) Yes, I'm sure", 0],
                         ["2) I don't want to throw up.", 0],
                         ["3) My stomach has it's own calendar and it's booked tonight.", 0]],
                         "I mean I can let everyone else know but they’re probably not gonna be happy about it…": 
                        [["1) Well, who cares what they think", 0],
                         ["2) It is what it is", 0],
                         ["3) Why would that matter", 0]],
}
 #Cameron - av Joe
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
