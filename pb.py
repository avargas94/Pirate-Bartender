import random

questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?",
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"],
}

qresults = {}

def askQuestions():
    for c, q in questions.items():
        print("{} Please enter Yes or No".format(q))
        val = input().capitalize()
        if val == "Yes": qresults.update({c: True})
        else: qresults.update({c: False})
    return qresults


def constructDrink(x):
    r = {}
    for f, y in x.items():
        if f in ingredients and y == True:
            ing = ingredients[f]
            r.update({f: random.choice(ing)})
    
    print("With what your taste buds are feeling right now. Your drink will have the following ingredients!")
    for d, n in r.items(): print(n)

if __name__ == '__main__':
    askQuestions()
    constructDrink(qresults)
    