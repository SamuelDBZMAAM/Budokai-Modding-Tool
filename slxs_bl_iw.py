# SLXS Battle List Maker - slxs_bl
# Purpose: To make a list of all story/fr battles for use in Budokai series


import struct
import math
import os


def main():
    print("SLUS or SLES?(1/2)")
    type = input("")
    type = type.lower()
    print("Drag and drop your SLXS")
    x = input("")
    x = x.replace("\"", "")
    f = open(x, "r+b")

    print("Name of list?")
    n = input("")
    y = open(n+".txt", "w")
    hti = 0
    ith = 0

    if type == "1" or type == "slus":
        offset = 3632464
    if type == "2" or type == "sles":
        offset = 3634512
    amount = 201
    for i in range(amount):
        f.seek(offset)
        hti = f.read(1)
        hti = offset_fix(hti)
        battle_num = hex_to_int(hti)
        y.write("Battle Number " + str(battle_num) + " --------------\r")
        # Grabbing stage setup
        f.seek(offset+8)                        # Stage
        stage = f.read(1)
        stage = calculate_stage(stage)
        y.write("Stage - " + str(stage)+"\r")
        f.seek(offset+10)                       # Music
        hti = f.read(1)
        hti = offset_fix(hti)
        music = hex_to_int(hti)+1
        y.write("Music Track " + str(music)+"\r")
        f.seek(offset+12)                       # Timer
        timer = f.read(1)
        timer = calculate_timer(timer)
        y.write("Timer - " + str(timer)+"\r")

        # Grabbing player character info
        y.write("--PLAYER DATA--"+"\r")
        f.seek(offset + 20)                     # Character
        char = f.read(1)
        player = calculate_character(char)
        y.write("Character - " + str(player)+"\r")
        f.seek(offset + 22)                     # Costume
        hti = f.read(1)
        hti = offset_fix(hti)
        alt = hex_to_int(hti)+1
        y.write("Costume " + str(alt)+"\r")
        f.seek(offset + 24)                     # Form at start
        hti = f.read(1)
        hti = offset_fix(hti)
        form_s = hex_to_int(hti)
        y.write("Start on form " + str(form_s)+"\r")
        f.seek(offset + 26)                     # Form after fatigue
        hti = f.read(1)
        hti = offset_fix(hti)
        form_f = hex_to_int(hti)
        y.write("After fatigue, revert to form " + str(form_f)+"\r")
        f.seek(offset + 28)                     # Forms available
        hti = f.read(1)
        hti = offset_fix(hti)
        form_c = hex_to_int(hti)
        y.write("Amount of forms available -  " + str(form_c)+"\r")

        # Grabbing CPU character info
        y.write("--ENEMY DATA--"+"\r")
        f.seek(offset + 58)                     # Character
        char = f.read(1)
        enemy = calculate_character(char)
        y.write("Character - " + str(enemy)+"\r")
        f.seek(offset + 60)                     # Costume
        hti = f.read(1)
        hti = offset_fix(hti)
        alt = hex_to_int(hti)+1
        y.write("Costume " + str(alt)+"\r")
        f.seek(offset + 62)                     # Form at start
        hti = f.read(1)
        hti = offset_fix(hti)
        form_s = hex_to_int(hti)
        y.write("Start on form " + str(form_s)+"\r")
        f.seek(offset + 64)                     # Form after fatigue
        hti = f.read(1)
        hti = offset_fix(hti)
        form_f = hex_to_int(hti)
        y.write("After fatigue, revert to form " + str(form_f)+"\r")
        f.seek(offset + 66)                     # Forms available
        hti = f.read(1)
        hti = offset_fix(hti)
        form_c = hex_to_int(hti)
        y.write("Amount of forms available -  " + str(form_c)+"\r")

        offset = offset+96
        y.write("\r")
    y.close()
    f.close()
    print("")
    print("Completed!")
    print("List located in tool folder")
    print("")


def hex_to_int(hti):
    # Converts hex offsets to integer format
    hti = hti.hex()
    hti = int(hti, 16)
    hti = struct.pack('<L', hti)
    hti = hti.hex()
    hti = int(hti, 16)
    #print("DEBUG:HTI - " + str(hti))
    return hti


def int_to_hex(ith):
    # Opposite of hex_to_int
    ith = struct.pack('<L', ith)
    #print("DEBUG:ITH - " + str(ith))
    return ith


def offset_fix(hti):
    # Setting up temp bins
    tn1 = "Files\offsetfix.bin"
    temp1 = open(tn1, "w+b")
    temp1.close()
    temp1 = open(tn1, "r+b")

    temp1.write(b'\x00\x00\x00\x00')
    temp1.seek(0)
    temp1.write(hti)
    temp1.seek(0)
    hti = temp1.read(4)

    # deletes temp files
    tn1 = "Files\offsetfix.bin"
    temp1 = open(tn1, "r+b")
    temp1.close()
    os.remove(tn1)

    return hti


def calculate_stage(stage):
    if stage == b'\x00':
        stage = "MARTIAL ARTS TOURNAMENT ARENA"
    if stage == b'\x01':
        stage = "HYPERBOLIC TIME CHAMBER"
    if stage == b'\x02':
        stage = "ARCHIPELAGO"
    if stage == b'\x03':
        stage = "URBAN AREA"
    if stage == b'\x04':
        stage = "MOUNTAINS"
    if stage == b'\x05':
        stage = "PLAINS"
    if stage == b'\x06':
        stage = "GRANDPA GOHAN'S PLACE"
    if stage == b'\x07':
        stage = "NAMEK "
    if stage == b'\x08':
        stage = "CELL GAMES ARENA"
    if stage == b'\x09':
        stage = "KAI PLANET"
    if stage == b'\x0A':
        stage = "INSIDE BUU"
    if stage == b'\x0B':
        stage = "DESTROYED ARCHIPELAGO"
    if stage == b'\x0C':
        stage = "DESTROYED WEST CITY"
    if stage == b'\x0D':
        stage = "DESTROYED PLAINS"
    if stage == b'\x0E':
        stage = "DESTROYED NAMEK"
    if stage == b'\x0F':
        stage = "KAI PLANET?"
    if stage == b'\x10':
        stage = "RED RIBBON BASE"
    return stage


def calculate_timer(timer):
    if timer == b"\x00":
        timer = "10 seconds"
    if timer == b"\x01":
        timer = "60 seconds"
    if timer == b"\x02":
        timer = "99 seconds"
    if timer == b"\x03":
        timer = "180 seconds"
    if timer == b"\x04":
        timer = "Infinite"
    if timer == b"\x05":
        timer = "120 seconds"
    if timer == b"\x06":
        timer = "90 seconds"
    if timer == b"\x07":
        timer = "0 seconds/Infinite"
    return timer


def calculate_character(char):
    if char == b'\x00':
        char = "GOKU"
    if char == b'\x02':
        char = "KID GOHAN"
    if char == b'\x03':
        char = "TEEN GOHAN"
    if char == b'\x04':
        char = "ADULT GOHAN"
    if char == b'\x05':
        char = "GREAT SAIYAMAN"
    if char == b'\x06':
        char = "GOTEN"
    if char == b'\x07':
        char = "VEGETA"
    if char == b'\x08':
        char = "FUTURE TRUNKS"
    if char == b'\x09':
        char = "KID TRUNKS"
    if char == b'\x0A':
        char = "KRILLIN"
    if char == b'\x0B':
        char = "PICCOLO"
    if char == b'\x0C':
        char = "TIEN"
    if char == b'\x0D':
        char = "YAMCHA"
    if char == b'\x0E':
        char = "HERCULE"
    if char == b'\x0F':
        char = "VIDEL"
    if char == b'\x12':
        char = "RADITZ"
    if char == b'\x13':
        char = "NAPPA"
    if char == b'\x14':
        char = "GINYU"
    if char == b'\x15':
        char = "RECOOME"
    if char == b'\x1B':
        char = "FRIEZA"
    if char == b'\x1C':
        char = "ANDROID 16"
    if char == b'\x1D':
        char = "ANDROID 17"
    if char == b'\x1E':
        char = "ANDROID 18"
    if char == b'\x20':
        char = "ANDROID 20 (GERO)"
    if char == b'\x21':
        char = "CELL"
    if char == b'\x22':
        char = "MAJIN BUU"
    if char == b'\x23':
        char = "SUPER BUU"
    if char == b'\x24':
        char = "KID BUU"
    if char == b'\x25':
        char = "DABURA"
    if char == b'\x26':
        char = "COOLER"
    if char == b'\x27':
        char = "BARDOCK"
    if char == b'\x28':
        char = "BROLY"
    if char == b'\x29':
        char = "SYN SHENRON/OMEGA SHENRON"
    if char == b'\x2A':
        char = "SAIBAMEN"
    if char == b'\x2C':
        char = "KID GOKU (GT)"
    if char == b'\x2D':
        char = "SUPER BABY VEGETA 2"
    if char == b'\x2E':
        char = "SUPER ANDROID 17"
    if char == b'\x2F':
        char = "SUPER JANEMBA"
    if char == b'\x30':
        char = "PIKKON"
    if char == b'\x36':
        char = "VEGETA (GT)"
    if char == b'\x37':
        char = "GREAT SAIYAMAN 2"
    if char == b'\x38':
        char = "PAN"
    if char == b'\x39':
        char = "GIRU??"
    if char == b'\x40':
        char = "GOTENKS"
    if char == b'\x44':
        char = "SUPER GOGETA"
    if char == b'\x46':
        char = "GOGETA SSJ4"
    if char == b'\x4A':
        char = "VEGITO"
    if char == b'\x4E':
        char = "BUUTENKS"
    if char == b'\x4F':
        char = "BUUHAN"
    if char == b'\x54':
        char = "BUUCCILO"
    if char == b'\x5B':
        char = "GOKU SSJ4"
    if char == b'\x5C':
        char = "VEGETA SSJ4"
    if char == b'\x5D':
        char = "MAJIN VEGETA"
    if char == b'\x5E':
        char = "FRIEZA 2ND FORM"
    if char == b'\x5F':
        char = "FRIEZA 3RD FORM"
    if char == b'\x60':
        char = "FRIEZA FINAL FORM"
    if char == b'\x61':
        char = "FRIEZA FULL POWER FINAL FORM"
    if char == b'\x62':
        char = "MECHA FRIEZA?? (B3)"
    if char == b'\x63':
        char = "CELL SEMI PERFECT FROM"
    if char == b'\x64':
        char = "CELL PERFECT FORM"
    if char == b'\x66':
        char = "COOLER FINAL FORM"

    return char


def again():
    yn = input("Would you like to load another? (Y/N)")
    yn = yn.lower()
    if yn == "y" or yn == "yes":
        main()
        again()
    else:
        print("")
        print("SLXS battle list maker by: Nexus-sama")
        print("Follow me on Twitter @NexusTheModder")
        print("")
        kill = input("press enter to close")


main()
again()
exit()
