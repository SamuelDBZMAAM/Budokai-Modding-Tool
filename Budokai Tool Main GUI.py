#The Main UI for the Budokai Tool
#
#
#
#



#extra stuff
#entries - use for taking in data or whatever
#f = StringVar()
#f_amo = Entry(window, textvariable=f)
#labels - use for what functions you want to use
#head = Label(window, text="Main Sections").grid(row=0,column=0)
#buttons - use for clicking and using stuff
#amo_ac = Button(window, text="Insert AMO").grid(row=1,column=0)




#imports tkinter, struct and math
from tkinter import *
import struct
import math

#-- Basic Variable Names for use

#sends the name of the tkinter file opening to window
window = Tk()

#sets name to the window as such
window.title("Budokai Modding Tool V1.0")

#sets window size (may differ or give options)
window.geometry("450x244")

#icon for the tool because i'm extra lmao
window.wm_iconbitmap("Files/UI/new_icon.ico")

#bg colour
window.configure(background = "#ffffff")

#img for title
x = "Files/UI/new_title.png"
img = PhotoImage(file=x)

#options variable for later
opts = 12

#creates values to pass through to the next window for display and usage
send_to = ""
send_speech = ""

#panel = window(title, image = img, height = 122, width = 405, borderwidth=0).grid(row=0,column=0)

#other window stuff
title = Toplevel(bg = "#ffffff")
title.title("Budokai Modding Tool V1.0")
title.geometry("510x160")
title.wm_iconbitmap("Files/UI/new_icon.ico")
panel = Label(title, image = img, height = 110, width = 510, borderwidth=0).grid(row=0,column=0)

#text stuff
T = Text(title, height=3, width=50)
T.grid(row=1,column=0)
T.insert(END, send_speech)

def pass_through(send_to, send_speech):
   T.delete("%s-1000c" % INSERT, INSERT)
   T.insert(CURRENT, send_speech)

def amb_c():
   send_to = "ambc"
   send_speech = "AMB Combiner creates a new file using both an AMO and AMT of a character model, use for IW > B3 and B1 > B3!"
   pass_through(send_to, send_speech)

def ame_ae():
   send_to = "ameae"
   send_speech = "AME Editor allows you to edit and create aura files for IW and B3! (Credit to Nexus-Sama)"
   pass_through(send_to, send_speech)
   
def amg_a():
   send_to = "amga"
   send_speech = "AMG Addition allows you to add AMG model parts onto a character with space!"
   pass_through(send_to, send_speech)
   
def amm_ta():
   send_to = "ammta"
   send_speech = "AMM Editor allows you to give characters tail animations, with a varying choice of animations! (Credit to Nexus-Sama)"
   pass_through(send_to, send_speech)
   
def amo_a():
   send_to = "amoa"
   send_speech = "AMO Addition inserts an extra line for AMGs on any AMO given (SB2 and B3 compatible!)"
   pass_through(send_to, send_speech)
   
def amo_aa():
   send_to = "amoaa"
   send_speech = "not-implemented-yet"
   pass_through(send_to, send_speech)
   
def amt_c():
   send_to = "amtc"
   send_speech = "AMT Creator gives you a choice of options on adding textures onto an AMT for use in any situation (16 and 256 colours!)"
   pass_through(send_to, send_speech)
   
def amt_sb():
   send_to = "amtsb"
   send_speech = "AMT SB2 converts SB2 AMTs to a format that GGS can read and puts it back(only compatible with character AMTs!) "
   pass_through(send_to, send_speech)
   
def amt_sr():
   send_to = "amsr"
   send_speech = "AMT Shader Replace replaces all traditional shaders of 64x64(256) into 8x512(256) for HD shading! (Credit to Nexus-Sama)"
   pass_through(send_to, send_speech)
   
def b_1_e():
   send_to = "b1e"
   send_speech = "Exports Budokai 1 files (AMO) into Non-B1 games!"
   pass_through(send_to, send_speech)
   
def b_1_i():
   send_to = "b1i"
   send_speech = "Exports Non-B1 files (AMO) into Budokai 1!"
   pass_through(send_to, send_speech)
   
def m_p_e():
   send_to = "mpe"
   send_speech = "Allows for various editing of model parts such as Borders, fixing non-shadable parts and more!"
   pass_through(send_to, send_speech)


#Header
head = Label(window, text="Select your tool!", bg = "white").grid(row=1,column=0)

#Section 1
amb_c = Button(window, text="AMB Combiner", command=amb_c, height = 1, width = 20).grid(row=2,column=0)
ame_ae = Button(window, text="AME Creation", command=ame_ae, height = 1, width = 20).grid(row=2,column=4)
amg_a = Button(window, text="AMG Addition", command=amg_a, height = 1, width = 20).grid(row=2,column=8)
#Section 2
amm_ta = Button(window, text="AMM Editor", command=amm_ta, height = 1, width = 20).grid(row=3,column=0)
amo_a = Button(window, text="AMO Addition", command=amo_a, height = 1, width = 20).grid(row=3,column=4)
amo_aa = Button(window, text="AMO Axis Addition", command=amo_aa, height = 1, width = 20).grid(row=3,column=8)
#Section 3
amt_c = Button(window, text="AMT Creation ", command=amt_c, height = 1, width = 20).grid(row=4,column=0)
amt_sb = Button(window, text="AMT SB2 Converter", command=amt_sb, height = 1, width = 20).grid(row=4,column=4)
amt_sr = Button(window, text="AMT Shader Replace", command=amt_sr, height = 1, width = 20).grid(row=4,column=8)
#Section 4
b_1_e = Button(window, text="Budokai 1 Exporter", command=b_1_e, height = 1, width = 20).grid(row=5,column=0)
b_1_i = Button(window, text="Budokai 1 Importer", command=b_1_i, height = 1, width = 20).grid(row=5,column=4)
m_p_e = Button(window, text="Model Part Editor", command=m_p_e, height = 1, width = 20).grid(row=5,column=8)


#drawing to window is last
window.mainloop()




