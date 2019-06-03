#AMB Combiner (amb_c)
#Purpose of this sub-program - To hold an AMO0 and AMT inside of an AMB
#For use for porting Infinite World or Budokai 1 models to Budokai 3

import struct

def main():
    print("This is the AMB Combiner")
    print("")
    print("Choose between SB2 or B3 AMB:")
    choice = input("")
    choice = choice[0:1]
    choice = choice.lower()
    if choice == "b":
        m = input("Name of AMO file: ")
        m = m.replace("\"", "")
        t = input("Name of AMT file: ")
        t = t.replace("\"", "")
        b3_main(m, t)
        again()
    if choice == "s":
        m = input("Name of AMO file: ")
        m = m.replace("\"", "")
        t = input("Name of AMT file: ")
        t = t.replace("\"", "")
        print("Please ensure that the #RPT is separated from the AMT")
        p = input("Name of RPT file:")
        p = p.replace("\"", "")
        sb2_main(m, t, p)
        again()
    else:
        print("Not a valid answer, try again")
        print("")
        main()

def b3_main(m, t):
    c = "Files/amb.bin"
    r = "Files/amb - copy.bin"
    n = "new_amb.bin"
    offsets = []
    print("Combining all for B3...")
    with open(c, "r+b") as output, open(m, "r+b") as input:
        output.seek(64)
        data = input.read()
        output.write(data)

    with open(c, "a+b") as output, open(t, "r+b") as input:
        data = input.read()
        output.write(data)

    output.close()
    input.close()

    amt = open(t, "r+b")
    amt.seek(0,2)
    amt_length = amt.tell()
    amt.close()

    f = open(c, "r+b")
    chunk = f.read(16)

    while chunk != b"":
        if chunk[0]== 0x23 and chunk[1] == 0x41 and chunk[2]== 0x4D and chunk[3] == 0x54:
            offsets.append(((f.tell() - 16)))
        chunk = f.read(16)

    f.seek(36)
    f.write(struct.pack("<I", offsets[0] - 64))

    f.seek(48)
    f.write(struct.pack("<I", offsets[0]))

    f.seek(52)
    f.write(struct.pack("<I", amt_length))

    f.seek(0)

    f_all = f.read()

    
    nf = open(n, "w+b")
    nf.write(f_all)
    
    nf.close()
    f.close()

    with open(c, "w+b") as output, open(r, "r+b") as input:
        output.seek(0)
        data = input.read()
        output.write(data)

    output.close()
    input.close()
    
    print("Successfully added all to the AMB")
    

def sb2_main(m, t, p):
    c = "Files/sb2_amb.bin"
    r = "Files/sb2_amb - copy.bin"
    n = "new_amb.bin"

    offsets = []
    print("Combining all for SB2...")
    with open(c, "r+b") as output, open(m, "r+b") as input:
        output.seek(128)
        data = input.read()
        output.write(data)

    with open(c, "a+b") as output, open(t, "r+b") as input:
        data = input.read()
        output.write(data)
        rpt_loc = output.seek(0,2)

    with open(c, "a+b") as output, open(p, "r+b") as input:
        data = input.read()
        rpt_loc = output.seek(0,2)
        output.write(data)
        

    output.close()
    input.close()

    amt = open(t, "r+b")
    amt.seek(0,2)
    amt_length = amt.tell()
    amt.close()

    rpt = open(p, "r+b")
    rpt.seek(0,2)
    rpt_length = rpt.tell()
    rpt.close()

    f = open(c, "r+b")
    chunk = f.read(16)

    while chunk != b"":
        if chunk[0]== 0x23 and chunk[1] == 0x41 and chunk[2]== 0x4D and chunk[3] == 0x54:
            offsets.append(((f.tell() - 16)))
        chunk = f.read(16)

    f.seek(36)
    f.write(struct.pack("<I", offsets[0] - 64))

    f.seek(48)
    f.write(struct.pack("<I", offsets[0]))

    f.seek(52)
    f.write(struct.pack("<I", amt_length))

    f.seek(64)
    f.write(struct.pack("<I", rpt_loc))

    f.seek(68)
    f.write(struct.pack("<I", rpt_length))
    

    f.seek(0)

    f_all = f.read()

    
    nf = open(n, "w+b")
    nf.write(f_all)
    
    nf.close()
    f.close()

    with open(c, "w+b") as output, open(r, "r+b") as input:
        output.seek(0)
        data = input.read()
        output.write(data)

    output.close()
    input.close()
    
    print("Successfully added all to the AMB")


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
exit()
