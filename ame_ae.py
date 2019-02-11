# AME Aura Editor - ame_ae
# Purpose: To create and edit aura color


import struct
import math
import os


def aura_type():
    # Let's the user select bin type
    print("Infinite World or Budokai 3?(I/B):")
    a_type = input("")
    a_type = a_type.lower()

    if a_type == "i":
        iw()
    elif a_type == "b":
        b3()
    else:
        print("Please type 'I' or 'B'!")
        print("")
        aura_type()

def iw():
    # Create or edit aura bin(TO EDIT, BIN MUST BE CREATED FROM THIS SCRIPT TO WORK)
    print("Infinite World Aura Type Selected")
    print("")
    print("Create or Edit?(C/E)):")
    print("(TO EDIT, BIN MUST BE CREATED FROM THIS SCRIPT FIRST TO WORK!!)")
    choose = input("")
    choose = choose.lower()
    if choose == "c":
        # Creates a new file for you aura
        print("Name your aura bin:")
        x = input("")
        x = x + ".bin"
        f = open(x, "w+b")
    if choose == "e":
        # Opens bin
        print("Name your aura bin to edit:")
        x = input("")
        x = x + ".bin"
        f = open(x, "r+b")
        # Choose Mode
        print("")
        print("AMT edit or Color edit?(A/C)")
        mode = input("")
        mode = mode.lower()
        if mode == "a":
            # Copying files needed
            bin = open(x, "r+b")
            bin_copy = bin.read()

            # Setting up temp bins
            tn1 = "Files\Aura\z.bin"  # Will hold edited bin
            temp1 = open(tn1, "w+b")
            temp1.write(bin_copy)
            temp1.close()
            temp1 = open(tn1, "r+b")
            tn2 = "AMT TO EDIT.amt"  # Will hold AMT data for user to edit
            temp2 = open(tn2, "w+b")
            temp1.seek(85712)
            amt_copy = temp1.read(38448)
            temp2.write(amt_copy)
            temp2.close()

            # Let's the user edit the AMT before replacing old AMT
            print("The AMT has been duplicated for you to edit. Look for \"AMT TO EDIT.amt\" in the tool folder")
            print("DO NOT CHANGE THE FILE NAME OR MOVE THE FILE!! IT WILL BE PASTED OVER THE OLD AMT IN THE BIN!!")
            print("Please close the AMT when you are finished so that we can copy it and paste it back into the bin")
            print("")
            kill = input("Press Enter 2 times when finished editing")
            kill = input("Press Enter 1 time when finished editing")
            print("")
            temp2 = open(tn2, "r+b")
            t_copy = temp2.read()
            temp1.seek(85712)
            temp1.write(t_copy)
            temp1.close()
            temp1 = open(tn1, "r+b")
            t_copy = temp1.read()
            f.write(t_copy)
            f.close()
            print("Completed!")

            # deletes temp files
            temp1 = open(tn1, "r+b")
            temp2 = open(tn2, "r+b")
            temp1.close()
            os.remove(tn1)
            temp2.close()
            os.remove(tn2)
        if mode != "c":
            choose = "no color"
        if mode == "c":
            choose = "e"


    # Changing color
    # Copying files needed
    if choose == "c":
        bin = open("Files\Aura\iw_temp.bin", "r+b")
        bin_copy = bin.read()
        amb = open("Files\Aura\iw_amb.bin", "r+b")
        amb_copy = amb.read()
        aura = open("Files\Aura\iw_aura.bin", "r+b")
        aura_copy = aura.read()
        bd = open("Files\Aura\iw_bd.bin", "r+b")
        bd_copy = bd.read()
        bs = open("Files\Aura\iw_bs.bin", "r+b")
        bs_copy = bs.read()
    elif choose == "e":
        bin = open(x, "r+b")
        bin_copy = bin.read()
        aura = open("Files\Aura\iw_aura.bin", "r+b")
        aura_copy = aura.read()
        bd = open("Files\Aura\iw_bd.bin", "r+b")
        bd_copy = bd.read()
        bs = open("Files\Aura\iw_bs.bin", "r+b")
        bs_copy = bs.read()
    elif choose == "no color":
        "finished"

    if choose == "c" or choose == "e":
        # Setting up temp bins
        tn1 = "Files\Aura\z.bin"    # Will hold edited bin
        temp1 = open(tn1, "w+b")
        temp1.write(bin_copy)
        temp1.close()
        temp1 = open(tn1, "r+b")
        tn2 = "Files\Aura\z2.bin"    # Will hold edited AMB
        temp2 = open(tn2, "w+b")
        if choose == "c":
            temp2.write(amb_copy)
            temp2.close()
            temp2 = open(tn2, "r+b")
        elif choose == "e":
            temp1.seek(84944)
            amb_copy = temp1.read()
            temp2.write(amb_copy)
            temp2.close()
            temp2 = open(tn2, "r+b")
            temp1.seek(0)
        tn3 = "Files\Aura\z3.bin"    # Will hold edited aura
        temp3 = open(tn3, "w+b")
        temp3.write(aura_copy)
        temp3.close()
        temp3 = open(tn3, "r+b")
        tn4 = "Files\Aura\z4.bin"    # Will hold edited burst dash
        temp4 = open(tn4, "w+b")
        temp4.write(bd_copy)
        temp4.close()
        temp4 = open(tn4, "r+b")
        tn5 = "Files\Aura\z5.bin"    # Will hold edited burst dash spark
        temp5 = open(tn5, "w+b")
        temp5.write(bs_copy)
        temp5.close()
        temp5 = open(tn5, "r+b")

    elif choose == "no color":
        "finished"

    if choose == "c" or choose == "e":
        # Selecting first aura color
        print("Primary aura color:")
        print("")
        print("Custom, B, K, SSJ, SSJ3, SSJ4, Mystic?")
        color_type = input("")
        color_type = color_type.lower()
        if color_type == "custom" or color_type == "c" or color_type == "1":
            color_type == "custom"
            # Converts RGB value to bytes
            print("Amount of red used? (between 0 and 255)")
            r_color = int(input("")) / 255
            r_color = bytes.fromhex(struct.pack("f", r_color).hex())
            print("Red: "+str(r_color))
            print("")
            print("Amount of green used? (between 0 and 255)")
            g_color = int(input("")) / 255
            g_color = bytes.fromhex(struct.pack("f", g_color).hex())
            print("Green: "+str(g_color))
            print("")
            print("Amount of blue used? (between 0 and 255)")
            b_color = int(input("")) / 255
            b_color = bytes.fromhex(struct.pack("f", b_color).hex())
            print("Blue: "+str(b_color))
            print("")
        elif color_type == "b" or color_type == "2":
            r_color = 0 / 255
            r_color = bytes.fromhex(struct.pack("f", r_color).hex())
            g_color = 165 / 255
            g_color = bytes.fromhex(struct.pack("f", g_color).hex())
            b_color = 255 / 255
            b_color = bytes.fromhex(struct.pack("f", b_color).hex())
            print("Red: "+str(r_color))
            print("Green: "+str(g_color))
            print("Blue: "+str(b_color))
            print("")
            color_type = "custom"
        elif color_type == "k" or color_type == "3":
            r_color = 255 / 255
            r_color = bytes.fromhex(struct.pack("f", r_color).hex())
            g_color = 58 / 255
            g_color = bytes.fromhex(struct.pack("f", g_color).hex())
            b_color = 58 / 255
            b_color = bytes.fromhex(struct.pack("f", b_color).hex())
            print("Red: "+str(r_color))
            print("Green: "+str(g_color))
            print("Blue: "+str(b_color))
            print("")
            color_type = "custom"
        elif color_type == "ssj" or color_type == "4":
            d_color = open("Files\Aura\d_color.bin", "r+b")
            d_color.seek(16)
            t_copy = d_color.read(64)   # 4 lines
            d_color.seek(16)
            t_copy2 = d_color.read(32)  # 2 lines
            print("RGB: Default")
            print("")
            color_type = "default"
        elif color_type == "ssj3" or color_type == "5":
            d_color = open("Files\Aura\d_color.bin", "r+b")
            d_color.seek(176)
            t_copy = d_color.read(64)   # 4 lines
            d_color.seek(176)
            t_copy2 = d_color.read(32)  # 2 lines
            print("RGB: Default")
            print("")
            color_type = "default"
        elif color_type == "ssj4" or color_type == "6":
            print("Goku, Vegeta, Gogeta?(G/V/GV)")
            ssj4 = input("")
            ssj4 = ssj4.lower()
            if ssj4 == "goku" or ssj4 == "g":
                d_color = open("Files\Aura\d_color.bin", "r+b")
                d_color.seek(336)
                t_copy = d_color.read(64)   # 4 lines
                d_color.seek(336)
                t_copy2 = d_color.read(32)  # 2 lines
                color_type = "default"
            elif ssj4 == "vegeta" or ssj4 == "v":
                d_color = open("Files\Aura\d_color.bin", "r+b")
                d_color.seek(496)
                t_copy = d_color.read(64)   # 4 lines
                d_color.seek(496)
                t_copy2 = d_color.read(32)  # 2 lines
                color_type = "default"
            elif ssj4 == "gogeta" or ssj4 == "gv":
                d_color = open("Files\Aura\d_color.bin", "r+b")
                d_color.seek(656)
                t_copy = d_color.read(64)   # 4 lines
                d_color.seek(656)
                t_copy2 = d_color.read(32)  # 2 lines
            print("RGB: Default")
            print("")
            color_type = "default"
        elif color_type == "mystic" or color_type == "7":
            d_color = open("Files\Aura\d_color.bin", "r+b")
            d_color.seek(816)
            t_copy = d_color.read(64)  # 4 lines
            d_color.seek(816)
            t_copy2 = d_color.read(32)  # 2 lines
            print("RGB: Default")
            print("")
            color_type = "default"

        # Replacing values with your color
        if color_type == "custom" or color_type == "1":
            old_r = b'\xAA\xAA\xAA\xAA'
            old_g = b'\xBB\xBB\xBB\xBB'
            old_b = b'\xCC\xCC\xCC\xCC'
            t_copy = temp3.read()
            t_copy = t_copy.replace(old_r, r_color)
            t_copy = t_copy.replace(old_g, g_color)
            t_copy = t_copy.replace(old_b, b_color)
            temp3.close()
            temp3 = open(tn3, "r+b")
            temp3.write(t_copy)
            t_copy = temp4.read()
            t_copy = t_copy.replace(old_r, r_color)
            t_copy = t_copy.replace(old_g, g_color)
            t_copy = t_copy.replace(old_b, b_color)
            temp4.close()
            temp4 = open(tn4, "r+b")
            temp4.write(t_copy)
            t_copy = temp5.read()
            t_copy = t_copy.replace(old_r, r_color)
            t_copy = t_copy.replace(old_g, g_color)
            t_copy = t_copy.replace(old_b, b_color)
            temp5.close()
            temp5 = open(tn5, "r+b")
            temp5.write(t_copy)
        elif color_type == "default":
            temp3.seek(144)
            temp3.write(t_copy)
            temp4.seek(528)
            temp4.write(t_copy)
            temp4.seek(1184)
            temp4.write(t_copy)
            temp4.seek(1840)
            temp4.write(t_copy)
            temp5.seek(272)
            temp5.write(t_copy2)
        temp3.close()
        temp4.close()
        temp5.close()
        temp3 = open(tn3, "r+b")
        temp4 = open(tn4, "r+b")
        temp5 = open(tn5, "r+b")


        # Selecting second aura color
        # Converts RGB value to bytes
        print ("Secondary Aura color:")
        print("")
        print("Custom, B, K, SSJ, SSJ3, SSJ4, Mystic?")
        color_type = input("")
        color_type = color_type.lower()
        if color_type == "custom" or color_type == "c" or color_type == "1":
            color_type == "custom"
            # Converts RGB value to bytes
            print("Amount of red used? (between 0 and 255)")
            r_color = int(input("")) / 255
            r_color = bytes.fromhex(struct.pack("f", r_color).hex())
            print("Red: "+str(r_color))
            print("")
            print("Amount of green used? (between 0 and 255)")
            g_color = int(input("")) / 255
            g_color = bytes.fromhex(struct.pack("f", g_color).hex())
            print("Green: "+str(g_color))
            print("")
            print("Amount of blue used? (between 0 and 255)")
            b_color = int(input("")) / 255
            b_color = bytes.fromhex(struct.pack("f", b_color).hex())
            print("Blue: "+str(b_color))
            print("")
        elif color_type == "b" or color_type == "2":
            r_color = b'\x00\x00\x80\x3F'
            g_color = b'\x00\x00\x80\x3F'
            b_color = b'\x00\x00\x80\x3F'
            print("Red: "+str(r_color))
            print("Green: "+str(g_color))
            print("Blue: "+str(b_color))
            print("")
            color_type = "custom"
        elif color_type == "k" or color_type == "3":
            r_color = 255 / 255
            r_color = bytes.fromhex(struct.pack("f", r_color).hex())
            g_color = 0 / 255
            g_color = bytes.fromhex(struct.pack("f", g_color).hex())
            b_color = 0 / 255
            b_color = bytes.fromhex(struct.pack("f", b_color).hex())
            print("Red: "+str(r_color))
            print("Green: "+str(g_color))
            print("Blue: "+str(b_color))
            print("")
            color_type = "custom"
        elif color_type == "ssj" or color_type == "4":
            d_color = open("Files\Aura\d_color.bin", "r+b")
            d_color.seek(96)
            t_copy = d_color.read(64)  # 4 lines
            d_color.seek(96)
            t_copy2 = d_color.read(32)  # 2 lines
            print("RGB: Default")
            print("")
            color_type = "default"
        elif color_type == "ssj3" or color_type == "5":
            d_color = open("Files\Aura\d_color.bin", "r+b")
            d_color.seek(256)
            t_copy = d_color.read(64)  # 4 lines
            d_color.seek(256)
            t_copy2 = d_color.read(32)  # 2 lines
            print("RGB: Default")
            print("")
            color_type = "default"
        elif color_type == "ssj4" or color_type == "6":
            print("Goku, Vegeta, Gogeta?(G/V/GV)")
            ssj4 = input("")
            ssj4 = ssj4.lower()
            if ssj4 == "goku" or ssj4 == "g":
                d_color = open("Files\Aura\d_color.bin", "r+b")
                d_color.seek(416)
                t_copy = d_color.read(64)  # 4 lines
                d_color.seek(416)
                t_copy2 = d_color.read(32)  # 2 lines
                color_type = "default"
            elif ssj4 == "vegeta" or ssj4 == "v":
                d_color = open("Files\Aura\d_color.bin", "r+b")
                d_color.seek(576)
                t_copy = d_color.read(64)  # 4 lines
                d_color.seek(576)
                t_copy2 = d_color.read(32)  # 2 lines
                color_type = "default"
            elif ssj4 == "gogeta" or ssj4 == "gv":
                d_color = open("Files\Aura\d_color.bin", "r+b")
                d_color.seek(736)
                t_copy = d_color.read(64)  # 4 lines
                d_color.seek(736)
                t_copy2 = d_color.read(32)  # 2 lines
            print("RGB: Default")
            print("")
            color_type = "default"
        elif color_type == "mystic" or color_type == "7":
            d_color = open("Files\Aura\d_color.bin", "r+b")
            d_color.seek(896)
            t_copy = d_color.read(64)  # 4 lines
            d_color.seek(896)
            t_copy2 = d_color.read(32)  # 2 lines
            print("RGB: Default")
            print("")
            color_type = "default"

        # Replacing values with your color
        if color_type == "custom" or color_type == "1":
            old_r = b'\xDD\xDD\xDD\xDD'
            old_g = b'\xEE\xEE\xEE\xEE'
            old_b = b'\xF7\xF7\xF7\xF7'
            t_copy = temp3.read()
            t_copy = t_copy.replace(old_r, r_color)
            t_copy = t_copy.replace(old_g, g_color)
            t_copy = t_copy.replace(old_b, b_color)
            temp3.close()
            temp3 = open(tn3, "r+b")
            temp3.write(t_copy)
            t_copy = temp4.read()
            t_copy = t_copy.replace(old_r, r_color)
            t_copy = t_copy.replace(old_g, g_color)
            t_copy = t_copy.replace(old_b, b_color)
            temp4.close()
            temp4 = open(tn4, "r+b")
            temp4.write(t_copy)
            t_copy = temp5.read()
            t_copy = t_copy.replace(old_r, r_color)
            t_copy = t_copy.replace(old_g, g_color)
            t_copy = t_copy.replace(old_b, b_color)
            temp5.close()
            temp5 = open(tn5, "r+b")
            temp5.write(t_copy)
        elif color_type == "default":
            temp3.seek(432)
            temp3.write(t_copy)
            temp4.seek(288)
            temp4.write(t_copy)
            temp4.seek(944)
            temp4.write(t_copy)
            temp4.seek(1600)
            temp4.write(t_copy)
            temp5.seek(928)
            temp5.write(t_copy2)
        temp3.close()
        temp4.close()
        temp5.close()
        temp3 = open(tn3, "r+b")
        temp4 = open(tn4, "r+b")
        temp5 = open(tn5, "r+b")



        # Paste aura parts into AMB
        print("Which aura slot?:")
        print("B, K, SSJ, SSJ2, SSJ3, SSJ4")
        slot = input("")
        slot = slot.lower()
        t_copy = temp3.read()
        t_copy2 = temp4.read()
        t_copy3 = temp5.read()
        if slot == "b" or slot == "1":
            temp2.seek(39216)
            print(hex(temp2.tell()))
            temp2.write(t_copy)
            temp2.seek(57264)
            print(hex(temp2.tell()))
            temp2.write(t_copy2)
            temp2.seek(71184)
            print(hex(temp2.tell()))
            temp2.write(t_copy3)
        elif slot == "k" or slot == "2":
            temp2.seek(39792)
            print(hex(temp2.tell()))
            temp2.write(t_copy)
            temp2.seek(59584)
            print(hex(temp2.tell()))
            temp2.write(t_copy2)
            temp2.seek(72512)
            print(hex(temp2.tell()))
            temp2.write(t_copy3)
        elif slot == "ssj" or slot == "3":
            temp2.seek(40368)
            print(hex(temp2.tell()))
            temp2.write(t_copy)
            temp2.seek(61904)
            print(hex(temp2.tell()))
            temp2.write(t_copy2)
            temp2.seek(73840)
            print(hex(temp2.tell()))
            temp2.write(t_copy3)
        elif slot == "ssj2" or slot == "4":
            temp2.seek(40944)
            print(hex(temp2.tell()))
            temp2.write(t_copy)
            temp2.seek(64224)
            print(hex(temp2.tell()))
            temp2.write(t_copy2)
            temp2.seek(75168)
            print(hex(temp2.tell()))
            temp2.write(t_copy3)
        elif slot == "ssj3" or slot == "5":
            temp2.seek(43280)
            print(hex(temp2.tell()))
            temp2.write(t_copy)
            temp2.seek(66544)
            print(hex(temp2.tell()))
            temp2.write(t_copy2)
            temp2.seek(76496)
            print(hex(temp2.tell()))
            temp2.write(t_copy3)
        elif slot == "ssj4" or slot == "6":
            temp2.seek(43856)
            print(hex(temp2.tell()))
            temp2.write(t_copy)
            temp2.seek(68864)
            print(hex(temp2.tell()))
            temp2.write(t_copy2)
            temp2.seek(77824)
            print(hex(temp2.tell()))
            temp2.write(t_copy3)
        temp2.close()

        # Paste into AMB, then saves it to your file
        temp2 = open(tn2, "r+b")
        t_copy = temp2.read()
        temp1.seek(84944)
        temp1.write(t_copy)
        temp1.close()
        temp1 = open(tn1, "r+b")
        t_copy = temp1.read()
        f.write(t_copy)
        f.close()
        print("")
        print("Completed!")

        # deletes temp files
        temp1 = open(tn1, "r+b")
        temp2 = open(tn2, "r+b")
        temp3 = open(tn3, "r+b")
        temp4 = open(tn4, "r+b")
        temp5 = open(tn5, "r+b")
        temp1.close()
        os.remove(tn1)
        temp2.close()
        os.remove(tn2)
        temp3.close()
        os.remove(tn3)
        temp4.close()
        os.remove(tn4)
        temp5.close()
        os.remove(tn5)
    elif choose == "no color":
        "finished"


def b3():
    # Create or edit aura bin(TO EDIT, BIN MUST BE CREATED FROM THIS SCRIPT TO WORK)
    print("Budokai 3 Aura Type Selected")
    print("")
    print("Create or Edit?(C/E)):")
    print("(TO EDIT, BIN MUST BE CREATED FROM THIS SCRIPT FIRST TO WORK!!)")
    choose = input("")
    choose = choose.lower()
    if choose == "c":
        # Creates a new file for you aura
        print("Name your aura bin:")
        x = input("")
        x = x + ".bin"
        f = open(x, "w+b")
    if choose == "e":
        # Opens bin
        print("Name your aura bin to edit:")
        x = input("")
        x = x + ".bin"
        f = open(x, "r+b")
        # Choose Mode
        print("")
        print("AMT edit or Color edit?(A/C)")
        mode = input("")
        mode = mode.lower()
        if mode == "a":
            # Copying files needed
            bin = open(x, "r+b")
            bin_copy = bin.read()

            # Setting up temp bins
            tn1 = "Files\Aura\z.bin"  # Will hold edited bin
            temp1 = open(tn1, "w+b")
            temp1.write(bin_copy)
            temp1.close()
            temp1 = open(tn1, "r+b")
            tn2 = "AMT TO EDIT.amt"  # Will hold AMT data for user to edit
            temp2 = open(tn2, "w+b")
            temp1.seek(85344)
            amt_copy = temp1.read(27840)
            temp2.write(amt_copy)
            temp2.close()

            # Let's the user edit the AMT before replacing old AMT
            print("The AMT has been duplicated for you to edit. Look for \"AMT TO EDIT.amt\" in the tool folder")
            print("DO NOT CHANGE THE FILE NAME OR MOVE THE FILE!! IT WILL BE PASTED OVER THE OLD AMT IN THE BIN!!")
            print("Please close the AMT when you are finished so that we can copy it and paste it back into the bin")
            print("")
            kill = input("Press Enter 2 times when finished editing")
            kill = input("Press Enter 1 time when finished editing")
            print("")
            temp2 = open(tn2, "r+b")
            t_copy = temp2.read()
            temp1.seek(85344)
            temp1.write(t_copy)
            temp1.close()
            temp1 = open(tn1, "r+b")
            t_copy = temp1.read()
            f.write(t_copy)
            f.close()
            print("Completed!")

            # deletes temp files
            temp1 = open(tn1, "r+b")
            temp2 = open(tn2, "r+b")
            temp1.close()
            os.remove(tn1)
            temp2.close()
            os.remove(tn2)
        if mode != "c":
            choose = "no color"
        if mode == "c":
            choose = "e"


    # Changing color
    # Copying files needed
    if choose == "c":
        bin = open("Files\Aura\dbz3_temp.bin", "r+b")
        bin_copy = bin.read()
        amb = open("Files\Aura\dbz3_amb.bin", "r+b")
        amb_copy = amb.read()
        aura = open("Files\Aura\dbz3_aura.bin", "r+b")
        aura_copy = aura.read()
    elif choose == "e":
        bin = open(x, "r+b")
        bin_copy = bin.read()
        aura = open("Files\Aura\dbz3_aura.bin", "r+b")
        aura_copy = aura.read()
    elif choose == "no color":
        "finished"

    if choose == "c" or choose == "e":
        # Setting up temp bins
        tn1 = "Files\Aura\z.bin"  # Will hold edited bin
        temp1 = open(tn1, "w+b")
        temp1.write(bin_copy)
        temp1.close()
        temp1 = open(tn1, "r+b")
        tn2 = "Files\Aura\z2.bin"  # Will hold edited AMB
        temp2 = open(tn2, "w+b")
        if choose == "c":
            temp2.write(amb_copy)
            temp2.close()
            temp2 = open(tn2, "r+b")
        elif choose == "e":
            temp1.seek(84944)
            amb_copy = temp1.read()
            temp2.write(amb_copy)
            temp2.close()
            temp2 = open(tn2, "r+b")
            temp1.seek(0)
        tn3 = "Files\Aura\z3.bin"  # Will hold edited aura
        temp3 = open(tn3, "w+b")
        temp3.write(aura_copy)
        temp3.close()
        temp3 = open(tn3, "r+b")
    elif choose == "no color":
        "finished"

    if choose == "c" or choose == "e":
        # Selecting first aura color
        print("Primary aura color:")
        print("")
        print("Custom, B, K, SSJ, SSJ3, SSJ4, Mystic?")
        color_type = input("")
        color_type = color_type.lower()
        if color_type == "custom" or color_type == "c" or color_type == "1":
            color_type == "custom"
            # Converts RGB value to bytes
            print("Amount of red used? (between 0 and 255)")
            r_color = int(input("")) / 255
            r_color = bytes.fromhex(struct.pack("f", r_color).hex())
            print("Red: "+str(r_color))
            print("")
            print("Amount of green used? (between 0 and 255)")
            g_color = int(input("")) / 255
            g_color = bytes.fromhex(struct.pack("f", g_color).hex())
            print("Green: "+str(g_color))
            print("")
            print("Amount of blue used? (between 0 and 255)")
            b_color = int(input("")) / 255
            b_color = bytes.fromhex(struct.pack("f", b_color).hex())
            print("Blue: "+str(b_color))
            print("")
        elif color_type == "b" or color_type == "2":
            r_color = 0 / 255
            r_color = bytes.fromhex(struct.pack("f", r_color).hex())
            g_color = 165 / 255
            g_color = bytes.fromhex(struct.pack("f", g_color).hex())
            b_color = 255 / 255
            b_color = bytes.fromhex(struct.pack("f", b_color).hex())
            print("Red: "+str(r_color))
            print("Green: "+str(g_color))
            print("Blue: "+str(b_color))
            print("")
            color_type = "custom"
        elif color_type == "k" or color_type == "3":
            r_color = 255 / 255
            r_color = bytes.fromhex(struct.pack("f", r_color).hex())
            g_color = 58 / 255
            g_color = bytes.fromhex(struct.pack("f", g_color).hex())
            b_color = 58 / 255
            b_color = bytes.fromhex(struct.pack("f", b_color).hex())
            print("Red: "+str(r_color))
            print("Green: "+str(g_color))
            print("Blue: "+str(b_color))
            print("")
            color_type = "custom"
        elif color_type == "ssj" or color_type == "4":
            d_color = open("Files\Aura\d_color.bin", "r+b")
            d_color.seek(16)
            t_copy = d_color.read(64)   # 4 lines
            d_color.seek(16)
            t_copy2 = d_color.read(32)  # 2 lines
            print("RGB: Default")
            print("")
            color_type = "default"
        elif color_type == "ssj3" or color_type == "5":
            d_color = open("Files\Aura\d_color.bin", "r+b")
            d_color.seek(176)
            t_copy = d_color.read(64)   # 4 lines
            d_color.seek(176)
            t_copy2 = d_color.read(32)  # 2 lines
            print("RGB: Default")
            print("")
            color_type = "default"
        elif color_type == "ssj4" or color_type == "6":
            print("Goku, Vegeta, Gogeta?(G/V/GV)")
            ssj4 = input("")
            ssj4 = ssj4.lower()
            if ssj4 == "goku" or ssj4 == "g":
                d_color = open("Files\Aura\d_color.bin", "r+b")
                d_color.seek(336)
                t_copy = d_color.read(64)   # 4 lines
                d_color.seek(336)
                t_copy2 = d_color.read(32)  # 2 lines
                color_type = "default"
            elif ssj4 == "vegeta" or ssj4 == "v":
                d_color = open("Files\Aura\d_color.bin", "r+b")
                d_color.seek(496)
                t_copy = d_color.read(64)   # 4 lines
                d_color.seek(496)
                t_copy2 = d_color.read(32)  # 2 lines
                color_type = "default"
            elif ssj4 == "gogeta" or ssj4 == "gv":
                d_color = open("Files\Aura\d_color.bin", "r+b")
                d_color.seek(656)
                t_copy = d_color.read(64)   # 4 lines
                d_color.seek(656)
                t_copy2 = d_color.read(32)  # 2 lines
            print("RGB: Default")
            print("")
            color_type = "default"
        elif color_type == "mystic" or color_type == "7":
            d_color = open("Files\Aura\d_color.bin", "r+b")
            d_color.seek(816)
            t_copy = d_color.read(64)  # 4 lines
            d_color.seek(816)
            t_copy2 = d_color.read(32)  # 2 lines
            print("RGB: Default")
            print("")
            color_type = "default"

        # Replacing values with your color
        if color_type == "custom" or color_type == "1":
            old_r = b'\xAA\xAA\xAA\xAA'
            old_g = b'\xBB\xBB\xBB\xBB'
            old_b = b'\xCC\xCC\xCC\xCC'
            t_copy = temp3.read()
            t_copy = t_copy.replace(old_r, r_color)
            t_copy = t_copy.replace(old_g, g_color)
            t_copy = t_copy.replace(old_b, b_color)
            temp3.close()
            temp3 = open(tn3, "r+b")
            temp3.write(t_copy)
        elif color_type == "default":
            temp3.seek(144)
            temp3.write(t_copy)
        temp3.close()
        temp3 = open(tn3, "r+b")


        # Selecting second aura color
        # Converts RGB value to bytes
        print ("Secondary Aura color:")
        print("")
        print("Custom, B, K, SSJ, SSJ3, SSJ4, Mystic?")
        color_type = input("")
        color_type = color_type.lower()
        if color_type == "custom" or color_type == "c" or color_type == "1":
            color_type == "custom"
            # Converts RGB value to bytes
            print("Amount of red used? (between 0 and 255)")
            r_color = int(input("")) / 255
            r_color = bytes.fromhex(struct.pack("f", r_color).hex())
            print("Red: "+str(r_color))
            print("")
            print("Amount of green used? (between 0 and 255)")
            g_color = int(input("")) / 255
            g_color = bytes.fromhex(struct.pack("f", g_color).hex())
            print("Green: "+str(g_color))
            print("")
            print("Amount of blue used? (between 0 and 255)")
            b_color = int(input("")) / 255
            b_color = bytes.fromhex(struct.pack("f", b_color).hex())
            print("Blue: "+str(b_color))
            print("")
        elif color_type == "b" or color_type == "2":
            r_color = b'\x00\x00\x80\x3F'
            g_color = b'\x00\x00\x80\x3F'
            b_color = b'\x00\x00\x80\x3F'
            print("Red: "+str(r_color))
            print("Green: "+str(g_color))
            print("Blue: "+str(b_color))
            print("")
            color_type = "custom"
        elif color_type == "k" or color_type == "3":
            r_color = 255 / 255
            r_color = bytes.fromhex(struct.pack("f", r_color).hex())
            g_color = 0 / 255
            g_color = bytes.fromhex(struct.pack("f", g_color).hex())
            b_color = 0 / 255
            b_color = bytes.fromhex(struct.pack("f", b_color).hex())
            print("Red: "+str(r_color))
            print("Green: "+str(g_color))
            print("Blue: "+str(b_color))
            print("")
            color_type = "custom"
        elif color_type == "ssj" or color_type == "4":
            d_color = open("Files\Aura\d_color.bin", "r+b")
            d_color.seek(96)
            t_copy = d_color.read(64)  # 4 lines
            d_color.seek(96)
            t_copy2 = d_color.read(32)  # 2 lines
            print("RGB: Default")
            print("")
            color_type = "default"
        elif color_type == "ssj3" or color_type == "5":
            d_color = open("Files\Aura\d_color.bin", "r+b")
            d_color.seek(256)
            t_copy = d_color.read(64)  # 4 lines
            d_color.seek(256)
            t_copy2 = d_color.read(32)  # 2 lines
            print("RGB: Default")
            print("")
            color_type = "default"
        elif color_type == "ssj4" or color_type == "6":
            print("Goku, Vegeta, Gogeta?(G/V/GV)")
            ssj4 = input("")
            ssj4 = ssj4.lower()
            if ssj4 == "goku" or ssj4 == "g":
                d_color = open("Files\Aura\d_color.bin", "r+b")
                d_color.seek(416)
                t_copy = d_color.read(64)  # 4 lines
                d_color.seek(416)
                t_copy2 = d_color.read(32)  # 2 lines
                color_type = "default"
            elif ssj4 == "vegeta" or ssj4 == "v":
                d_color = open("Files\Aura\d_color.bin", "r+b")
                d_color.seek(576)
                t_copy = d_color.read(64)  # 4 lines
                d_color.seek(576)
                t_copy2 = d_color.read(32)  # 2 lines
                color_type = "default"
            elif ssj4 == "gogeta" or ssj4 == "gv":
                d_color = open("Files\Aura\d_color.bin", "r+b")
                d_color.seek(736)
                t_copy = d_color.read(64)  # 4 lines
                d_color.seek(736)
                t_copy2 = d_color.read(32)  # 2 lines
            print("RGB: Default")
            print("")
            color_type = "default"
        elif color_type == "mystic" or color_type == "7":
            d_color = open("Files\Aura\d_color.bin", "r+b")
            d_color.seek(896)
            t_copy = d_color.read(64)  # 4 lines
            d_color.seek(896)
            t_copy2 = d_color.read(32)  # 2 lines
            print("RGB: Default")
            print("")
            color_type = "default"

        # Replacing values with your color
        if color_type == "custom" or color_type == "1":
            old_r = b'\xDD\xDD\xDD\xDD'
            old_g = b'\xEE\xEE\xEE\xEE'
            old_b = b'\xF7\xF7\xF7\xF7'
            t_copy = temp3.read()
            t_copy = t_copy.replace(old_r, r_color)
            t_copy = t_copy.replace(old_g, g_color)
            t_copy = t_copy.replace(old_b, b_color)
            temp3.close()
            temp3 = open(tn3, "r+b")
            temp3.write(t_copy)
        elif color_type == "default":
            temp3.seek(432)
            temp3.write(t_copy)
        temp3.close()
        temp3 = open(tn3, "r+b")



        # Paste aura parts into AMB
        print("Which aura slot?:")
        print("B, K, SSJ, SSJ2, SSJ3, SSJ4")
        slot = input("")
        slot = slot.lower()
        t_copy = temp3.read()
        if slot == "b" or slot == "1":
            temp2.seek(28240)
            print(hex(temp2.tell()))
            temp2.write(t_copy)
        elif slot == "k" or slot == "2":
            temp2.seek(28816)
            print(hex(temp2.tell()))
            temp2.write(t_copy)
        elif slot == "ssj" or slot == "3":
            temp2.seek(29392)
            print(hex(temp2.tell()))
            temp2.write(t_copy)
        elif slot == "ssj2" or slot == "4":
            temp2.seek(29968)
            print(hex(temp2.tell()))
            temp2.write(t_copy)
        elif slot == "ssj3" or slot == "5":
            temp2.seek(32304)
            print(hex(temp2.tell()))
            temp2.write(t_copy)
        elif slot == "ssj4" or slot == "6":
            temp2.seek(32880)
            print(hex(temp2.tell()))
            temp2.write(t_copy)
        temp2.close()

        # Paste into AMB, then saves it to your file
        temp2 = open(tn2, "r+b")
        t_copy = temp2.read()
        temp1.seek(84944)
        temp1.write(t_copy)
        temp1.close()
        temp1 = open(tn1, "r+b")
        t_copy = temp1.read()
        f.write(t_copy)
        f.close()
        print("")
        print("Completed!")

        # deletes temp files
        temp1 = open(tn1, "r+b")
        temp2 = open(tn2, "r+b")
        temp3 = open(tn3, "r+b")
        temp1.close()
        os.remove(tn1)
        temp2.close()
        os.remove(tn2)
        temp3.close()
        os.remove(tn3)
    elif choose == "no color":
        "finished"



def again():
    yn = input("Load another? (Y/N)")
    yn = yn.lower()
    if yn == "y" or yn == "yes":
        aura_type()
        again()
    else:
        print("Aura creator by: Nexus-sama")
        print("Follow me on Twitter @NexusTheModder")
        kill = input("press enter to close")



aura_type()
again()


exit()
