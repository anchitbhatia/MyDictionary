import json
from difflib import get_close_matches

def meaning(word):
    global data
    if word in data:
        return data[word]
    match = get_close_matches(word, data.keys())
    if len(match)>0:
        cont = input("Do you mean %s ? Enter y/n "%match[0]).lower()
        if cont =="y":
            return data[match[0]]
        elif cont =="n":
            return "Word doesn't exist !"
        else:
            return "Wrong entry !"
    else:
        return "Word doesn't exist !"

if __name__ == '__main__':
    data = json.load(open("data.json", "r"))
    while 1:
        w = input("Enter word : ").lower()
        m = meaning(w)
        if type(m)==list:
            for i in m:
                print(i)
        else:
            print(m)
        print("------")

