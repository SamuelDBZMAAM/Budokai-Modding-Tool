#AMM Tail Animator - amm_ta
#Purpose: To give characters without tail animations tail animations


import struct
import math
import os


def bsk_type():
    #Let's the user select bin type
    print("Main BSK (Large in size with AMMs) or Special BSK (Small in size w/o AMMs)?(M/S):")
    b_type = input("")
    if b_type == "M" or b_type == "m":
        main()
    elif b_type == "S" or b_type == "s":
        special()
    else:
        print("Please type 'M' or 'S'!")
        bsk_type()

def main():
    # opens BSK
    print("BSK name (with extension):")
    x = input("")
    x = x.replace("\"", "")
    f = open(x, "r+b")
    print("Which tail animation would you like to use?")
    print("SSJ4, Cell, Frieza, Cooler?(S/C/F/CO)")
    tail_type = input("")
    tail_type = tail_type.lower()
    if tail_type == "s" or tail_type == "ssj4":
        # Copying files needed
        bin_copy = f.read()
        amm = open("Files\Tail_SSJ4.bin", "r+b")
        amm_copy = amm.read()

        # Setting up temp bins
        tn1 = "Files\z.bin"     # Will hold edited bin
        temp1 = open(tn1, "w+b")
        temp1.write(bin_copy)
        temp1.close()
        temp1 = open(tn1, "r+b")
        tn2 = "Files\z2.bin"    # Will hold tail AMM
        temp2 = open(tn2, "w+b")
        temp2.write(amm_copy)
        temp2.close()
        temp2 = open(tn2, "r+b")

        # Changes the size of the 3rd AMM in the AMB of the  MAIN BSK bin
        temp1.seek(84)
        temp1.write(b'\x50\xF1\x02\x00')

        # Goes to 3rd AMM
        temp1.seek(80)
        offset = temp1.read(4)
        print("bytes: " + str(offset))
        offset = offset.hex()
        print("hex(LE): " + str(offset))
        offset = int(offset, 16)
        print("dec: " + str(offset))
        offset = struct.pack('<L', offset)
        print("bytes(BE): " + str(offset))
        offset = offset.hex()
        print("hex(BE): " + str(offset))
        offset = int(offset, 16)
        print("dec: " + str(offset))
        print("")

        # Paste over old AMM with new AMM
        temp1.seek(offset)
        t_copy = temp2.read()
        temp1.write(t_copy)

        # Deletes extra bytes at the bottom of the bin
        temp1.seek(84)
        offset2 = temp1.read(4)
        print("bytes: " + str(offset2))
        offset2 = offset2.hex()
        print("hex(LE): " + str(offset2))
        offset2 = int(offset2, 16)
        print("dec: " + str(offset2))
        offset2 = struct.pack('<L', offset2)
        print("bytes(BE): " + str(offset2))
        offset2 = offset2.hex()
        print("hex(BE): " + str(offset))
        offset2 = int(offset2, 16) + offset
        print("dec: " + str(offset2))
        print("")

        # Paste over old AMM with new AMM
        temp1.seek(0)
        t_copy = temp1.read(offset2)
        tn3 = "Files\z3.bin"
        temp3 = open(tn3, "w+b")
        temp3.write(t_copy)
    if tail_type == "c" or tail_type == "cell":
        # Copying files needed
        bin_copy = f.read()
        amm = open("Files\Tail_Cell.bin", "r+b")
        amm_copy = amm.read()

        # Setting up temp bins
        tn1 = "Files\z.bin"  # Will hold edited bin
        temp1 = open(tn1, "w+b")
        temp1.write(bin_copy)
        temp1.close()
        temp1 = open(tn1, "r+b")
        tn2 = "Files\z2.bin"  # Will hold tail AMM
        temp2 = open(tn2, "w+b")
        temp2.write(amm_copy)
        temp2.close()
        temp2 = open(tn2, "r+b")

        # Changes the size of the 3rd AMM in the AMB of the  MAIN BSK bin
        temp1.seek(84)
        temp1.write(b'\xE4\xF2\x02\x00')

        # Goes to 3rd AMM
        temp1.seek(80)
        offset = temp1.read(4)
        print("bytes: " + str(offset))
        offset = offset.hex()
        print("hex(LE): " + str(offset))
        offset = int(offset, 16)
        print("dec: " + str(offset))
        offset = struct.pack('<L', offset)
        print("bytes(BE): " + str(offset))
        offset = offset.hex()
        print("hex(BE): " + str(offset))
        offset = int(offset, 16)
        print("dec: " + str(offset))
        print("")

        # Paste over old AMM with new AMM
        temp1.seek(offset)
        t_copy = temp2.read()
        temp1.write(t_copy)

        # Deletes extra bytes at the bottom of the bin
        temp1.seek(84)
        offset2 = temp1.read(4)
        print("bytes: " + str(offset2))
        offset2 = offset2.hex()
        print("hex(LE): " + str(offset2))
        offset2 = int(offset2, 16)
        print("dec: " + str(offset2))
        offset2 = struct.pack('<L', offset2)
        print("bytes(BE): " + str(offset2))
        offset2 = offset2.hex()
        print("hex(BE): " + str(offset))
        offset2 = int(offset2, 16)+offset
        print("dec: " + str(offset2))
        print("")

        # Paste over old AMM with new AMM
        temp1.seek(0)
        t_copy = temp1.read(offset2)
        tn3 = "Files\z3.bin"
        temp3 = open(tn3, "w+b")
        temp3.write(t_copy)

    if tail_type == "f" or tail_type == "frieza":
        # Copying files needed
        bin_copy = f.read()
        amm = open("Files\Tail_Frieza.bin", "r+b")
        amm_copy = amm.read()

        # Setting up temp bins
        tn1 = "Files\z.bin"  # Will hold edited bin
        temp1 = open(tn1, "w+b")
        temp1.write(bin_copy)
        temp1.close()
        temp1 = open(tn1, "r+b")
        tn2 = "Files\z2.bin"  # Will hold tail AMM
        temp2 = open(tn2, "w+b")
        temp2.write(amm_copy)
        temp2.close()
        temp2 = open(tn2, "r+b")

        # Changes the size of the 3rd AMM in the AMB of the  MAIN BSK bin
        temp1.seek(84)
        temp1.write(b'\x88\xF8\x02\x00')


        # Goes to 3rd AMM
        temp1.seek(80)
        offset = temp1.read(4)
        print("bytes: " + str(offset))
        offset = offset.hex()
        print("hex(LE): " + str(offset))
        offset = int(offset, 16)
        print("dec: " + str(offset))
        offset = struct.pack('<L', offset)
        print("bytes(BE): " + str(offset))
        offset = offset.hex()
        print("hex(BE): " + str(offset))
        offset = int(offset, 16)
        print("dec: " + str(offset))
        print("")

        # Paste over old AMM with new AMM
        temp1.seek(offset)
        t_copy = temp2.read()
        temp1.write(t_copy)

        # Deletes extra bytes at the bottom of the bin
        temp1.seek(84)
        offset2 = temp1.read(4)
        print("bytes: " + str(offset2))
        offset2 = offset2.hex()
        print("hex(LE): " + str(offset2))
        offset2 = int(offset2, 16)
        print("dec: " + str(offset2))
        offset2 = struct.pack('<L', offset2)
        print("bytes(BE): " + str(offset2))
        offset2 = offset2.hex()
        print("hex(BE): " + str(offset))
        offset2 = int(offset2, 16)+offset
        print("dec: " + str(offset2))
        print("")

        # Paste over old AMM with new AMM
        temp1.seek(0)
        t_copy = temp1.read(offset2)
        tn3 = "Files\z3.bin"
        temp3 = open(tn3, "w+b")
        temp3.write(t_copy)

    if tail_type == "co" or tail_type == "cooler":
        # Copying files needed
        bin_copy = f.read()
        amm = open("Files\Tail_Cooler.bin", "r+b")
        amm_copy = amm.read()

        # Setting up temp bins
        tn1 = "Files\z.bin"  # Will hold edited bin
        temp1 = open(tn1, "w+b")
        temp1.write(bin_copy)
        temp1.close()
        temp1 = open(tn1, "r+b")
        tn2 = "Files\z2.bin"  # Will hold tail AMM
        temp2 = open(tn2, "w+b")
        temp2.write(amm_copy)
        temp2.close()
        temp2 = open(tn2, "r+b")

        # Changes the size of the 3rd AMM in the AMB of the  MAIN BSK bin
        temp1.seek(84)
        temp1.write(b'\x20\xA0\x02\x00')

        # Goes to 3rd AMM
        temp1.seek(80)
        offset = temp1.read(4)
        print("bytes: " + str(offset))
        offset = offset.hex()
        print("hex(LE): " + str(offset))
        offset = int(offset, 16)
        print("dec: " + str(offset))
        offset = struct.pack('<L', offset)
        print("bytes(BE): " + str(offset))
        offset = offset.hex()
        print("hex(BE): " + str(offset))
        offset = int(offset, 16)
        print("dec: " + str(offset))
        print("")

        # Paste over old AMM with new AMM
        temp1.seek(offset)
        t_copy = temp2.read()
        temp1.write(t_copy)

        # Deletes extra bytes at the bottom of the bin
        temp1.seek(84)
        offset2 = temp1.read(4)
        print("bytes: " + str(offset2))
        offset2 = offset2.hex()
        print("hex(LE): " + str(offset2))
        offset2 = int(offset2, 16)
        print("dec: " + str(offset2))
        offset2 = struct.pack('<L', offset2)
        print("bytes(BE): " + str(offset2))
        offset2 = offset2.hex()
        print("hex(BE): " + str(offset))
        offset2 = int(offset2, 16)+offset
        print("dec: " + str(offset2))
        print("")

        # Paste over old AMM with new AMM
        temp1.seek(0)
        t_copy = temp1.read(offset2)
        tn3 = "Files\z3.bin"
        temp3 = open(tn3, "w+b")
        temp3.write(t_copy)

    # replacing old bytes with new ones
    temp3.close()
    temp3 = open(tn3, "r+b")
    t_copy = temp3.read()
    old_b = b'\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF'
    new_b = b'\xFF\xFF\xFF\xFF\x00\x00\x00\x00\xFF\xFF\xFF\xFF'
    t_copy = t_copy.replace(old_b, new_b)
    temp3.close
    temp3 = open(tn3, "r+b")
    temp3.write(t_copy)


    # Saves it to your file
    temp3.close()
    temp3 = open(tn3, "r+b")
    t_copy = temp3.read(offset2)
    f.close()
    temp1.close()
    temp2.close()
    temp3.close()
    os.remove(x)
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
    os.remove(tn1)
    os.remove(tn2)
    os.remove(tn3)

def special():
    # opens BSK
    print("BSK name (with extension):")
    x = input("")
    f = open(x, "r+b")
    chunk = f.read()

    # replacing old bytes with new ones
    old_b = b'\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF'
    new_b = b'\xFF\xFF\xFF\xFF\x00\x00\x00\x00\xFF\xFF\xFF\xFF'
    chunk = chunk.replace(old_b, new_b)
    f.close

    f = open(x, "r+b")
    f.seek(0)
    f.write(chunk)
    print("Completed!")

    #closes bin
    f.close()

def again():
    yn = input("Load another? (Y/N)")
    if yn == "Y" or yn == "y" or yn == "Yes" or yn == "yes":
        bsk_type()
        again()
    else:
        print("Tail AMM replacer by: Nexus-sama")
        print("Follow me on Twitter @NexusTheModder")
        kill = input("press enter to close")

bsk_type()
again()


exit()
