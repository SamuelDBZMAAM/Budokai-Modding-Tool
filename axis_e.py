#Axis Editor - axis_e
#Purpose of tool:
#To edit the axis' of the first AMG to adjust sizes of bones such as
#arm1, arm2, waist, stmc, neck, etc
#
#You can add in values manually, or you can edit then use the preset file
#to edit the axis to a set design


import struct
import os
import math
import random
#importing random for giving the user random effects lol



def main():
    #--first, open character file
    print("Insert the AMO:")
    x = input("")
    x = x.replace("\"", "")
    f = open(x, "r+b")
    #--second, open preset file
    p = "Files\AMG\presets\list_of_presets.txt"
    lop = open(p, "r")
    lop_choices = lop.read()
    print("The basic presets are:")
    print(lop_choices)
    print("")
    lop.close()

    ##opens up the preset of choice
    
    print("Insert _T file (no extension):")
    choice = input("")
    choice = choice + ".txt"
    choice_t = "Files\AMG\presets\\"
    choice_t = choice_t + choice
    t = open(choice_t, "r")

    print("Insert _H file (no extension):")
    choice = input("")
    choice = choice + ".bin"
    choice_h = "Files\AMG\presets\\"
    choice_h = choice_h + choice
    h = open(choice_h, "r+b")
    h_len = h.seek(0,2)
    h_line_len = (int(h_len)/16)
    h_line_len = int(h_line_len)

    #--third, gain axis locations
    f_axis_names = []
    f_axis_pos = []
    f_axis_dat = []
    f_new_names = []

    ##gathering axis amounts
    f.seek(0)
    f.seek(16)
    hti = f.read(4)
    f_name_amnt = hex_to_int(hti)
    f_amnt = f_name_amnt
    f_name_amnt = (f_name_amnt * 16 * 2)

    ##first amg location
    f.seek(0)
    f.seek(48)
    hti = f.read(4)
    f_amg_loc = hex_to_int(hti)

    ##first amg length
    f.seek(0)
    f.seek(f_amg_loc + 28)
    hti = f.read(4)
    f_amg_len = hex_to_int(hti)
    

    ##gathering names
    for i in range(((f_amnt))):
        f.seek(0)
        f.seek((f_amg_loc + (i*32) + f_amg_len))
        f_axis_names.append(f.read(32))


    ##gathering axis locs + data
    for i in range(((f_amnt))):
        f.seek(0)
        f.seek(f_amg_loc + (32*(i+1)) + (48*i))
        f_axis_pos.append(f.tell())
        f_axis_dat.append(f.read(48))
    #print(f_axis_pos)

    ##adding names to a list
    for i in range(int(len(f_axis_names))):
        new_value = f_axis_names[i]
        new_value = new_value.replace(b"\x00", b"\x2e")
        new_value = str(bytes(new_value))
        new_value = new_value.replace(".", "")
        new_value = new_value.replace("b'", "")
        new_value = new_value.replace("'", "")
        new_value = new_value.replace("_", "")
        new_value = new_value.replace("L00", "")
        new_value = new_value[3:]
        new_value = new_value.replace("X", "")
        f_new_names.append(new_value)
    print(f_new_names)


    ##taking _t names
    t_vals = []
    lines = t.readlines()
    for i in range(h_line_len):
        fff = str(lines[i].strip("\n"))
        t_vals.append(fff)



    ##taking _h values
    h_vals = []
    h.seek(0)
    for i in range(h_line_len):
        h.seek((i*16))
        fff = h.read(16)
        h_vals.append(fff)



    #print(t_vals)
    #print(h_vals)

    
    #--fourth, apply edits from preset
    axis_to_edit_name = []
    axis_to_edit_locs = []

    ##assign each wanted pos and data with one another
    for i in range(h_line_len):
        want_pos_name = t_vals[i]
        #want_pos_data = h_vals[i]

        ##grabs the wanted name from file and puts it in a list
        for i in range(len(f_new_names)):
            aaa = want_pos_name
            bbb = f_new_names[i]
            if aaa == bbb:
                got_pos_name = f_new_names[i]
                got_pos_locs = f_axis_pos[i]
                axis_to_edit_name.append(got_pos_name)
                axis_to_edit_locs.append(got_pos_locs)
                
    #print(axis_to_edit_name)
    #print(axis_to_edit_locs)

    for i in range(len(axis_to_edit_name)):
        f.seek(0)
        f.seek(axis_to_edit_locs[i]+32)
        f.write(h_vals[i])


    print("Completed!")
    


    f.close()
    t.close()
    h.close()




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
    yn = input("Would you like to load another? (Y/N)")
    yn = yn.lower()
    if yn == "y" or yn == "yes":
        main()
        again()
    else:
        print("")
        kill = input("press enter to close")


main()
again()

exit()
