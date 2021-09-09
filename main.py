import json
from difflib import get_close_matches

data=json.load(open("data.json"))

def translate(word):
    if word in data:
          return data[word]
    elif (word.lower() in data):
        return data[word.lower()]
    elif (word.upper() in data):
        return data[word.upper()]
    elif word.title() in data:
        return data[word.title()]


    elif len(get_close_matches(word, data.keys()))>0:
        yesorno=input("Did you mean %s instead?Enter y if yes and n if no"% get_close_matches(word,data.keys())[0])
        yesorno=yesorno.lower()
        if yesorno=="y":
            return data[get_close_matches(word,data.keys())[0]]
        elif yesorno=="n":
            return "Word doesn't exist in the dictionary.Please double check it."

        else:
            return "Sorry ,We don't get it."
    else:
        return "Word doesn't exist in the dictionary.Please double check it."
word=input("enter word:")
output=translate(word)
if type(output)==list:
     for i in output:
        print(i)
else:
    print(output)
