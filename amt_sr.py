#AMT Shader replacer - amt_sr
#Purpose: To replace all old 64x64 shaders with 512x8 UHD shaders


import struct
import math
import os

print("ONLY WORKS WITH 64x64 SHADERS, NOT 64x8 SHADERS USED IN NEWER IW MODELS")

def main():
    print("AMT name (with extension):")
    #opens AMT
    x = input("")
    x = x.replace("\"", "")
    f = open(x, "r+b")
    hti = None
    ith = None

    # Copying files needed
    nxs_shader = open("Files/AMT/Nexus Shader (UHD).bin", "r+b")  # NXS UHD shader
    nxs_shader.seek(48)
    nxs_shader = nxs_shader.read()

    # Setting up temp bins
    tn1 = "Files\z.bin"  # Will hold edited bin
    temp1 = open(tn1, "w+b")
    temp1.close()
    temp1 = open(tn1, "r+b")

    # Making a copy of your bin to edit and checks each texture for shader
    t_copy = f.read()
    temp1.write(t_copy)
    temp1.seek(16)
    hti = temp1.read(4)
    num_of_tex = hex_to_int(hti)
    tex_offset = 32
    for i in range(num_of_tex):
        temp1.seek(tex_offset)

        hti = temp1.read(4)
        new_offset = hex_to_int(hti)
        temp1.seek(new_offset + 4)

        shader_check = temp1.read(4)
        if shader_check == b'\x01\x00\x00\x80':
            #print("DEBUG: Shader found")
            temp1.seek(new_offset + 16)
            size_check = temp1.read(4)
            if size_check == b'\x40\x00\x40\x00':
                temp1.seek(new_offset + 12)
                temp1.write(b'\x09\x00\x03\x00')
                temp1.seek(new_offset + 16)
                temp1.write(b'\x00\x02\x08\x00')
                temp1.seek(new_offset + 20)
                hti = temp1.read(4)
                offset = hex_to_int(hti)
                temp1.seek(offset)
                temp1.write(nxs_shader)
        tex_offset = tex_offset + 4

    # Assembles and Saves new AMT
    temp1.close()
    temp1 = open(tn1, "r+b")
    t_copy = temp1.read()
    f.seek(0)
    f.write(t_copy)
    f.close()
    print("")
    print("Completed!")

    # deletes temp files
    tn1 = "Files\z.bin"
    temp1 = open(tn1, "r+b")
    temp1.close()
    os.remove(tn1)


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
        print("AMT creator by: Nexus-sama")
        print("credit to SamuelDBZMA&M for some parts")
        print("Follow me on Twitter @NexusTheModder")
        print("")
        kill = input("press enter to close")


main()
again()

exit()
