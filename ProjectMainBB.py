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
           "Dawn: And you thought I was just gonna let that go? C’mon, you know what I’m\nabout right? This is a no fly zone for BS {player_name} Are you gonna try to\npretend you have amnesia now?": 
           [["1) I have been feeling a bit forgetful lately.", 2], 
           ["2) There’s no forgetting an asshole like you.", 1], 
           ["3) No BS here, these ducks are neat and orderly in their rows.", 3]],
           "Dawn: Oh for the love of… Why do I hang out with you again?": 
           [["1) Your friend options are limited because you greet people by punching them?", 2], 
           ["2) I ask that same question every day.", 1], 
           ["3) Because I make the best damn enchiladas you’ve ever had.", 3]],
           "Dawn: That aside, since when do you skip out on free drinks and bad karaoke?\nDon’t give me any of that ‘I’m not feeling it’ crap. We both know that lie’s\nlike a cheap rug.": 
           [["1) I just don’t want to.", 1], 
           ["2) Stomach’s being weird, probably not good for drinking. It’ll lead to puking.", 2], 
           ["3) My karaoke is legendary, thank you.", 3]],
           "Dawn: So I’m just gonna tell you what I think. I think you're actively\navoiding us. You blew Cameron off twice in the past month.": 
           [["1) Hey, woah! Let’s back pedal a bit here, I am not avoiding anyone.", 3], 
           ["2) Alright maybe I did dodge a few hang outs, but you’re reaching pretty far \nhere.", 2], 
           ["3) It’s Sock. He’s just so… Wimpy.", 1]],
           "Dawn: You also seem to  find every excuse under the sun not to hang out\nwith Sock.": 
           [["1) What did I just say? Are you hard of hearing or something?", 1], 
           ["2) It's not that I don't want to hang out with Sock...", 2], 
           ["3) Yeah, and?", 3]],
           "Dawn: And let’s be very clear, only I am allowed to make fun of sad Sock.\nGot it?":
           [["1) Whatever.", 1], 
           ["2) Got it.", 2], 
           ["3) Okay buddy...", 3]],
           "Dawn: You get that privilege when you spend the better part of your last two\nyears of high school pulling straws out of his hair and un-gumming his locker.": 
           [["1) Well aren't you just a saint.", score], 
           ["2) I feel like you also are one of the causes of the gum on his \n    locker.", score2], 
           ["3) That's... surprisingly nice of you. Ya'll go that far back?", score3]],
           "Dawn: If you come to the party you’ll get to hear all about the ancient\nhistory. I’ve got tons of stories about what those two chuckle heads got up\nto. No spoilers, that’s a live event or you wait for the day Cameron or Sock\nMAY tell you.": 
           [["1) Well... guess I gotta wait for one of them to spill the beans.", score], 
           ["2) Not even a little spoiler?", score2], 
           ["3) Oh no... anyway.", score3]],
           "Dawn: Seriously {player_name}, you’re telling me with all that, you’d still\nrather rot in that crap apartment watching shitty reruns than hang out with\nus at one of Johnny's parties?": 
           [["1) No, but I just need to stay home and decompress tonight.", score], 
           ["2) Absolutely.", score2], 
           ["3) It’s a toss up really, kind of worried about my… appetite.", score3]],
           "Dawn: Okay if I’m being for real though, I probably would ditch to if it\nwere to re-watch the last season of 12 Desperate Women and 1 Paid Actor.\nI’m more than certain at least one of those women were also paid actors.": 
           [["1) I. am. shocked.", score], 
           ["2) Nah, no way dude.", score2], 
           ["3) I really don't care.", score3]],
           "Dawn: Pretty sure it was the one with the high cheekbones, sharp jawline, and\ntiny nose. Not that first one that everyone thinks of, the other one.": 
           [["1) That's so specific.", score], 
           ["2) I really really don't care.", score2], 
           ["3) Rebecca? No... Tammy?", score3]],
           "Dawn: I know none of it’s real. I'm not a god damn moron. It’s fun to pick at\nbecause it’s so glaringly fake. Like eating chicken nuggets from Clown Burger.": 
           [["1) That's a weird connection between those two things.", score], 
           ["2) Ugh, now I really want chicken nuggets. Damnit, Dawn.", score2], 
           ["3) At least you're not delusional.", score3]],
           "Dawn: Okaaaaay, trash tv aside. You do need to make some kind of effort here\nto hang out with us.": 
           [["1) I mean I really want to, but just not tonight.", score], 
           ["2) Thank god, you're done going on and on about that.", score2], 
           ["3) I do make the effort!", score3]],
           "Dawn: Pretty sure the last time you hung out with all of us was at the beginning\nof the month. We all tried making breakfast with Cameron’s grandma’s prehistoric\nwaffle pan and it almost burned a hole in the counter.": 
           [["1) That only happened because Cameron’s an idiot.", score], 
           ["2) Y’know, I think waffles are an acceptable reason to cause a house fire.", score2], 
           ["3) That wasn’t our best idea.", score3]], #intended answer weights: 1 = high impact, 2 = light, 3 = medium
           "Dawn: I’ve got half a mind to come down there and drag you out myself. How\nmuch do you weigh again? Nevermind, the exact number doesn’t matter, I’m\npretty sure I can deadlift your ass.": 
           [["1) NO! THAT IS FORBIDDEN! NO LIFTING OF THE ME!", score], 
           ["2) That’s a lot of effort for you to waste on my feeble, pathetic ass.",score2], 
           ["3) Wow.", score3]],
           "Dawn: Actually I’m certain I can. I’m up to 1.5x my own body weight. My new\nmetric is gonna be in how many {player_name}’s I can lift.": 
           [["1) That'd be kind of rad actually.", score], 
           ["2) This is dumb. Why are you dumb?", score2], 
           ["3) No. Absolutely not. Don't ever. Bad!", score3]],
           "Dawn: Then you’re going to show up to prevent that very real possibility?\nCan't do much else to prevent the darkest timeline.": 
           [["1) I can hang up.", score], 
           ["2) What if... we just didn't do that? Eh???", score2], 
           ["3) COME AT ME YOU COWARD!", score3]],
           "Dawn: Okay, I’ve got better. If threatening to chuck your ass like the\nuseless boulder you are doesn't work, then think of all the drunken\ndumbassery that you’re gonna miss out on! ...Not that I keep receipts of this\nstuff or anything.": 
           [["1) We both know that’s a lie. I don't even want to know how many lives\n   you've ruined.", score], 
           ["2) Riiiiiight.", score2], 
           ["3) That's just... kind of awful.", score3]],
           "Dawn: Oh come on. What else keeps people in check other than the irrational\nfear that a stranger might think what they’re currently doing is really\nembarrassing? It makes for great currency.": 
           [["1) Now I am more than certain you run a blackmail ring.", score], 
           ["2) That’s a red flag in a pile of red flags.", score2], 
           ["3) Ugh… getting uncomfortable.", score3]],
           "Dawn: Now you sound like sad Sock, ‘D-dawn that’s mu-mu-mu-mean!’ I can’t\ncarry two perpetual whiners, you need to pick a different role.": 
           [["1) How about the guy that stays home from parties?", score], 
           ["2) Maybe I LIKE being a giant crybaby!", score2], 
           ["3) Or you could stop being such a jerk for five whole minutes?", score3]],
           "Dawn: This again? Shelve it. It’s kind of pathetic.": 
           [["1) Not as pathetic as you.", score], 
           ["2) Alright fine, it’s shelved.", score2], 
           ["3) I’m forgetting what the purpose of this conversation was.", score3]],
           "Dawn: Yucks aside, whole point of this song and dance: You. Party. Tonight\nNon-negotiable. I’m getting tired of repeating the same thing. When is it\ngetting into your thick skull that you’re going to the party?": 
           [["1) I’m. Busy. Tonight. Non-negotiable.", score], 
           ["2) I really can’t Dawn, I’ll try to make it up to you guys another time.", score2], 
           ["3) I just want to watch bad movies by myself and sleep, is that a crime?", score3]],
           "Dawn: Alright, you’ve forced my hand. I’m calling in the big guns. There’s\nno point in trying to stop me. It’s happening.": 
           [["1) What are you doing?", score], 
           ["2) I swear if you show up at my house to try to lift me...", score2], 
           ["3) Dawn, please...", score3]],
           "Dawn: I’m messaging Sock and telling him you’re trying to flake on us. You\nleft me no choice.": 
           [["1) Ugh... why???", score], 
           ["2) You absolute horse's ass! Stop it!", score2], 
           ["3) I mean... oh no?", score3]],
           "Dawn: Aaaaaaand done. Get ready for that because it’s going to be waaaaay\nworse than talking to me or Cameron was.": 
           [["1) You suck.", score], 
           ["2) Thanks... really.", score2], 
           ["3) Okay, that's gonna be a time.", score3]],
           "Dawn: I tried to give you an out. Now you get to explain it to King\nWaterworks why one of his security buddies is going to be MIA.": 
           [["1) AAAAAAAAAAAAAAAAAA-", score], 
           ["2) Yep, now I get to do that. Again, thanks.", score2], 
           ["3) I'm genuinely questioning the basis of our friendship right now.", score3]],
           "Dawn: Is it so hard to believe we’re all doing this because we haven’t seen\nyou in a while and want to hang out with you, {player_name}?": 
           [["1) You have a REALLY funny way of showing THAT.", score], 
           ["2) I think you enjoy being as annoying as possible.", score2], 
           ["3) I mean... kind of with how you've gone about this?", score3]],
           "Dawn: That is the closest you are going to get to me saying anything of that\nsort. I don’t do mush.": 
           [["1) I don't think that can count as \'mush\'.", score], 
           ["2) I guess that was... an attempt made.", score2], 
           ["3) We're aware.", score3]],
           "Dawn: Alright, I’m already regretting trying to appeal to pathos. Retracting\nall sentimentality. Just get your ass to the party.": 
           [["1) No.", score], 
           ["2) Sorry, Dawn. Maybe next time.", score2], 
           ["3) This has been utterly exhausting. I need a nap.", score3]],
           "ENDINGS DIALOGUE": 
           [["Dawn: Ugh, fine. Enjoy your night alone or whatever, but you’ve got to come\nout with us next week.", score], #Good ending
           ["Dawn: Y’know what? I don’t know why I’m trying so hard. This is just a giant\nwaste of time", score2], #Neutral/hates you ending
           ["Dawn: Okay, I hear what you’re saying but you’re acting really weird. I’m\ncoming to pick you up. Be ready at 9.", score3]]},
    #Dawn - bully
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

    
    ending1_text = """
                The full moon rises but the evening remains calm. 

    Your friends are blissfully unaware of the transformation occurring in your
    solitary apartment. The group chat is filling with messages. Pictures and 
    videos of varying clarity or what’s happening at the party. It seems this 
    is how they’re trying to include you, and maybe convince you to come to the
    next one.

    Cameron’s sending pictures of everyone having a good time. You can see Dawn
    standing by while Sock tries to talk to Johnny’s randos. From the still 
    shots it looks like their actually doing pretty well, even if they look 
    like they want to throw up. 

    Dawn of course is sending snippets of people doing dumb things. You’re not 
    surprised in the slightest. There’s clips of Cameron singing Bowie Mercury 
    and it’s a time.

    You don’t get a single SOS message from Sock. They’ve been sending pictures 
    of Johnny’s new cat, apparently named Felicity. For a horrible, free loading 
    furball, she’s actually just a little cute.

    You’re gonna have a lot of catching up to do with them tomorrow.

                                You Win!
                                """
    
    ending2_text = f"""
                Your friends couldn’t be convinced to stay away. 

                            Do you know what that means? 

             That means they’re coming to your house {player_name}. 

                    You failed them in the worst possible way.

    The night of the full moon and subsequently Johnny’s party arrives. 
    Your transformation was interrupted by a knock on the door. It opens and
    concerned gazes of the people you care about witness you hunched over and 
    writhing. They hear your bones snap as they reshape and you are molded into
    a monster.

    Maybe it’s for the best you don’t exactly remember what happened next. 
    You’ll never forget the sight of the remains you left behind though.

    You couldn’t stomach hiding them away like so many other unfortunate 
    bystanders before. You run, leaving this version of your life behind.

                                    Bad End
                                    """
    
    ending3_text = """
       The night of the full moon comes and goes without incident.

               
       The sun rises to a slightly disheveled apartment, but a quick tidy and 
       nothing out of the ordinary appears to have occurred.

       There’s no messages on your phone. No one has checked in on you since 
       yesterday and the group chat is weirdly silent. 

       You may have lost all of your friends, but at least they’re alive! You 
       didn’t just eat a bunch of innocent people! So you stand in your newly 
       re-organized apartment and cling to that small victory. 

       You can’t help but feel a little lonely though…

       
                                       Bad End?
                                """

    if victory == 1:
        print(ending1_text)
        sleep(2) #1.2 conditions, flawless victory- all alive, all positive
    elif victory == 2:
        print(ending2_text)
        sleep(2) #2 conditions- all eaten
    elif victory == 3:
        print(ending3_text)
        sleep(2) #3 conditions- all negative
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
