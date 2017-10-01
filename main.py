import json
from difflib import get_close_matches

def meaning(word):
    global data
    if word in data:
        return data[word]
    match = get_close_matches(word, data.keys())
    return "Do you mean " + str(match)

if __name__ == '__main__':
    data = json.load(open("data.json", "r"))
    while 1:
        w = input("Enter word : ").lower()
        print( meaning(w))
        print("------")

