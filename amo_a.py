#AMO Addition - amo_a
#Purpose: To add an extra line to an AMO for more AMGs
#unnamed_99.bin
#note - sometimes it doesn't correct a value, find error


print("Please only insert the AMO of a character")

import struct
import math

def main():
    ####Part 1 - gathering data, values, and splitting
    
    #lists for later stuff
    amg_offsets = []
    ax_li_offsets = []
    amo_offsets = []
    
    print("AMO Addition, Insert AMO file:")
    x = input("")
    f = open(x, "r+b")
    chunk = f.read(16)

    #opens files needed
    temp1 = open("Files/temp1.bin", "w+b")
    temp2 = open("Files/temp2.bin", "w+b")
    temp3 = open("Files/temp3.bin", "w+b")
    temp4 = open("Files/temp4.bin", "w+b")
    temp5 = open("Files/temp5.bin", "w+b")
    temp6 = open("Files/temp6.bin", "w+b")
    temp7 = open("Files/temp7.bin", "w+b")
    temp8 = open("Files/temp8.bin", "w+b")
    lines = open("Files/lines.bin", "r+b")


    #ask how many lines are to be added
    #open the files, split them, put them together, close the files

    line_am = int(input("How many lines are to be added? "))

    
    f.seek(0)
    f.seek(16)
    am_axis = f.read(1)#how many axis there are for later in calcs
    f.seek(0)
    f.seek(32)
    len_ax_lines = f.read(1)
    f.seek(0)
    f.seek(24)
    am_amg = f.read(1)
    

    
    am_axis = int(am_axis.hex(), 16)#how many axis there are
    len_ax_lines = int(len_ax_lines.hex(), 16)#how many axis lines
    am_amg = int(am_amg.hex(), 16)#amount of amgs
    
    #print(am_axis, len_ax_lines, am_amg)

    #length of part that includes AMO + amgs
    amo_amg = int(((math.ceil(am_amg/4))*16)+48)
    #print(amo_amg)

    #length of the stuff after amg numbers but before axis lines
    amo_other_len = ((am_axis * 16)*2)
    #axis lines length value

    #part where you split the files
    f.seek(0)
    #copies the top part of the amo and puts into temp1
    main_copy = f.read(amo_amg)
    temp1.write(main_copy)
    f.seek(0)
    #copies the first part after the amo_amg but before the axis lines
    #to temp2
    f.seek(amo_amg)
    rest_copy = f.read(amo_other_len)
    temp2.write(rest_copy)
    #copies the axis lines to the temp3
    f.seek(0)
    f.seek(int(amo_amg + amo_other_len))
    ax_li_len = int(am_axis * len_ax_lines * 16)
    rest2_copy = f.read(ax_li_len)
    temp3.write(rest2_copy)
    #copies rest of data to temp4
    #print((am_axis*len_ax_lines) + ax_li_len + amo_amg)
    f.seek(((amo_amg + (amo_other_len) + ax_li_len)))
    rest3_copy = f.read()
    temp4.write(rest3_copy)
    

    #copies the line file to paste onto temp1
    line_copy = lines.read()

    #paste the lines file into temp1 for as many times as requested
    for i in range(line_am):
        temp1.write(line_copy)

    ####Part 2 editing the header + amgs

    #editing the temp1 (amo_amg)
    #grabbing the length and adding 10
    temp1.seek(0)
    temp1.seek(36)
    len_offset = temp1.read(3)
    len_offset = int(len_offset.hex(), 16)
    len_offset = struct.pack("<I", len_offset)
    len_offset = int(len_offset.hex(), 16)
    len_offset += (4096 * line_am)
    len_offset = struct.pack("<I", len_offset)
    #print((len_offset))
    temp1.seek(0)
    temp1.seek(35)
    temp1.write(len_offset)
    temp1.seek(0)

    #edits the small offset that points to a part of the amo
    temp1.seek(0)
    temp1.seek(20)
    xyz_off = temp1.read(3)
    xyz_off = int(xyz_off.hex(), 16)
    xyz_off = struct.pack("<I", xyz_off)
    xyz_off = int(xyz_off.hex(), 16)
    xyz_off += (4096 * line_am)
    xyz_off = struct.pack("<I", xyz_off)
    #print((len_offset))
    temp1.seek(0)
    temp1.seek(19)
    temp1.write(xyz_off)
    temp1.seek(0)

    chunk1 = temp1.read(16)


    #automating amg editing - gets all the offsets that need editing
    temp1.seek(48)
    while chunk1 != b"":
        if chunk1[1] != 00:
            amg_offsets.append(((temp1.tell())))
            #print(((temp1.tell()-16)))
        chunk1 = temp1.read(16)
   #print(amg_offsets)
    amg_offsets = amg_offsets[:-1]
    #print(amg_offsets)

    #reads and writes each offset
    for i in amg_offsets:
        #goes to the first value, reads, then writes
        temp1.seek(0)
        temp1.seek(i)
        value_to_change_1 = temp1.read(3)
        #print(value_to_change_1)
        if value_to_change_1 == b"\x00\x00\x00":
            counter+=1
        else:
            value_to_change_1 = int(value_to_change_1.hex(), 16)
            value_to_change_1 = struct.pack("<I", value_to_change_1)
            value_to_change_1 = int(value_to_change_1.hex(), 16)
            value_to_change_1 += (4096 * line_am)
            value_to_change_1 = struct.pack("<I", value_to_change_1)
        #again but for the next value on the line
        temp1.seek(0)
        temp1.seek(i+4)
        value_to_change_2 = temp1.read(3)
        #print(value_to_change_2)
        if value_to_change_2 == b"\x00\x00\x00":
            counter+=1
        else:
            value_to_change_2 = int(value_to_change_2.hex(), 16)
            value_to_change_2 = struct.pack("<I", value_to_change_2)
            value_to_change_2 = int(value_to_change_2.hex(), 16)
            value_to_change_2 += (4096 * line_am)
            value_to_change_2 = struct.pack("<I", value_to_change_2)
        #repeat x2
        temp1.seek(0)
        temp1.seek(i+8)
        value_to_change_3 = temp1.read(3)
        #print(value_to_change_3)
        if value_to_change_3 == b"\x00\x00\x00":
            counter+=1
        else:
            value_to_change_3 = int(value_to_change_3.hex(), 16)
            value_to_change_3 = struct.pack("<I", value_to_change_3)
            value_to_change_3 = int(value_to_change_3.hex(), 16)
            value_to_change_3 += (4096 * line_am)
            value_to_change_3 = struct.pack("<I", value_to_change_3)
        #repeat x3
        temp1.seek(0)
        temp1.seek(i+12)
        value_to_change_4 = temp1.read(3)
        #print(value_to_change_4)
        if value_to_change_4 == b"\x00\x00\x00":
            counter+=1
        else:
            value_to_change_4 = int(value_to_change_4.hex(), 16)
            value_to_change_4 = struct.pack("<I", value_to_change_4)
            value_to_change_4 = int(value_to_change_4.hex(), 16)
            value_to_change_4 += (4096 * line_am)
            value_to_change_4 = struct.pack("<I", value_to_change_4)

        #writes all the values down, even adding extra 10s elsewhere
        temp1.seek(0)
        temp1.seek(i-1)
        temp1.write(value_to_change_1)
        temp1.seek(i+3)
        temp1.write(value_to_change_2)
        temp1.seek(i+7)
        temp1.write(value_to_change_3)
        temp1.seek(i+11)
        temp1.write(value_to_change_4)


    ####Part 3 - editing whatever the hell is inbetween header and axis lines
    temp2.seek(0)
    chunk2 = temp2.read(16)
    oth_off_1 = []
    
    while chunk2 != b"":
        if chunk2[0] != 0xFF:
            oth_off_1.append(((temp2.tell()-16)))
            #print(hex(temp2.tell()-16))
        chunk2 = temp2.read(16)
    #print(oth_off_1)


    for i in oth_off_1:
        #goes to the first value, reads, then writes
        #does everything except the first 4 values
        temp2.seek(0)
        temp2.seek(i+4)
        value_to_change_2 = temp2.read(3)
        #print(value_to_change_2)
        if value_to_change_2 == b"\x00\x00\x00":
            counter+=1
        else:
            value_to_change_2 = int(value_to_change_2.hex(), 16)
            value_to_change_2 = struct.pack("<I", value_to_change_2)
            value_to_change_2 = int(value_to_change_2.hex(), 16)
            value_to_change_2 += (4096 * line_am)
            value_to_change_2 = struct.pack("<I", value_to_change_2)
        #repeat x2
        temp2.seek(0)
        temp2.seek(i+8)
        value_to_change_3 = temp2.read(3)
        #print(value_to_change_3)
        if value_to_change_3 == b"\x00\x00\x00":
            counter+=1
        else:
            value_to_change_3 = int(value_to_change_3.hex(), 16)
            value_to_change_3 = struct.pack("<I", value_to_change_3)
            value_to_change_3 = int(value_to_change_3.hex(), 16)
            value_to_change_3 += (4096 * line_am)
            value_to_change_3 = struct.pack("<I", value_to_change_3)
        #repeat x3
        temp2.seek(0)
        temp2.seek(i+12)
        value_to_change_4 = temp2.read(3)
        #print(value_to_change_4)
        if value_to_change_4 == b"\x00\x00\x00":
            counter+=1
        else:
            value_to_change_4 = int(value_to_change_4.hex(), 16)
            value_to_change_4 = struct.pack("<I", value_to_change_4)
            value_to_change_4 = int(value_to_change_4.hex(), 16)
            value_to_change_4 += (4096 * line_am)
            value_to_change_4 = struct.pack("<I", value_to_change_4)

        #writes all the values down, even adding extra 10s elsewhere
        temp2.seek(0)
        temp2.seek(i+3)
        temp2.write(value_to_change_2)
        temp2.seek(i+7)
        temp2.write(value_to_change_3)
        temp2.seek(i+11)
        temp2.write(value_to_change_4)


    oth_off_1 = oth_off_1[1::2]
    for i in oth_off_1:
        #goes to the first value, reads, then writes
        #does the first 4 values
        temp2.seek(0)
        temp2.seek(i)
        value_to_change_1 = temp2.read(3)
        #print(value_to_change_1)
        if value_to_change_1 == b"\x00\x00\x00":
            counter+=1
        else:
            value_to_change_1 = int(value_to_change_1.hex(), 16)
            value_to_change_1 = struct.pack("<I", value_to_change_1)
            value_to_change_1 = int(value_to_change_1.hex(), 16)
            value_to_change_1 += (4096 * line_am)
            value_to_change_1 = struct.pack("<I", value_to_change_1)
            #print(value_to_change_1)


        #writes all the values down, even adding extra 10s elsewhere
        temp2.seek(0)
        temp2.seek(i-1)
        temp2.write(value_to_change_1)


    ####Part 4 - axis lines
    for i in range((am_axis*len_ax_lines)):
        #goes to the first value, reads, then writes
        #does everything except the first 4 values
        temp3.seek(0)
        temp3.seek((i*16)+8)
        value_to_change_1 = temp3.read(3)
        #print(value_to_change_1)
        if value_to_change_1 == b"\x00\x00\x00":
            counter+=1
        else:
            value_to_change_1 = int(value_to_change_1.hex(), 16)
            value_to_change_1 = struct.pack("<I", value_to_change_1)
            value_to_change_1 = int(value_to_change_1.hex(), 16)
            value_to_change_1 += (4096 * line_am)
            value_to_change_1 = struct.pack("<I", value_to_change_1)
        temp3.seek(0)
        temp3.seek((i*16)+7)
        temp3.write(value_to_change_1)


    f.close()
    temp1.close()
    temp2.close()
    temp3.close()
    temp4.close()
    temp5.close()
    temp6.close()
    temp7.close()
    temp8.close()
    lines.close()


    temp1 = open("Files/temp1.bin", "r+b")
    temp2 = open("Files/temp2.bin", "r+b")
    temp3 = open("Files/temp3.bin", "r+b")
    temp4 = open("Files/temp4.bin", "r+b")
    temp5 = open("Files/temp5.bin", "r+b")
    temp6 = open("Files/temp6.bin", "r+b")
    temp7 = open("Files/temp7.bin", "r+b")
    temp8 = open("Files/temp8.bin", "r+b")
    lines = open("Files/lines.bin", "r+b")



    f.close()
    f = open(x, "w+b")
    f.close()
    f = open(x, "r+b")

    t1 = temp1.read()
    f.write(t1)
    
    t2 = temp2.read()
    f.write(t2)
    
    t3 = temp3.read()
    f.write(t3)
    
    t4 = temp4.read()
    f.write(t4)

    

    f.close()
    temp1.close()
    temp2.close()
    temp3.close()
    temp4.close()
    temp5.close()
    temp6.close()
    temp7.close()
    temp8.close()
    lines.close()

    print("")
    print("Complete")

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
