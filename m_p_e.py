#Model Part Editor (MPE)
#Purpose of this sub-program - To edit the model parts of a character file i.e.
#Editing the texture number, shader number, border number and model type

options = ["Border", "Shader Fix"]
border_option = ["r", "a"]

def main():
    y = input("Insert name of file: ")
    f = open(y, "r+b")
    print("")
    print(options)
    print("What would you like to do? ")
    x = input("")
    while x not in options:
        x = input("That is not a valid option, please select from above: ")
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
