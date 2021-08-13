import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def getDefinition(word):
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys(),1)) > 0:
        correction = input("Did you mean %s? Enter Y if yes, or N if no. " % get_close_matches(word, data.keys(),1))
        if correction == "Y":
            return data[get_close_matches(word, data.keys(),1)[0]]
        elif correction == "N":
            return "Please re-enter word."
        else:
            return "We didn't understand your entry"
    else:
        return "The word doesn't exist. Please re-enter word."

word = input("Enter Word: ").lower()

output = getDefinition(word)

if type(output) == list:
    for defintion in output:
        print(defintion)
else:
    print(output)



