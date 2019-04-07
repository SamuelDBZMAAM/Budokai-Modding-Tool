# AMT SB2 Converter
# Purpose of this sub-program - To convert SB2 AMTs to be read in GGS easily


import struct
import math
import os
import subprocess


print("")
print("Shin Budokai 2 AMT converter by: Nexus-sama")
print("credit to SamuelDBZMA&M for some parts")
print("Follow me on Twitter @NexusTheModder")
print("")

print("Instructions:")
print("- Drag and drop you SB2 AMT here")
print("- Replace/edit your textures in the GGS window")
print("that pops up with \"Interlace\" set to \"PSP\"")
print("- CLOSE GGS FIRST BEFORE CLOSING THE TOOL")
print("")

def main():
    # Loading tools
    print("Loading tools...")
    folder = "None"
    ggs = "None"
    tool = 1
    folder = tool_check(ggs, folder, tool)
    tool = 2
    ggs = tool_check(ggs, folder, tool)
    print("")

    # Loading your bin and copying data
    print("Drag and drop SB2 AMT here:")
    x = input("")
    x = x.replace("\"", "")
    f = open(x, "r+b")

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

    # Copying files needed
    header = f.read(48)
    f.seek(0)
    line = open("Files/AMT/line.bin", "r+b")
    line = line.read()
    d_heading = open("Files/AMT/double_heading.bin", "r+b")
    d_heading = d_heading.read()
    index_list_size = 0
    header_size = 0

    # -------------------------[CONVERTING SB2 TO GGS FORMAT]-------------------------

    # Writes header
    temp1.write(header)

    # Will read the total amount of textures in AMT
    f.seek(16)
    hti = f.read(4)
    tex_amount = hex_to_int(hti)
    temp1.seek(16)
    ith = tex_amount
    tex_am_value = int_to_hex(ith)
    temp1.write(tex_am_value)

    # amount of blanks in header
    tex_amount_0 = 0
    offset2 = 32
    for i in range(tex_amount):
        f.seek(offset2)
        hti = f.read(4)
        offset = hex_to_int(hti)
        if offset != 0:
            "Nothing"
        else:
            tex_amount_0 = tex_amount_0 + 1
        offset2 = offset2 + 4

    temp1.seek(32)
    tex_am_lines = tex_line_calc(tex_amount - tex_amount_0)
    for i in range(tex_am_lines):
        temp1.write(line)

    # Writing index offsets
    switch = 0
    header_size = temp1.tell()
    temp1.seek(32)
    ith = header_size
    hti = int_to_hex(ith)
    index_o3 = 0
    ith = hex_to_int(hti) + index_o3
    index_o2 = int_to_hex(ith)
    for i in range(tex_amount - tex_amount_0):
        temp1.write(index_o2)
        index_o3 = index_offset2(index_o3, switch, index_list_size, header_size)
        ith = hex_to_int(hti) + index_o3
        index_o2 = int_to_hex(ith)

    # Copying old index shit
    tex_amount_0 = 0
    offset2 = 32
    for i in range(tex_amount):
        f.seek(offset2)
        hti = f.read(4)
        offset = hex_to_int(hti)
        if offset != 0:
            f.seek(offset)
            data = f.read(48)
            temp2.write(data)
        else:
            tex_amount_0 = tex_amount_0 + 1
        offset2 = offset2 + 4

    # Updates amount of tex in header
    temp1.seek(16)
    ith = tex_amount - tex_amount_0
    t_copy = int_to_hex(ith)
    temp1.write(t_copy)

    # Copying old TEX/PAL shit
    f.seek(32)
    hti = f.read(4)
    offset = hex_to_int(hti)
    f.seek(offset + 20)
    hti = f.read(4)
    offset = hex_to_int(hti)
    f.seek(offset)
    data = f.read()
    temp3.write(data)
    f.seek(0)

    # Changing the TEX/PAL offsets
    prev_offset = 0
    prev_offset2 = 0
    temp2.seek(0)
    temp2.read()
    index_list_size = temp2.tell()
    temp2.seek(20)
    ith = index_list_size + header_size
    total = int_to_hex(ith)
    temp2.write(total)
    total = index_list_size + header_size
    hti = temp2.read(4)
    prev = hex_to_int(hti)
    ith = prev + 32 + total
    prev_offset = int_to_hex(ith)
    temp2.seek((temp2.tell() + 8))
    temp2.write(prev_offset)
    for i in range(tex_amount - 1 - tex_amount_0):
        previous_offset(prev, temp2, prev_offset, total)

    # Assembles new AMT
    temp1.close()
    temp1 = open(tn1, "r+b")
    temp2.close()
    temp2 = open(tn2, "r+b")
    temp3.close()
    temp3 = open(tn3, "r+b")
    temp1.read()
    t_copy = temp2.read()
    temp1.write(t_copy)

    temp1.seek(32)
    hti = temp1.read(4)
    offset = hex_to_int(hti)
    temp3.seek(0)

    for i in range(tex_amount - tex_amount_0):
        temp1.seek(offset+20)
        hti = temp1.read(4)
        offset2 = hex_to_int(hti)
        hti = temp1.read(4)

        tex_data = hex_to_int(hti)
        ith = int(tex_data/16 + 1342177281)
        tex_data2 = int_to_hex(ith)     # 1st double line value
        ith = int(tex_data/16 + 32768)
        tex_data3 = int_to_hex(ith)     # 2nd double line value

        temp1.seek(temp1.tell() + 8)
        hti = temp1.read(4)
        offset3 = hex_to_int(hti)
        hti = temp1.read(4)

        pal_data = hex_to_int(hti)
        ith = int(pal_data/16 + 1342177281)
        pal_data2 = int_to_hex(ith)  # 1st double line value
        ith = int(pal_data/16 + 32768)
        pal_data3 = int_to_hex(ith)  # 2nd double line value

        temp1.seek(offset2)
        temp1.write(d_heading)
        temp1.seek(temp1.tell() - 20)
        temp1.write(tex_data2)
        temp1.write(tex_data3)
        temp1.read()
        t_copy = temp3.read(tex_data)
        temp1.write(t_copy)

        temp1.seek(offset3)
        temp1.write(d_heading)
        temp1.seek(temp1.tell() - 20)
        temp1.write(pal_data2)
        temp1.write(pal_data3)
        temp1.read()
        t_copy = temp3.read(pal_data)
        temp1.write(t_copy)

        offset = offset + 48

    # Changing AA and 2A values
    temp1.seek(32)
    hti = temp1.read(4)
    offset = hex_to_int(hti)
    temp1.seek(offset)
    for i in range(tex_amount - tex_amount_0):
        temp1.seek(temp1.tell() + 25)
        aa = temp1.read(2)
        if aa == b'\xAA\x00':
            temp1.seek(temp1.tell() - 2)
            temp1.write(b'\x80\x00')
        if aa == b'\x2A\x00':
            temp1.seek(temp1.tell() - 2)
            temp1.write(b'\x20\x00')
        if aa == b'\x54\x00':
            temp1.seek(temp1.tell() - 2)
            temp1.write(b'\x40\x00')
        if aa == b'\x0A\x00':
            temp1.seek(temp1.tell() - 2)
            temp1.write(b'\x08\x00')
        if aa == b'\x04\x00':
            temp1.seek(temp1.tell() - 2)
            temp1.write(b'\x02\x00')
        if aa == b'\x15\x00':
            temp1.seek(temp1.tell() - 2)
            temp1.write(b'\x10\x00')
        if aa == b'\x54\x01':
            temp1.seek(temp1.tell() - 2)
            temp1.write(b'\x00\x01')
        temp1.seek(temp1.tell() + 21)

    # Opens the new AMT in GGS
    temp1.close()
    subprocess.call([ggs, folder + "\Files\z.bin"])
    temp1 = open(tn1, "r+b")

    # -------------------------[CONVERTING IT BACK TO SB2]-------------------------
    temp1.seek(0)
    temp2.seek(0)
    temp3.seek(0)

    # Changing AA and 2A values
    temp1.seek(32)
    hti = temp1.read(4)
    offset = hex_to_int(hti)
    temp1.seek(offset)
    for i in range(tex_amount - tex_amount_0):
        temp1.seek(temp1.tell() + 25)
        aa = temp1.read(2)
        if aa == b'\x80\x00':
            temp1.seek(temp1.tell() - 2)
            temp1.write(b'\xAA\x00')
        if aa == b'\x20\x00':
            temp1.seek(temp1.tell() - 2)
            temp1.write(b'\x2A\x00')
        if aa == b'\x40\x00':
            temp1.seek(temp1.tell() - 2)
            temp1.write(b'\x54\x00')
        if aa == b'\x08\x00':
            temp1.seek(temp1.tell() - 2)
            temp1.write(b'\x0A\x00')
        if aa == b'\x02\x00':
            temp1.seek(temp1.tell() - 2)
            temp1.write(b'\x04\x00')
        if aa == b'\x10\x00':
            temp1.seek(temp1.tell() - 2)
            temp1.write(b'\x15\x00')
        if aa == b'\x00\x01':
            temp1.seek(temp1.tell() - 2)
            temp1.write(b'\x54\x01')
        temp1.seek(temp1.tell() + 21)

    # Updates temp3's data
    temp1.seek(32)
    hti = temp1.read(4)
    offset = hex_to_int(hti)
    temp3.seek(0)

    for i in range(tex_amount - tex_amount_0):
        temp1.seek(offset + 20)
        hti = temp1.read(4)
        offset2 = hex_to_int(hti)
        hti = temp1.read(4)
        tex_data = hex_to_int(hti)

        temp1.seek(temp1.tell() + 8)
        hti = temp1.read(4)
        offset3 = hex_to_int(hti)
        hti = temp1.read(4)
        pal_data = hex_to_int(hti)

        temp1.seek(offset2 + 32)
        t_copy = temp1.read(tex_data)
        temp3.write(t_copy)

        temp1.seek(offset3 + 32)
        t_copy = temp1.read(pal_data)
        temp3.write(t_copy)

        offset = offset + 48

    # Saves new data into your bin
    f.seek(32)
    hti = f.read(4)
    offset = hex_to_int(hti)
    f.seek(offset + 20)
    hti = f.read(4)
    offset = hex_to_int(hti)
    f.seek(offset)
    temp3.seek(0)
    t_copy = temp3.read()
    f.write(t_copy)
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

def tool_check(ggs, folder, tool):
    if tool == 1:
        folder = open("Files\Tools\Tool_Folder.txt", "r+t")
        x = folder.read()
        if x == "":
            print("No data, drag and drop the \"Budokai Modding Tool\" folder here here:")
            x = input("")
            x = x.replace("\"", "")
            folder = folder.write(x)
        else:
            print("Modding Tool Folder located...")
        folder = x
        return folder
    elif tool == 2:
        ggs = open("Files\Tools\GGS.txt", "r+t")
        x = ggs.read()
        if x == "":
            print("No data, drag and drop your Game Graphic Studio EXE here:")
            x = input("")
            x = x.replace("\"", "")
            ggs = ggs.write(x)
        else:
            print("Game Graphic Studio loaded...")
        ggs = x
        return ggs


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


def tex_line_calc(tex_amount):
    #print("calulating lines required...")

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
    prev_offset = prev + 32 + total

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
    prev_offset2 = prev + 32 + total

    prev_offset2 = struct.pack('<L', prev_offset2)
    temp2.seek((temp2.tell() + 8))
    temp2.write(prev_offset2)

    return prev_offset2


def again():
    print("")
    print("Ready for another")
    print("")
    main()
    again()


main()
again()


