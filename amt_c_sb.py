# AMT Creator - amt_c_sb2
# Purpose: To create and edit AMTs for SB2


import struct
import math
import os

def main():
    print("")
    print("Create or Edit AMT?(C/E)")

    mode = input("")
    mode = mode.lower()
    if mode == "c" or mode == "create":
        create_amt()
    elif mode == "e" or mode == "edit":
        edit_amt()


def create_amt():
    print("")
    print("Name your new AMT name?")
    x = input("")
    f = open(x+".amt", "w+b")

    # Copying files needed
    header = open("Files/AMT/header.bin", "r+b")
    header = header.read()
    line = open("Files/AMT/line.bin", "r+b")
    line = line.read()
    rpt = open("Files/AMT/RPT.bin", "r+b")
    rpt = rpt.read()

    a128x128_16 = open("Files/AMT/SB2_128x128.bin", "r+b")          # 16 color
    a256x256_16 = open("Files/AMT/SB2_256x256.bin", "r+b")

    a128x128_256 = open("Files/AMT/SB2_128x128(256).bin", "r+b")        # 256 Color
    a256x256_256 = open("Files/AMT/SB2_256x256(256).bin", "r+b")

    # Making list
    col_16 = [a128x128_16, a256x256_16]

    col_256 = [a128x128_256, a256x256_256]

    tex_list = ["128x128(1)", "256x256(2)"]

    # Setting up temp bins
    tn1 = "Files\z.bin"  # Will hold edited bin
    temp1 = open(tn1, "w+b")
    temp1.close()
    temp1 = open(tn1, "r+b")
    tn2 = "Files\z2.bin"  # Will hold indexes
    temp2 = open(tn2, "w+b")
    temp2.close()
    temp2 = open(tn2, "r+b")
    tn3 = "Files\z3.bin"  # Will hold TEX/Palette data
    temp3 = open(tn3, "w+b")
    temp3.close()
    temp3 = open(tn3, "r+b")

    index_list_size = 0
    header_size = 0

    # Writes header
    temp1.write(header)
    temp1.seek(8)
    temp1.write(b'\x01')
    print("How many textures?")
    tex_amount = int(input(""))
    temp1.seek(16)
    tex_am_value = struct.pack('<L', tex_amount)
    temp1.write(tex_am_value)
    temp1.seek(32)
    tex_am_lines = tex_line_calc(tex_amount)
    for i in range(tex_am_lines):
        temp1.write(line)

    # Writing index offsets
    switch = 0
    header_size = temp1.tell()
    temp1.seek(32)
    index_o = struct.pack('<L', header_size)
    index_o3 = 0
    print("")
    print("writing tex index offsets...")
    index_o2 = index_offset(index_o, index_o3)
    for i in range(tex_amount):
        temp1.write(index_o2)
        index_o3 = index_offset2(index_o3, switch, index_list_size, header_size)
        index_o2 = index_offset(index_o, index_o3)

    # Selecting texture and putting them in temp bins
    choice_list = []
    print("")
    print(tex_list)
    counter = 0
    for i in range(tex_amount):
        if counter >= 3:
            print("")
            print(tex_list)
            counter = 0
        print("")
        print("Pick the texture you want")
        print("(select the texture by typing it's position on the list)")
        choice = int(input(""))
        choice = choice - 1
        print(choice)
        while choice >= int(len(tex_list)):
            # if it is not within range, it asks again
            print("Not within range, try again:")
            choice = int(input(""))
            choice = choice - 1
        choice_list.append(choice)
        # prints the chosen texture
        print(tex_list[choice])
        print(choice_list)
        # sets a variable to be the result of the function
        index_block_copy = index_block_pick(col_16, col_256, choice, temp3)
        # writes that data to file
        temp2.write(index_block_copy)
        counter = counter + 1
        
    # Changing the index number
    switch = 1
    temp2.seek(0)
    index_o = struct.pack('<L', 0)
    index_o3 = 0
    n_index = 0
    print("")
    print("correcting tex index numbers...")
    index_o2 = index_offset(index_o, index_o3)
    for i in range(tex_amount):
        temp2.write(index_o2)
        index_o3 = index_offset2(index_o3, switch, index_list_size, header_size)
        n_index = next_index(n_index)
        temp2.seek(n_index)
        index_o2 = index_offset(index_o, index_o3)

    # Changing the TEX/PAL offsets
    prev_offset = 0
    prev_offset2 = 0
    temp2.seek(0)
    temp2.read()
    index_list_size = temp2.tell()
    temp2.seek(20)
    total = index_list_size + header_size
    total = struct.pack('<L', total)
    temp2.write(total)
    total = index_list_size + header_size
    prev = temp2.read(4)
    prev = prev.hex()

    prev = int(prev, 16)
    prev = struct.pack('<L', prev)
    prev = prev.hex()
    prev = int(prev, 16)
    prev_offset = prev + total

    prev_offset = struct.pack('<L', prev_offset)
    print(temp2.seek((temp2.tell() + 8)))
    temp2.write(prev_offset)

    for i in range(tex_amount-1):
        previous_offset(prev, temp2, prev_offset, total)

    # Assembles and Saves new AMT
    temp1.close()
    temp1 = open(tn1, "r+b")
    temp2.close()
    temp2 = open(tn2, "r+b")
    temp3.close()
    temp3 = open(tn3, "r+b")
    t_copy = temp1.read()
    f.seek(0)
    f.write(t_copy)
    t_copy = temp2.read()
    f.write(t_copy)
    t_copy = temp3.read()
    f.write(t_copy)
    f.write(rpt)
    f.close()
    print("")
    print("Completed!")

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


def edit_amt():
    print("")
    print("Drag and drop SB2 AMT")
    x = input("")
    x = x.replace("\"", "")
    f = open(x, "r+b")

    # Copying files needed
    header = f.read(48)
    f.seek(0)
    line = open("Files/AMT/line.bin", "r+b")
    line = line.read()

    a128x128_16 = open("Files/AMT/SB2_128x128.bin", "r+b")  # 16 color
    a256x256_16 = open("Files/AMT/SB2_256x256.bin", "r+b")

    a128x128_256 = open("Files/AMT/SB2_128x128(256).bin", "r+b")  # 256 Color
    a256x256_256 = open("Files/AMT/SB2_256x256(256).bin", "r+b")

    # Making list
    col_16 = [a128x128_16, a256x256_16]

    col_256 = [a128x128_256, a256x256_256]

    tex_list = ["128x128(1)", "256x256(2)"]

    # Setting up temp bins
    tn1 = "Files\z.bin"  # Will hold edited bin
    temp1 = open(tn1, "w+b")
    temp1.close()
    temp1 = open(tn1, "r+b")
    tn2 = "Files\z2.bin"  # Will hold indexes
    temp2 = open(tn2, "w+b")
    temp2.close()
    temp2 = open(tn2, "r+b")
    tn3 = "Files\z3.bin"  # Will hold TEX/Palette data
    temp3 = open(tn3, "w+b")
    temp3.close()
    temp3 = open(tn3, "r+b")

    index_list_size = 0
    header_size = 0

    # Writes header
    temp1.write(header)
    # Will read the total amount of textures in AMT
    temp1.seek(0)
    f.seek(16)
    tex_amount_orig = f.read(4)
    tex_amount_orig = tex_amount_orig.hex()
    tex_amount_orig = int(tex_amount_orig, 16)
    tex_amount_orig = struct.pack('<L', tex_amount_orig)
    tex_amount_orig = tex_amount_orig.hex()
    tex_amount_orig = int(tex_amount_orig, 16)

    print("How many textures do you wanna add?")
    tex_amount_add = int(input(""))
    tex_amount = tex_amount_add + tex_amount_orig
    temp1.seek(16)
    tex_am_value = struct.pack('<L', tex_amount)
    temp1.write(tex_am_value)
    temp1.seek(32)
    tex_am_lines = tex_line_calc(tex_amount)
    for i in range(tex_am_lines):
        temp1.write(line)

    # Writing index offsets
    switch = 0
    header_size = temp1.tell()
    temp1.seek(32)
    index_o = struct.pack('<L', header_size)
    index_o3 = 0
    print("")
    print("writing tex index offsets...")
    index_o2 = index_offset(index_o, index_o3)
    for i in range(tex_amount):
        temp1.write(index_o2)
        index_o3 = index_offset2(index_o3, switch, index_list_size, header_size)
        index_o2 = index_offset(index_o, index_o3)

    # Selecting texture and putting them in temp bins
    choice_list = []
    # Copying old index shit
    f.seek(0)
    f.seek(32)
    offset = f.read(4)
    offset = offset.hex()
    offset = int(offset, 16)
    offset = struct.pack('<L', offset)
    offset = offset.hex()
    offset = int(offset, 16)
    f.seek(offset)
    data = tex_amount_orig * 48
    data = f.read(data)
    temp2.write(data)
    # Copying old TEX/PAL shit
    f.seek(offset + 4+16)
    offset = f.read(4)
    offset = offset.hex()
    offset = int(offset, 16)
    offset = struct.pack('<L', offset)
    offset = offset.hex()
    offset = int(offset, 16)
    f.seek(offset-12)

    total = f.read(4)
    total = total.hex()
    total = int(total, 16)
    total = struct.pack('<L', total)
    total = total.hex()
    total = int(total, 16)

    total2 = f.read(4)
    total2 = total2.hex()
    total2 = int(total2, 16)
    total2 = struct.pack('<L', total2)
    total2 = total2.hex()
    total2 = int(total2, 16)
    total = total + total2 - offset
    f.seek(offset)
    data = f.read(total)
    temp3.write(data)
    # Copying RPT data
    rpt = f.read()
    f.seek(0)

    print("DEBUG: Total - " + str(total))
    input("WAITING")

    print("")
    print(tex_list)
    counter = 0
    for i in range(tex_amount_add):
        if counter >= 3:
            print("")
            print(tex_list)
            counter = 0
        print("")
        print("Pick the texture you want")
        print("(select the texture by typing it's position on the list)")
        choice = int(input(""))
        choice = choice - 1
        print(choice)
        while choice >= int(len(tex_list)):
            # if it is not within range, it asks again
            print("Not within range, try again:")
            choice = int(input(""))
            choice = choice - 1
        choice_list.append(choice)
        # prints the chosen texture
        print(tex_list[choice])
        print(choice_list)
        # sets a variable to be the result of the function
        index_block_copy = index_block_pick(col_16, col_256, choice, temp3)
        # writes that data to file
        temp2.write(index_block_copy)
        counter = counter + 1

    # Changing the index number
    switch = 1
    temp2.seek(0)
    index_o = struct.pack('<L', 0)
    index_o3 = 0
    n_index = 0
    print("")
    print("correcting tex index numbers...")
    index_o2 = index_offset(index_o, index_o3)
    for i in range(tex_amount):
        temp2.write(index_o2)
        index_o3 = index_offset2(index_o3, switch, index_list_size, header_size)
        n_index = next_index(n_index)
        temp2.seek(n_index)
        index_o2 = index_offset(index_o, index_o3)

    # Changing the TEX/PAL offsets
    prev_offset = 0
    prev_offset2 = 0
    temp2.seek(0)
    temp2.read()
    index_list_size = temp2.tell()
    temp2.seek(20)
    total = index_list_size + header_size
    total = struct.pack('<L', total)
    temp2.write(total)
    total = index_list_size + header_size
    prev = temp2.read(4)
    prev = prev.hex()
    prev = int(prev, 16)
    prev = struct.pack('<L', prev)
    prev = prev.hex()
    prev = int(prev, 16)
    prev_offset = prev + total

    prev_offset = struct.pack('<L', prev_offset)
    print(temp2.seek((temp2.tell() + 8)))
    temp2.write(prev_offset)

    for i in range(tex_amount - 1):
        previous_offset(prev, temp2, prev_offset, total)

    # Assembles and Saves new AMT
    temp1.close()
    temp1 = open(tn1, "r+b")
    temp2.close()
    temp2 = open(tn2, "r+b")
    temp3.close()
    temp3 = open(tn3, "r+b")
    f.close()
    os.remove(x)
    f = open(x, "w+b")
    t_copy = temp1.read()
    f.seek(0)
    f.write(t_copy)
    t_copy = temp2.read()
    f.write(t_copy)
    t_copy = temp3.read()
    f.write(t_copy)
    f.write(rpt)
    f.close()
    print("")
    print("Completed!")

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


def tex_line_calc(tex_amount):
    print("calulating lines required...")

    line_break = 4

    tex_am_lines = math.ceil(tex_amount / line_break)

    return tex_am_lines


def index_offset(index_o,index_o3):
    index_o = index_o.hex()
    index_o = int(index_o, 16)
    index_o = struct.pack('<L', index_o)
    index_o = index_o.hex()
    index_o = int(index_o, 16)+index_o3
    index_o = struct.pack('<L', index_o)
    print(index_o.hex())
    return index_o


def index_offset2(index_o3, switch, index_list_size, header_size):
    if switch == 0:
        index_o3 = index_o3 + 48
    elif switch == 1:
        index_o3 = index_o3 + 1
    elif switch == 1:
        index_o3 = index_o3 + index_list_size + header_size
    return index_o3


def next_index(n_index):
    n_index = n_index + 48
    return n_index


def index_block_pick(col_16, col_256, choice, temp3):
    if choice == 9 or choice == 10:
        index_block = col_16[choice]
        index_block.seek(0)
        index_block_copy = index_block.read(48)
        index_block.seek(48)
        index_data_copy = index_block.read()
        temp3.write(index_data_copy)
    else:
        print("")
        print("16 colors or 256 colors?(1/2)")
        color = input("")
        if color == "16" or color == "1":
            index_block = col_16[choice]
            index_block.seek(0)
            index_block_copy = index_block.read(48)
            index_block.seek(48)
            index_data_copy = index_block.read()
            temp3.write(index_data_copy)
        elif color == "256" or color == "2":
            index_block = col_256[choice]
            index_block.seek(0)
            index_block_copy = index_block.read(48)
            index_block.seek(48)
            index_data_copy = index_block.read()
            temp3.write(index_data_copy)
        else:
            print("Incorrect value. Please choose how many colors next time.")
            print("Error")
            exit()
    print("")
    print("adding texture...")
    return index_block_copy


def previous_offset(prev, temp2, prev_offset, total):

    temp2.seek((temp2.tell()-4))
    total = temp2.read(4)
    total = total.hex()
    total = int(total, 16)
    total = struct.pack('<L', total)
    total = total.hex()
    total = int(total, 16)

    prev = temp2.read(4)
    prev = prev.hex()
    prev = int(prev, 16)
    prev = struct.pack('<L', prev)
    prev = prev.hex()
    prev = int(prev, 16)
    prev_offset = prev + total

    prev_offset = struct.pack('<L', prev_offset)
    temp2.seek((temp2.tell() + 24))
    temp2.write(prev_offset)

    # test
    temp2.seek((temp2.tell() - 4))
    total = temp2.read(4)
    total = total.hex()
    total = int(total, 16)
    total = struct.pack('<L', total)
    total = total.hex()
    total = int(total, 16)

    prev = temp2.read(4)
    prev = prev.hex()

    prev = int(prev, 16)
    prev = struct.pack('<L', prev)
    prev = prev.hex()
    prev = int(prev, 16)
    prev_offset2 = prev + total

    prev_offset2 = struct.pack('<L', prev_offset2)
    print(temp2.seek((temp2.tell() + 8)))
    temp2.write(prev_offset2)

    return prev_offset2


def again():
    yn = input("Would you like to load another? (Y/N)")
    yn = yn.lower()
    if yn == "y" or yn == "yes":
        main()
        again()
    else:
        print("")
        print("AMT creator by: Nexus-sama")
        print("credit to SamuelDBZMA&M for some parts")
        print("Follow me on Twitter @NexusTheModder")
        print("")
        kill = input("press enter to close")


main()
again()

exit()
