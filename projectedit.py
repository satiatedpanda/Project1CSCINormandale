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

Mainscore = [] #idx+1 equals person number
scorecard = []

numofPeople = int(0)
startval = 1 #this changes the starting number in MainScore 

#functions
#call score from questions
#MainScore[idx] = int(MainScore * 0.75)
def ScoreAnswer(score):
    result = 0
    result += sum(scorecard) #add scores to get result
    if result > 15: #placeholder value is 15 - median
        Mainscore.append(result)
    else:
        pass
    return(result)

def NextQuestion(score, questionNum):
    question = ""
    answers = []
    scorecard.append(answers(input()))
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
    pass



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