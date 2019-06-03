#Model Part Editor (MPE)
#Purpose of this sub-program - To edit the model parts of a character file i.e.
#Editing the texture number, shader number, border number and model type

options = ["Border", "Shader Fix"]
border_option = ["r", "a"]
#print("You can shorten the phrases to one letter 'Border' = 'b', 'shader fix' = 'sf', and so on")



def mpe(f):
    ##code for model part extractor
    print("")
    counter = 0
    mpe_offsets = []
    print("Gathering model part locations...")
    chunk = f.read(16)
    while chunk != b"":
        if chunk[0] == 0xB5 and chunk[1] == 0x01:
            mpe_offsets.append(((f.tell()-16)))
            counter += 1
        if chunk[0] == 0xB4 and chunk[1] == 0x01:
            mpe_offsets.append(((f.tell()-16)))
            counter += 1
        if chunk[0] == 0xB5 and chunk[1] == 0x21:
            mpe_offsets.append(((f.tell()-16)))
            counter += 1
        if chunk[0] == 0xB4 and chunk[1] == 0x11:
            mpe_offsets.append(((f.tell()-16)))
            counter += 1
        if chunk[0] == 0xB4 and chunk[1] == 0x21:
            mpe_offsets.append(((f.tell()-16)))
            counter += 1
        if chunk[0] == 0xBD and chunk[1] == 0x01:
            mpe_offsets.append(((f.tell()-16)))
            counter += 1
        if chunk[0] == 0xBD and chunk[1] == 0x11:
            mpe_offsets.append(((f.tell()-16)))
            counter += 1
        if chunk[0] == 0xFF and chunk[1] == 0xFF:
            mpe_offsets.append(((f.tell()-16)))
            counter += 1
        chunk = f.read(16)
    print("Model parts located!")
    print("")
    mep_op = ["Texture Swap", "Shader Swap", "Invisible", "MPExtractor"]
    print(mep_op)
    print("What would you like to do?")
    ch = input("")
    if ch == "Texture Swap" or ch == "ts":
        print("")
        print(mpe_offsets)
        print("There are", counter, "many model parts, give me a texture number to search through and further options shall be shown")
        #add that shiiiettt
        
    if ch == "Shader Swap" or ch == "ss":
        print("building")
        print("There are", counter, "many model parts, give me a texture number to search through and further options shall be shown")
        #and this
        
    if ch == "Invisible" or ch == "i":
        print("building")
        print("There are", counter, "many model parts, give me a texture number to search through and further options shall be shown")
        #this toooo
        
    if ch == "MPExtractor" or ch == "mpe":
        print("building")
        print("There are", counter, "many model parts, give me a texture number to search through and further options shall be shown")
        #yeetus
        
    
        


def main():
    y = input("Insert name of file (AMO0 Only): ")
    y = y.replace("\"", "")
    f = open(y, "r+b")
    print("")
    print(options)
    print("What would you like to do? ")
    x = input("")
    if x == "Border" or x == "b":
        #blah blah
        choice = input("Remove or Add borders? (r/a): ")
        while choice not in border_option:
            choice = input("Not an option, enter again (r/a): ")
        if choice == "r":
            chunk = f.read(16)
            offsets = []
            counter = 0
            while chunk != b"":
                if chunk[0] == 0x1 and chunk[8] == 0x46:
                    offsets.append(((f.tell()-16)))
                    #print(hex(f.tell()-16))
                    counter += 1
                chunk = f.read(16)

            for i in offsets:
                f.seek(i+8)
                f.write(b"\x47")
                f.seek(i+8)
                f.write(b"\x47")
            print("Replaced", counter, "values with 47")
            f.close()
        if choice == "a":
            chunk = f.read(16)
            offsets = []
            counter = 0
            while chunk != b"":
                if chunk[0] == 0x1 and chunk[8] == 0x47:
                    offsets.append(((f.tell()-16)))
                    #print(hex(f.tell()-16))
                    counter += 1
                chunk = f.read(16)

            for i in offsets:
                f.seek(i+8)
                f.write(b"\x46")
                f.seek(i+8)
                f.write(b"\x46")
            print("Replaced", counter, "values with 46")
            f.close()

    if x == "Shader Fix" or x == "sf":
        print("Converting all B4 01 model parts to B4 62...")
        chunk = f.read(16)
        offsets = []
        counter = 0
        shader_number = int(input("Give the number of shader (in hex): "))
        shader = shader_number
        shader_number = chr(shader_number)
        shader_number = bytes(shader_number, ("utf-8"))
        while chunk != b"":
            if chunk[0] == 0xB4 and chunk[12] == 0xFF:
                offsets.append(((f.tell()-16)))
                #print(hex(f.tell()-16))
                counter += 1
            chunk = f.read(16)
        for i in offsets:
            f.seek(i+1)
            f.write(b"\x62")
            f.seek(i+4)
            f.write(b"\xBD")
            f.seek(i+5)
            f.write(B"\x29")
            f.seek(i+12)
            f.write(shader_number)
            f.seek(i+13)
            f.write(b"\x00")
            f.seek(i+14)
            f.write(b"\x00")
            f.seek(i+15)
            f.write(b"\x00")
        print("Replaced", counter, "of FFs with 0" + str(shader), "00 00 00")
        print("")
        f.close()

    if x == "Model Part Extraction" or x == "mpe":
        mpe(f)

    else:
        print("not an option, please try again")
        f.close()
        again()

        
def again():
    yn = input("Load another? (Y/N)")
    yn = yn.lower()
    yn = yn[0:1]
    if yn == "y":
        main()
        again()
    else:
        kill = input("press enter to close")





    
main()
again()
exit()
