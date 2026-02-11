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
person1Questions = {} #food guy
person2Questions = {} #bully
Person3Questions = {} #meek

MainScore = [1, 1, 1] #idx+1 equals person number



def ScoreAnswer(answer):
    result = 0


    return(result)
    #


def NextQuestion(scoremaybe, questionnumber):
    


    return()



def EndingGame():

    exit()

def StartGame():
    return()



def Tutorial():
    return()



def Updatelog():
    exit()
    #next submission



def MainFun():
    while True: #asks for input to do tutorial or not
        try:
            tutorial = input("Do Tutorial? Y/n\n")
            corlist = ["Y", "n"]
            if tutorial not in corlist:
                raise ValueError
            break
        except ValueError:
            print("Invalid input, please type exactly \"Y\" or \"n\"\n")
        #block was found in stackoverflow: https://stackoverflow.com/questions/41832613/python-input-validation-how-to-limit-user-input-to-a-specific-range-of-integers
    
    
    
    return()







if __name__ == '__main__':
    MainFun()