import random
easy = "easy.txt"
med = "med.txt"
hard = "hard.txt"





#get user input
def main():
    word = randomword(easy)
    current = getblankword(word)




def randomword(dificulty):
    words = []
    f = open(dificulty, "r")
    for x in f:
        words.append(x.strip())
    x = random.randrange(0,len(words))
    return words[x]

    


def getblankword(word):
    blank = []
    for x in word:
        blank.append("_")
    return blank




main()