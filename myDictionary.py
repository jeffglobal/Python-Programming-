import json
# from difflib import get_close_matches

data = json.load(open('data.json'))


def myDictionary(word):        # Remember 'word' is local variable
    word = word.lower()
    if word in data:
        return data[word]
    else:
        return 'I don\'t have that word in my Dictionary'


word = input('What word are you looking for?')

print(myDictionary(word))       # Remember 'word' is global variable

