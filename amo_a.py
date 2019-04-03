# AMO line adder - amo_a
# Purpose: To add extra lines in the AMO for more AMG space for use in Budokai series


import struct
import math
import os


def main():
    print("")
    print("AMO name? (add extension)")
    x = input("")
    x = x.replace("\"", "")
    f = open(x, "r+b")

    # Copying files needed
    hti = 0
    ith = 0
    line = open("Files\lines.bin", "r+b")
    line = line.read()

    # Setting up temp bins
    tn1 = "Files\z.bin"  # Will hold edited bin
    temp1 = open(tn1, "w+b")
    temp1.close()
    temp1 = open(tn1, "r+b")
    tn2 = "Files\z2.bin"  # Will hold First Part
    temp2 = open(tn2, "w+b")
    temp2.close()
    temp2 = open(tn2, "r+b")
    tn3 = "Files\z3.bin"  # Will hold Second Part
    temp3 = open(tn3, "w+b")
    temp3.close()
    temp3 = open(tn3, "r+b")
    tn4 = "Files\z4.bin"  # Will hold Third Part
    temp4 = open(tn4, "w+b")
    temp4.close()
    temp4 = open(tn4, "r+b")
    tn5 = "Files\z5.bin"  # Will hold AMGs
    temp5 = open(tn5, "w+b")
    temp5.close()
    temp5 = open(tn5, "r+b")

    # Pasting parts into temp bins
    # 1st Part
    f.seek(20)
    hti = f.read(4)
    size = hex_to_int(hti, f, temp1, temp2, temp3, temp4)
    f.seek(0)
    t_copy = f.read(size)
    temp2.write(t_copy)
    # 2nd Part
    f.seek(16)
    hti = f.read(4)
    p2_amount = hex_to_int(hti, f, temp1, temp2, temp3, temp4)
    size = p2_amount* 32
    f.seek(20)
    hti = f.read(4)
    offset = hex_to_int(hti, f, temp1, temp2, temp3, temp4)
    f.seek(offset)
    t_copy = f.read(size)
    offset = f.tell()
    temp3.write(t_copy)
    # 3rd Part
    f.seek(16)
    hti = f.read(4)
    amount = hex_to_int(hti, f, temp1, temp2, temp3, temp4)
    f.seek(32)
    hti = f.read(4)
    size = hex_to_int(hti, f, temp1, temp2, temp3, temp4)
    p3_amount = size
    size = size * 16 * amount
    f.seek(offset)
    t_copy = f.read(size)
    temp4.write(t_copy)
    # AMGs
    t_copy = f.read()
    temp5.write(t_copy)

    # Gather information from user
    print("How many extra lines do you want to add?")
    amount = int(input(""))

    #print("")
    #print("DEBUG: First Part")
    # EDITING FIRST PART:
    # Changing size of first part and total model size while adding extra lines
    temp2.seek(20)
    hti = temp2.read(4)
    size = hex_to_int(hti, f, temp1, temp2, temp3, temp4)
    temp2.seek(size)
    for i in range(amount):
        temp2.write(line)
    temp2.seek(20)
    size = size + (amount*16)
    ith = size
    size = int_to_hex(ith, f, temp1, temp2, temp3, temp4)
    temp2.write(size)
    temp2.seek(36)
    hti = temp2.read(4)
    size = hex_to_int(hti, f, temp1, temp2, temp3, temp4) + (amount * 16)
    ith = size
    size = int_to_hex(ith, f, temp1, temp2, temp3, temp4)
    temp2.seek(36)
    temp2.write(size)
    # Editing the offsets for all of the AMGs
    temp2.seek(24)
    hti = temp2.read(4)
    amgs = hex_to_int(hti, f, temp1, temp2, temp3, temp4)
    temp2.seek(48)
    for i in range(amgs):
        hti = temp2.read(4)
        offset = hex_to_int(hti, f, temp1, temp2, temp3, temp4) + (amount*16)
        ith = offset
        offset = int_to_hex(ith, f, temp1, temp2, temp3, temp4)
        temp2.seek(temp2.tell()-4)
        temp2.write(offset)

    #print("")
    #print("DEBUG: Second Part")
    # EDITING SECOND PART:
    # Changing all offsets in first column
    temp3.seek(16)
    for i in range(p2_amount):
        hti = temp3.read(4)
        offset = hex_to_int(hti, f, temp1, temp2, temp3, temp4)
        temp3.seek(temp3.tell()-4)
        if offset == 0:
            "Nothing"
        else:
            offset = offset + (amount*16)
            ith = offset
            offset = int_to_hex(ith, f, temp1, temp2, temp3, temp4)
            temp3.write(offset)
            temp3.seek(temp3.tell() - 4)
        temp3.seek(temp3.tell() + 32)
    # Changing all offsets in second column
    temp3.seek(4)
    for i in range(p2_amount*2):
        hti = temp3.read(4)
        offset = hex_to_int(hti, f, temp1, temp2, temp3, temp4)
        temp3.seek(temp3.tell() - 4)
        if offset == 0:
            "Nothing"
        else:
            offset = offset + (amount * 16)
            ith = offset
            offset = int_to_hex(ith, f, temp1, temp2, temp3, temp4)
            temp3.write(offset)
            temp3.seek(temp3.tell() - 4)
        temp3.seek(temp3.tell() + 16)
    # Changing all offsets in third column
    temp3.seek(8)
    for i in range(p2_amount*2):
        hti = temp3.read(4)
        offset = hex_to_int(hti, f, temp1, temp2, temp3, temp4)
        temp3.seek(temp3.tell() - 4)
        if offset == 0:
            "Nothing"
        else:
            offset = offset + (amount * 16)
            ith = offset
            offset = int_to_hex(ith, f, temp1, temp2, temp3, temp4)
            temp3.write(offset)
            temp3.seek(temp3.tell() - 4)
        temp3.seek(temp3.tell() + 16)
    # Changing all offsets in fourth column
    temp3.seek(12)
    for i in range(p2_amount * 2):
        hti = temp3.read(4)
        offset = hex_to_int(hti, f, temp1, temp2, temp3, temp4)
        temp3.seek(temp3.tell() - 4)
        if offset == 0:
            "Nothing"
        else:
            offset = offset + (amount * 16)
            ith = offset
            offset = int_to_hex(ith, f, temp1, temp2, temp3, temp4)
            temp3.write(offset)
            temp3.seek(temp3.tell() - 4)
        temp3.seek(temp3.tell() + 16)

    #print("")
    #print("DEBUG: Third Part")
    # EDITING THIRD PART:
    # Changing all offsets in first column
    temp4.seek(8)
    for i in range(p2_amount*p3_amount):
        hti = temp4.read(4)
        offset = hex_to_int(hti, f, temp1, temp2, temp4, temp4) + (amount * 16)
        temp4.seek(temp4.tell() - 4)
        ith = offset
        offset = int_to_hex(ith, f, temp1, temp2, temp4, temp4)
        temp4.write(offset)
        temp4.seek(temp4.tell() + 12)

    # Assembles and Saves new AMO
    temp1.close()
    temp1 = open(tn1, "r+b")
    temp2.close()
    temp2 = open(tn2, "r+b")
    temp3.close()
    temp3 = open(tn3, "r+b")
    temp4.close()
    temp4 = open(tn4, "r+b")
    temp5.close()
    temp5 = open(tn5, "r+b")
    t_copy = temp2.read()
    temp1.write(t_copy)
    t_copy = temp3.read()
    temp1.write(t_copy)
    t_copy = temp4.read()
    temp1.write(t_copy)
    t_copy = temp5.read()
    temp1.write(t_copy)
    temp1.seek(0)
    t_copy = temp1.read()
    f = open(x, "w+b")
    f.write(t_copy)
    f.close()
    print("")
    print("Completed!")

    # deletes temp files
    tn1 = "Files\z.bin"
    temp1 = open(tn1, "r+b")
    temp1.close()
    tn2 = "Files\z2.bin"
    temp2 = open(tn2, "r+b")
    temp2.close()
    tn3 = "Files\z3.bin"
    temp3 = open(tn3, "r+b")
    temp3.close()
    tn4 = "Files\z4.bin"
    temp4 = open(tn4, "r+b")
    temp4.close()
    tn5 = "Files\z5.bin"
    temp5 = open(tn5, "r+b")
    temp5.close()
    os.remove(tn1)
    os.remove(tn2)
    os.remove(tn3)
    os.remove(tn4)
    os.remove(tn5)


def hex_to_int(hti, f, temp1, temp2, temp3, temp4):
    # Converts hex offsets to integer format
    hti = hti.hex()
    hti = int(hti, 16)
    hti = struct.pack('<L', hti)
    hti = hti.hex()
    hti = int(hti, 16)
    #print("DEBUG:HTI - " + str(hti))
    return hti


def int_to_hex(ith, f, temp1, temp2, temp3, temp4):
    # Opposite of hex_to_int
    ith = struct.pack('<L', ith)
    #print("DEBUG:ITH - " + str(ith))
    return ith


def again():
    yn = input("Would you like to load another? (Y/N)")
    yn = yn.lower()
    if yn == "y" or yn == "yes":
        main()
        again()
    else:
        print("")
        print("AMO line adder by: Nexus-sama")
        print("Follow me on Twitter @NexusTheModder")
        print("")
        kill = input("press enter to close")


main()
again()

exit()
