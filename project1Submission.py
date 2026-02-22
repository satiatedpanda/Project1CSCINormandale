from time import sleep
import random

"""
Docstring for project 1


Need to pip install pynput, pip install keyboard
"""



"""
personality types


person x: food obscessed, sarcastic, manipulative, peer-
person y: bully, abrasive
person z: meek, needy lil' guy, 


30 distinct ones, 5-10 variable standard
"""

#person1Questions = {"question": [["answer1", score], ["answer2", score2] ["answers3", score3]] <- example 
#intended answer weights: 1 = coming to house (-), 2 = no change (-+), 3 = hate you (+)
person1 = {"Cameron: Hey {player_name}, it’s Cam again. Just leaving you a mess-\nwait a minute… Holy hell, you picked up!": #Question-Answer dictionary
           [["1) Yeah... hey buddy!", 1], 
            ["2) I would've called back eventually.", 3], 
            ["3) I'm as shocked as you are if I'm being totally real right now.", 2]],
            "Cameron: Dude! It’s been like… I don’t even know actually when the last time\nwe talked was.": 
            [["1) Not that long I don't think.", 2], 
            ["2) Oh gee, I wonder why.", 3], 
            ["3) Yeah, it's been a hot minute.", 1]],
            "Cameron: Where have you been? Lemme guess, you also got your life eaten by\nthat really extensive story driven fantasy game that came out a while back?": 
            [["1) Are you saying a look like some kind of nerd?", 3], 
            ["2) ... yes. That is exactly what has been happening. Nothing else.", 2], 
            ["3) I mean... no?", 3]],
            "Cameron: Ugh... I wish I had time for games. I’ve had to set it down because\nwork ramped up again.": 
            [["1) Already?", 2], 
            ["2) I think I remember you talking about this.", 1], 
            ["3) Oh, wow, bummer.", 3]],
            "Cameron: We're preparing for the seasonal crap six months ahead of time. I’m\nalready tired of hearing about the holidays. Remember enjoying the holidays?": 
            [["1) Oh no... that's the worst.", 1], 
            ["2) Mmmhmmm.", 3], 
            ["3) It's not nearly that bad.", 1]],
            "Cameron: You’re still coming to Johnny’s party tonight right? You know it’s\ngonna be good. The guy always says he’s got a few things and then BOOM, whole\nfricken buffet of stuff you’ve never even heard of. Some of it you never\nwanted to hear of.": 
            [["1) Oh shoot... I forgot...", 3], 
            ["2) Nah, I'm going to skip it.", 3], 
            ["3) That sounds great but I'm thinking of staying home tonight.", 2]],
            "Cameron: Hazelnut spread, banana pizza was a bit weird. I think it would’ve\nbeen better with cheese…": 
            [["1) I missed that one, it sounds like a recipe for stomach sadness.", 1], 
            ["2) I'm sorry, but what did you just say to me? God no.", 3], 
            ["3) Ugh... sure.", 2]],
            "Cameron: Johnny’s got weird taste but I don’t think he’s a bad guy. Don’t be\nsurprised if you hear from him too.": 
            [["1) Noted...", 2], 
            ["2) Yeah, he's an alright guy.", 1], 
            ["3) I genuinely can't stand him. It's why I don't want to go to the party.", 3]],
            "Cameron: He also got a new cat. Have you seen the pictures in the group chat?": 
            [["1) Oh... Good for him.", 2], 
            ["2) No, and I don't want to. I hate cats on a fundamental level for complex\n   reasons.", 3], 
            ["3) Why would anyone want a cat?", 3]],
            "Cameron: Wait, you seriously don’t like cats? That’s messed up {player_name}.": 
            [["1) They're just not my favorite things on this planet.", 1], 
            ["2) It's a pretty deep rooted dislike, very instinctual.", 2], 
            ["3) They're all a bunch of con artists. They pretend to sound like babies to\n   get you to feed them.", 2]], 
            "Cameron: Well… we’re gonna have some movies on! He’s got a poll going in the\ngroup chat for what we watch.": 
            [["1) Oh, that's fun.", 1], 
            ["2) No one's really gonna sit and watch a movie during a party.", 2], 
            ["3) I haven't seen, I've had that thing muted for months.", 3]],
            "Cameron: It's gonna be great! First spot is at a tie between two old horror\nmovies.": 
            [["1) I bet I can guess what kind of movie is in the top spot.", 1], 
            ["2) Oh, rad.", 1], 
            ["3) Why are we even bothering with this?", 3]],
            "Cameron: There’s a slasher flick and a werewolf movie.": 
            [["1) Aw damn, I'm gonna miss that.", 1], 
            ["2) Of course there is...", 2], 
            ["3) Both are probably lame as hell.", 3]],
            "Cameron: Obviously ‘Guy With Knife III’ is the correct choice.": 
            [["1) Go on... explain your poor choice.", 3], 
            ["2) The third anything is when it all goes downhill though.", 1], 
            ["3) I'm a little biased towards the werewolf movie.", 1]],
            "Cameron: Who’s gonna pick a movie about some overgrown pooch when you’ve got the\nclassic horror movie set up that is stupid teenagers get got?":
            [["1) Teenagers get got is so overplayed, it's just a cop out at this point.", 2], 
            ["2) But have you considered: big dog go bork?", 2], 
            ["3) Eh, maybe?", 3]],
            "Cameron: Nah dude, werewolves are lame.":
            [["1) Okay. You're wrong, but okay.", 3], 
            ["2) That's what makes them fun!", 2], 
            ["3) Slashers are overgrown babies that didn't get enough mommy hugs.", 3]],
            "Cameron: Kinda sad about Sock’s recommendation. They were the only one who\nvoted for ‘The Night is Short, Walk on Girl’. I just don’t think anyone is\ngonna be up for reading subtitles.":
            [["1) I don't even know what that is.", 3], 
            ["2) Drunk subtitles leads to puking.", 3], 
            ["3) RIP Sock.", 2]],
            "Cameron: Oh, if movies don’t sell it, there’s also gonna be Karaoke! Everyone\nshould be drunk so no one will care how bad you sound {player_name}.":
            [["1) Oh, rad!", 1], 
            ["2) That's cool, I guess.", 2], 
            ["3) My ears are already bleeding.", 1]], 
            "Cameron: Nah, see the way you get ahead of that is to go all in on the most\nridiculous pop song ever. Just give the most hammered performance of your life.":
            [["1) That just seems like a good way to get immortalized for drunk karoake.\n     No thanks.", 3], 
            ["2) I'll keep that in mind.", 2], 
            ["3) mmmhmmm.", 2]],
            "Cameron: Oh y’know what I was just thinking about? We never finished that\nboard game from last time.":
            [["1) Proprietorship? I was doing pretty well as the shoe.", 2], 
            ["2) Who cares if we didn't finish Apologies?", 3], 
            ["3) I don't think anyone actually gets to the end of Risks.", 3]],
            "Cameron: No, not that one. The one where you build the house and then someone is\na traitor.":
            [["1) Doesn't ring a bell.", 2], 
            ["2) Oh yeah! Backstabbing at Shack on the Mountain!", 1], 
            ["3) Sounds like you just hallucinated a memory from your childhood.", 3]],
            "Cameron: Pretty sure Dawn got pissy and scattered the pieces after taking a\nbunch of sanity damage like three times in a row during their turn and then they\nweren’t the traitor.":
            [["1) Classic Dawn.", 1], 
            ["2) What a giant baby!", 3], 
            ["3) If they hadn't, I would've.", 3]],
            "Cameron: It could be fun to try it again. We could also play something with a\nrule book that isn’t 45 pages long though.":
            [["1) PLEASE SOMETHING ELSE!", 3], ######
            ["2) No, I think you're right.", 1], 
            ["3) Maybe see what the room is like first.", 2]],
            "Cameron: So, do you need me to pick you up?":
            [["1) I can't go.", 3], 
            ["2) You sneaky bitch, tried to pull a fast one!", 3], 
            ["3) Not in your deathtrap of a car.", 3]],
            "Cameron: Come on dude, my car finally stopped making that sound!":
            [["1) I'm pressing x to doubt.", 2], 
            ["2) Neat, your car is still terrifying.", 3], 
            ["3) I'd just rather not.", 3]],
            "Cameron: Well first I thought maybe a racoon or something got in there with\nthe way the speakers were thumping around. Something about the cold and the\nwiring to the radio.":
            [["1) Death. Trap.", 3], 
            ["2) This isn't inspiring confidence.", 2],
            ["3) If it's just the radio that was acting up then I guess that's a little\n    less terrifying.", 1]],
            "Cameron: I think it’s unfair to keep calling her a death trap. Her engine hadn’t\nstarted smoking in a good few months!":
            [["1) Oh.... good.", 2], 
            ["2) How about we don't?", 3],
            ["3) I CHOOSE LIFE!", 2]],
            "Cameron: Alright, alright. Enough of these lies and slander. Carlotta is a\nfantastic machine and she deserves the world.":
            [["1) She deserves to be buried respectfully.", 2], 
            ["2) Fine, I'll tone it down.", 1],
            ["3) Who names their car \'Carlotta\'?", 3]],
            "Cameron: You’re seriously gonna miss out on the party tonight because of \'vague\ntummy troubles\'?":
            [["1) Yeah, unfortunately.", 2], 
            ["2) Don't say \'tummy,\' you're a whole ass adult.", 3],
            ["3) It's pretty serious. I'm probably dying.", 3]],
            "Cameron: I mean I can let everyone else know but they’re probably not gonna be\nhappy about it…":
            [["1) They'll find a way to live...", 3], 
            ["2) Don't worry about it, I'm probably gonna have to explain to them myself...", 1],
            ["3) I trust you to make me not sound like a complete jackass...", 2]]}
person1keys = list(person1.keys()) # This is for the question indexes
MainScore = [] #idx+1 equals person number. will be in form [pers1, pers2,...,persX]


#helper functions
def ScoreAnswer(answer):
    #This Function takes a chosen answer in the form of a list, and returns the appropriate score with some variance for replayability
    #Retuned ansScore is of type Float
    ansScore: float = 0.00
    anschoice: int = answer[1] #this gets the score from the answer sub list
    if anschoice == 3:
        ansScore = 0.1 + (random.randint(-5,10) / 100)
    if anschoice == 2:
        ansScore = random.randint(-10,10) / 100 #for variance with basic options
    if anschoice == 1:
        ansScore = -0.1 + (random.randint(-10,5) / 100)
    return(ansScore)
 
def NextQuestion(questionNum):
    #This function takes in the current question number in the game, and returns the appropriate question-answer pair along- 
    # with the friend associated with the questions.
    #Returned values will be of Str, List, Int types
    question: str = ""
    answers: list = []
    question = question + str(person1keys[questionNum]) #temporarry
    answers = person1[person1keys[questionNum]] #temporary
    num_friend: int = 1


    return(question, answers, num_friend)

def friendsCnt(numpep, startvalue):
    #This function takes in the number of friends decided, and the start value for Friendship points (default 0.50) 
    #Returns the new value of friends based on user input (currently disabled -just sets the value to 1) 
    startloop: str = "oranges"
    if startloop == "oranges":
        print("Support for multiple friends is currently unavalible, please come back later...\n...")
        print("Friends is set to 1\n")
        numpep: int = 1
    for idx in range(numpep):
        MainScore.append(startvalue)
    return numpep

def nameSet(person_name):
    #This takes in the current name string, and returns the new one based on user input
    #This function restricts the name to being over 0 characters long
    while True:
        try:
            person_name: str = input("What should we call you?\n-> ")     
            if len(person_name) != 0:          
                print(f"That's a good name, {person_name}! Your friends will remember it!")
                break
            else:
                raise ValueError
        except ValueError:
            print("Name cannot be empty. Try again")
    return person_name

def VictoryConditions(score):
    #This function takes in a score value, and returns values based upon if the score meets certain criteria
    #Returns Endgametype of type int
    Endgametype: int = 0
    if score <= 0.25: #1 gets eaten
        return 2
    if score >= 0.75: #1 hates you
        return 3
    if 0.25 < score < 0.75: #winning condition
        return 1
    else:
        print("how did you get here, this is not supposed to happen. Please report this to devs")
        print("Exiting game...")
        exit()

    #victory conditions are in the docstring for endinggame()
    #scores larger than 100 are victory conditions
    return Endgametype



#game functions
def StartGame(name, startval, numpeople):
    #Takes in the player name, the starting value of Friendship Points, and the number of friends
    #Prints out the intro, and asks for tutorial. Then goes into the main game
    Intro_text: str = f"""
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
    if len(MainScore) == 0: #TEMPORARY, only works with 1 friend. This is a fix for if friends is not called
        for i in range(numpeople):
            MainScore.append(startval)
    
    while True: #asks for input to do tutorial or not
        try: #this is for input validation
            tutorialY: str = input("""                                   1) View Tutorial?
                                   2) Answer the call\n-> """)
            corlist: list = ["1", "2"]
            if tutorialY not in corlist:
                raise ValueError
            if "1" in tutorialY:
                Tutorial()
            break
        except ValueError:
            print("Invalid input, please type exactly \"1\" or \"2\"")
    print("\n-- Game Start --\n----------------")
    sleep(1)
    MainGame(name) #this goes into the main game
        #block was found in stackoverflow: https://stackoverflow.com/questions/41832613/python-input-validation-how-to-limit-user-input-to-a-specific-range-of-integers

def Tutorial():
    #Prints the tutorial
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

    Your goal is to keep your friendship points between 0.25 and 0.75. 
    If you manage this by the last question, and the value is in that interval 
                                   you win!

                                   Be Warned -
        if it ever falls to 0, or makes it to 1, the game will end immediatly.

    You should really pick up that phone now, Cameron’s waiting, good luck!\n"""
    print(Tut_text)
    sleep(2)

def MainGame(name):
    #Takes in the Player name, and then does the rest of the main stuff in the game
    numquestions: int = len(person1keys)
    questionnumber: int = 0
    VictoryCond: int = 0
    player_name: str = name
    while VictoryCond == 0: #main loop for the game
        friend_number: int = 0
        anslenlist: list = []
        anslenstr: str = ""
        curquestion, curanswers, friend_number = NextQuestion(questionnumber)
        curquestion = curquestion.format(player_name = player_name) #formats the player name into the text
        if numquestions > 1:    
            print(f"\n{numquestions} questions remain\n")
        else:
            print(f"Final Question")
        sleep(1.5)
        print(f"{curquestion}\n")
        sleep(2)
        for i in range(len(curanswers)): #prints answers out
            print(curanswers[i][0])
            anslenlist.append(i+1)
            sleep(0.5)
        for i in range(len(anslenlist)):
            anslenstr = anslenstr + str(anslenlist[i]) + ", "
        anslenstr = anslenstr[:-3] + f"or {anslenlist[-1]}"
        while True:
            try: #this is for input validation
                if questionnumber < 4:
                    choice = input(f"Pick Answers {anslenstr} by typing that number (ex to exit if stuck)\n-> ")
                else:
                    choice = input(f"Pick Answers {anslenstr}\n-> ")
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
        CurAnswScore = ScoreAnswer(curanswers[choice-1])
        MainScore[friend_number-1] = round(MainScore[friend_number-1] + CurAnswScore, 3) #this is to stop floating point weirdness
        for i in range(len(MainScore)):
            friend_name_list = ["Cameron", "Dawn", "Sock"]
            print (f"\n{friend_name_list[i]} is at {MainScore[i]} friendship points")
            sleep(1)
            if (MainScore[i] <= 0) or (MainScore[i] >= 1):
                VictoryCond = VictoryConditions(MainScore[friend_number-1])  
            elif MainScore[i] < 0.25:
                print("Warning! Eating imminent")
            elif MainScore[i] > 0.75:
                print("Warning! Hatred is seeping through your friend")
            sleep(2)
            print("\n\n")
        questionnumber += 1
        numquestions -= 1 #this prevents endless loops
        if numquestions == 0:
            VictoryCond = VictoryConditions(MainScore[friend_number-1])  
        if CurAnswScore > 10: #for special conditions - not currently used
            VictoryCond = VictoryConditions(MainScore[friend_number-1])            
        
    EndingGame(VictoryCond, player_name)
    
def EndingGame(victory, player_name):
    #Takes in the victory condition of type int, and the player name (str)
    #Prints the endings depending on the victory condition
    """
    victory condition 0: not possible, 0 means game is running

    victory condition 1: out of questions. This is good, and can lead into winning flawlessly
        victory condition 1.2: Flawless victory, all friends dont come and dont hate you
        victory condition 1.3: Atleast 1 friend died
        victory condition 1.4: All survived, but at least 1 hates you 
    victory condition 2: All eaten - all friends get eaten
    victory condition 3: All hate you - all friends hate you
    """

    
    ending1_text: str = """
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

    You’re gonna have a lot of catching up to do with them tomorrow.

                                You Win!
                                """
    
    ending2_text: str = f"""
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
    
    ending3_text: str = """
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

    print("Game end\n...\n...\n...")
    sleep(2)
   
def RetryGame():
    #Asks to replay the game, and clears the score to reset the game if answer is 'Y'
    exitgame: str = input("Do you want to play again or exit? \"Y\" for yes, anything else for no\n-> ")
    if exitgame != "Y":
        print("Thank you for playing")
        exit()
    if exitgame == "Y":
        MainScore.clear

def Menuscreen():
    #Main menu
    player_name: str = ""
    nonamechecknum: int = 2
    numofPeople: int = 1
    startval: float = 0.50 #this changes the starting number in MainScore. This is for us to tinker with to adjust difficulty/game length
    
    Menu_text: str = """
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

            menuinput: str = input("What do you want to do? Type \"Play\", \"Name\", \"Friends\", or \"Exit\"\n-> ").upper()
            inputcheck: list = ["PL", "NA", "FR", "EX"] #checking substrings for higher chance of getting right thing
            
            if any(substring in menuinput for substring in inputcheck) == False:
                raise ValueError
            if "PL" in menuinput: #play
                if len(player_name) == 0:
                    if nonamechecknum == 0: #this is a funny easteregg
                        print("Fine, name has been set to 'Billybob'. You win")
                        player_name = "Billybob"
                        StartGame(player_name, startval, numofPeople)
                        break
                    else:
                        print("Please set a name first")
                        nonamechecknum -= 1
                else:
                    StartGame(player_name, startval, numofPeople)
                    break
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

def WholeProgram():
    #combines main functions to make seemless retrying of the game
    while True:
        Menuscreen()
        RetryGame()




if __name__ == '__main__':
    # Write all functions in here that will be called when running the program
    WholeProgram()