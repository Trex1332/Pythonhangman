import random
easy = "easy.txt"
med = "med.txt"
hard = "hard.txt"





#get user input
def main():
    word = randomword(easy).lower()
    current = getblankword(word)
    lives = 8
    usedletters = set()
    print(" ".join(current))
    print(word)
    while True:
        guess = input("Guess word Or Letter: ")

        if len(guess) > 1:
            if guess == word:
                print("win")
                break
            else:
                lives -= 1
                print(f"Incorrect you have {lives} left")
        else:
            if guess in word:
                num = 0
                for x in word:
                    
                    if x == guess:
                        current[num] = guess
                    num +=1
        print(" ".join(current))
        if "".join(current) == word:
            print("win")
            break
       




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