from random import choice
import json
    
def ReadFile():
    with open("settings.json", "r") as f:
        return json.load(f)

def SaveFile(dictionary):
    with open("settings.json", "w") as f:
        json.dump(dictionary, f, indent=4)

class Settings:
    
    def  __init__(self):
        settings = ReadFile()
        self.turns = settings["turns"]
        self.level = settings["level"]
        self.words = settings["words"]
        
        
    def change_turns(self):
        chances = int(input("Enter the number of wrong attempts you want- "))
        settings = ReadFile()
        settings["turns"] = chances
        SaveFile(settings)
        self.turns = chances
        
        
    def change_level(self):
        difficulty = None
        while not difficulty:
            try:
                difficulty=int(input("Enter the level you want (Select from 1/2/3)- "))
                if difficulty not in [1,2,3]:
                    difficulty = None
                    raise ValueError
            except ValueError:
                print("(Select from 1/2/3")
         
        settings = ReadFile()
        settings["level"] = difficulty
        SaveFile(settings)
        self.level = difficulty
    
            
    def custom_wordset(self):
        new_word=input("Enter a new word you want to add to the game- ")
        settings = ReadFile()
        
        if len(new_word) in range(2,4):
            settings['words']['easy'].append(new_word.lower())
            print("Word added to easy list")
        elif len(new_word) in range(5,6):
            settings['words']['medium'].append(new_word.lower())
            print("Word added to medium list")
        else:
            settings['words']['hard'].append(new_word.lower())
            print("Word added to hard list")
        
        self.words = settings['words']
        SaveFile(settings)