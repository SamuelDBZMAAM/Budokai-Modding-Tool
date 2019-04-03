#SHIN BUDOKAI 2 MODEL COMBINER
#Purpose - Basically the LGBT Method of SB2 lmao

import struct
import math
import os



def main():
    hti = 0
    ith = 0
    
    #print("")
    print("Insert Base Model AMO:")
    x = input("")
    x = x.replace("\"", "")
    f = open(x, "r+b")

    print("")
    print("Insert Add-on Model AMO:")
    y = input("")
    y = y.replace("\"", "")
    g = open(y, "r+b")

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





    #-Opens both files, reads then writes to temp1
    f_read = f.read()

    #first amg location
    #print("------------------")
    #print("G Values")
    g.seek(48)
    hti = g.read(4)
    #print(hti)
    g_amg_loc = hex_to_int(hti)
    #print(g_amg_loc)

    #first amg length
    g.seek(0)
    g.seek(g_amg_loc + 28)
    hti = g.read(4)
    #print(hti)
    g_amg_len = hex_to_int(hti)
    #print(g_amg_len)

    #gathering the name list
    g.seek(0)
    g.seek(16)
    hti = g.read(4)
    #print(hti)
    g_name_amnt = hex_to_int(hti)
    #print(g_name_amnt)
    g_amnt = g_name_amnt
    g_name_amnt = (g_name_amnt * 16 * 2)
    #print(g_name_amnt)

    #reading, then writing both f and g to temp1
    temp1.write(f_read)
    amg_pos = temp1.seek(0,2)
    #print("amg pos", str(amg_pos))
    g.seek(0)
    g.seek(g_amg_loc)
    g_read = g.read((g_amg_len + g_name_amnt))
    temp1.write(g_read)


    #-Search and assign values

    
    #gathering f values same as above + axis lines
    #print("------------------")
    #print("F Values")
    temp1.seek(48)
    hti = temp1.read(4)
    #print(hti)
    f_amg_loc = hex_to_int(hti)
    #print(f_amg_loc)

    temp1.seek(0)
    temp1.seek(f_amg_loc + 28)
    hti = temp1.read(4)
    #print(hti)
    f_amg_len = hex_to_int(hti)
    #print(f_amg_len)

    temp1.seek(0)
    temp1.seek(16)
    hti = temp1.read(4)
    #print(hti)
    f_name_amnt = hex_to_int(hti)
    #print(f_name_amnt)
    f_amnt = f_name_amnt
    f_name_amnt = (f_name_amnt * 16 * 2)
    #print(f_name_amnt)

    temp1.seek(0)
    temp1.seek(32)
    hti = temp1.read(4)
    #print(hti)
    f_ax_li_len = hex_to_int(hti)
    #print(f_ax_li_len)

    temp1.seek(0)
    temp1.seek(20)
    hti = temp1.read(4)
    #print(hti)
    f_bl_loc = hex_to_int(hti)
    #print(f_bl_loc)

    
    #assigning each f_name to an f_axis

    #axis names
    f_axis_names = []
    #axis pos and data
    f_axis_pos = []
    f_axis_dat = []
    #axis first line loc
    f_axis_line_pos = []
    

    #gathering names
    for i in range(((f_amnt))):
        temp1.seek(0)
        temp1.seek((f_amg_loc + (i*32) + f_amg_len))
        f_axis_names.append(temp1.read(32))
    #print(f_axis_names)

    #gathering axis locs
    for i in range(((f_amnt))):
        temp1.seek(0)
        temp1.seek(f_amg_loc + (32*(i+1)) + (48*i))
        f_axis_pos.append(temp1.tell())
        f_axis_dat.append(temp1.read(48))
    #print(f_axis_pos)
    #print(f_axis_dat)

    #gathering axis line pos
    for i in range(((f_amnt))):
        temp1.seek(0)
        temp1.seek(f_bl_loc + (f_name_amnt) + (i*f_ax_li_len*16))
        f_axis_line_pos.append(temp1.tell())
    #print(f_axis_line_pos)
        
        

    #assigning each g_name to an g_axis

    #axis names
    g_axis_names = []
    #axis pos and data
    g_axis_pos = []
    g_axis_dat = []
    

    #gathering names
    for i in range(((g_amnt))):
        temp1.seek(0)
        temp1.seek(((i*32) + g_amg_len)+ amg_pos)
        g_axis_names.append(temp1.read(32))
    #print(g_axis_names)

    #gathering axis locs
    for i in range(((g_amnt))):
        temp1.seek(0)
        temp1.seek((32*(i+1)) + (48*i)+ amg_pos)
        g_axis_pos.append(temp1.tell())
        g_axis_dat.append(temp1.read(48))
    #print(g_axis_pos)
    #print(g_axis_dat)




    g_new_names = []
    f_new_names = []

    #-Write values
    #g values
    for i in range(int(len(g_axis_names))):
        #print("")
        new_value = g_axis_names[i]
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
        g_new_names.append(new_value)

    #print(g_new_names)

    #f values
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

    #print(f_new_names)

    #placing the axis on the axis lines
    types = ["number", "text"]
    print(types)
    insert_type = input("Choose how you want to insert axis: ")
    insert_type = insert_type.lower()

    while insert_type not in types:
        print(types)
        insert_type = input("Not in the types list choose again: ")

    if insert_type == "number":
        
        cancel = False

        while cancel != True:
            print(g_new_names)
            print("The last value is: " + str(len(g_new_names) - 1))
            print("Choose an axis from the add-on model")
            print("(body = 0, waist = 1):")
            g_choice = int(input(""))


            #picks the axis location based on the choice
            ith = g_axis_pos[g_choice]
            print(ith)
            g_choice = int_to_hex(ith)
            print(g_choice)
            


            print(f_new_names)
            print("The last value is: " + str(len(f_new_names) - 1))
            print("Choose an axis from the base model")
            print("(body = 0, waist = 1):")
            f_choice = int(input(""))

            
            temp1.seek(0)
            temp1.seek(f_axis_line_pos[f_choice]+8)
            temp1.write(g_choice)

            print("Added!")
            print("Continue? (y/n)")
            cho = input("")
            cho = cho.lower()
            cho = cho[0:1]
            if cho == "y":
                cancel = False
            if cho == "n":
                cancel = True

        
    if insert_type == "text":
        print(g_new_names)
        print("Choose an axis from the add-on model")
        g_choice = input("")
        g_choice = g_choice.upper()

        while g_choice not in g_new_names:
            print("Not a valid axis, try again.")
            g_choice = input("")

        g_cho_pos = int(g_new_names.index(g_choice))

        ith = g_axis_pos[g_cho_pos]
        print(ith)
        g_choice = int_to_hex(ith)
        print(g_choice)
            

        print(f_new_names)
        print("Choose an axis from the add-on model")
        f_choice = input("")
        f_choice = f_choice.upper()

        while f_choice not in f_new_names:
            print("Not a valid axis, try again.")
            f_choice = input("")

        f_cho_pos = int(f_new_names.index(f_choice))

        
        temp1.seek(0)
        temp1.seek(f_axis_line_pos[f_cho_pos]+8)
        temp1.write(g_choice)
    


    #-Write to a new made file for realises
    print("Final Touches...")
    #file size
    temp1.seek(0)
    temp1.seek(0,2)
    
    ith = temp1.tell()
    file_len = int_to_hex(ith)

    temp1.seek(0)
    temp1.seek(36)
    temp1.write(file_len)
    
    #writes amg loc on nearest space
    temp1.seek(0)
    temp1.seek(24)
    hti = temp1.read(4)
    amg_amnt = hex_to_int(hti)
    amo_head = 48
    next_space = (amo_head + (amg_amnt * 4))
    temp1.seek(0)
    temp1.seek(next_space)
    ith = amg_pos
    new_loc = int_to_hex(ith)
    
    temp1.write(new_loc)
    

    #amg number edit
    temp1.seek(0)
    temp1.seek(24)

    hti = temp1.read(4)
    amg_no = hex_to_int(hti)
    amg_no += 1
    amg_no = int_to_hex(amg_no)

    temp1.seek(0)
    temp1.seek(24)

    temp1.write(amg_no)


    
    #read all then paste to new file
    temp1.seek(0)
    ccc = temp1.read()

    new_file = open("new_file.bin", "w+b")
    new_file.write(ccc)

    
    
    





    

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


    #closing files
    f.close()
    g.close()
    new_file.close()


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
    yn = yn[0:1]
    if yn == "y":
        main()
        again()
    else:
        print("")
        kill = input("press enter to close")








main()
again()

exit()
