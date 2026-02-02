'''Hi!

This is a cipher I made! 
if you decrypt a message someone gave you,
you will find no spaces and maybe find an extra x at the end.

This is normal!
Just remove the x and add spaces where necessary!

    -Noomklaw
'''
running = True

def encrypt():
    text = input("Enter text: ").replace(" ", "")
    text_list = list(text)
    
    if len(text_list) % 2 != 0:
        text_list.append("x")
        
    midpoint = len(text_list) // 2
    l1 = text_list[:midpoint]
    l2 = text_list[midpoint:]
    
    final_word = []
    for i in range(midpoint):
        final_word.append(l1[i])
        final_word.append(l2[i])
        
    print("Encrypted:", "".join(final_word))

def decrypt():
    text = input("Enter text: ").replace(" ", "")
    if len(text) % 2 != 0:
        text += "x"
        
    midpoint = len(text) // 2
    final_word = []
    
    for i in range(midpoint):
        final_word.append(text[2*i])
    
    for i in range(midpoint):
        final_word.append(text[2*i + 1])
        
    print("Decrypted:", "".join(final_word))
    
while running:
    while True:
        mode = input("encrypt or decrypt?(e,d)")
        if mode.lower() == "e":
            break
        elif mode.lower() == "d":
            break
        else:
            print("Enter a valid option")
    if mode == "e":
        encrypt()
    else:
        decrypt()
    rep = input("Want to go again?(n for no)")
    if rep.lower() == "n":
        running = False
    
