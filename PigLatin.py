'''ONE WORD ONLY!!!'''
def process():
    word = " ".join(input("Enter: ")).lower()
    word = word.split(' ')
    word.append(word[0])
    if word[0] in "aeiou":
        word.append("way")
    else:
        word.append("ay")
    word.pop(0)

    print("".join(word))
def unprocess():
    word = " ".join(input("Enter: "))
    word = word.split(' ')
    word.pop(-1)
    word.pop(-1)
    if word[-2] in "aeiou" and word[-1] == "w":
        word.pop(-1)
    word = list(word[-1])+word[:]
    word.pop(-1)

    print("".join(word))
while True:
    inp = input()
    if inp.lower() == "e":
        process()
    if inp.lower() == "d":
        unprocess()
