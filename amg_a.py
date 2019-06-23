#AMG Addition - amg_a
#Purpose: To add an AMG onto a character's model with their AMO0
#Not to be used with characters with no space left, please add an extra line
#before using this, please using the extra line function

print("Please only insert the AMO of a character")
print("With this you can only add one AMG at a time")

import struct
import math
        

def main():
    #print("")
    print("Insert AMO:")
    x = input("")
    x = x.replace("\"", "")
    f = open(x, "r+b")

    print("Insert AMG to add:")
    y = input("")
    y = y.replace("\"", "")
    amg = open(y, "r+b")

    #open and write amg to amo
    full_amg = amg.read()
    amg_pos = f.seek(0,2)
    f.write(full_amg)

    #writes necessary data to amo
    f.seek(0)
    f.seek(24)
    hti = f.read(4)
    amg_amnt = hex_to_int(hti)
    ith = (amg_amnt + 1)
    new_amnt = int_to_hex(ith)
    f.seek(0)
    f.seek(24)
    f.write(new_amnt)
    
    amo_head = 48
    next_space = (amo_head + (amg_amnt * 4))
    f.seek(0)
    f.seek(next_space)
    ith = amg_pos
    ith2 = amg_pos + 32
    new_loc = int_to_hex(ith)
    amg_axis_loc = int_to_hex(ith2)
    
    f.write(new_loc)

    f.seek(0)
    amo_len = f.seek(0,2)
    ith = amo_len
    amo_len = int_to_hex(ith)
    f.seek(0)
    f.seek(36)
    f.write(amo_len)


    #locates each axis name and line
    f_axis_names = []
    f_axis_line_pos = []

    #--gathering names

    #-gathering locations and sizes

    #first amg location
    f.seek(0)
    f.seek(48)
    hti = f.read(4)
    f_amg_loc = hex_to_int(hti)

    #amount of axis
    f.seek(0)
    f.seek(16)
    hti = f.read(4)
    f_name_amnt = hex_to_int(hti)

    f_amnt = f_name_amnt
    f_name_amnt = (f_name_amnt * 32)


    #axis line size
    f.seek(0)
    f.seek(32)
    hti = f.read(4)
    f_ax_li_len = hex_to_int(hti)


    #axis line locations
    f.seek(0)
    f.seek(20)
    hti = f.read(4)
    f_bl_loc = hex_to_int(hti)


    #first amg length
    f.seek(0)
    f.seek(f_amg_loc + 28)
    hti = f.read(4)
    f_amg_len = hex_to_int(hti)


    #gathering names of axis
    for i in range(((f_amnt))):
        f.seek(0)
        f.seek((f_amg_loc + (i*32) + f_amg_len))
        f_axis_names.append(f.read(32))

    #gathering axis line pos
    for i in range(((f_amnt))):
        f.seek(0)
        f.seek(f_bl_loc + (f_name_amnt) + (i*f_ax_li_len*16))
        f_axis_line_pos.append(f.tell())




    f_new_names = []

    #-Writing New Values

    #fixes names
    for i in range(int(len(f_axis_names))):
        #print("")
        new_value = f_axis_names[i]
        #print(new_value)
        new_value = new_value.replace(b"\x00", b"\x2e")
        #print(new_value)
        new_value = str(bytes(new_value))
        #print(new_value)
        new_value = new_value.replace(".", "")
        #print(new_value)
        new_value = new_value.replace("b'", "")
        #print(new_value)
        new_value = new_value.replace("'", "")
        #print(new_value)
        new_value = new_value.replace("X", "")
        #print(new_value)
        new_value = new_value.replace("_", "")
        #print(new_value)
        new_value = new_value[3:]
        #print(new_value)
        f_new_names.append(new_value)


    #new text file for pastingin new data
    text_file = open("b3_axis_locs.txt", "w+")



    cancel = False
    while cancel != True:
        print(f_new_names)
        print("Choose an axis from the add-on model")
        f_choice = input("")
        f_choice = f_choice.upper()

        while f_choice not in f_new_names:
            print("Not a valid axis, try again.")
            f_choice = input("")
            f_choice = f_choice.upper()

        f_cho_pos = int(f_new_names.index(f_choice))


        
        f.seek(0)
        for i in range(f_ax_li_len):
            f.seek(f_axis_line_pos[f_cho_pos]+8+(i*16))
            f.write(amg_axis_loc)
        
        axi_loc_name = amg_axis_loc
        axi_loc_name = hex_to_int(axi_loc_name)
        axi_loc_name = hex(axi_loc_name)
        axi_loc_name = axi_loc_name.replace("0x", "")

        
        #writes data to text file for people who want to further use
        text_file.write(str(f_choice) + " = " + str(axi_loc_name) + "\n")

        print("Added!")
        cancel = True
    

    text_file.close()







    

    #closing files
    f.close()
    amg.close()
    


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
