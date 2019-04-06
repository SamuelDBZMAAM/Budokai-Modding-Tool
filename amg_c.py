#AMG Creation - amg_c
#Purpose: To create an AMG to hold model parts


print("Create an AMG ")
print("With this you can add model parts into an AMG")
print("Works in B3 and SB2!")
       

import struct
import math
import os

def main():
    print("AMG Creation Tool")
    print("Insert the name of AMG you want: ")
    x = input("")
    f = open(x, "w+b")

    amg_choice = ["b3", "sb2"]
    
    print("Is this AMG for B3 or SB2?")
    pick_choice = input("")
    pick_choice = pick_choice.lower()

    while pick_choice not in amg_choice:
        print("Please pick B3 or SB2")
        pick_choice = input("")

    if pick_choice == "b3":

        # Copying files needed
        hti = 0
        ith = 0

        #b3 axis bins
        b3_amg_head = open("Files/AMG/b3_amg_head.bin", "r+b")
        b3ah = b3_amg_head.read()
        b3_amg_axis = open("Files/AMG/b3_amg_axis.bin", "r+b")
        b3aa = b3_amg_axis.read()
        b3_amg_mp1 = open("Files/AMG/b3_amg_mp1.bin", "r+b")
        b3am1 = b3_amg_mp1.read()
        b3_amg_mp2 = open("Files/AMG/b3_amg_mp2.bin", "r+b")
        b3am2 = b3_amg_mp2.read()
        b3_amg_end = open("Files/AMG/b3_amg_end.bin", "r+b")
        b3ae = b3_amg_end.read()
        
        

        # Setting up temp bins
        tn1 = "Files\z.bin" 
        temp1 = open(tn1, "w+b")
        temp1.close()
        temp1 = open(tn1, "r+b")
        tn2 = "Files\z2.bin" 
        temp2 = open(tn2, "w+b")
        temp2.close()
        temp2 = open(tn2, "r+b")
        tn3 = "Files\z3.bin" 
        temp3 = open(tn3, "w+b")
        temp3.close()
        temp3 = open(tn3, "r+b")
        tn4 = "Files\z4.bin"
        temp4 = open(tn4, "w+b")
        temp4.close()
        temp4 = open(tn4, "r+b")
        tn5 = "Files\z5.bin"
        temp5 = open(tn5, "w+b")
        temp5.close()
        temp5 = open(tn5, "r+b")


        #inserts the header of an AMG
        f.write(b3ah)
        f.seek(0)


        # - Insert how many axis user wants
        print("How many axis do you want?")
        axis_amnt = int(input(""))

        #adds each axis
        for i in range(axis_amnt):
            f.seek(0,2)
            f.write(b3aa)

        #gets the offset location of each mp offset on an axis
        axis_mp_loc = []
        for i in range(axis_amnt):
            f.seek(0)
            f.seek(32 + 52 + (i*80))
            axis_mp_loc.append(f.tell())
        #print(axis_mp_loc)
        
        
        # - Insert model part chunks and insert model parts to each
        mp_ch_locs = []
        mp_lcs = []
        mp_end_locs = []
        
        

        #writes mp chunks
        for i in range(axis_amnt):
            mp_chunk_locs = []
            mp_locs = []
            cur_amg_len = f.seek(0,2)
            #writes the model part chunk
            mp_chunk_locs.append(f.seek(0,2))
            mp_ch_locs.append(f.seek(0,2))
            f.write(b3am1)
            print("How many model parts are there?")
            b3am2_amnt = int(input(""))
            new_amnt = int(((math.ceil(b3am2_amnt/4))))
            #writes in the amount of lines needed for adding model parts
            for i in range(new_amnt):
                f.seek(0,2)
                f.write(b3am2)
            #adds in those model parts
            for i in range(b3am2_amnt):
                mp_locs.append(f.seek(0,2))
                mp_lcs.append(f.seek(0,2))
                print("Insert Model Part:")
                y = input("")
                new_part = open(y, "r+b")
                npr = new_part.read()
                f.write(npr)
            #writes the offsets of each model part to the mp chunk
            for i in range(b3am2_amnt):
                f.seek(cur_amg_len+32+(i*4))
                ith = (mp_locs[i] - 16 - cur_amg_len)
                hex_mp = int_to_hex(ith)
                f.write(hex_mp)

            #mp_ch_locs.append(mp_chunk_locs[i])
            #mp_lcs.append(mp_locs[i])
                

            
            #writes the end of model part data to not make them disappear
            mp_end_locs.append(f.seek(0,2))
            f.seek(0,2)
            f.write(b3ae)

        
        # - Adjust length and variables
        #print(mp_ch_locs)
        #print(mp_lcs)

        #changes all the mp chunk locations on an amg
        for i in range(len(axis_mp_loc)):
            f.seek(0)
            f.seek(axis_mp_loc[i])
            ith = mp_ch_locs[i]
            mpchlocs = int_to_hex(ith)
            f.write(mpchlocs)
            
        #fixes the mp chunk end locations
        for i in range(len(mp_ch_locs)):
            f.seek(0)
            f.seek(mp_ch_locs[i] + 12)
            ith = mp_end_locs[i]
            mpendlocs = int_to_hex(ith)
            f.write(mpendlocs)

        #fixes the amg length
        f.seek(0)
        ith = f.seek(0,2)
        amg_length = int_to_hex(ith)
        f.seek(0)
        f.seek(28)
        f.write(amg_length)
        
        # - Write data to a text file for use
        text_file = open("b3_axis_locs.txt", "w+")
        
        #options to write axis names
        print("Do you want to add names for each axis? (y/n) ")
        name_ask = input("")
        name_ask = name_ask.lower()
        name_ask = name_ask[0:1]
        if name_ask == "y":
            for i in range(axis_amnt):
                print("Please insert the name of axis", str(i + 1))
                text_insert = input("")
                if len(text_insert) > 32:
                    print("Please keep within the 32 character limit")
                    text_insert = input("")
                text_insert = text_insert.upper()
                text_insert = bytes(text_insert, "utf-8")
                for i in range(32 - len(text_insert)):
                    text_insert = text_insert + b"\x00"
                f.seek(0,2)
                f.write(text_insert)
                
                
                
        else:
            print("")
        
        print("Complete!")
        
        







        f.close()
        text_file.close()




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
