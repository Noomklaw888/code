letters = "q w e r t y u i o p a s d f g h j k l z x c v b n m Q W E R T Y U I O P A S D F G H J K L Z X C V B N M ` 1 2 3 4 5 6 7 8 9 0 - = [ ] \\ ; ' , . / ~ ! @ # $ % ^ & * ( ) _ + { } | : \" < > ?".split()
letters.append(" ")
x = ""
w = ""
def get():
    global s, w
    while True:
        try:
            s = input("Enter shift: ")
            s = int(s)
            if isinstance(s, int):
                break
            else:
                print("Please enter a whole number")
        except ValueError:
            print("Please enter a whole number")
    w = input("Enter word: ")    
def cipher(shift, word):
    new_word = ""
    for i in range(len(word)):
        x = letters.index(word[i])
        new_word += letters[(x+shift)%len(letters)]
    print(new_word)

print("Welcome to my cipher program!")
print("Type E to encrypt, D to decrypt, or Q to quit")
while True:
    hi = input()
    if hi.lower() == "e":
        get()
        cipher(s,w)
    elif hi.lower() == "d":
        get()
        cipher(-s,w)
    elif hi.lower() == "q":
        break
    else:
        print("Please enter a valid input")
