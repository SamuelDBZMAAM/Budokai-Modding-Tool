#AMT SB2 Converter
#Purpose of this sub-program - To convert SB2 AMTs to be read in GGS easily
#Files/sb2_tex.amt

print("This part of the tool converts SB2 textures to a readable AMT format")
print("and can convert them back into SB2 for use in game.")
print("Right now only AMTs with a size format like Goku's AMT work so far")
print("And when converting to SB2 again, there will be a lot of 00s at the end")
print("just remove the 00s when in HxD and placing it in the model")
print("")

import struct
options = ["ggs", "sb2"]

def main():
    aa_offsets = []
    a2_offsets = []
    
    print(options)

    print("Choose how to edit the AMT file from above:")
    choice = input("")
    choice = choice.lower()
    if choice == "ggs":
        print("")
        print("Insert SB2 AMT file: ")
        x = input("")
        f = open(x, "r+b")
        chunk = f.read(16)
        #searches for aa and 2a and fixes them
        while chunk != b"":
            if chunk[9] == 0xAA and chunk[10] == 0x00 and chunk[11] == 0x00 and chunk[12] == 0x01:
                aa_offsets.append(((f.tell()-16)))
                #print(hex(f.tell()-16))
            if chunk[9] == 0x2A and chunk[10] == 0x00 and chunk[11] == 0x00 and chunk[12] == 0x01:
                a2_offsets.append(((f.tell()-16)))
                #print(hex(f.tell()-16))
            chunk = f.read(16)
        for i in aa_offsets:
            f.seek(i+9)
            f.write(b"\x80")
        for i in a2_offsets:
            f.seek(i+9)
            f.write(b"\x20")

        f.seek(0)
        #goes to the start of the file, opens a bunch of temp files and fills it in

        temp1 = open("Files/temp1.bin", "w+b")
        temp2 = open("Files/temp2.bin", "r+b")
        temp3 = open("Files/temp3.bin", "r+b")
        temp4 = open("Files/temp4.bin", "r+b")
        temp5 = open("Files/temp5.bin", "r+b")
        temp6 = open("Files/temp6.bin", "r+b")
        temp7 = open("Files/temp7.bin", "r+b")
        temp8 = open("Files/temp8.bin", "r+b")
        lines = open("Files/lines.bin", "r+b")

        

        amt_h = 192
        tex_big = 43520
        tex_small = 10752
        shader = 64 #this is meant to be palette but I cannot be bothered fixing
        rpt = 16

        amt_h_copy = f.read(amt_h)
        temp1.write(amt_h_copy)
        f.seek(0)

        f.seek(192)
        tex1_c = f.read(tex_big)
        temp2.write(tex1_c)
        f.seek(0)

        f.seek(43712)
        shd1_c = f.read(shader)
        temp3.write(shd1_c)
        f.seek(0)

        f.seek(43776)
        tex2_c = f.read(tex_big)
        temp4.write(tex2_c)
        f.seek(0)

        f.seek(87296)
        shd2_c = f.read(shader)
        temp5.write(shd2_c)
        f.seek(0)

        f.seek(87360)
        tex3_c = f.read(tex_small)
        temp6.write(tex3_c)
        f.seek(0)

        f.seek(98112)
        shd3_c = f.read(shader)
        temp7.write(shd3_c)

        f.seek(98176)
        rpt_c = f.read(rpt)
        temp8.write(rpt_c)
        f.seek(0)

        lines_c = lines.read(rpt)
        temp2.seek(0)
        t2_c = temp2.read(tex_big)
        temp3.seek(0)
        t3_c = temp3.read(shader)
        temp4.seek(0)
        t4_c = temp4.read(tex_big)
        temp5.seek(0)
        t5_c = temp5.read(shader)
        temp6.seek(0)
        t6_c = temp6.read(tex_small)
        temp7.seek(0)
        t7_c = temp7.read(shader)
        temp8.seek(0)
        t8_c = temp8.read(rpt)


        #adding all the things to temp1
        temp1.write(lines_c)
        temp1.write(lines_c)
        temp1.write(t2_c)
        temp1.write(lines_c)
        temp1.write(lines_c)
        temp1.write(t3_c)
        temp1.write(lines_c)
        temp1.write(lines_c)
        temp1.write(t4_c)
        temp1.write(lines_c)
        temp1.write(lines_c)
        temp1.write(t5_c)
        temp1.write(lines_c)
        temp1.write(lines_c)
        temp1.write(t6_c)
        temp1.write(lines_c)
        temp1.write(lines_c)
        temp1.write(t7_c)
        temp1.write(lines_c)
        temp1.write(lines_c)
        temp1.write(t8_c)

        
        temp1.seek(0)
        temp1.seek(84)
        temp1.write(b"\xE0")
        temp1.seek(0)
        temp1.seek(116)
        temp1.write(b"\x40")
        temp1.seek(0)
        temp1.seek(132)
        temp1.write(b"\x60")
        temp1.seek(0)
        temp1.seek(164)
        temp1.write(b"\xC0")
        temp1.seek(0)
        temp1.seek(180)
        temp1.write(b"\xE0")
        

        temp1.seek(0)
        temp_all = temp1.read()

        f.seek(0)
        f.write(temp_all)




    if choice == "sb2":
        print("")
        print("Insert the GGS edited AMT: ")
        x = input("")
        f = open(x, "r+b")
        chunk = f.read(16)
        #searches for aa and 2a and fixes them
        while chunk != b"":
            if chunk[9] == 0x80 and chunk[10] == 0x00 and chunk[11] == 0x00 and chunk[12] == 0x01:
                aa_offsets.append(((f.tell()-16)))
                #print(hex(f.tell()-16))
            if chunk[9] == 0x20 and chunk[10] == 0x00 and chunk[11] == 0x00 and chunk[12] == 0x01:
                a2_offsets.append(((f.tell()-16)))
                #print(hex(f.tell()-16))
            chunk = f.read(16)
        for i in aa_offsets:
            f.seek(i+9)
            f.write(b"\xAA")
        for i in a2_offsets:
            f.seek(i+9)
            f.write(b"\x2A")

        f.seek(0)
        #goes to the start of the file, opens a bunch of temp files and fills it in

        temp1 = open("Files/temp1.bin", "w+b")
        temp2 = open("Files/temp2.bin", "r+b")
        temp3 = open("Files/temp3.bin", "r+b")
        temp4 = open("Files/temp4.bin", "r+b")
        temp5 = open("Files/temp5.bin", "r+b")
        temp6 = open("Files/temp6.bin", "r+b")
        temp7 = open("Files/temp7.bin", "r+b")
        temp8 = open("Files/temp8.bin", "r+b")


        amt_h = 192
        tex_big = 43520
        tex_small = 10752
        shader = 64 #this is meant to be palette but I cannot be bothered fixing
        rpt = 16

        amt_h_copy = f.read(amt_h)
        temp1.write(amt_h_copy)
        f.seek(0)

        f.seek(224)
        tex1_c = f.read(tex_big)
        temp2.write(tex1_c)
        f.seek(0)

        f.seek(43776)
        shd1_c = f.read(shader)
        temp3.write(shd1_c)
        f.seek(0)

        f.seek(43872)
        tex2_c = f.read(tex_big)
        temp4.write(tex2_c)
        f.seek(0)

        f.seek(87424)
        shd2_c = f.read(shader)
        temp5.write(shd2_c)
        f.seek(0)

        f.seek(87520)
        tex3_c = f.read(tex_small)
        temp6.write(tex3_c)
        f.seek(0)

        f.seek(98304)
        shd3_c = f.read(shader)
        temp7.write(shd3_c)

        f.seek(98400)
        rpt_c = f.read(rpt)
        temp8.write(rpt_c)
        f.seek(0)

        temp2.seek(0)
        t2_c = temp2.read(tex_big)
        temp3.seek(0)
        t3_c = temp3.read(shader)
        temp4.seek(0)
        t4_c = temp4.read(tex_big)
        temp5.seek(0)
        t5_c = temp5.read(shader)
        temp6.seek(0)
        t6_c = temp6.read(tex_small)
        temp7.seek(0)
        t7_c = temp7.read(shader)
        temp8.seek(0)
        t8_c = temp8.read(rpt)


        #adding all the things to temp1
        temp1.write(t2_c)
        temp1.write(t3_c)
        temp1.write(t4_c)
        temp1.write(t5_c)
        temp1.write(t6_c)
        temp1.write(t7_c)
        temp1.write(t8_c)

        
        temp1.seek(0)
        temp1.seek(84)
        temp1.write(b"\xC0")
        temp1.seek(0)
        temp1.seek(116)
        temp1.write(b"\x00")
        temp1.seek(0)
        temp1.seek(132)
        temp1.write(b"\x00")
        temp1.seek(0)
        temp1.seek(164)
        temp1.write(b"\x40")
        temp1.seek(0)
        temp1.seek(180)
        temp1.write(b"\x40")
        

        temp1.seek(0)
        temp_all = temp1.read(98192)

        f.seek(0)
        f.write(temp_all)

        f.seek(0)
        f.seek(98192)
        for i in range(45008):
            f.write(b"\x00")
        
        
        






    f.close()
    temp1.close()
    temp2.close()
    temp3.close()
    temp4.close()
    temp5.close()
    temp6.close()
    temp7.close()
    temp8.close()
    
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


