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

#how to call
# person1[person1keys[0]][2][1]  =  #question=idx > answer#=idx > score=1,answerstr=0
person2 = {

} #bully

person3 = {

} #meek


MainScore = [] #idx+1 equals person number
numofPeople = int(0)
startval = 1

#functions
def ScoreAnswer(score):
    result = -1



    #MainScore[idx] = int(MainScore * 0.75)
    return(result)
    #



def NextQuestion(scoremaybe, questionnumber):
    


    return()


def EndingGame():
    pass

def StartGame():
    numpeople = int(input("number of people: 1,2 or 3\n")) #sets number of people for game
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
    return()



def Updatelog():
    exit()
    #next submission



def MainFun():
    StartGame()


    
    
    return()







if __name__ == '__main__':
# Write all functions in here that will be called when running the program
    MainFun()