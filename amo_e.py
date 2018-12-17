#AMO Editor (AMOE)
#Purpose of this sub-program - To edit the AMO0 in such a way that will
#allow for extra space on the AMO0 for extra AMGs to be placed
#Files/brl - Copy.bin

import struct

options = ["Extra Line", "a"]
amb_skip = 64
plus = 16

def main():

    #Insert the model file
    print("Insert Model file: ")
    x = input("")

    #Choice of what to do to the file
    choice = input("What would you like to do?: ")
    while choice not in options:
        choice = input("Not an option: ")

    #If one of the choices was extra line:
    if choice == "Extra Line" or choice == "a":
        #array for the offsets to store the location the first AMG
        offsets = []
        #if the model has an AMB or not, used for fixing IW and B3 models
        amb = input("Is there an AMB (t/f)? ")
        while amb != "t" and amb != "f":
            amb = input("Not a valid answer: ")
        if amb == "t":
            amb_skip = 64
        if amb == "f":
            amb_skip = 0
        #Opens all the neccesary files for spearating the AMO0
        with open(x, "r+b") as f, open("Files/lines.bin", "r+b") as line, open("Files/temp1.bin", "r+b") as temp1, open("Files/temp2.bin", "r+b") as temp2, open("Files/temp3.bin", "r+b") as temp3:
            amg_count = int(input("How many AMG lines are there (deci)? "))
            #f.seek((amb_skip + (amg_count *16) + 48))

            #Reads only up to the size of the AMO and the AMB if applicableg
            f_chunk_ex = f.read((amb_skip + (amg_count *16) + 48))
            print((amb_skip + (amg_count *16) + 48))
            #Writes it to temp1
            temp1.write(f_chunk_ex)
            #reads the rest of the file
            rest = f.read()
            #writes the rest of the file into temp2
            temp2.write(rest)
            f.close()
            #reads all of the line
            line_temp = line.read(16)
            #writes it to temp1
            temp1.write(line_temp)
            #closes everything for simplicity
            line.close()
            f.close()
            line.close()
            temp1.close()
            temp2.close()
            temp3.close()

        #Opens temp2 for searching for the first AMG
        with open("Files/temp2.bin", "r+b") as temp2:
            chunk = temp2.read(16)
            while chunk != b"":
                if chunk[0] == 0x23 and chunk[1] == 0x41 and chunk[2] == 0x4D and chunk[3] == 0x47:
                    offsets.append(((temp2.tell() - 16)))
                    print(hex(temp2.tell() - 16))
                chunk = temp2.read(16)

            print(offsets)
        temp2.close()

        #Opens temp2 and temp3 for extracting the parts of the AMO0 and paste it into temp3
        with open("Files/temp2.bin", "r+b") as temp2, open("Files/temp3.bin", "r+b") as temp3:
            temp_chunk = temp2.read(offsets[0])
            temp3.write(temp_chunk)
        temp2.close()
        temp3.close()

        #Opens temp3 and searches for all of the values that aren't 00
        t3_offsets = []
        with open("Files/temp3.bin", "r+b") as temp3:
            chunk = temp3.read(16)
            while chunk != b"":
                if chunk[0] != 0x00:
                    t3_offsets.append(((temp3.tell() - 16)))
                    #print(hex(temp3.tell() - 16))
                chunk = temp3.read(16)
            print(t3_offsets)
            for i in t3_offsets:
                g = temp3.seek(i)
                if g == 0x30:
                    temp3.write(b"\x80")
                
    
    #here will be where temp3 (with the amo0 data) will have the values edited
    #then temp3 will be thrown into temp2 and saved
    #the data for temp1 will be edited (the location of each AMG which is already saved)
    #the length willbe altered too, after that, data from temp1 gets placed in the file,
    #followed by temp2
    #Wipe data in all temps for later use

#Files/brl - Copy.bin
##            data = line.read()
##            f.seek((amb_skip + (amg_count * 16) + 48))
##            print(f.tell())
##            temp_data = f.read(0,(amb_skip + (amg_count * 16) + 48))
##            
##            temp.write(temp_data)
            #f_chunk = f.read(16)
            #l_chunk = line.read(16)
            #t1_chunk = temp1.read(16)
            #t2_chunk = temp2.read(16)
            

    f.close()
    line.close()
    temp1.close()
    temp2.close()
    temp3.close()
    #Open the file, determine if it has an AMB or not, ask for the lines
    #Split the file for where the line would be placed, add the line
    #merge the file, close, open again
    #go to the line and add in a blank line of 00s
    #correct all values on the header of the AMO0
    #correct all values on the AMG connection of the AMO0
    #adjust other values
    #save file









main()
exit()
