#AMB Combiner (amb_c)
#Purpose of this sub-program - To hold an AMO0 and AMT inside of an AMB
#For use for porting Infinite World or Budokai 1 models to Budokai 3

import struct

c = "Files/amb.bin"
r = "Files/amb - copy.bin"
n = "new_amb.bin"
m = input("Name of AMO file: ")
m = m.replace("\"", "")
t = input("Name of AMT file: ")
t = t.replace("\"", "")

def main():
    offsets = []
    print("Combining the AMT and AMO0...")
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
    
    print("Successfully added the AMO and AMT to an AMB")
    

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
