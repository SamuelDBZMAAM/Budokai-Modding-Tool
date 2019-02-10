#AMM Tail Animator - amm_ta
#Purpose: To give characters without tail animations tail animations


import struct
import math


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
    f = open(x, "r+b")
    amm = open("Files\AMM - Tail.bin", "r+b")
    amm_copy = amm.read()
    chunk = f.read(16)
    offsets = []
    counter = 0

    #Changes the size of the 3rd AMM in the AMB of the  MAIN BSK bin
    while chunk != b"":
        if chunk[0] == 0x23 and chunk[1] == 0x41 and chunk[2] == 0x4D and chunk[3] == 0x42 and chunk[4] == 0x20 and chunk[12] == 0x03:
            offsets.append(((f.tell()-16)))
            print(hex(f.tell()-16))
            counter += 1
        chunk = f.read(16)
    for i in offsets:
        f.seek(i+84)
        f.write(b"\x50\xF1\x02\x00")
    f.close()

    #replaces old 3rd AMM with Goku's for the tail animation data
    f = open(x, "r+b")
    chunk = f.read(16)
    offsets = []
    counter = 0
    while chunk != b"":
        if chunk[0] == 0x01 and chunk[1] == 0x01 and chunk[2] == 0x00 and chunk[3] == 0x00 and chunk[4] == 0x20:
            offsets.append(((f.tell() - 16)))
            print(hex(f.tell() - 16))
            counter += 1
        chunk = f.read(16)
    for i in offsets:
        f.seek(i + 0)
        f.write(amm_copy)

    #closes bin
    f.close()
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

    # closes bin
    f.close()

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
