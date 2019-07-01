5#AMG LGBT - amg_lgbt
#Purpose: to merge and fuse model parts and animations together using
#"LGBT" - Lean's Ginyu Bodyswap Technique

##-Insert Model Parts (Work with GGS) DONE
##-Better way of inserting animations DONE
##-Option for merging or replacing animations DONE
##-Correct the length of the first AMG DONE
##-Organise it more so it is cleaner DONE
##-Better export to .txt DONE





import random
import struct
import math
import os

def main():
    print("Welcome to the LGBT Tool!")
    print("")
    print("Please insert the base model (AMO):")
    x = input("")
    x = x.replace("\"", "")
    f = open(x, "r+b")

    print("Please insert the add-on model (AMO):")
    y = input("")
    y = y.replace("\"", "")
    g = open(y, "r+b")

    new_file = open("New_File.bin", "w+b")

    # Setting up temp bins
    tn1 = "Files\z1.bin" 
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
    tn6 = "Files\z6.bin"
    temp6 = open(tn6, "w+b")
    temp6.close()
    temp6 = open(tn6, "r+b")
    tn7 = "Files\z7.bin"
    temp7 = open(tn7, "w+b")
    temp7.close()
    temp7 = open(tn7, "r+b")
    tn8 = "Files\z8.bin"
    temp8 = open(tn8, "w+b")
    temp8.close()
    temp8 = open(tn8, "r+b")


    #-1. Extract first AMGs from each AMO (I can automate the new location of each AMG and axis on the main model)

    #Search and Extract first AMG to temp1
    chunk = f.read(16)
    lgbt_locs = []
    lgbt_lens = []
    f.seek(0)
    f.seek(16)
    hti = f.read(4)
    f_name_amnt_x = hex_to_int(hti)
    f_name_amnt = (f_name_amnt_x * 16 * 2)
    f.seek(0)
    f.seek(48)
    hti = f.read(4)
    first_amg = hex_to_int(hti)
    f.seek(0)
    f.seek(first_amg + 28)
    hti = f.read(4)
    first_amg_length = hex_to_int(hti)  


    #searches for already lgbt'd part
    while chunk != b"":
        if chunk[0] == 0x23 and chunk[1] == 0x4C and chunk[2] == 0x47 and chunk[3] == 0x42 and chunk[4] == 0x54:
            lgbt_locs.append(((f.tell()-16)))
        chunk = f.read(16)

    for i in range(int(len(lgbt_locs))):
        f.seek(0)
        f.seek(lgbt_locs[i]+28)
        hti = f.read(4)
        lgbt_len = hex_to_int(hti)
        lgbt_lens.append(lgbt_len)

    #print(lgbt_locs, lgbt_lens)



    ##get all of the file + other lgbts
    to_add = 0
    for i in range(int(len(lgbt_locs))):
        current = lgbt_lens[i]
        to_add += current
        
    f.seek(0)
    f.seek(first_amg) 
    first_amg_all = f.read(first_amg_length + f_name_amnt + to_add)
    to_add = 0
    temp1.write(first_amg_all)
    f.seek(0) 
        
    
    
    #Search and Extract first AMG to temp2
    g.seek(0)
    g.seek(16)
    hti = g.read(4)
    g_name_amnt_x = hex_to_int(hti)
    g_name_amnt = (g_name_amnt_x * 16 * 2)
    g.seek(0)
    g.seek(48)
    hti = g.read(4)
    second_amg = hex_to_int(hti)
    g.seek(0)
    g.seek(second_amg + 28)
    hti = g.read(4)
    second_amg_length = hex_to_int(hti)
    g.seek(0)
    g.seek(second_amg)
    second_amg_all = g.read(second_amg_length + g_name_amnt)
    temp2.write(second_amg_all)
    





    #-2. On the 2nd AMG, adjust ALL animations (even hands)

    #separates this amg from the rest for more than one round of lgbt
    temp2.seek(0)
    temp2.write(bytes("#LGBT", "utf-8"))

    #prepare values by gatheing the length of f and rounding it up
    ttt = first_amg_length + f_name_amnt
    #print(ttt)
    to_add = math.ceil(ttt / 65536)
    #print(to_add)
    to_add = to_add*65536
    #print(to_add)
   
    #gather all animation locations on temp2
    g_locs = []
    #print(g_name_amnt_x, "g_name_amnt_x")
    for i in range(int(g_name_amnt_x)):
        temp2.seek(16)
        #print(16+(((i+1) * 80)-12))
        temp2.seek(16+(((i+1) * 80)-12))
        hti = temp2.read(4)
        #print(hti, "hti")
        g_anim = hex_to_int(hti)
        g_locs.append(g_anim)

    
    #removing any animations that are empty or are not model part heavy
    #they will be separated and dealt with too

    g_anim_locs = []
    g_anim_other = []

    #emptiness check to get all the main anims with links and not empty or model parts
    for i in range(int(len(g_locs))):
        temp2.seek(0)
        temp2.seek(g_locs[i]+8)
        hti = temp2.read(4)
        empt_check = hex_to_int(hti)
        
        if empt_check != 0:
            g_anim_locs.append(g_locs[i])


    #model part check to get all the animations linked to model parts
    for i in range(int(len(g_locs))):
        temp2.seek(0)
        temp2.seek(g_locs[i]+4)
        hti = temp2.read(4)
        mp_check_1 = hex_to_int(hti)

        temp2.seek(0)
        temp2.seek(g_locs[i]+12)
        hti = temp2.read(4)
        mp_check_2 = hex_to_int(hti)
        
        if mp_check_1 != 0 and mp_check_2 != 0:
            g_anim_other.append(g_locs[i])
            
    #print(g_anim_other)
    #print(g_anim_locs)






    ##do the same, but for the f values

    #gather all animation locations on temp2
    f_locs = []
    temp1.seek(0)
    #print(g_name_amnt_x)
    for i in range(int(f_name_amnt_x)):
        temp1.seek(16)
        #print(16+(((i+1) * 80)-12))
        temp1.seek(16+(((i+1) * 80)-12))
        hti = temp1.read(4)
        f_anim = hex_to_int(hti)
        f_locs.append(f_anim)
    #print(f_anim_locs)

    
    #removing any animations that are empty or are not model part heavy
    #they will be separated and dealt with too

    f_anim_locs = []
    f_anim_other = []

    #emptiness check to get all the main anims with links and not empty or model parts
    #print(f_locs, "list")
    for i in range(int(len(f_locs))):
        temp1.seek(0)
        #print(temp1.seek(f_locs[i]+8), "seek")
        temp1.seek(0)
        temp1.seek(f_locs[i]+8)
        hti = temp1.read(4)
        #print(hti)
        empt_check = hex_to_int(hti)
        #print(empt_check, "empt")
        
        if empt_check != 0:
            #print(f_locs[i], "flocs")
            f_anim_locs.append(f_locs[i])

    #model part check to get all the animations linked to model parts
    for i in range(int(len(f_locs))):
        temp1.seek(0)
        temp1.seek(f_locs[i]+4)
        hti = temp2.read(4)
        mp_check_1 = hex_to_int(hti)

        temp1.seek(0)
        temp1.seek(f_locs[i]+12)
        hti = temp2.read(4)
        mp_check_2 = hex_to_int(hti)
        
        if mp_check_1 != 0 and mp_check_2 != 0:
            f_anim_other.append(f_locs[i])
            
    #print(g_anim_other)
    #print(g_anim_locs)

        

    #-3. Do calculations on adding 00s and then place 2nd AMG in main

    anim_chunk_len_list = []
    anim_chunk_len_other_list = []
    anim_chunk_loc_list = []
    anim_chunk_loc_other_list = []
    anim_ids = []
    
    #finding, counting and adding 00s on the normal anims
    for i in range(int(len(g_anim_locs))):
        #print(i)
        temp2seek = temp2.seek(g_anim_locs[i])
        temp2.seek(0)
        temp2.seek(g_anim_locs[i])
        hti = temp2.read(4)
        ids = hex_to_int(hti)
        anim_ids.append(ids)

        #print(anim_ids)
        
        temp2.seek(0)
        temp2.seek(g_anim_locs[i]+28)
        hti = temp2.read(4)
        anim_chunk_amnt = hex_to_int(hti)

        #print(str(anim_ids[i]), "is the id")
        
        for i in range(anim_chunk_amnt):
            #counter to keep it all even
            counter = i
            
            #gathers the amount of anim chunks there are in one section
            temp2.seek(0)
            temp2.seek(temp2seek + 32 + ((i)*32) + 4)
            hti = temp2.read(4)
            anim_chunk_len = hex_to_int(hti)
            anim_chunk_len_list.append(anim_chunk_len)
            
            #gathers the location of each chunk section or whatever lmao
            temp2.seek(0)
            temp2.seek(temp2seek + 32 + ((i)*32) + 8)
            hti = temp2.read(4)
            anim_chunk_loc = hex_to_int(hti)
            anim_chunk_loc_list.append(anim_chunk_loc)

            #gathers the amount of anim chunks in the other sections
            temp2.seek(0)
            temp2.seek(temp2seek + 32 + ((i)*32) + 12)
            hti = temp2.read(4)
            anim_chunk_len_other = hex_to_int(hti)
            if anim_chunk_len_other != 0:
                anim_chunk_len_other_list.append(anim_chunk_len_other)

            #gathers the location of each chunk section or whatever lmao
            temp2.seek(0)
            temp2.seek(temp2seek + 32 + ((i)*32) + 16)
            hti = temp2.read(4)
            anim_chunk_loc_other = hex_to_int(hti)
            if anim_chunk_len_other != 0:
                anim_chunk_loc_other_list.append(anim_chunk_loc_other)

            #print(anim_chunk_len_list, anim_chunk_len_other_list, anim_chunk_loc_list, anim_chunk_loc_other_list)

            
            #for actually adding the 00s to each part
            for i in range(int(len(anim_chunk_len_list))):
                old_loc = []
                new_loc = []
                
                #seek to the chunk position
                chunkseek = temp2.seek(anim_chunk_loc_list[i])
                #print(str(chunkseek), "is seek")

                #amount in one chunk
                chunkval = anim_chunk_len_list[i]
                #print(str(chunkval), "is val")


                
                #now for as many parts as there are collect them
                for i in range(int(chunkval)):
                    temp2.seek(chunkseek + (((i+1)*32)-20))
                    hti = temp2.read(4)
                    oloc = hex_to_int(hti)
                    old_loc.append(oloc)

                #make all old locations into the new ones
                for i in range(int(len(old_loc))):
                    nloc = old_loc[i]
                    nloc = nloc + to_add
                    new_loc.append(nloc)
                    
                #now for as many parts as there are, replace them
                for i in range(int(chunkval)):
                    temp2.seek(chunkseek + (((i+1)*32)-20))
                    ith = new_loc[i]
                    to_write = int_to_hex(ith)
                    temp2.write(to_write)

                #clear the lists for other anim chunks
                old_loc = []
                new_loc = []


            #for actually adding the 00s to each part in the smaller sections
                
            for i in range(int(len(anim_chunk_len_other_list))):
                old_loc = []
                new_loc = []
                
                #seek to the chunk position
                chunkseek = temp2.seek(anim_chunk_loc_other_list[i])
                #print(str(chunkseek), "is other seek")

                #amount in one chunk
                chunkval = anim_chunk_len_other_list[i]
                #print(str(chunkval), "is other val")
                
                #now for as many parts as there are collect them
                for i in range(int(chunkval)):
                    temp2.seek(chunkseek + (((i+1)*16)-4))
                    hti = temp2.read(4)
                    oloc = hex_to_int(hti)
                    old_loc.append(oloc)
    
                #make all old locations into the new ones
                for i in range(int(len(old_loc))):
                    nloc = old_loc[i]
                    nloc = nloc + to_add
                    new_loc.append(nloc)
                    
                    
                #now for as many parts as there are, replace them
                for i in range(int(chunkval)):
                    temp2.seek(chunkseek + (((i+1)*16)-4))
                    ith = new_loc[i]
                    to_write = int_to_hex(ith)
                    temp2.write(to_write)

                
                #clear the lists for other anim chunks
                old_loc = []
                new_loc = []



            anim_chunk_len_list = []
            anim_chunk_len_other_list = []
            anim_chunk_loc_list = []
            anim_chunk_loc_other_list = []


    #now to do the same as above but on the other anims

    anim_other_part_1 = []
    anim_other_part_2 = []
    anim_other_ids = []

    for i in range(int(len(g_anim_other))):
        temp2seek = temp2.seek(g_anim_other[i])
        temp2.seek(0)
        temp2.seek(g_anim_other[i])
        hti = temp2.read(4)
        ids = hex_to_int(hti)
        anim_other_ids.append(ids)
        
        temp2.seek(0)
        temp2.seek(g_anim_other[i]+4)
        hti = temp2.read(4)
        anim_p1 = hex_to_int(hti)
        anim_other_part_1.append(anim_p1)


        temp2.seek(0)
        temp2.seek(g_anim_other[i]+12)
        hti = temp2.read(4)
        anim_p2 = hex_to_int(hti)
        anim_other_part_2.append(anim_p2)

    #print(anim_other_part_1, anim_other_part_2)
    #print(anim_other_ids)

    old_locs_1 = []
    new_locs_1 = []
    old_locs_2 = []
    new_locs_2 = []

    for i in range(int(len(g_anim_other))):
        temp2.seek(0)
        temp2.seek(g_anim_other[i]+4)
        hti = temp2.read(4)
        ol1 = hex_to_int(hti)
        old_locs_1.append(ol1)

        temp2.seek(0)
        temp2.seek(g_anim_other[i]+12)
        hti = temp2.read(4)
        ol2 = hex_to_int(hti)
        old_locs_2.append(ol2)

    for i in range(int(len(old_locs_1))):
        to_new = old_locs_1[i]
        to_new = to_new + to_add
        new_locs_1.append(to_new)

        to_new = old_locs_2[i]
        to_new = to_new + to_add
        new_locs_2.append(to_new)

    for i in range(int(len(g_anim_other))):
        temp2.seek(0)
        temp2.seek(g_anim_other[i]+4)
        ith = new_locs_1[i]
        to_write = int_to_hex(ith)
        temp2.write(to_write)

        temp2.seek(0)
        temp2.seek(g_anim_other[i]+12)
        ith = new_locs_2[i]
        to_write = int_to_hex(ith)
        temp2.write(to_write)




    #-3.5. connect each anim to an axis name for easier lgbt'ing

    #basically copy and paste from axis_e lmao
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
        #print(f.seek((f_amg_loc + (i*32) + f_amg_len)))
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
    #print(f_new_names)


    g_axis_names = []
    g_axis_pos = []
    g_axis_dat = []
    g_new_names = []

    ##gathering axis amounts
    g.seek(0)
    g.seek(16)
    hti = g.read(4)
    g_name_amnt = hex_to_int(hti)
    g_amnt = g_name_amnt
    g_name_amnt = (g_name_amnt * 16 * 2)
    #print(g_name_amnt, g_amnt)

    ##first amg location
    g.seek(0)
    g.seek(48)
    hti = g.read(4)
    g_amg_loc = hex_to_int(hti)
    #print(g_amg_loc)

    ##first amg length
    g.seek(0)
    g.seek(g_amg_loc + 28)
    hti = g.read(4)
    g_amg_len = hex_to_int(hti)
    #print(g_amg_len)
    

    ##gathering names
    for i in range(((g_amnt))):
        g.seek(0)
        g.seek((g_amg_loc + (i*32) +g_amg_len))
        g_axis_names.append(g.read(32))


    ##gathering axis locs + data
    for i in range(((g_amnt))):
        g.seek(0)
        g.seek(g_amg_loc + (32*(i+1)) + (48*i))
        g_axis_pos.append(g.tell())
        g_axis_dat.append(g.read(48))
    #print(g_axis_pos)

    ##adding names to a list
    for i in range(int(len(g_axis_names))):
        new_value = g_axis_names[i]
        new_value = new_value.replace(b"\x00", b"\x2e")
        new_value = str(bytes(new_value))
        new_value = new_value.replace(".", "")
        new_value = new_value.replace("b'", "")
        new_value = new_value.replace("'", "")
        new_value = new_value.replace("_", "")
        new_value = new_value.replace("L00", "")
        new_value = new_value[3:]
        new_value = new_value.replace("X", "")
        g_new_names.append(new_value)
    #print(g_new_names)

        
    #-4. Grab all new locations of Animations (and model parts) and place them in

    #gets the lengths of each temp files, subtract and find how many 00s are needed
    temp1.seek(0)
    temp1_len = temp1.seek(0,2)
    
    temp2.seek(0)
    temp2_len = temp2.seek(0,2)
    
    temp2.seek(0)
    temp2_all = temp2.read()

    temp_zero_mix = math.ceil(temp1_len /  65536)
    temp_zero_mix *= 65536
    #print(temp_zero_mix)
    to_zero_add = temp_zero_mix - temp1_len
    #print(to_zero_add)

    for i in range(to_zero_add):
        temp1.seek(0,2)
        temp1.write(b"\x00")

    temp2_loc = temp1.seek(0,2)
    temp1.seek(0)
    temp1.seek(0,2)
    temp1.write(temp2_all)

    temp_all_len = temp1_len + temp2_len
    temp_all_len_extra = (math.ceil(temp_all_len/65536)) * 65536
    temp_all_to_add = temp_all_len_extra - temp_all_len
    #print(temp_all_len,temp_all_len_extra,temp_all_to_add)
    #print(temp_all_len_extra - (math.ceil(temp2_len/65536)*65536))

    

    #-5. Ask for which axis' need replaced

    #ask for what names you want, and remembers the position
    text_file = open("LGBT ANIM LOCATIONS.txt", "w+")

    gposes = []
    fposes = []
    if_merge = []
    print("")
    counter = 0
    cancel = False
    while cancel != True:
        counter +=1
        print(g_new_names)
        print("Please select the axis from the add-on model:")
        g_choice = input("")
        g_choice = g_choice.upper()

        while g_choice not in g_new_names:
            print("Not a valid axis, try again.")
            g_choice = input("")
            g_choice = g_choice.upper()

        g_cho_pos = int(g_new_names.index(g_choice))
        gposes.append(g_cho_pos)
        vvv = g_choice
        vvv = vvv.replace("0x", "")

        print(f_new_names)
        print("Choose an axis from the base model:")
        f_choice = input("")
        f_choice = f_choice.upper()


        while f_choice not in f_new_names:
            print("Not a valid axis, try again.")
            f_choice = input("")
            f_choice = f_choice.upper()

        f_cho_pos = int(f_new_names.index(f_choice))
        fposes.append(f_cho_pos)
        uuu = f_choice
        uuu = uuu.replace("0x", "")

        print("Does this axis merge? (y/n)")
        merge_choice = input("")
        merge_choice = merge_choice[0:1]
        merge_choice = merge_choice.lower()

        if merge_choice == "y":
            if_merge.append("y")
        if merge_choice == "":
            if_merge.append("y")
        if merge_choice == "n":
            if_merge.append("n")
        


        
        print("Continue? (y/n)")
        cho = input("")
        cho = cho.lower()
        cho = cho[0:1]
        if cho == "y":
            cancel = False
        if cho == "n":
            cancel = True
        #print(if_merge, "if_merge")

    #print(fposes)
    #print(g_locs,f_locs)


    #-6. Grab all animation location blocks (old and new) that are needing replaced and put them at the end 
    anim_3_locs = []
    f_amnts = []
    g_amnts = []
    for i in range(int(len(gposes))):
        index_locate_g = gposes[i]
        index_locate_f = fposes[i]
        to_go_to_g = g_locs[index_locate_g] + to_add
        to_go_to_f = f_locs[index_locate_f]
        knowing_merge = if_merge[i]
        
        
        #g anims
        temp1.seek(0)
        temp1seek_g = temp1.seek(to_go_to_g)
        temp1.seek(0)
        temp1.seek(to_go_to_g + 28)
        hti = temp1.read(4)
        chunk_amnt_g = hex_to_int(hti)
        g_amnts.append(chunk_amnt_g)

        if knowing_merge == "y":
            #f anims
            temp1.seek(0)
            temp1seek_f = temp1.seek(to_go_to_f)
            temp1.seek(0)
            temp1.seek(to_go_to_f+28)
            hti = temp1.read(4)
            chunk_amnt_f = hex_to_int(hti)
            f_amnts.append(chunk_amnt_f)
        if knowing_merge == "n":
            f_amnts.append(0)

        #print(chunk_amnt_g, "chunk amt g")
        
        for i in range(chunk_amnt_g):
            temp1.seek(0)
            temp1.seek(temp1seek_g)
            had_to_grab_g = temp1.read(32 + (chunk_amnt_g*32))


        if knowing_merge == "y":
            for i in range(chunk_amnt_f):
                temp1.seek(0)
                temp1.seek(temp1seek_f + 32)
                had_to_grab_f = temp1.read((chunk_amnt_f*32))

        anim_3 = temp3.seek(0,2)
        anim_3_locs.append(anim_3)
        temp3.write(had_to_grab_g)

        ####SEARCH FOR ANY EXTRA ANIM LOCS
        temp3.seek(0)
        end = temp3.seek(0,2)
        temp3.seek(end-16)
        hti = temp3.read(4)
        other_old = hex_to_int(hti)
        if other_old != 0:
            other_old += (to_add)
            other_old = int(other_old)
            ith = other_old
            other_new = int_to_hex(ith)
            temp3.seek(0)
            end = temp3.seek(0,2)
            temp3.seek(end-16)
            temp3.write(other_new)

        temp3.seek(0)
        temp3.seek(0,2)
            
        if knowing_merge == "y":
            temp3.write(had_to_grab_f)
        
        #writes data to text file for people who want to further use
        
    #print(anim_3_locs)

    #Edits the new anims
    for i in range(int(len(anim_3_locs))):
        temp3.seek(0)
        current_anim = temp3.seek(anim_3_locs[i])
        current_amnt = g_amnts[i]
            
        for i in range(current_amnt):
            temp3.seek(0)
            temp3.seek(current_anim + 32 + (32*(i+1)) - 24)
            hti = temp3.read(4)
            old = hex_to_int(hti)
            #print(to_add, "to_add")
            ith = old + to_add
            new = int_to_hex(ith)
            temp3.seek(0)
            temp3.seek(current_anim + 32 + (32*(i+1)) - 24)
            temp3.write(new)

            

    
        
        
   
            
    #Edits the amounts
    for i in range(int(len(anim_3_locs))):
        temp3.seek(0)
        current_anim = temp3.seek(anim_3_locs[i])
        #print(current_anim, "current_anim")
        current_amnt_f = f_amnts[i]
        #print(current_amnt_f, "current_amnt_f")
        current_amnt_g = g_amnts[i]
        #print(current_amnt_g, "current_amnt_g")
        for i in range(current_amnt):
            temp3.seek(0)
            temp3.seek(current_anim + 28)
            hti = temp3.read(4)
            old = hex_to_int(hti)
            ith = current_amnt_g + current_amnt_f
            #print(ith, "ith")
            new = int_to_hex(ith)
            temp3.seek(0)
            temp3.seek(current_anim + 28)
            temp3.write(new)

    #grabs all of temp3 and pastes it in temp1
    temp3.seek(0)
    len_of_3 = temp3.seek(0,2)
    temp3.seek(0)
    all_of_3 = temp3.read()
    temp1.seek(0,2)
    temp1.write(all_of_3)
    
    #-7. Grab new locations
    final_new_len = temp1.seek(0,2)
    #print(final_new_len)
    final_new_locs = []
    for i in range(int(len(anim_3_locs))):
        index_locate_g = gposes[i]
        index_locate_f = fposes[i]
        
        new_loc = (final_new_len - (len_of_3 - anim_3_locs[i]))
        #print(new_loc)
        final_new_locs.append(new_loc)
        text_file.write("Base Anim Location " + f_new_names[index_locate_f] + " = " + str((hex(to_go_to_f))).replace("0x", "") + "\n"
                    + "Addon Anim Locations " + g_new_names[index_locate_g] + " = " + str((hex(to_go_to_g)).replace("0x", "")) + "\n" + 
                    "New Anim Locations " + g_new_names[index_locate_g] + " = " + str(hex(final_new_locs[i]).replace("0x", "")) + "\n" +
                        "--------------------------------------------------" + "\n")
    final_new_locs.reverse()
    
    
    #print(final_new_locs)

    #edit top files
    for i in range(int(len(final_new_locs))):
        ppp = final_new_locs[i]+16
        ith = ppp
        ppp = int_to_hex(ith)
        temp1.seek(final_new_locs[i]+8)
        temp1.write(ppp)

    #-8. Place new locations
    final_new_locs.reverse()
    for i in range(int(len(final_new_locs))):
        temp1.seek(0)
        
        go_to = fposes[i]
        
        temp1.seek((f_axis_pos[go_to]-first_amg)+52)
        
        to_paste_in = int_to_hex(final_new_locs[i])
        
        temp1.write(to_paste_in)
        

    #Correct AMG Length
    temp1.seek(0)
    ith = temp1.seek(0,2)
    new_amg_length = int_to_hex(ith)
    temp1.seek(0)
    temp1.seek(28)
    temp1.write(new_amg_length)
    

    #-9. Put all new model part locations as the user wants
    print("Gathering Model Part Locations...")
    
    #seek to and cut and paste in temp5
    axis_to_mp_seek = (48 + (f_name_amnt_x*80))
    temp1.seek(0)
    temp1.seek(axis_to_mp_seek)
    for_6 = temp1.read()
    temp6.write(for_6)

    #read all model part locations on model F
    f_mp_locs = []
    f_mp_texs = []
    f_mp_shad = []
    f_mp_counter = 0

    temp6.seek(0)
    hti = temp6.read(4)
    f_mp_counter = hex_to_int(hti)
    temp6.seek(0)

    for i in range(f_mp_counter):
        mp_to_go =(i*4)
        temp6.seek(mp_to_go+16)
        hti = temp6.read(4)
        mp = hex_to_int(hti)
        f_mp_locs.append(mp)

    #gets texture and shader values of each model part
    for i in f_mp_locs:
        temp6.seek(0)
        temp6.seek(i+8)
        hti = temp6.read(4)
        f_tex = hex_to_int(hti)
        f_mp_texs.append(f_tex)

        temp6.seek(0)
        temp6.seek(i+12)
        hti = temp6.read(4)
        f_sha = hex_to_int(hti)
        f_mp_shad.append(f_sha)

    


    g_mp_seek = (temp2_loc - axis_to_mp_seek)
    temp6.seek(g_mp_seek)
    #print(temp6.tell())
    #read all model part locations on model G
    g_mp_locs = []
    g_mp_shad = []
    g_mp_texs = []
    g_mp_counter = 0

    g_axis_to_mp_seek = 48+(g_name_amnt_x*80)
    temp6.seek(g_axis_to_mp_seek+g_mp_seek)
    #print(temp6.tell())
    hti = temp6.read(4)
    g_mp_counter = hex_to_int(hti)
    
    
    for i in range(g_mp_counter):
        mp_to_go =(g_axis_to_mp_seek+g_mp_seek+(i*4))
        temp6.seek(mp_to_go+16)
        hti = temp6.read(4)
        mp = hex_to_int(hti)
        mp += (g_axis_to_mp_seek+g_mp_seek)
        g_mp_locs.append(mp)
    #print(g_mp_locs)


    #gets texture and shader values of each model part
    for i in g_mp_locs:
        temp6.seek(0)
        temp6.seek(i+8)
        hti = temp6.read(4)
        g_tex = hex_to_int(hti)
        g_mp_texs.append(g_tex)

        temp6.seek(0)
        temp6.seek(i+12)
        hti = temp6.read(4)
        g_sha = hex_to_int(hti)
        g_mp_shad.append(g_sha)


    #removing model parts section
    cont_val = True
    while cont_val == True:
        choice = input("Do you want to remove model parts (y/n)")
        choice = choice.lower()
        choice = choice[0:1]
        if choice == "y":
            cont_val = True
            print("Base Model Parts:")
            for i in range(int(len(f_mp_shad))):        
                print("MP", f_mp_locs[i], "TEX", f_mp_texs[i], "SHA", f_mp_shad[i], "("+str(i)+")")
            print("")
            print("What model parts do you want to remove?")
            print("Pick the model part in order of appearance (1-" + str(int(len(f_mp_locs)))+")")
            mp_input = int(input(""))
            while mp_input > int(len(f_mp_locs)):
                print("Not within range, try again")
                mp_input = int(input(""))

            mp_input -=1
            #remove the model parts
            temp6.seek(0)
            temp6.seek(16+(mp_input*4))
            for i in range(4):
                temp6.write(b"\x00")
            f_rest_amnt = (int(len(f_mp_locs)) - mp_input)*4
            mp_rest = temp6.read(f_rest_amnt)
            temp6.seek(16 + (mp_input*4))
            temp6.write(mp_rest)
            temp6.seek(0)
            hti = temp6.read(4)
            xxx = hex_to_int(hti)
            ith = xxx-1
            mp_counter = int_to_hex(ith)
            temp6.seek(0)
            temp6.write(mp_counter)
            f_mp_locs.remove(f_mp_locs[mp_input])
            f_mp_texs.remove(f_mp_texs[mp_input])
            f_mp_shad.remove(f_mp_shad[mp_input])            

        if choice == "n":
            cont_val = False

    #inserting model parts
    cont_val = True
    while cont_val == True:
        choice = input("Do you want to insert model parts (y/n)")
        choice = choice.lower()
        choice = choice[0:1]
        if choice == "y":
            cont_val = True
            print("Addon Model Parts:")
            for i in range(int(len(g_mp_shad))):        
                print("MP", g_mp_locs[i], "TEX", g_mp_texs[i], "SHA", g_mp_shad[i], "("+str(i)+")")
            print("")
            print("What model parts do you want to remove?")
            print("Pick the model part in order of appearance (1-" + str(int(len(g_mp_locs)))+")")
            mp_input = int(input(""))
            while mp_input > int(len(g_mp_locs)):
                print("Not within range, try again")
                mp_input = int(input(""))
            mp_input -=1
            temp6.seek(0)
            hti = temp6.read(4)
            mp_counter = hex_to_int(hti)
            temp6.seek(0)
            temp6.seek(16+(mp_counter*4))
            ith = g_mp_locs[mp_input]
            g_to_write = int_to_hex(ith)
            temp6.write(g_to_write)
            temp6.seek(0)
            hti = temp6.read(4)
            xxx = hex_to_int(hti)
            ith = xxx+1
            xxx = int_to_hex(ith)
            temp6.seek(0)
            temp6.write(xxx)


            
        if choice == "n":
            cont_val = False

    #placing temp6 in the temp1 file for rebuilding
    temp6.seek(0)
    temp6_all = temp6.read()
    temp1.seek(0)
    temp1.seek(axis_to_mp_seek)
    temp1.write(temp6_all)
    

    #-10. Rebuild AMO and add in the old AMGs and grab locations, place, etc
    f.seek(0)
    amo_read = f.read(first_amg)
    temp4.write(amo_read)

    temp1.seek(0)
    temp1_read = temp1.read()
    temp1_size = temp1.seek(0,2)
    temp4.write(temp1_read)

    

    f.seek(0)
    f.seek(first_amg + first_amg_length)
    rest_of_1 = f.read()
    temp4.write(rest_of_1)


    #rewrites locations and stuff for all of the amo parts
    temp4.seek(0)
    temp4.seek(48)
    amg_to_add = temp1_size - first_amg_length
    temp4.seek(0)
    temp4.seek(24)
    hti = temp4.read(4)
    amg_amnt = hex_to_int(hti)
    amg_amnt-=1

    old_amgs = []
    new_amgs = []
    for i in range(amg_amnt):
        temp4.seek(0)
        temp4.seek(52 + (i*4))
        hti = temp4.read(4)
        xxx = hex_to_int(hti)
        old_amgs.append(hex(xxx))
        ith = xxx + amg_to_add
        xxx = int_to_hex(ith)
        new_amgs.append((xxx))
        temp4.seek(0)
        temp4.seek(52 + (i*4))
        temp4.write(xxx)

    temp4.seek(0)
    temp4.seek(16)
    hti = temp4.read(4)
    axis_amnt = hex_to_int(hti)
    axis_amnt-=1
    temp4.seek(0)
    temp4.seek(32)
    hti = temp4.read(4)
    axis_line_len = hex_to_int(hti)
    temp4.seek(0)
    temp4.seek(20)
    hti = temp4.read(4)
    ppp = hex_to_int(hti)
    temp4.seek(ppp+4)
    hti = temp4.read(4)
    go_to = hex_to_int(hti)
    

    llll = ((axis_amnt+1)*axis_line_len)
    #print(str(llll), "look at dis")

    old_amgs = []
    for i in range(llll):
        temp4.seek(0)
        temp4.seek(go_to + (i*16) + 4)
        hti = temp4.read(4)
        to_compare = hex_to_int(hti)
        if to_compare > axis_amnt:
            old_amgs.append((temp4.tell()-8))

    
    for i in range(int(len(old_amgs))):
        temp4.seek(0)
        temp4.seek(old_amgs[i]+8)
        hti = temp4.read(4)
        to_upgrade = hex_to_int(hti)
        ith = to_upgrade + amg_to_add
        to_upgrade = int_to_hex(ith)
        temp4.seek(0)
        temp4.seek(old_amgs[i]+8)
        temp4.write(to_upgrade)
        
        
    
    temp4.seek(0)
    ith = temp4.seek(0,2)
    full_file = int_to_hex(ith)
    temp4.seek(0)
    temp4.seek(36)
    temp4.write(full_file)
    temp4.seek(0)
    final = temp4.read(ith)
    new_file.write(final)

    #For adding/removing model parts
    
    


    # deletes temp files
    tn1 = "Files\z1.bin"
    #temp1 = open(tn1, "r+b")
    #temp1.close()
    tn2 = "Files\z2.bin"
    #temp2 = open(tn2, "r+b")
    #temp2.close()
    tn3 = "Files\z3.bin"
    #temp3 = open(tn3, "r+b")
    #temp3.close()
    tn4 = "Files\z4.bin"
    #temp4 = open(tn4, "r+b")
    #temp4.close()
    tn5 = "Files\z5.bin"
    #temp5 = open(tn5, "r+b")
    #temp5.close()
    tn6 = "Files\z6.bin"
    #temp6 = open(tn6, "r+b")
    #temp6.close()
    tn7 = "Files\z7.bin"
    temp7 = open(tn7, "r+b")
    temp7.close()
    tn8 = "Files\z8.bin"
    temp8 = open(tn8, "r+b")
    temp8.close()
    #os.remove(tn1)
    #os.remove(tn2)
    #os.remove(tn3)
    #os.remove(tn4)
    #os.remove(tn5)
    #os.remove(tn6)
    os.remove(tn7)
    os.remove(tn8)

    f.close()
    g.close()
    text_file.close()
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
