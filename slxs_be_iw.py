# SLXS Battle List Maker - slxs_be
# Purpose: To edit story/fighter's road battle scenarios


import struct
import math
import os


def main():
    print("SLUS or SLES?(1/2)")
    type = input("")
    type = type.lower()
    while type != "1" and type != "2" and type != "sles" and type != "slus":
        print("Please choose between SLUS or SLES. (1/2)")
        type = input("")
        type = type.lower()
    print("Drag and drop your SLXS")
    x = input("")
    x = x.replace("\"", "")
    f = open(x, "r+b")

    # Copying files needed
    hti = 0
    ith = 0
    offset = 0
    condition_list = ["Defeat the enemy(1)",
                      "Reduce the enemy's health to a certain level or survive until time runs out(2)",
                      "Lose by ring out(3)", "Don't attack the enemy, survive until time runs out(4)",
                      "Tutorial or Fighter's Road battle(5)"]
    stage_list = ["MARTIAL ARTS TOURNAMENT ARENA(1)", "HYPERBOLIC TIME CHAMBER(2)", "ARCHIPELAGO(3)", "URBAN AREA(4)",
                  "MOUNTAINS(5)", "PLAINS(6)", "GRANDPA GOHAN'S PLACE(7)", "NAMEK(8)", "CELL GAMES ARENA(9)",
                  "KAI PLANET(10)", "INSIDE BUU(11)", "DESTROYED ARCHIPELAGO(12)", "DESTROYED WEST CITY(13)",
                  "DESTROYED PLAINS(14)", "DESTROYED NAMEK(15)", "KAI PLANET?(16)", "RED RIBBON BASE(17)"]
    timer_list = ["10 seconds(1)", "60 seconds(2)", "99 seconds(3)", "180 seconds(4)", "Infinite(5)",
                  "120 seconds(6)", "90 seconds(7)"]
    char_list = ["GOKU(1)", "KID GOHAN(2)", "TEEN GOHAN(3)", "ADULT GOHAN(4)", "GREAT SAIYAMAN(5)", "GOTEN(6)",
                 "VEGETA(7)", "FUTURE TRUNKS(8)", "KID TRUNKS(9)", "KRILLIN(10)", "PICCOLO(11)", "TIEN(12)",
                 "YAMCHA(13)", "HERCULE(14)", "VIDEL(15)", "RADITZ(16)", "NAPPA(17)", "GINYU(18)", "RECOOME(19)",
                 "FRIEZA(20)", "ANDROID 16(21)", "ANDROID 17(22)", "ANDROID 18(23)", "ANDROID 20(GERO)(24)",
                 "CELL(25)", "MAJIN BUU(26)", "SUPER BUU(27)", "KID BUU(28)", "DABURA(29)", "COOLER(30)", "BARDOCK(31)",
                 "BROLY(32)", "SYN SHENRON/OMEGA SHENRON(33)", "SAIBAMEN(34)", "KID GOKU(GT)(35)",
                 "SUPER BABY VEGETA 2(36)", "SUPER ANDROID 17(37)", "SUPER JANEMBA(38)", "PIKKON(39)",
                 "VEGETA (GT)(40)", "GREAT SAIYAMAN 2(41)", "PAN(42)", "GIRU??(43)", "GOTENKS(44)", "SUPER GOGETA(45)",
                 "GOGETA SSJ4(46)", "VEGITO(47)", "BUUTENKS(48)", "BUUHAN(49)", "BUUCCILO(50)", "GOKU SSJ4(51)",
                 "VEGETA SSJ4(52)", "MAJIN VEGETA(53)", "FRIEZA 2ND FORM(54)", "FRIEZA 3RD FORM(55)",
                 "FRIEZA FINAL FORM(56)", "FRIEZA FULL POWER FINAL FORM(57)", "MECHA FRIEZA?? (B3)(58)",
                 "CELL SEMI PERFECT FROM(59)", "CELL PERFECT FORM(60)", "COOLER FINAL FORM(61)", ]



    # Setting up temp bins
    tn1 = "Files\z.bin"  # Will hold edited battle data
    temp1 = open(tn1, "w+b")
    temp1.close()
    temp1 = open(tn1, "r+b")

    # Goes to beginning of offset
    if type == "1" or type == "slus":
        offset = 3632464
    if type == "2" or type == "sles":
        offset = 3634512

    cancel = False
    while cancel is not True:
        f.seek(offset)
        # Locating battle chosen and copying it to temp
        print("Input the battle number you're to edit.")
        b_num = int(input(""))
        while b_num > 201:
            print("Number is too large. there are only 201 battles available. Please try another number.")
            b_num = int(input(""))
        b_num = (b_num - 1) * 96
        f.seek(offset+b_num)
        t_copy = f.read(96)
        temp1.seek(0)
        temp1.write(t_copy)
        # Gathers the data from fight
        print("")
        gather_info(temp1)
        print("Is this the correct one?(y/n)")
        q = input("").lower()
        while q != "y":
            while q != "n" and q != "y":
                print("Please answer the question.")
                q = input("").lower()
            if q == "n":
                print("")
                print("Gathering info again...")
                print("Input the battle number you're to edit.")
                b_num = int(input(""))
                while b_num > 201:
                    print("Number is too large. there are only 201 battles available. Please try another number.")
                    b_num = int(input(""))
                b_num = (b_num - 1) * 96
                f.seek(offset + b_num)
                t_copy = f.read(96)
                temp1.seek(0)
                temp1.write(t_copy)
                print("")
                gather_info(temp1)
                print("Is this the correct one?(y/n)")
                q = input("")

        # Editing battle data
        print("")
        print("---------------NOW EDITING---------------")
        print("Stage and other settings:")
        # Condition
        temp1.seek(2)
        print("")
        print(condition_list)
        print("")
        print("Please choose a battle condition for this fight.")
        print("Type the number next to your choice to select it.")
        condition = int(input(""))
        while condition > int(len(condition_list)):
            print("Invalid, try again")
            condition = int(input(""))
        print(condition_list[condition-1] + " was selected...")
        condition = calculate_condition2(condition)
        temp1.write(condition)
        # Stage
        temp1.seek(8)
        print("")
        print(stage_list)
        print("")
        print("Please choose a stage for this fight.")
        stage = int(input(""))
        while stage > int(len(stage_list)):
            print("Invalid, try again")
            stage = int(input(""))
        print(stage_list[stage - 1] + " was selected...")
        stage = calculate_stage2(stage)
        temp1.write(stage)
        # Music
        temp1.seek(10)
        print("")
        print("Select the music to play in the background. There are only 39 tracks.")
        music = int(input(""))
        while music > 39:
            print("Invalid, only 39 tracks available. Please choose a number between 1-39.")
            music = int(input(""))
        print("Music Track " + str(music) + " selected.")
        ith = music - 1
        ith = int_to_hex(ith)
        music = offset_fix2(ith)
        temp1.write(music)
        # Timer
        temp1.seek(12)
        print("")
        print(timer_list)
        print("")
        print("Please choose a timer for this fight.")
        timer = int(input(""))
        while timer > int(len(timer_list)):
            print("Invalid, try again")
            timer = int(input(""))
        print(timer_list[timer - 1] + " was selected...")
        timer = calculate_timer2(timer)
        temp1.write(timer)

        print("")
        print("")
        print("Player settings:")
        # Removing capsule limitations
        temp1.seek(30)
        temp1.write(b'\xFF\xFF\xFF\xFF\xFF\xFF')
        temp1.seek(44)
        temp1.write(b'\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF')
        # Character
        temp1.seek(20)
        print("")
        print(char_list)
        print("")
        print("Please choose the player's character.")
        print("Type the number next to your choice to select it.")
        char = int(input(""))
        while char > int(len(char_list)):
            print("Invalid, try again")
            char = int(input(""))
        print(char_list[char - 1] + " was selected...")
        char = calculate_character2(char)
        temp1.write(char)
        # Costume
        temp1.seek(22)
        print("")
        print("Type the number of which costume you want. 1 being costume 1, 2 being costume 2, and so on.")
        costume = int(input(""))
        print("Costume " + str(costume) + " selected.")
        ith = costume - 1
        ith = int_to_hex(ith)
        costume = offset_fix2(ith)
        temp1.write(costume)
        # Form at start
        temp1.seek(24)
        print("")
        print("Type the number of which form the player starts at. 0 being base form, 1 being 1st form, and so on.")
        form_s = int(input(""))
        # Adds transform capsule if forced to use form
        if form_s >= 1:
            temp1.seek(46)
            t_copy = form_capsule(char)
            temp1.write(t_copy)
            temp1.seek(24)
        print("The player starts on form number " + str(form_s))
        ith = form_s
        ith = int_to_hex(ith)
        form_s = offset_fix2(ith)
        temp1.write(form_s)
        # Form after fatigue
        temp1.seek(26)
        print("")
        print("Type the number of which form the player reverts to after fatigue. 0 being base form, 1 being 1st form, "
              "and so on.")
        form_f = int(input(""))
        print("The player reverts to form number " + str(form_f) + " after fatigue gauge fills up.")
        ith = form_f
        ith = int_to_hex(ith)
        form_f = offset_fix2(ith)
        temp1.write(form_f)
        # Forms available
        temp1.seek(28)
        print("")
        print("Type the maximum number of forms available player.")
        form_c = int(input(""))
        print("The player can use " + str(form_c) + " forms in the match.")
        ith = form_c
        ith = int_to_hex(ith)
        form_c = offset_fix2(ith)
        temp1.write(form_c)

        print("")
        print("")
        print("Enemy settings")
        # Removing capsule limitations
        temp1.seek(68)
        temp1.write(b'\xFF\xFF\xFF\xFF\xFF\xFF')
        temp1.seek(82)
        temp1.write(b'\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF')
        # Character
        temp1.seek(58)
        print("")
        print(char_list)
        print("")
        print("Please choose the enemy's character.")
        print("Type the number next to your choice to select it.")
        char = int(input(""))
        while char > int(len(char_list)):
            print("Invalid, try again")
            char = int(input(""))
        print(char_list[char - 1] + " was selected...")
        char = calculate_character2(char)
        temp1.write(char)
        # Costume
        temp1.seek(60)
        print("")
        print("Type the number of which costume you want. 1 being costume 1, 2 being costume 2, and so on.")
        costume = int(input(""))
        print("Costume " + str(costume) + " selected.")
        ith = costume - 1
        ith = int_to_hex(ith)
        costume = offset_fix2(ith)
        temp1.write(costume)
        # Form at start
        temp1.seek(62)
        print("")
        print("Type the number of which form the enemy starts at. 0 being base form, 1 being 1st form, and so on.")
        form_s = int(input(""))
        # Adds transform capsule if forced to use form
        if form_s >= 1:
            temp1.seek(84)
            t_copy = form_capsule(char)
            temp1.write(t_copy)
            temp1.seek(62)
        print("The enemy starts on form number " + str(form_s))
        ith = form_s
        ith = int_to_hex(ith)
        form_s = offset_fix2(ith)
        temp1.write(form_s)
        # Form after fatigue
        temp1.seek(64)
        print("")
        print("Type the number of which form the enemy reverts to after fatigue. 0 being base form, 1 being 1st form, "
              "and so on.")
        form_f = int(input(""))
        print("The enemy reverts to form number " + str(form_f) + " after fatigue gauge fills up.")
        ith = form_f
        ith = int_to_hex(ith)
        form_f = offset_fix2(ith)
        temp1.write(form_f)
        # Forms available
        temp1.seek(66)
        print("")
        print("Type the maximum number of forms available enemy.")
        form_c = int(input(""))
        print("The enemy can use " + str(form_c) + " forms in the match.")
        ith = form_c
        ith = int_to_hex(ith)
        form_c = offset_fix2(ith)
        temp1.write(form_c)
        print("---------------EDITING COMPLETED---------------")

        # Showing the new data
        print("")
        print("")
        print("Here is your new battle scenario:")
        print("")
        gather_info(temp1)
        print("")
        # Replaces old data
        temp1.seek(0)
        t_copy = temp1.read()
        f.seek(offset+b_num)
        f.write(t_copy)

        print("Edit another battle?(y/n)")
        q = input("")
        while q != "y" and q != "n":
            print("Please answer the question.")
            q = input("")
        if q == "y":
            print("")
        if q == "n":
            f.close()
            print("")
            print("Completed!")

            # deletes temp files
            #tn1 = "Files\z.bin"
            #temp1 = open(tn1, "r+b")
            #temp1.close()
            #os.remove(tn1)

            cancel = True


def gather_info(temp1):
    print("-----------------BATTLE DATA---------------------")
    temp1.seek(0)
    hti = temp1.read(1)
    hti = offset_fix(hti)
    battle_num = hex_to_int(hti)
    print("Battle Number " + str(battle_num) + " --------------")
    # Grabbing stage setup
    temp1.seek(2)  # Battle Condition
    condition = temp1.read(2)
    condition = calculate_condition(condition)
    print("Battle Condition - " + str(condition) + "")
    temp1.seek(8)  # Stage
    stage = temp1.read(1)
    stage = calculate_stage(stage)
    print("Stage - " + str(stage) + "")
    temp1.seek(10)  # Music
    hti = temp1.read(1)
    hti = offset_fix(hti)
    music = hex_to_int(hti) + 1
    print("Music Track " + str(music) + "")
    temp1.seek(12)  # Timer
    timer = temp1.read(1)
    timer = calculate_timer(timer)
    print("Timer - " + str(timer) + "")

    # Grabbing player character info
    print("--PLAYER DATA--" + "")
    temp1.seek(20)  # Character
    char = temp1.read(1)
    player = calculate_character(char)
    print("Character - " + str(player) + "")
    temp1.seek(22)  # Costume
    hti = temp1.read(1)
    hti = offset_fix(hti)
    alt = hex_to_int(hti) + 1
    print("Costume " + str(alt) + "")
    temp1.seek(24)  # Form at start
    hti = temp1.read(1)
    hti = offset_fix(hti)
    form_s = hex_to_int(hti)
    print("Start on form " + str(form_s) + "")
    temp1.seek(26)  # Form after fatigue
    hti = temp1.read(1)
    hti = offset_fix(hti)
    form_f = hex_to_int(hti)
    print("After fatigue, revert to form " + str(form_f) + "")
    temp1.seek(28)  # Forms available
    hti = temp1.read(1)
    hti = offset_fix(hti)
    form_c = hex_to_int(hti)
    print("Amount of forms available -  " + str(form_c) + "")

    # Grabbing CPU character info
    print("--ENEMY DATA--" + "")
    temp1.seek(58)  # Character
    char = temp1.read(1)
    enemy = calculate_character(char)
    print("Character - " + str(enemy) + "")
    temp1.seek(60)  # Costume
    hti = temp1.read(1)
    hti = offset_fix(hti)
    alt = hex_to_int(hti) + 1
    print("Costume " + str(alt) + "")
    temp1.seek(62)  # Form at start
    hti = temp1.read(1)
    hti = offset_fix(hti)
    form_s = hex_to_int(hti)
    print("Start on form " + str(form_s) + "")
    temp1.seek(64)  # Form after fatigue
    hti = temp1.read(1)
    hti = offset_fix(hti)
    form_f = hex_to_int(hti)
    print("After fatigue, revert to form " + str(form_f) + "")
    temp1.seek(66)  # Forms available
    hti = temp1.read(1)
    hti = offset_fix(hti)
    form_c = hex_to_int(hti)
    print("Amount of forms available -  " + str(form_c) + "")
    print("")

    return


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


def offset_fix2(ith):
    # Setting up temp bins
    tn1 = "Files\offsetfix.bin"
    temp1 = open(tn1, "w+b")
    temp1.close()
    temp1 = open(tn1, "r+b")

    temp1.write(b'\x00\x00\x00\x00')
    temp1.seek(0)
    temp1.write(ith)
    temp1.seek(0)
    ith = temp1.read(2)

    # deletes temp files
    tn1 = "Files\offsetfix.bin"
    temp1 = open(tn1, "r+b")
    temp1.close()
    os.remove(tn1)

    return ith


def calculate_condition(condition):
    if condition == b"\x00\x00":
        condition = "Defeat the enemy"
    if condition == b"\x01\x00":
        condition = "Reduce the enemy's health to a certain level or survive until time runs out"
    if condition == b"\x02\x00":
        condition = "Lose by ring out"
    if condition == b"\x03\x00":
        condition = "Don't attack the enemy, survive until time runs out"
    if condition == b"\xFF\xFF":
        condition = "Tutorial or Fighter's Road battle"
    return condition


def calculate_condition2(condition):
    if condition == 1:
        condition = b"\x00\x00"
    if condition == 2:
        condition = b"\x01\x00"
    if condition == 3:
        condition = b"\x02\x00"
    if condition == 4:
        condition = b"\x03\x00"
    if condition == 5:
        condition = b"\xFF\xFF"
    return condition


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


def calculate_stage2(stage):
    if stage == 1:
        stage = b'\x00'
    if stage == 2:
        stage = b'\x01'
    if stage == 3:
        stage = b'\x02'
    if stage == 4:
        stage = b'\x03'
    if stage == 5:
        stage = b'\x04'
    if stage == 6:
        stage = b'\x05'
    if stage == 7:
        stage = b'\x06'
    if stage == 8:
        stage = b'\x07'
    if stage == 9:
        stage = b'\x08'
    if stage == 10:
        stage = b'\x09'
    if stage == 11:
        stage = b'\x0A'
    if stage == 12:
        stage = b'\x0B'
    if stage == 13:
        stage = b'\x0C'
    if stage == 14:
        stage = b'\x0D'
    if stage == 15:
        stage = b'\x0E'
    if stage == 16:
        stage = b'\x0F'
    if stage == 17:
        stage = b'\x10'
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


def calculate_timer2(timer):
    if timer == 1:
        timer = b"\x00"
    if timer == 2:
        timer = b"\x01"
    if timer == 3:
        timer = b"\x02"
    if timer == 4:
        timer = b"\x03"
    if timer == 5:
        timer = b"\x04"
    if timer == 6:
        timer = b"\x05"
    if timer == 7:
        timer = b"\x06"
    if timer == 8:
        timer = b"\x07"
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


def calculate_character2(char):
    if char == 1:
        char = b'\x00'
    if char == 2:
        char = b'\x02'
    if char == 3:
        char = b'\x03'
    if char == 4:
        char = b'\x04'
    if char == 5:
        char = b'\x05'
    if char == 6:
        char = b'\x06'
    if char == 7:
        char = b'\x07'
    if char == 8:
        char = b'\x08'
    if char == 9:
        char = b'\x09'
    if char == 10:
        char = b'\x0A'
    if char == 11:
        char = b'\x0B'
    if char == 12:
        char = b'\x0C'
    if char == 13:
        char = b'\x0D'
    if char == 14:
        char = b'\x0E'
    if char == 15:
        char = b'\x0F'
    if char == 16:
        char = b'\x12'
    if char == 17:
        char = b'\x13'
    if char == 18:
        char = b'\x14'
    if char == 19:
        char = b'\x15'
    if char == 20:
        char = b'\x1B'
    if char == 21:
        char = b'\x1C'
    if char == 22:
        char = b'\x1D'
    if char == 23:
        char = b'\x1E'
    if char == 24:
        char = b'\x20'
    if char == 25:
        char = b'\x21'
    if char == 26:
        char = b'\x22'
    if char == 27:
        char = b'\x23'
    if char == 28:
        char = b'\x24'
    if char == 29:
        char = b'\x25'
    if char == 30:
        char = b'\x26'
    if char == 31:
        char = b'\x27'
    if char == 32:
        char = b'\x28'
    if char == 33:
        char = b'\x29'
    if char == 34:
        char = b'\x2A'
    if char == 35:
        char = b'\x2C'
    if char == 36:
        char = b'\x2D'
    if char == 37:
        char = b'\x2E'
    if char == 38:
        char = b'\x2F'
    if char == 39:
        char = b'\x30'
    if char == 40:
        char = b'\x36'
    if char == 41:
        char = b'\x37'
    if char == 42:
        char = b'\x38'
    if char == 43:
        char = b'\x39'
    if char == 44:
        char = b'\x40'
    if char == 45:
        char = b'\x44'
    if char == 46:
        char = b'\x46'
    if char == 47:
        char = b'\x4A'
    if char == 48:
        char = b'\x4E'
    if char == 49:
        char = b'\x4F'
    if char == 50:
        char = b'\x54'
    if char == 51:
        char = b'\x5B'
    if char == 52:
        char = b'\x5C'
    if char == 53:
        char = b'\x5D'
    if char == 54:
        char = b'\x5E'
    if char == 55:
        char = b'\x5F'
    if char == 56:
        char = b'\x60'
    if char == 57:
        char = b'\x61'
    if char == 58:
        char = b'\x62'
    if char == 59:
        char = b'\x63'
    if char == 60:
        char = b'\x64'
    if char == 61:
        char = b'\x66'

    return char


def form_capsule(char):
    if char == b'\x00':
        char = b'\x30\x01'
    if char == b'\x02':
        char = b'\x3C\x01'
    if char == b'\x03':
        char = b'\x45\x01'
    if char == b'\x04':
        char = b'\x4E\x01'
    if char == b'\x05':
        char = b'\xFF\xFF'
    if char == b'\x06':
        char = b'\x54\x01'
    if char == b'\x07':
        char = b'\x5E\x01'
    if char == b'\x08':
        char = b'\x6D\x01'
    if char == b'\x09':
        char = b'\x74\x01'
    if char == b'\x0A':
        char = b'\x7C\x01'
    if char == b'\x0B':
        char = b'\x85\x01'
    if char == b'\x0C':
        char = b'\xFF\xFF'
    if char == b'\x0D':
        char = b'\xFF\xFF'
    if char == b'\x0E':
        char = b'\x8C\x01'
    if char == b'\x0F':
        char = b'\xFF\xFF'
    if char == b'\x12':
        char = b'\xFF\xFF'
    if char == b'\x13':
        char = b'\xFF\xFF'
    if char == b'\x14':
        char = b'\xFF\xFF'
    if char == b'\x15':
        char = b'\xFF\xFF'
    if char == b'\x1B':
        char = b'\x97\x01'
    if char == b'\x1C':
        char = b'\xFF\xFF'
    if char == b'\x1D':
        char = b'\xFF\xFF'
    if char == b'\x1E':
        char = b'\xFF\xFF'
    if char == b'\x20':
        char = b'\xFF\xFF'
    if char == b'\x21':
        char = b'\x9E\x01'
    if char == b'\x22':
        char = b'\xFF\xFF'
    if char == b'\x23':
        char = b'\xFF\xFF'
    if char == b'\x24':
        char = b'\xFF\xFF'
    if char == b'\x25':
        char = b'\xA4\x01'
    if char == b'\x26':
        char = b'\xAC\x01'
    if char == b'\x27':
        char = b'\xFF\xFF'
    if char == b'\x28':
        char = b'\xB4\x01'
    if char == b'\x29':
        char = b'\xBC\x01'
    if char == b'\x2A':
        char = b'\xFF\xFF'
    if char == b'\x2C':
        char = b'\x36\x01'
    if char == b'\x2D':
        char = b'\xFF\xFF'
    if char == b'\x2E':
        char = b'\xFF\xFF'
    if char == b'\x2F':
        char = b'\xFF\xFF'
    if char == b'\x30':
        char = b'\xFF\xFF'
    if char == b'\x36':
        char = b'\x65\x01'
    if char == b'\x37':
        char = b'\xFF\xFF'
    if char == b'\x38':
        char = b'\xFF\xFF'
    if char == b'\x39':
        char = b'\xFF\xFF'
    if char == b'\x40':
        char = b'\xFF\xFF'
    if char == b'\x44':
        char = b'\xFF\xFF'
    if char == b'\x46':
        char = b'\xFF\xFF'
    if char == b'\x4A':
        char = b'\xFF\xFF'
    if char == b'\x4E':
        char = b'\xFF\xFF'
    if char == b'\x4F':
        char = b'\xFF\xFF'
    if char == b'\x54':
        char = b'\xFF\xFF'
    if char == b'\x5B':
        char = b'\xFF\xFF'
    if char == b'\x5C':
        char = b'\xFF\xFF'
    if char == b'\x5D':
        char = b'\xFF\xFF'
    if char == b'\x5E':
        char = b'\xFF\xFF'
    if char == b'\x5F':
        char = b'\xFF\xFF'
    if char == b'\x60':
        char = b'\xFF\xFF'
    if char == b'\x61':
        char = b'\xFF\xFF'
    if char == b'\x62':
        char = b'\xFF\xFF'
    if char == b'\x63':
        char = b'\xFF\xFF'
    if char == b'\x64':
        char = b'\xFF\xFF'
    if char == b'\x66':
        char = b'\xFF\xFF'

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
