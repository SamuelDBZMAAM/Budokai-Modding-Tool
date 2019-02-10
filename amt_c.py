#AMT Creator - amt_c
#Purpose: To create an AMT for use in Budokai series


import struct
import math


def main():
    print("Give me a name for the new AMT file (with extension):")
    #creates a new AMT file entirely
    x = input("")
    f = open(x, "w+b")
    chunk = f.read(16)

    tex_offsets = []
    pal_offsets = []
    block_offsets = []
    
    #open up all the files for choice
    #the "a" before variables is because python doesn't like numbers
    #as variables, thus a64x64 and etc
    
    #basic shit for an amt to build
    block = open("AMT/block.bin", "r+b")
    header = open("AMT/header.bin", "r+b")
    line = open("AMT/line.bin", "r+b")
    
    #16 colours
    a64x64_16 = open("AMT/64x64.amt", "r+b")
    a128x64_16 = open("AMT/128x64.amt", "r+b")
    a128x128_16 = open("AMT/128x128.amt", "r+b")
    a128x256_16 = open("AMT/128x256.amt", "r+b")
    a256x128_16 = open("AMT/256x128.amt", "r+b")
    a256x256_16 = open("AMT/256x256.amt", "r+b")
    a256x512_16 = open("AMT/256x512.amt", "r+b")
    a512x512_16 = open("AMT/512x512.amt", "r+b")
    a512x256_16 = open("AMT/512x256.amt", "r+b")

    #256 colours
    a64x64_256 = open("AMT/64x64(256).amt", "r+b")
    a128x64_256 = open("AMT/128x64(256).amt", "r+b")
    a128x128_256 = open("AMT/128x128(256).amt", "r+b")
    a128x256_256 = open("AMT/128x256(256).amt", "r+b")
    a256x128_256 = open("AMT/256x128(256).amt", "r+b")
    a256x256_256 = open("AMT/256x256(256).amt", "r+b")
    a256x512_256 = open("AMT/256x512(256).amt", "r+b")
    a512x512_256 = open("AMT/512x512(256).amt", "r+b")
    a512x256_256 = open("AMT/512x256(256).amt", "r+b")
    a512x8_256 = open("AMT/512x8(256).amt", "r+b")

    col_16 = [a64x64_16, a128x64_16, a128x128_16,
              a128x256_16, a256x128_16, a256x256_16,
              a256x512_16, a512x512_16, a512x256_16]

    col_256 = [a64x64_256, a128x64_256, a128x128_256,
              a128x256_256, a256x128_256, a256x256_256,
              a256x512_256, a512x512_256, a512x256_256, a512x8_256]

    tex_16 = ["64x64", "128x64", "128x128",
              "128x256", "256x128", "256x256",
              "256x512", "512x512", "512x256"]

    tex_256 = ["64x64", "128x64", "128x128",
               "128x256", "256x128", "256x256",
               "256x512", "512x512", "512x256", "512x8"]

    #code to use for making the amt
    print("How many textures are there: ")
    tex_amount = int(input(""))
    tex_am_lines = tex_line_calc(tex_amount)

    #copies all of the data from header and line to paste in f
    header_copy = header.read()
    line_copy = line.read()
    f.write(header_copy)

    #for every line there is, paste it
    for i in range(tex_am_lines):
        f.write(line_copy)

    #insert asking for what textures one would want
    col_list = ["16", "256"]
    print(col_list)
    print("How many colours: ")
    col_choice = input("")
    while col_choice != "16" and col_choice != "256":
        print("Not an option, please choose, please choose either 16 or 256")
        col_choice = input("")

    if col_choice == ("16"):
        choice_list = []
        #show list of different textures available
        #print(tex_16)
        #for loop that lasts for as many textures as you have asked for
        #this is to psate the blocks first
        for i in range(tex_amount):
            print("Pick the texture you want")
            print("(select the texture by typing it's position on the list)")
            #asks you to chose what texture you want by number on the options
            #so 64x64 = 1, 128x64 = 2, etc
            choice = int(input(""))
            #-1 from the choice so it works with picking the correct texture
            #from the array and is correct
            choice = choice - 1
            print(choice)

            while choice >= int(len(tex_16)):
                #if it is not within range, it asks again
                print("Not within range, try again:")
                choice = int(input(""))
                choice = choice - 1
            choice_list.append(choice)

            #prints the chosen texture
            #print(tex_16[choice])
            print(choice_list)


            #sets a variable to be the result of the function
            tex_block_copy = block_16_pick(col_16, choice)

            #writes that data to file
            f.write(tex_block_copy)

        #for the texture data
        for i in range(tex_amount):
            print("")
            #another function that gets the variable the function
            tex_data = col_16[choice_list[i]]
            tex_data.seek(96)
            tex_data_copy = tex_data.read(300000)
            #writes that
            f.write(tex_data_copy)





            
        
    #for if 256 colours was chosen
    if col_choice == ("256"):
        choice_list = []
        #show list of different textures available
        print(tex_256)
        #for loop that lasts for as many textures as you have asked for
        #this is to psate the blocks first
        for i in range(tex_amount):
            print("Pick the texture you want")
            print("(select the texture by typing it's position on the list)")
            #asks you to chose what texture you want by number on the options
            #so 64x64 = 1, 128x64 = 2, etc
            choice = int(input(""))
            #-1 from the choice so it works with picking the correct texture
            #from the array and is correct
            choice = choice - 1
            #print(choice)

            while choice >= int(len(tex_256)):
                #if it is not within range, it asks again
                print("Not within range, try again:")
                choice = int(input(""))
                choice = choice - 1
            choice_list.append(choice)

            #prints the chosen texture
            #print(tex_256[choice])
            #print(choice_list)


            #sets a variable to be the result of the function
            tex_block_copy = block_256_pick(col_256, choice)

            #writes that data to file
            f.write(tex_block_copy)

        #for the texture data
        for i in range(tex_amount):
            #print("")
            #another function that gets the variable the function
            tex_data = col_256[choice_list[i]]
            tex_data.seek(96)
            tex_data_copy = tex_data.read(300000)
            #writes that
            f.write(tex_data_copy)


    #this changes the number of textures in the amt
    f.seek(0)
    f.seek(16)
    shader_number = tex_amount
    shader_number = chr(shader_number)
    shader_number = bytes(shader_number, ("utf-8"))
    
    f.write(shader_number)
    f.seek(0)


    chunk = f.read(16)
    #finds offsets of every texture and palette
    while chunk != b"":
        if chunk[12] == 0x54 and chunk[13] == 0x41 and chunk[14] == 0x5F:
            tex_offsets.append(((f.tell()-16)))
            #print(hex(f.tell()-16))
            
        if chunk[12] == 0x4C and chunk[13] == 0x45 and chunk[14] == 0x54:
            pal_offsets.append(((f.tell()-16)))
            #print(hex(f.tell()-16))

        chunk = f.read(16)

    #print(tex_offsets)
    #print(pal_offsets)

    #for extracting and placing the texture offsets
    f.seek(0)
    jump = (32 + (tex_am_lines * 16))
    for i in range(tex_amount):
        f.seek(((i*48)+20) + jump)
        offset_grab = tex_offsets[i]
        offset_grab_1 = struct.pack("<I", offset_grab)
        f.write(offset_grab_1)
    #for extracting and placing the palette offsets
    f.seek(0)
    for i in range(tex_amount):
        f.seek(((i*48)+36) + jump)
        offset_grab = pal_offsets[i]
        offset_grab_1 = struct.pack("<I", offset_grab)
        f.write(offset_grab_1)    

        
    #for finding and placing the texture block locations
    f.seek(0)
    chunk = f.read(16)
    while chunk != b"":
        if chunk[0] == 0xFF and chunk[1] == 0x00:
            block_offsets.append(((f.tell()-16)))
            #print(hex(f.tell()-16))
        chunk = f.read(16)
    #print(block_offsets)

    for i in range(tex_amount):
        f.seek(block_offsets[i])
        block_number = 0 + i
        block_number = chr(block_number)
        block_number = bytes(block_number, ("utf-8"))
        f.write(block_number)

    f.seek(0)
    for i in range(tex_amount):
        f.seek(32 + (i*4))
        block_grab = block_offsets[i]
        block_grab_1 = struct.pack("<I", block_grab)
        f.write(block_grab_1)



    #closing 16 colours
    a64x64_16.close()
    a128x64_16.close()
    a128x128_16.close()
    a128x256_16.close()
    a256x128_16.close()
    a256x256_16.close()
    a256x512_16.close()
    a512x256_16.close()
    a512x512_16.close()
    #closing 256 colours
    a64x64_256.close()
    a128x64_256.close()
    a128x128_256.close()
    a128x256_256.close()
    a256x128_256.close()
    a256x256_256.close()
    a256x512_256.close()
    a512x256_256.close()
    a512x512_256.close()
    a512x8_256.close()
    #closes amt
    f.close()
    print("AMT Creation Complete!")
    print("")
    print("If you want to change any of the textures on the AMT to a shader,")
    print("Use Nexus-Sama's guide on to how to correct any texture blocks as shaders,")
    print("This will be fixed in a later update but for now, please do it manually, thanks!")
    print("")


#this calculates how many lines are needed for 
def tex_line_calc(tex_amount):
    print("calulating lines required...")

    line_break = 4
    
    tex_am_lines = math.ceil(tex_amount / line_break)

    return tex_am_lines



def block_256_pick(col_256, choice):
    print("adding texture...")

    tex_block = col_256[choice]

    tex_block.seek(48)

    tex_block_copy = tex_block.read(48)

    return tex_block_copy





def block_16_pick(col_16, choice):
    print("adding texture...")

    tex_block = col_16[choice]

    tex_block.seek(48)

    tex_block_copy = tex_block.read(48)

    return tex_block_copy



def data_16_pick(col_16, choice):

    tex_data = col_16[choice]

    tex_data.seek(96)

    tex_data_copy = tex_data.read(41000)

    return tex_data_copy

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
