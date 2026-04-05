from time import sleep
from random import randint
from colorama import Fore, Style, init, just_fix_windows_console
from platform import system
from math import floor

"""
Docstring for project 2

Colorama library will need to be installed for full experience. See sources here:
https://pypi.org/project/colorama/
https://www.geeksforgeeks.org/python/introduction-to-python-colorama/

Personality types for NPCs:
Cameron: average joe-type
Dawn: bully, abrasive
Sock: meek, needy lil' guy, 
Dawn and Sock are fully written and will appear in the second iteration of Stay Home Moon. Only Cameron is utilized for ease of testing and to trouble shoot 
score weights which may be altered for the second project.

"""


#Helper functions! These are the bones of our game!
#helepr functions in MenuScreen
def friendsCnt(numpep: int) -> int:
    """Asks user for how many characters they want to play against

    Args:
        numpep (int): Number of friends currently selected

    Raises:
        ValueError: catches if user input is not an integer from 1-3
    Returns:
        int: New value for number of friends selected
    """
    while True:
        try: #this is for input validation
            print(Fore.CYAN + "Difficulty scales on number of people. 1= Easy, 2= Medium, 3= Hard")
            numpep = int(input(Fore.BLACK + "Enter number of friends: 1,2 or 3. Current value is: " + Fore.CYAN + f"{numpep}\n"+Fore.WHITE+"-> ")) #sets number of people for game              
            peoplelist = [1,2,3]
            if numpep not in peoplelist:
                raise ValueError
            break
        except ValueError:
            print(Fore.RED + "Invalid input, please type exactly \"1\", \"2\", or \"3\"")
    return numpep

def nameSet(person_name: str) -> str:
    """Sets a new name from user imput

    Args:
        person_name (str): old user name

    Raises:
        ValueError: catches if user input was 0 length

    Returns:
        str: new user name
    """
 
    while True:
        try:
            person_name: str = input(Fore.BLACK + "What should we call you?\n" + Fore.WHITE + "-> ").title()
            if ("\\" not in person_name) and (person_name[0]+person_name[-1]).isalnum():     
                print(Fore.LIGHTGREEN_EX + f"That's a good name, " + Fore.CYAN + person_name + Fore.LIGHTGREEN_EX +"! Your friends will remember it!\n")
                break
            else:
                raise ValueError
        except ValueError:
            print(Fore.RED + "Name cannot be empty or contain backspaces. Try again.")
    return person_name

def checkpoint_assign(checkp_score: dict[str, list[tuple[float,...], tuple[int,...]]], MainScore: list[float], answered_questions: list[int], player_name) -> None:
    """Takes current place in game and assigns a new checkpoint with your scores and answered questions

    Args:
        checkp_score (dict[str, list[tuple[float,...], tuple[int,...]]]): list of all checkpoints reached
        MainScore (list[float]): current score in main game
        answered_questions (list[int]): all answered questions in current game

    Returns:
        None: 
    """
    checkp_score: dict
    checkpoint_list: list[str] = ["bees", "turnip", "matcha", "robot", "dolphin", "pickle", "toast"] #more words
    placement: int
    placement = (sum(answered_questions) // 12) - 1 #index of question at specified checkpoint
    key = checkpoint_list[placement]
    checkp_score.update({f"{key}\\{player_name}": [tuple(MainScore) , tuple(answered_questions)]}) 
    print(Fore.CYAN + f"Checkpoint hit! Checkpoint is: {key}")
    return None

def checkpoint_execute() -> tuple[str, list[tuple[float,...], tuple[int,...]]]:
    """Asks user for the checkpoint the want to start from, and returns the name and the values from that checkpoint. Exits if theres not checkpoints

    Raises:
        KeyError: imput validation 

    Returns:
        tuple[str, list[tuple[float,...], tuple[int,...]]]: list of tuples of floats
    """
    checkpoint_dictionary = {}
    checkpoint_dictionary.clear()
    try:
        with open("checkpoints.txt", "r") as fs:
            file = fs.read().split("\n")
            file.pop(-1)
            if len(file) < 1:
                print(Fore.RED + "Nothing to load. . .\n")
                return None, None
            temp_check_list = file
            for i in range(len(file)):
                c_vals = tuple(temp_check_list[i].split(","))
                if len(c_vals) == 7:
                    ckey, csc1, csc2, csc3, cq1, cq2, cq3 = c_vals
                    player_name = ckey[ckey.find("\\")+1:]
                    ckey = ckey[:-len(player_name)-1].upper()             
                    checkpoint_dictionary[ckey] = [(float(csc1),float(csc2),float(csc3)), (int(cq1),int(cq2),int(cq3))]
                elif len(c_vals) == 5:
                    ckey, csc1, csc2, cq1, cq2 = c_vals
                    player_name = ckey[ckey.find("\\")+1:]
                    ckey = ckey[:-len(player_name)-1].upper()              
                    checkpoint_dictionary[ckey] = [(float(csc1),float(csc2)), (int(cq1),int(cq2))]
                elif len(c_vals) == 3:
                    ckey, csc1, cq1 = c_vals
                    player_name = ckey[ckey.find("\\")+1:]
                    ckey = ckey[:-len(player_name)-1].upper()
                    checkpoint_dictionary[ckey] = [(float(csc1)), (int(cq1))]    #if you see this, please explain why I cant do tuple(float(csc1))... keeps saying its not iterable
                else:
                    print(Fore.RED + "ERROR how did this happen.... must be buggy code" + Style.RESET_ALL)
                    exit()
    except FileNotFoundError:
        print(Fore.RED + "Nothing to load. . .\n")     
        return None, None

    print(Fore.CYAN + "Where do you want to start at?")

    checkp_key_list: list[str] = list(checkpoint_dictionary.keys())
    for key in checkp_key_list:
        print(Fore.CYAN + key.title())

    #main game
    password = ""
    while True:
        try:
            access = input(Fore.BLACK + "Would you like to access a checkpoint? Y/N \n"+Fore.WHITE+"-> ").upper()
            if "Y" in access:
                try:
                    password: str = input(Fore.BLACK + "Please enter a password or type \'back\' to continue to retry.\n"+Fore.WHITE+"-> ").upper()                   
                    if "BACK" in password:
                        break
                    elif password not in checkp_key_list:
                        raise KeyError
                    break
                except KeyError:
                    print(Fore.RED + "Please enter a valid password or type 'back'.")
            elif "N" in access:
                return None, "no"
        except KeyError:
            print(Fore.RED + "Please type \'Y\' or \'N\'.")
    current_loc = checkpoint_dictionary[password]
    return player_name, current_loc


#Helper functions in MainGame
def ScoreAnswer(anschoice: int) -> float:
    """scores answer chosen 

    Args:
        anschoice (int): int 1-3 corresponding to weight of answer chosen
    Returns:
        float: score of answer
    """
    #This Function takes a chosen answer in the form of a list, and returns the appropriate score with some variance for replayability
    #Retuned ansScore is of type Float
    ansScore: float = 0.00
    if anschoice == 3:
        ansScore = 0.1 + (randint(-5,10) / 100)
    if anschoice == 2:
        ansScore = randint(-10,10) / 100 #for variance with basic options
    if anschoice == 1:
        ansScore = -0.1 + (randint(-10,5) / 100)
    return(ansScore)

def define_likeability(score: float) -> str:
    """returns a color string relating to the score of the character 

    Args:
        score (float): float from 0-1

    Returns:
        str: colored string
    """
    
    char_str = ""
    if score < 0.25:
        char_str = Fore.LIGHTGREEN_EX + "They like you too much - they are in danger of coming to your house"
    elif score > 0.75:
        char_str = Fore.LIGHTRED_EX + "Your responses have been too hurtful - they hate you"
    else:
        char_str = Fore.LIGHTYELLOW_EX + "Their opinion of you is still in flux - they feel neutral towards you"
    return char_str

def character_selection(num_of_friends: int, character_picked: int, charcter_scores: list[float]) -> int:
    """Allows the user to pick what character to talk to next. If num_of_friends is below 3, it has alternate logic

        Args:
            num_of_friends (int): The number of friends picked in the main menu for difficulty
            character_picked (int): The character that the player wants to tak to next
            charcter_scores (list[float]): Current scores for all characters

        Returns:
            int: The next character chosen for dialoge
        """
    try:
        list_num: list[int]= [1,2,3]
        char_list = ['Cameron', 'Dawn', 'Sock']
        if num_of_friends < 3:
            if num_of_friends == 2: #switches the person you are calling if you only have 2 friends
                if 0.0 < charcter_scores[character_picked-2] < 1.0: 
                    if character_picked == 2:
                        print("Now Calling Cameron...")
                        return (character_picked%2)+1
                    print("Now Calling Dawn...")
                    return (character_picked%2)+1
                print("Redialing...")
                return character_picked
            if num_of_friends == 1: #this skips picking the person if you only have 1 friend
                character_picked = 1
                return character_picked

        #will only reach here if you have 3 friends selected
        if character_picked != 0:    
            list_num.remove(int(character_picked))
        else: #this returns 1 for the first character
            if answered_questions[0] < 30:
                character_picked = 1
                return character_picked
        for i in range(len(list_num)-1,-1,-1): #restricts character picked to only ones with questions left to be answered
            if answered_questions[list_num[i]-1] >= 30:
                list_num.remove(i+1)
        if len(list_num) == 0:
            print(Fore.WHITE+"All other friends "+Fore.RED+"wont talk to you right now...\n"+Fore.WHITE+f"Redialing {char_list[character_picked-1]}...")        
            return character_picked


        person_info: dict[str] = {"Cameron": "He is suprisingly normal compared to your other friends\n(515) 602-6027\n",
                                "Don": "He is very abrasive and difficult but has very good social connections\n(603) 502-6015\n", 
                                "Sock": "They can be very anxious and high maintence sometimes but can make a mean pumpkin pie\n(703) 503-6029\n"}
        

        if 1 in list_num: 
            print("Cameron \n\n"+Fore.WHITE+f"{person_info['Cameron']}{define_likeability(charcter_scores[0])}\n" + Fore.BLACK + "Type 1 to choose\n------------------------------------------")
        if 2 in list_num: 
            print("Dawn \n\n"+Fore.WHITE+f"{person_info['Don']}{define_likeability(charcter_scores[1])}\n" + Fore.BLACK + "Type 2 to choose\n------------------------------------------")
        if 3 in list_num: 
            print("Sock \n\n"+Fore.WHITE+f"{person_info['Sock']}{define_likeability(charcter_scores[2])}\n" + Fore.BLACK + "Type 3 to choose\n------------------------------------------")
        if len(list_num) == 1:
            anslenstr= f"{list_num[0]}"
        else:
            anslenstr = f"{list_num[0]}, or {list_num[1]}"
        
        while True:
            try: 
                character_picked_new = input(Fore.BLACK + f"Which character would you like to call next? Type {anslenstr} to choose. or \"exit\" to exit\n"+ Fore.WHITE +"-> ") 
                if "EX" in character_picked_new.upper():
                    exit_fun()
                if int(character_picked_new) not in list_num: 
                    raise ValueError
                break
            except ValueError:
                print(Fore.RED + "That wasn't an option!") 
        if character_picked == None:
            print(Fore.RED + "How did this happen\nexiting code" + Style.RESET_ALL)
            exit()
        character_picked = int(character_picked_new)
        
        return character_picked
    except ValueError:
        print(character_picked, "value error somehow")
        exit_fun()

def NextQuestion(friend_num: int, answered_questions_list: list[int]) -> tuple[str, list]:
    """Function gets the next question-answer pair in the dictionary of the passed friend_num

    Args:
        friend_num (int): friend number to get next question-answer pair
        answered_questions_list (list[int]): previous questions answered

    Returns:
        question, answer (tuple[str,list]): next question answer pair
    """
    
    
    #This function takes in the current question number in the game, and returns the appropriate question-answer pair along- 
    # with the friend associated with the questions.
    #Returned values will be of Str, List, Int types
    question: str = ""
    answers: list = []
    answered_ques_friend = answered_questions_list[friend_num-1]
    try:
        if friend_num == 1:
            question = question + str(person1keys[answered_ques_friend])
            answers = person1[question]
        elif friend_num == 2:
            question = question + str(person2keys[answered_ques_friend])
            answers = person2[question]
        elif friend_num == 3:
            question = question + str(person3keys[answered_ques_friend])
            answers = person3[question]          
        else:
            print(Fore.RED + "error" + Style.RESET_ALL)
            print(checkp_score)
            exit()
    except IndexError:
        print("This is index out of bounds error. Friend num = ", friend_num)
        print(checkp_score)


    return(question, answers)

def VictoryConditions(scores: list[float]) -> int:
    """Gets victory conditions for current friend score 

    Args:
        score (float): Current score for current character

    Returns:
        int: int describing the endgametype reached, returns 0 if no endgame was reached
    """

    #This function takes in a score value, and returns values based upon if the score meets certain criteria
    #Returns Endgametype of type int
    Endgametype: int = 0
    ending_values = []
    for value in scores:
        if value > 0.75:
            ending_values.append(0)
        elif value < 0.25:
            ending_values.append(2)
        else:
            ending_values.append(1)
    if len(set(ending_values)) == 1:
        idx = ending_values[0]
        if idx == 2: #all eaten
            Endgametype = 20
        elif idx == 0: #all come to house
            Endgametype = 30
        else: #best ending, nobody gets hurt
            Endgametype = 11
    elif 2 in ending_values:
        Endgametype = 12 #atleast one person dies
    elif 1 in ending_values:
        Endgametype = 13 #atleast one person hates you, but none died
    else:
        print(Fore.RED + "this is not supposed to happen... I blame the users" + Style.RESET_ALL)
        exit()

    #victory conditions are in the docstring for endinggame()
    #scores larger than 100 are victory conditions
    return Endgametype

def sleep_func(n: int) -> None:
    """checks if debug mode is enabled (true/false value) in main block

    Args:
        n (int): int for how long to sleep
    """
    global debugmode
    if debugmode == True:
        return
    else:
        sleep(n)
        return


#game functions
def WholeProgram() -> None:
    """Endlessly repeats menuscreen

    Returns:
        None: none
    """   

    while True:
        Menuscreen()

def Menuscreen() -> None:
    """Menu screen, this leads into the main game, sets your name, number of friends, loads game from checkpoint if selected, and can exit the program.

    Returns:
        None: none
    """   
    #Main menu
    player_name: str = ""
    nonamechecknum: int = 2
    numofPeople: int = 3
    startval: float = 0.50 #this changes the starting number in MainScore. This is for us to tinker with to adjust difficulty/game length
    Menu_text: str = """
                            
                        Stay Home Moon
                            
                            
                        Play
                        Set Name
                        Friends Count
                        Load
                        Exit

    """
    #ascii pattern made from https://www.aestheticsymbols.me/dot.html
    print(Fore.MAGENTA + "            ┌── " + Fore.YELLOW + "⋆⋅☆⋅⋆ " + Fore.MAGENTA + "──.·:*¨༺ " + Fore.YELLOW + "☾" + Fore.MAGENTA + " ༻¨*:·.── " + Fore.YELLOW + "⋆⋅☆⋅⋆" + Fore.MAGENTA + " ──┐")
    print(Menu_text)
    print(Fore.MAGENTA + "            └── " + Fore.YELLOW + "⋆⋅☆⋅⋆" + Fore.MAGENTA + " ──•,¸,.·'  '·.,¸,•── " + Fore.YELLOW + "⋆⋅☆⋅⋆" + Fore.MAGENTA + " ──┘")
    while True:
        try: #this is for input validation

            menuinput: str = input(Fore.BLACK + "What do you want to do? Type \"Play\", \"Name\", \"Friends\", \"Load\", or \"Exit\"\n"+ Fore.WHITE +"-> ").upper()
            inputcheck: list = ["PL", "NA", "FR", "LO", "EX", "DEBUG"] #checking substrings for higher chance of getting right thing
            
            if any(substring in menuinput for substring in inputcheck) == False:
                raise ValueError
            if "PL" in menuinput: #play
                if len(player_name) == 0:
                    if nonamechecknum == 0: #this is a funny easteregg
                        print(Fore.CYAN + "Fine, name has been set to 'Billybob'. You win")
                        player_name = "Billybob"
                        sleep_func(2)
                        return StartGame(player_name, startval, numofPeople)
                    else:
                        print("Please set a name first")
                        nonamechecknum -= 1
                else:
                    return StartGame(player_name, startval, numofPeople)

            elif "NA" in menuinput:
                player_name = nameSet(player_name)
            elif "FR" in menuinput: #sets friends
                numofPeople = friendsCnt(numofPeople)
            elif "LO" in menuinput:
                checkpoint = checkpoint_execute()
                player_name, game_vals = checkpoint
                if (not player_name or not game_vals): #I think this will work, it checks if the bool(value) equals false
                    break
                if type(game_vals[0]) is float:
                    MainScore.append(game_vals[0])
                    answered_questions.append(game_vals[1])
                else:
                    for i in game_vals[0]:
                        MainScore.append(i)
                    for i in game_vals[1]:
                        answered_questions.append(i)
                global loaded_checkpoint
                loaded_checkpoint = True
                return MainGame(player_name)

            elif "EX" in menuinput: #exits program
                exit_fun()
            elif "DEBUG" in menuinput:
                debugval = input("Do you want to engage debug mode? This will turn off all 'sleep' statements. Y/n\n-> ").upper()
                if "Y" in debugval:
                    print("Debug mode enabled")
                    global debugmode
                    debugmode = True
                    player_name = "debugname"
                    print("set name to 'debugname'")

            else: #this is for wrong inputs not caught
                print(Fore.RED + "how did you get here. bad !!@%$@#@#!!!$#@#@#@\n" + Style.RESET_ALL)
                exit()
        except ValueError:
            print(Fore.RED + "Invalid input, please type one of the four options\n")    
 
def StartGame(name: str, startval: float, numpeople: int) -> None:
    """Prints start game text, assigns MainScore starting values, and asks user if they want to start the tutorial

    Args:
        name (str): User name
        startval (float): starting value for all character's scores (0.5)
        numpeople (int): number of friends chosen for the game
    Raises:
        ValueError: restricts user input to value in corlist
    Returns:
        None: none
    """
    
    Intro_text1: str = Fore.WHITE + f"""
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
    teensy little security measure just doesn’t hold up.\n"""

    introtex2 = Fore.WHITE + """    It’s been a couple months since the last time you’ve had to jump ship, and 
    this time you’re going by """ + Fore.CYAN + name + Fore.WHITE +  """.\n"""

    introtex3 = Fore.WHITE + """    You’ve managed to settle in quite nicely. You’ve scored a great job and 
    managed to land a spot in a semi-stable group of friends. You’ve finally 
    found the best way to keep from going on a bloodthirsty rampage during the 
    full moons. Thanks to your new iron clad security, courtesy of ‘Trademarked 
    Hardware and Home Improvement’ store, there’s absolutely no way you’re 
    busting through those locks! So now it’s just you, a movie that you 
    probably won’t finish due to your impending transformation, and a supply 
    of tranquilizer laced meat in the fridge all settled in for a completely 
    uneventful evening."""
    
    introtex5:str = """

                            """+Fore.RED+"""So why is your phone ringing?"""
    
    introtext6: str = Fore.WHITE+""" 

    Looking at the number on display, you see Cameron’s name popping up. Before
    you can think to answer it all rushes in: the party and the plans you made 
    with each of your friends. That was tonight! You scheduled that all on the 
    night of the full moon like some giant idiot!

    You’re gonna have to cancel all of your plans and you just know your 
    friends aren’t going to make that easy. The alternative however is 
    potentially eating them at worst, possibly only mauling them at best. It’s
    what you’ve gotta do."""
    
    
    print(Intro_text1)
    sleep_func(4)
    print(introtex2)
    sleep_func(3)
    print(introtex3)
    sleep_func(2)
    print(introtex5)
    sleep_func(4)
    print(introtext6)
    sleep_func(4)
    if len(MainScore) == 0: #assigns startval for each friend. wont work if mainscore has somthing in it - possible error there
        for i in range(numpeople):
            MainScore.append(startval)
            answered_questions.append(0)


    while True: #asks for input to do tutorial or not
        try: #this is for input validation
            tutorialY: str = input(Fore.BLACK + """\n                                   1) View Tutorial?
                                   2) Answer the call\n"""+Fore.WHITE+"-> ")
            corlist: list = ["1", "2"]
            if tutorialY not in corlist:
                raise ValueError
            if "1" in tutorialY:
                Tutorial()
            break
        except ValueError:
            print(Fore.RED + "Invalid input, please type exactly \"1\" or \"2\"")
    print(Style.DIM + "\nPicking up the call in 3...\n2...\n1...")
    sleep_func(1)
    MainGame(name) #this goes into the main game
        #block was found in stackoverflow: https://stackoverflow.com/questions/41832613/python-input-validation-how-to-limit-user-input-to-a-specific-range-of-integers

def Tutorial() -> None:
    """Prints tutorial text (potential to add stuff later)

    Returns:
        None: none
    """
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
    print(Fore.WHITE + Tut_text)
    sleep_func(2)

def MainGame(name: str) -> None:
    """Main block of code for game. Runs the game until a victory condition is reached

    Args:
        name (str): user name
        num_of_friends (int): selected number of characters to play against

    Raises:
        ValueError: restricts user input to be either a number 1-3, or include the str 'ex' to exit the game
    
    Returns:
        None: none
    """
    #The guts of our game! Takes in the Player name, and then calls the helper functions to complete the processes in the game!
    VictoryCond: int = 0
    player_name: str = name
    friend_number: int = 0
    num_of_friends = len(MainScore)
    numquestions: int = 30 * num_of_friends
    questionnumber: int = sum(answered_questions)
    checkpoint_loaded_ques_num: int = 0

    while questionnumber < numquestions: #main loop for the game
        anslenlist: list = []
        anslenstr: str = ""
        if (questionnumber % 12 == 0) and (checkpoint_loaded_ques_num != 0): #checking the number of the question to spit out checkpoint
            checkpoint_assign(checkp_score, MainScore, answered_questions, player_name) #assigns checkpoints to current position        
        if questionnumber % 6 == 0:
            friend_number = character_selection(num_of_friends, friend_number, MainScore)
        curquestion, curanswers = NextQuestion(friend_number, answered_questions)
        curquestion = curquestion.format(player_name = player_name) #formats the player name into the text
        if numquestions - questionnumber > 1:
            print(Fore.MAGENTA + "──" + Fore.YELLOW + " ⋆⋅☆⋅⋆ " + Fore.MAGENTA + "──.·:*¨༺" + Fore.YELLOW + " ☾ " + Fore.MAGENTA + "༻¨*:·.──" + Fore.YELLOW + " ⋆⋅☆⋅⋆ " + Fore.MAGENTA + "──" + Fore.WHITE +Style.DIM + f"\n\n{numquestions - questionnumber} questions remain\n")
        else:
            print(Fore.YELLOW+ Style.BRIGHT + f"Final Question")
        sleep_func(1.5)
        lonegest_newline_length = max(curquestion.split("\n"), key=len)
        dash_str = ""
        for idx in range(0,len(lonegest_newline_length)-4,2):
            dash_str = dash_str + "- "
        dash_str = dash_str + "-"
        print(Fore.RED+ "┌──" + Fore.BLACK + dash_str + Fore.RED+"──┐")
        for i in curquestion.split("\n"):
            print(Fore.BLUE +"  "+ i)
        print(Fore.RED+ "└──" + Fore.BLACK + dash_str + Fore.RED+"──┘\n")
        sleep_func(2)
        
        for i in range(len(curanswers)): #prints answers out
            print(Fore.WHITE + curanswers[i][0])
            anslenlist.append(i+1)
            sleep_func(0.5)
        for i in range(len(anslenlist)):
            anslenstr = anslenstr + str(anslenlist[i]) + ", "
        anslenstr = anslenstr[:-3] + f"or {anslenlist[-1]}"
        while True:
            try: #this is for input validation
                if questionnumber < 4:
                    choice = input(Fore.BLACK + f"Pick Answers {anslenstr} by typing that number (ex to exit if stuck)\n"+Fore.WHITE+"-> ")
                else:
                    choice = input(Fore.BLACK + f"Pick Answers {anslenstr}\n"+Fore.WHITE+"-> ")
                if choice.isdigit() == True:
                    choice = int(choice)
                    if choice not in anslenlist:
                        raise ValueError
                    break
                else:
                    if "ex" in choice.lower():
                        exit_fun()
                    raise ValueError
            except ValueError:
                print(Fore.RED + "Invalid input, please type exactly one of the numbers shown")
            print()
        CurAnswScore = ScoreAnswer(curanswers[choice-1][1])
        answered_questions[friend_number - 1] += 1
        MainScore[friend_number-1] = round(MainScore[friend_number-1] + CurAnswScore, 4) #this is to stop floating point weirdness
        friend_name_list = ["Cameron", "Dawn", "Sock"]
        color_val = str(MainScore[friend_number-1])
        badendtxt = ""
        match floor(float(color_val)*4):
            case -1:
                color_val = Fore.RED + color_val    
                badendtxt = badendtxt + "Somethings up with you, imma "+Fore.RED+"come over"+Fore.WHITE+" right away..\n"
            case 4:
                color_val = Fore.RED + color_val    
                badendtxt = badendtxt + "You suck today, you know that? Goodbye, "+Fore.RED+"I dont think I want to speak to you again\n"                
            case 0 | 3:
                color_val = Fore.YELLOW + color_val
            case _:
                color_val = Fore.GREEN + color_val


        print (Style.DIM + f"\n{friend_name_list[friend_number-1]} is at {color_val}" + Style.DIM + " friendship points")
        print(badendtxt,end="")
        sleep_func(1)



        if (MainScore[friend_number-1] <= 0.0) or (MainScore[friend_number-1] >= 1.0): 
            answered_questions[friend_number - 1] = 30
        elif MainScore[friend_number-1] <= 0.25:
            print("Warning! Your friend is growing concerned!")
        elif MainScore[friend_number-1] >= 0.75:
            print("Warning! Hatred is seeping through your friend!")
        sleep_func(2)

        if (sum(answered_questions) % 6 == 0) and num_of_friends != 1:
            char_list = ['Cameron', 'Dawn', 'Sock']
            print(f"\nCall ended with {char_list[friend_number-1]}")        
            sleep_func(1)
        print("\n\n")
        questionnumber: int = sum(answered_questions)
        checkpoint_loaded_ques_num += 1
                 
    VictoryCond = VictoryConditions(MainScore)
    EndingGame(VictoryCond, player_name)

def EndingGame(victory: int, player_name: str) -> None:
    """Prints ending game text based on victory condition

    Args:
        victory (int): integer correspoding to a specific victory condition
        player_name (str): user name

    Returns:
        None: none
    """   
    #Takes in the victory condition of type int, and the player name (str)
    #Prints the endings depending on the victory condition
    """
    victory condition 0: not possible, 0 means game is running

    victory condition 10: out of questions. This is good, and can lead into winning flawlessly
        victory condition 1.1: Flawless victory, all friends dont come and dont hate you
        victory condition 1.2: Atleast 1 friend died
        victory condition 1.3: All survived, but at least 1 hates you 
    victory condition 2: All eaten - all friends get eaten
    victory condition 3: All hate you - all friends hate you
    """

    
    ending1_text: str = Fore.WHITE + """
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

                                """+Fore.GREEN+"""You Win!
                                """
    
    ending2_text: str = f"""
                Your friends couldn’t be convinced to """+Fore.RED+"""stay away. 

                            """+Fore.BLACK+"""Do you know what that means? 

             """+Fore.RED+"""That means they’re coming to your house """ +Fore.CYAN+ player_name+Fore.WHITE + """. 

                    You """+Fore.BLACK+"""failed"""+Fore.WHITE+""" them in the worst possible way.

    The night of the full moon and subsequently Johnny’s party arrives. 
    Your transformation was interrupted by a knock on the door. It opens and
    concerned gazes of the people you care about witness you hunched over and 
    writhing. They hear your bones snap as they reshape and you are molded into
    a monster.

    """+Fore.RED+"""Maybe it’s for the best you don’t exactly remember what happened next. 
    You’ll never forget the sight of the remains you left behind though.

    """+Fore.WHITE+"""You couldn’t stomach hiding them away like so many other unfortunate 
    bystanders before. You run, leaving this version of your life behind.

                                    """+Fore.RED+"""Bad End
                                    """
    
    ending3_text: str = Fore.WHITE + """
       The night of the full moon comes and goes without incident.

               
       The sun rises to a slightly disheveled apartment, but a quick tidy and 
       nothing out of the ordinary appears to have occurred.

       There’s no messages on your phone. No one has checked in on you since 
       yesterday and the group chat is weirdly silent. 

       You may have lost all of your friends, but at least they’re alive! You 
       didn’t just eat a bunch of innocent people! So you stand in your newly 
       re-organized apartment and cling to that small victory. 

       """+Fore.RED+"""You can’t help but feel a little lonely though…

       
                                       """+Fore.RED+"""Bad End?
                                """

    ending12_text: str = Fore.WHITE + """
                                It was """+Fore.RED+ Style.BRIGHT+ """almost"""+Fore.WHITE+ Style.NORMAL+ """ perfect.
        
                     Maybe not""" + Style.BRIGHT + Fore.RED + """ perfect""" +Style.NORMAL+ Fore.WHITE+ """ but it would've been """ +Style.BRIGHT+ Fore.YELLOW+ """okay""" +Style.NORMAL+ Fore.WHITE+ """.
        
        You just couldn't pretend things were normal. You couldn't find a way to
        maintain a middle ground or playful aloofness. You let slip one too
        many things that raised eyebrows and now... \n""" +Fore.RED+ Style.BRIGHT+ """
                                  You're here.""" +Fore.WHITE+ Style.NORMAL+ """
        
        The night comes and goes in a blur as it typically does for you when
        you're forced to endure the full moon's deadly whims. You 
        haven't looked at your messages to see how the party went. There's been
        more pressing matters to attend to. Namely, the stench of death that
        once again permeates your home and the dreadful mess you've made.
        
        It's not all of your friends but that's no consolidation. There is no
        acceptable amount of corpses. Only a concealable amount.""" +Fore.RED+ Style.BRIGHT+"""
        
        You work to hide your crimes away like they were nothing more than a
        dirty secret. And not for the first time you wished silver bullets
        worked on monsters like you the way fairy tales promised they would.
        
                                    Bad End""" + Fore.WHITE + Style.NORMAL
    
    ending13_text: str = Fore.WHITE + """
                       Well.... That could've gone """ +Fore.YELLOW+ Style.BRIGHT+ """better"""+Fore.WHITE+ Style.NORMAL+ """.                     

    The night of Johnny's party came and went without any unexpected
    interruptions. As usual, there was a considerable amount of dog hair to 
    vacuum up. It's a little embarrassing actually, be glad no one will ever 
    see what a filthy animal you are.
    
    Your phone is considerably quieter as you mill about your \'morning after\'
    chores. There's some alerts but not as many as what's usually expected 
    after one of Johnny's ragers.
    
    """ +Fore.YELLOW+ Style.BRIGHT+ """Perhaps you should've been kinder when turning down some of your friends.
    
                                    Bad End?""" +Fore.WHITE+ Style.NORMAL

    match victory:
        case 11: #1.1 condition, flawless victory- all alive, all positive
            print(ending1_text)

        case 12: #1.2 condition, atleast one guy died
            print(ending12_text)

        case 13: #1.3 condition, atleast one person hates you but none died
            print(ending13_text)

        case 20: #2 conditions- all eaten
            print(ending2_text)

        case 30: #3 conditions- all negative
            print(ending3_text)

        case _: #error case
            print("unknown ending...\n...\n..")
            print("bugged code srry")

    sleep_func(2)
    print(Style.DIM + "Game end\n...\n...\n...\n\n\n\n")
    sleep_func(2)
    exit_fun(True)
    
    checkp_score.clear()
    MainScore.clear()
    answered_questions.clear()
    global loaded_checkpoint
    loaded_checkpoint = False

def exit_fun(go_to_menuscreen=False) -> None:
    """Ask user if they want to save their progress, then exits programme

    Returns:
        None: None
    """
    if len(checkp_score) != 0:
        checkpoint_write = input(Fore.BLACK + "Do you want to save your progress? Type \"1\" for yes, anything else for no\n"+ Fore.WHITE +"-> ")
        if "1" in checkpoint_write:
            global loaded_checkpoint
            if loaded_checkpoint == True:
                with open("checkpoints.txt", "a") as fd:
                    for key, value in checkp_score.items():
                        if len(value[0]) == 3:
                            sc1, sc2, sc3 = value[0]
                            q1, q2, q3 = value[1]
                            fd.write(f"{key},{sc1},{sc2},{sc3},{q1},{q2},{q3}\n")
                        elif len(value[0]) == 2:
                            sc1, sc2 = value[0]
                            q1, q2 = value[1]
                            fd.write(f"{key},{sc1},{sc2},{q1},{q2}\n")
                        elif len(value[0]) == 1:
                            sc1, = value[0]
                            q1, = value[1]
                            fd.write(f"{key},{sc1},{q1}\n")
                        else:
                            print(Fore.RED + "Error, bad code alert!!" + Style.RESET_ALL)
                            exit()            
            else:    
                with open("checkpoints.txt", "w") as fd:
                    for key, value in checkp_score.items():
                        if len(value[0]) == 3:
                            sc1, sc2, sc3 = value[0]
                            q1, q2, q3 = value[1]
                            fd.write(f"{key},{sc1},{sc2},{sc3},{q1},{q2},{q3}\n")
                        elif len(value[0]) == 2:
                            sc1, sc2 = value[0]
                            q1, q2 = value[1]
                            fd.write(f"{key},{sc1},{sc2},{q1},{q2}\n")
                        elif len(value[0]) == 1:
                            sc1, = value[0]
                            q1, = value[1]
                            fd.write(f"{key},{sc1},{q1}\n")
                        else:
                            print(Fore.RED + "Error, bad code alert!!" + Style.RESET_ALL)
                            exit()
    if go_to_menuscreen == False:
        print(Fore.WHITE + "Thank you for playing\n Exiting Program . . . " + Style.RESET_ALL)
        exit()
    


if __name__ == '__main__':
    # Write all functions in here that will be called when running the program

    #This is the meat of our game! We formatted our NPC conversations into dictionaries instead of relying on numerous else-if statements.
    #intended answer weights: 1 = coming to house (-), 2 = no change (-+), 3 = hate you (+)
    person1: dict[str, list[list[str, int]]] = {"Cameron: Hey {player_name}, it’s Cam again. Just leaving you a mess-\nwait a minute… Holy hell, you picked up!": #Question-Answer dictionary
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
    person2: dict[str, list[list[str, int]]] = {"Dawn: {player_name}, I got a funny text from Cameron. He said you’re not\n going to the party tonight. I told him that was a pretty good joke but he\n says he’s serious, so how about you set the record straight for the both of us.": 
        [["1) Ugh… He’s right?", 2], 
        ["2) Okay first, you’re at an 11 when this should be a 4 conversation, and\n   second, yeah I’m staying in tonight.", 3], 
        ["3) I’m just not really feeling it tonight.", 1]], 
        "Dawn: And you thought I was just gonna let that go? C’mon, you know what I’m\nabout right? This is a no fly zone for BS {player_name} Are you gonna try to\npretend you have amnesia now?": 
        [["1) I have been feeling a bit forgetful lately.", 2], 
        ["2) There’s no forgetting an asshole like you.", 3], 
        ["3) No BS here, these ducks are neat and orderly in their rows.", 1]],
        "Dawn: Oh for the love of… Why do I hang out with you again?": 
        [["1) Your friend options are limited because you greet people by punching them?", 2], 
        ["2) I ask that same question every day.", 3], 
        ["3) Because I make the best damn enchiladas you’ve ever had.", 1]],
        "Dawn: That aside, since when do you skip out on free drinks and bad karaoke?\nDon’t give me any of that ‘I’m not feeling it’ crap. We both know that lie’s\nlike a cheap rug.": 
        [["1) I just don’t want to.", 2], 
        ["2) Stomach’s being weird, probably not good for drinking. It’ll lead to puking.", 3], 
        ["3) My karaoke is legendary, thank you.", 1]],
        "Dawn: So I’m just gonna tell you what I think. I think you're actively\navoiding us. You blew Cameron off twice in the past month.": 
        [["1) Hey, woah! Let’s back pedal a bit here, I am not avoiding anyone.", 2], 
        ["2) Alright maybe I did dodge a few hang outs, but you’re reaching pretty far \nhere.", 1], 
        ["3) It’s Sock. He’s just so… Wimpy.", 3]],
        "Dawn: You also seem to  find every excuse under the sun not to hang out\nwith Sock.": 
        [["1) What did I just say? Are you hard of hearing or something?", 3], 
        ["2) It's not that I don't want to hang out with Sock...", 2], 
        ["3) Yeah, and?", 3]],
        "Dawn: And let’s be very clear, only I am allowed to make fun of sad Sock.\nGot it?":
        [["1) Whatever.", 2], 
        ["2) Got it.", 1], 
        ["3) Okay buddy...", 3]],
        "Dawn: You get that privilege when you spend the better part of your last two\nyears of high school pulling straws out of his hair and un-gumming his locker.": 
        [["1) Well aren't you just a saint.", 2], 
        ["2) I feel like you also are one of the causes of the gum on his \n    locker.", 3], 
        ["3) That's... surprisingly nice of you. Ya'll go that far back?", 1]],
        "Dawn: If you come to the party you’ll get to hear all about the ancient\nhistory. I’ve got tons of stories about what those two chuckle heads got up\nto. No spoilers, that’s a live event or you wait for the day Cameron or Sock\nMAY tell you.": 
        [["1) Well... guess I gotta wait for one of them to spill the beans.", 2], 
        ["2) Not even a little spoiler?", 1], 
        ["3) Oh no... anyway.", 3]],
        "Dawn: Seriously {player_name}, you’re telling me with all that, you’d still\nrather rot in that crap apartment watching shitty reruns than hang out with\nus at one of Johnny's parties?": 
        [["1) No, but I just need to stay home and decompress tonight.", 1], 
        ["2) Absolutely.", 3], 
        ["3) It’s a toss up really, kind of worried about my… appetite.", 2]],
        "Dawn: Okay if I’m being for real though, I probably would ditch to if it\nwere to re-watch the last season of 12 Desperate Women and 1 Paid Actor.\nI’m more than certain at least one of those women were also paid actors.": 
        [["1) I. am. shocked.", 1], 
        ["2) Nah, no way dude.", 2], 
        ["3) I really don't care.", 3]],
        "Dawn: Pretty sure it was the one with the high cheekbones, sharp jawline, and\ntiny nose. Not that first one that everyone thinks of, the other one.": 
        [["1) That's so specific.", 2], 
        ["2) I really really don't care.", 3], 
        ["3) Rebecca? No... Tammy?", 1]],
        "Dawn: I know none of it’s real. I'm not a god damn moron. It’s fun to pick at\nbecause it’s so glaringly fake. Like eating chicken nuggets from Clown Burger.": 
        [["1) That's a weird connection between those two things.", 2], 
        ["2) Ugh, now I really want chicken nuggets. Damnit, Dawn.", 2], 
        ["3) At least you're not delusional.", 1]],
        "Dawn: Okaaaaay, trash tv aside. You do need to make some kind of effort here\nto hang out with us.": 
        [["1) I mean I really want to, but just not tonight.", 2], 
        ["2) Thank god, you're done going on and on about that.", 2], 
        ["3) I do make the effort!", 3]],
        "Dawn: Pretty sure the last time you hung out with all of us was at the beginning\nof the month. We all tried making breakfast with Cameron’s grandma’s prehistoric\nwaffle pan and it almost burned a hole in the counter.": 
        [["1) That only happened because Cameron’s an idiot.", 1], 
        ["2) Y’know, I think waffles are an acceptable reason to cause a house fire.", 2], 
        ["3) That wasn’t our best idea.", 1]],
        "Dawn: I’ve got half a mind to come down there and drag you out myself. How\nmuch do you weigh again? Nevermind, the exact number doesn’t matter, I’m\npretty sure I can deadlift your ass.": 
        [["1) NO! THAT IS FORBIDDEN! NO LIFTING OF THE ME!", 3], 
        ["2) That’s a lot of effort for you to waste on my feeble, pathetic ass.",2], 
        ["3) Wow.", 1]],
        "Dawn: Actually I’m certain I can. I’m up to 1.5x my own body weight. My new\nmetric is gonna be in how many {player_name}’s I can lift.": 
        [["1) That'd be kind of rad actually.", 1], 
        ["2) This is dumb. Why are you dumb?", 3], 
        ["3) No. Absolutely not. Don't ever. Bad!", 2]],
        "Dawn: Then you’re going to show up to prevent that very real possibility?\nCan't do much else to prevent the darkest timeline.": 
        [["1) I can hang up.", 3], 
        ["2) What if... we just didn't do that? Eh???", 2], 
        ["3) COME AT ME YOU COWARD!", 1]],
        "Dawn: Okay, I’ve got better. If threatening to chuck your ass like the\nuseless boulder you are doesn't work, then think of all the drunken\ndumbassery that you’re gonna miss out on! ...Not that I keep receipts of this\nstuff or anything.": 
        [["1) We both know that’s a lie. I don't even want to know how many lives\n   you've ruined.", 2], 
        ["2) Riiiiiight.", 1], 
        ["3) That's just... kind of awful.", 3]],
        "Dawn: Oh come on. What else keeps people in check other than the irrational\nfear that a stranger might think what they’re currently doing is really\nembarrassing? It makes for great currency.": 
        [["1) Now I am more than certain you run a blackmail ring.", 3], 
        ["2) That’s a red flag in a pile of red flags.", 2], 
        ["3) Ugh… getting uncomfortable.", 2]],
        "Dawn: Now you sound like sad Sock, ‘D-dawn that’s mu-mu-mu-mean!’ I can’t\ncarry two perpetual whiners, you need to pick a different role.": 
        [["1) How about the guy that stays home from parties?", 3], 
        ["2) Maybe I LIKE being a giant crybaby!", 1], 
        ["3) Or you could stop being such a jerk for five whole minutes?", 2]],
        "Dawn: This again? Shelve it. It’s kind of pathetic.": 
        [["1) Not as pathetic as you.", 2], 
        ["2) Alright fine, it’s shelved.", 1], 
        ["3) I’m forgetting what the purpose of this conversation was.", 3]],
        "Dawn: Yucks aside, whole point of this song and dance: You. Party. Tonight\nNon-negotiable. I’m getting tired of repeating the same thing. When is it\ngetting into your thick skull that you’re going to the party?": 
        [["1) I’m. Busy. Tonight. Non-negotiable.", 3], 
        ["2) I really can’t Dawn, I’ll try to make it up to you guys another time.", 1], 
        ["3) I just want to watch bad movies by myself and sleep, is that a crime?", 2]],
        "Dawn: Alright, you’ve forced my hand. I’m calling in the big guns. There’s\nno point in trying to stop me. It’s happening.": 
        [["1) What are you doing?", 2], 
        ["2) I swear if you show up at my house to try to lift me...", 2], 
        ["3) Dawn, please...", 3]],
        "Dawn: I’m messaging Sock and telling him you’re trying to flake on us. You\nleft me no choice.": 
        [["1) Ugh... why???", 2], 
        ["2) You absolute horse's ass! Stop it!", 3], 
        ["3) I mean... oh no?", 1]],
        "Dawn: Aaaaaaand done. Get ready for that because it’s going to be waaaaay\nworse than talking to me or Cameron was.": 
        [["1) You suck.", 3], 
        ["2) Thanks... really.", 2], 
        ["3) Okay, that's gonna be a time.", 1]],
        "Dawn: I tried to give you an out. Now you get to explain it to King\nWaterworks why one of his security buddies is going to be MIA.": 
        [["1) AAAAAAAAAAAAAAAAAA-", 3], 
        ["2) Yep, now I get to do that. Again, thanks.", 2], 
        ["3) I'm genuinely questioning the basis of our friendship right now.", 1]],
        "Dawn: Is it so hard to believe we’re all doing this because we haven’t seen\nyou in a while and want to hang out with you, {player_name}?": 
        [["1) You have a REALLY funny way of showing THAT.", 2], 
        ["2) I think you enjoy being as annoying as possible.", 3], 
        ["3) I mean... kind of with how you've gone about this?", 1]],
        "Dawn: That is the closest you are going to get to me saying anything of that\nsort. I don’t do mush.": 
        [["1) I don't think that can count as \'mush\'.", 1], 
        ["2) I guess that was... an attempt made.", 2], 
        ["3) We're aware.", 3]],
        "Dawn: Alright, I’m already regretting trying to appeal to pathos. Retracting\nall sentimentality. Just get your ass to the party.": 
        [["1) No.", 3], 
        ["2) Sorry, Dawn. Maybe next time.", 1], 
        ["3) This has been utterly exhausting. I need a nap.", 2]]}
    person2keys = list(person2.keys())
    person3: dict[str, list[list[str, int]]] = {"Sock: Ugh… heeeey {player_name}. Long time no see… or talk…": 
        [["1) Who is this again?", 2], 
        ["2) Oh, hey sock.", 1], 
        ["3) Ew, vermin in my dms!", 3]],
        "Sock: Are you really not going to Johnny’s party? It’s supposed to be a\ngood one since… y’know it’s one of *Johnny’s* parties…": 
        [["1) There's so many better things to do at home though...", 2], 
        ["2) No.", 3], 
        ["3) Maybe another time.", 1]],
        "Sock: Is it weird if I ask why? I mean, it’s your business and all but… I\ndon’t know {player_name}, I just feel weird going to one of those things without\nthe whole group.": 
        [["1) I want to eat chips and sleep instead.", 1], 
        ["2) Ugh... That's a secret...", 2], 
        ["3) Don't be such a wuss.", 3]],
        "Sock: I mean I guess it’s fine if you don’t want to go. It’l just be me,\nCameron, and Dawn…": 
        [["1) I believe in you space cadet.", 1], 
        ["2) You'll live.", 3], 
        ["3) Could be so much worse.", 2]],
        "Sock: So would you rather just want to hang out at your place instead? Not that\nI don’t want to go! I love parties!": 
        [["1) Oh no... no no no.", 2], 
        ["2) It's okay, you don't have to pretend.", 3], 
        ["3) Cool, have fun then!", 2]],
        "Sock: No I-I really love parties! With how loud everything is and how\neveryone is just in your face slurring…": 
        [["1) Wear headphones.", 3], 
        ["2) Aw yeah, it's the best!", 1], 
        ["3) It gets pretty annoying.", 2]],
        "Sock: I mean… It's what everyone likes to do and I want to hang out with\neveryone. I don’t want to muck up what already works.": 
        [["1) I can get that.", 1], 
        ["2) Why don't you plan your own thing?", 2], 
        ["3) You're kind of a doormat.", 3]],
        "Sock: I tried making a book club happen. No one actually read the books… I\ndon’t think Dawn even tried.": 
        [["1) Maybe pick better books?", 3], 
        ["2) That's rough buddy.", 1], 
        ["3) Sounds like something Dawn would do.", 2]],
        "Sock: It’s just… Why can’t we just do stuff that isn’t so loud and obnoxious?\nWhy does Johnny have to invite a bunch of weird people we’ve never met before?": 
        [["1) The more the merrier!", 1], 
        ["2) Have you tried earplugs?", 2], 
        ["3) Whiner, you're a whiner.", 3]],
        "Sock: It would be way better if it were just us. I really don’t like a bunch of\nstrangers looking at me and then I have to make small talk that I’m pretty sure\nthey don’t care about.": 
        [["1) Odds are no one is staring at you as hard as you think.", 1],
        ["2) Just talk to people, it's not hard.", 3], 
        ["3) Yeah...", 2]],
        "Sock: I just walk away feeling like I’ve made a giant idiot of myself and now\nthey’re laughing at me with the next person they talk to. ‘Hey see that person\nover there? They’ve never spent a day on earth before.’":
        [["1) Holy catastrophizing Manbat.", 3], 
        ["2) It can be scary putting yourself out there.", 1], 
        ["3) Uhm... you okay buddy?", 2]],
        "Sock: ‘They probably never leave their house that smells like old mustard,\ntheir friends are all carefully constructed lies assigned by the government,\nand they suck at dancing.’": 
        [["1) Sock, snap out of it!", 1], 
        ["2) Holy shit dude.", 3], 
        ["3) You do kinda smell like old mustard.", 2]],
        "Sock: Except the government wouldn’t assign me friends. You’d all\njust be like… alien surveillance agents here to make sure I don’t spread my\nsocial ineptitude to every actual human on this planet.": 
        [["1) When was the last time you went outside?", 1], 
        ["2) Yep, we're just the Sock Survelliance Experts.", 2], 
        ["3) No one would waste that kind of effort.", 3]],
        "Sock: Yeah… actually let’s just forget the whole thing. I’ll come hang out\nwith you tonight instead!": 
        [["1) Abort this mission!", 2], 
        ["2) No!", 3], 
        ["3) Let's think of something else to do here.", 1]],
        "Sock: It’ll be way better than whatever happens at Johnny’s place. Cam tried to\nget me excited about the whole thing because I guess Johnny got a new cat?": 
        [["1) Think of the horrible creature you're fond of!", 2], 
        ["2) No one would be excited by a cat.", 3], 
        ["3) Maybe it likes to be petted?", 1]],
        "Sock: The poor thing is probably going to be hiding under the couch the entire\ntime…": 
        [["1) Where it belongs.", 3], 
        ["2) Oh, poor goblin creature I guess.", 2], 
        ["3) Where it'll need a friend!", 1]],
        "Sock: It’s probably weird being a cat. Animals just blindly trust that we know\nwhat we’re doing and that what we’re doing is the correct thing.": 
        [["1) Pets have it rough.", 1], 
        ["2) Ugh... okay?", 2], 
        ["3) Who cares.", 3]],
        "Sock: My dog probably doesn’t even know when or if I’m coming home when I leave.\nHe’s just trusting that the loneliness is only temporary.": 
        [["1) Oh... oh no.", 1], 
        ["2) I'm worried about you, Sock.", 2], 
        ["3) Can you cut the crazy talk for five seconds?", 3]],
        "Sock: If I’m being honest… I wish I could just crawl under the furniture during\nthe party. I really don’t want to go if everyone isn’t gonna be there.": 
        [["1) Therapy. Acquire the therapy.", 2], 
        ["2) With enough alchohol, you too can crawl under the couch.", 1], 
        ["3) Yikes.", 3]],
        "Sock: Dawn says I should go because I have to at least try not to be a\nsniveling slug for my entire life but it’s just a lot, {player_name}.": 
        [["1) Wow, Dawn sure is a peach.", 2], 
        ["2) Yeah, I hear ya.", 1], 
        ["3) Slug Soooooooooock!", 3]],
        "Sock: They’re kind of a jerk but I think they mean well… I hope they do at least. They’re pretty excited about the karaoke.": 
        [["1) I guess...", 3], 
        ["2) Say \'potato\' if you need help.", 2],
        ["3) Oh god, not karoake again.", 1]],
        "Sock: We’re probably gonna have to listen to Dawn sing Seasoning Women again and\nthen complain that it wasn’t good because we didn’t want to join them for it.": 
        [["1) They never let me be Scary Spice.", 2], 
        ["2) NOOOOOOOO!", 3],
        ["3) It'll be a time.", 1]],
        "Sock: I was hoping maybe the movie thing would pan out but it looks like it’s\njust a bunch of dated horror flicks.": 
        [["1) Let me guess, too spooky for you?", 3], 
        ["2) The two Cam mentioned are actually not bad.", 2],
        ["3) It's so lame!", 1]],
        "Sock: They’re just boring, {player_name}. I don’t get why so many people go nuts\nfor the same thing over and over again.": 
        [["1) Something something consumerism.", 2], 
        ["2) I know right?", 1],
        ["3) Genuinely shocked that horror movies don't ruffle your feathers but\ntalking to strangers does.", 3]],
        "Sock: I threw in what was basically the movie version of the anime series\nTatami Galaxy. The art style is pretty neat.":
        [["1) What Galaxy?", 2], 
        ["2) Are people gonna be able to read subs that fast drunk?", 1],
        ["3) That movie sucks.", 3]],
        "Sock: That show was made over ten years ago though so I don’t know if anyone\ncares about it now.":
        [["1) Might be a bit of a deep cut.", 2], 
        ["2) Yeah, no one cares about it.", 3],
        ["3) It's still good even if it isn't recent.", 1]],
        "Sock: Maybe I can run away halfway through the party? Give it just enough time\nfor people to start drinking and then I sneak away. They’ll think the aliens\nfinally came back to take me home.":
        [["1) People are gonna report you as missing.", 3], 
        ["2) Sneaking out of a party isn't necessary.", 1],
        ["3) Just leave if you want to like a normal person.", 2]],
        "Sock: So you’re really, really serious about not going? Even though it’ll\nprobably be a giant disaster without you there?":
        [["1) I trust you to weather this storm.", 1], 
        ["2) Dead serious.", 3],
        ["3) I really can't tonight.", 2]],
        "Sock: I suppose… I guess I can try to find a way to survive with just Cameron\nand Dawn there…":
        [["1) Good luck!", 1], 
        ["2) It's not that bad.", 2],
        ["3) Okay, Sock.", 3]],
        "Sock: This is going to go one of two ways... maybe a fire somewhere in between…":
        [["1) Just don't make any waffles and you'll be fine.", 2], 
        ["2) You can do this!", 1],
        ["3) Send pics of Johnny's house burning.", 3]]} 
    person3keys = list(person3.keys())

    #change this to false when sending to prof
    debugmode = False


    checkp_score: dict[str, list[tuple[float,...], tuple[int,...]]] = {} #scores for people, index of questions answered
    MainScore = [] #idx+1 equals the number of friends you are conversing with, currently only one friend is available. will be in form [pers1, pers2,...,persX]   
    answered_questions: list[int] = []
    loaded_checkpoint = False
    if system() == 'Windows': #colorama thing
        just_fix_windows_console()
    init(autoreset=True)

    WholeProgram()