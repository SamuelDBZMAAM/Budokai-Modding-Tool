# AMO Model Separator - amo_s
# Purpose: To make every model part in the character a separate AMG for use in Budokai series


import struct
import math
import os

def main():
    print("")
    print("Drag and drop AMO here")
    x = input("")
    x = x.replace("\"", "")
    f = open(x, "r+b")

    # Copying files needed
    hti = 0
    ith = 0
    chunk = f.read(16)
    amg_head = open("Files\AMG\B3_amg_head.bin", "r+b")
    amg_head = amg_head.read()
    amg_axis = open("Files\AMG\B3_amg_axis.bin", "r+b")
    amg_axis = amg_axis.read()
    amg_mp1 = open("Files\AMG\B3_amg_mp1.bin", "r+b")
    amg_mp1 = amg_mp1.read()
    amg_mp2 = open("Files\AMG\B3_amg_mp2.bin", "r+b")
    amg_mp2 = amg_mp2.read()
    amg_end = open("Files\AMG\B3_amg_end.bin", "r+b")
    amg_end = amg_end.read()

    # Setting up temp bins
    tn1 = "Files\z.bin"  # Will hold edited bin
    temp1 = open(tn1, "w+b")
    temp1.close()
    temp1 = open(tn1, "r+b")

    # Setting up AMG template
    temp1.write(amg_head)
    temp1.seek(16)
    temp1.write(b'\x01')
    temp1.read()
    temp1.write(amg_axis)
    temp1.seek(84)
    temp1.write(b'\x70\x00\x00\x00')
    temp1.read()
    temp1.write(amg_mp1)
    temp1.seek(116)
    temp1.write(b'\x80\x00\x00\x00')
    temp1.read()
    temp1.write(amg_mp2)
    temp1.seek(144)
    temp1.write(b'\x20\x00\x00\x00')
    temp1.seek(0)
    amg_temp = temp1.read()

    # Searches how many model parts are in the AMO and creates AMGs
    amount_parts = 0
    while chunk != b"":
        if chunk[0] == 0x01 and chunk[8] == 0x46:
            amount_parts += 1
            part_offset = f.tell()
            #print("DEBUG: Model part position - " + str(f.tell()))
            # Collects mesh-----------------------------------------
            f.seek(part_offset+64)
            hti = f.read(4)
            mesh_size = hex_to_int(hti)
            mesh_size = (mesh_size-1610612736)*16
            #print("DEBUG: Mesh size - " + str(mesh_size))
            f.seek(part_offset+80)
            mesh = f.read(mesh_size)
            # Collects the model part heading-----------------------
            f.seek(part_offset-80)
            mesh_heading = f.read(160)
            #print("DEBUG: Heading data collected...")
            f.seek(part_offset-72)  # Texture number
            hti = f.read(4)
            if hti == b'\xFF\xFF\xFF\xFF':
                t_numb = "N"
            else:
                t_numb = hex_to_int(hti)+1
            f.seek(part_offset-68)  # Shader number
            hti = f.read(4)
            if hti == b'\xFF\xFF\xFF\xFF':
                s_numb = "N"
            else:
                s_numb = hex_to_int(hti) + 1
            #print("DEBUG: Texture - " + str(t_numb))
            #print("DEBUG: Shader - " + str(s_numb))
            # Creating AMG for part found--------------------------
            f_name = "Model Part " + str(amount_parts) + " - T" + str(t_numb) + "_S" + str(s_numb) + ".bin"
            #print("DEBUG: File name - " + f_name)
            folder = x+" - All parts\\"
            if not os.path.exists(folder):      # Creates new folder for model parts
                os.makedirs(folder)
            amg = open(folder+f_name, "w+b")
            amg.close()
            amg = open(folder+f_name, "r+b")
            amg.write(amg_temp)
            amg.write(mesh_heading)
            amg.write(mesh)
            amg.write(amg_end)
            amg_size = amg.tell()
            #print("DEBUG: AMG size - " + str(amg_size))
            amg.seek(28)
            amg.write(b'\x00\x00\x00\x00')
            amg.seek(28)
            ith = amg_size
            amg_size2 = int_to_hex(ith)
            amg.write(amg_size2)
            amg.seek(124)
            amg.write(b'\x00\x00\x00\x00')
            amg.seek(124)
            ith = amg_size-64
            amg_size2 = int_to_hex(ith)
            amg.write(amg_size2)

            #print("")
            f.seek(part_offset)

        chunk = f.read(16)
    #print("DEBUG: Total amount of model parts - " + str(amount_parts))

    print("")
    print("Completed!")

    # deletes temp files
    tn1 = "Files\z.bin"
    temp1 = open(tn1, "r+b")
    temp1.close()
    os.remove(tn1)

    print("")
    print("T#_S# = Texture used [Texture number in GGS], Shader used [Texture number in GGS].")
    print("TN or SN = No texture used.")
    print("You now have a new folder with all of the model parts in it located at [" + folder + "]")
    print("")


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
