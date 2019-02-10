#AMG Addition - amg_a
#Purpose: To add an AMG onto a character's model with their AMO0
#Not to be used with characters with no space left, please add an extra line
#before using this, please using the extra line function

print("Please only insert the AMO of a character")
print("With this you can only add one AMG at a time")

import struct
import math

def main():
    print("AMG Editor, Insert AMG file:")

    #only will add the amg and will not edit any texture or shader values
    #on the amg jsut yet, this will be later after the main code is done

    x = input("")
    amg = open(x, "r+b")
    amg.seek(28)
    amg_length = amg.read(3)
    amg.seek(0)
    amg_copy = amg.read()
   # print(amg_length)

    print("Insert AMO file:")
    x = input("")
    f = open(x, "r+b")
    chunk = f.read(16)
    f.seek(0)

    #grabing values like length of amo, amount of amgs, etc

    f.seek(24)#amount of amgs
    am_amg = f.read(1)
    am_amg = int(am_amg.hex(), 16)
    #print(am_amg)
    
    #f.seek(0)
    #f.seek(23)
    #f.write(am_amg)

    f.seek(0)

    f.seek(36)#length of amo
    len_amo = f.read(3)
    len_amo = int(len_amo.hex(), 16)

    f.seek(0)

    amo_head = 48#finding the next empty space
    next_space = (amo_head + (am_amg * 4)) 
    f.seek(next_space)
    #print(f.tell())

    f.seek(0,2)#goes to end of file, pastes the amg, gets it's location
    amg_loc = f.tell()
    amg_ax_loc = amg_loc + 32
    #print(f.tell())
    #print("locbelow")
    #print(amg_ax_loc)
    f.write(amg_copy)
    f.seek(0)

    f.seek(next_space)#seeks to the next space and writes the offset
    amg_loc = struct.pack("<I", amg_loc)
    
    f.write(amg_loc)

    f.seek(0)

    #asks what axis to replace in decimal, user must know what to replace
    print("start counting from _body axis...")
    ax_to_rep = int(input("Number of axis to replace (dec.): "))
    ax_to_rep -= 1
    #print(ax_to_rep)
    ax_to_rep = int(ax_to_rep)
    #print(ax_to_rep)
    ax_to_rep = struct.pack("<I", ax_to_rep)
    #print(ax_to_rep)
    #print(ax_to_rep[0])

    #ax_to_rep_line = (ax_to_rep + b"\x00\x00\x00")
    #print(ax_to_rep_line)

    atp_offset = []

    f.seek(0)

    #searches for all axis points with the id
    while chunk != b"":
        if chunk[4] == ax_to_rep[0] and chunk[5] == ax_to_rep[1] and chunk[6] == ax_to_rep[2] and chunk[7] == ax_to_rep[3]:
            atp_offset.append(((f.tell() - 16)))
            print(f.tell()-16)
        chunk = f.read(16)

    #changes amg_ax_loc to bytes to write
    amg_ax_loc = struct.pack("<I", amg_ax_loc)

    #certain ids will be found throughout the file, so it will be cut out with
    #the amount of times it should be there
    #print(len(atp_offset))
    f.seek(0)
    f.seek(32)
    am_axis = f.read(1)
    #print(am_axis)
    am_axis = int(am_axis.hex(), 16)
    #print(am_axis)
    atp_offset = atp_offset[0:am_axis]
    #print(len(atp_offset))

    
    #doesn't change id since it doesn't matter, only offset is changed
    for i in atp_offset:
        f.seek(i+8)
        f.write(amg_ax_loc)


    #misc actions, editing the length of amo, editing the amg amount
    f.seek(0)
    f.seek(24)
    am_amg += 1
    am_amg = struct.pack("<I", am_amg)
    f.write(am_amg)
    f.seek(0)
    f.seek(0,2)
    len_amo = f.tell()
    len_amo = struct.pack("<I", len_amo)
    f.seek(0)
    f.seek(36)
    f.write(len_amo)
    

    f.close()
    amg.close()

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
