#Budokai 1 Exporter (B1E)
#Purpose of this sub-program - To export any Budokai 1 model into a Non-Budokai 1 Game
#Editing the shader number, model part number and general data


def main():
    y = input("Insert file: ")
    y = y.replace("\"", "")
    f = open(y, "r+b")
    chunk = f.read(16)
    offsets = []
    counter = 0
    print("What is the number of the shader you want (hex): ")
    shader_number = int(input(""))
    shader = shader_number
    shader_number = chr(shader_number)
    shader_number = bytes(shader_number, ("utf-8"))
    
    while chunk != b"":
        if chunk[0] == 0xBD and chunk[1] == 0x11:
            offsets.append(((f.tell()-16)))
            #print(hex(f.tell()-16))
            counter += 1
        if chunk[0] == 0xBD and chunk[1] == 0x01:
            offsets.append(((f.tell()-16)))
            #print(hex(f.tell()-16))
            counter += 1
        chunk = f.read(16)
    for i in offsets:
        f.seek(i+0)
        f.write(b"\xB5")
        f.seek(i+1)
        f.write(b"\x01")
        f.seek(i+4)
        f.write(b"\xBD")
        f.seek(i+5)
        f.write(b"\x29")
        f.seek(i+12)
        f.write(shader_number)
        f.seek(i+13)
        f.write(b"\x00")
        f.seek(i+14)
        f.write(b"\x00")
        f.seek(i+15)
        f.write(b"\x00")
        f.seek(i+32)
        f.write(b"\x00")
        f.seek(i+33)
        f.write(b"\x00")
        f.seek(i+34)
        f.write(b"\x80")
        f.seek(i+35)
        f.write(b"\x3f")
        f.seek(i+36)
        f.write(b"\x00")
        f.seek(i+37)
        f.write(b"\x00")
        f.seek(i+38)
        f.write(b"\x80")
        f.seek(i+39)
        f.write(b"\x3f")
        f.seek(i+40)
        f.write(b"\x00")
        f.seek(i+41)
        f.write(b"\x00")
        f.seek(i+42)
        f.write(b"\x80")
        f.seek(i+43)
        f.write(b"\x3f")
        f.seek(i+44)
        f.write(b"\x00")
        f.seek(i+45)
        f.write(b"\x00")
        f.seek(i+46)
        f.write(b"\x80")
        f.seek(i+47)
        f.write(b"\x3f")
        f.seek(i+48)
        f.write(b"\x00")
        f.seek(i+49)
        f.write(b"\x00")
        f.seek(i+50)
        f.write(b"\x80")
        f.seek(i+51)
        f.write(b"\x3f")
        f.seek(i+52)
        f.write(b"\x00")
        f.seek(i+53)
        f.write(b"\x00")
        f.seek(i+54)
        f.write(b"\x80")
        f.seek(i+55)
        f.write(b"\x3f")
        f.seek(i+56)
        f.write(b"\x00")
        f.seek(i+57)
        f.write(b"\x00")
        f.seek(i+58)
        f.write(b"\x80")
        f.seek(i+59)
        f.write(b"\x3f")
        f.seek(i+60)
        f.write(b"\x00")
        f.seek(i+61)
        f.write(b"\x00")
        f.seek(i+62)
        f.write(b"\x80")
        f.seek(i+63)
        f.write(b"\x3f")

    print(str(counter) + " model parts of Budokai 1 model converted to Budokai 3 with shader as 0" + str(shader) + " 00 00 00")
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
