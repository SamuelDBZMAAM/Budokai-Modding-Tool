#Dragon Ball Z Budokai Modding Tool
#Created by SamuelDBZMAAM, -----,-----,-----,-----,
#Start Date - 06/12/18
#Completion Date - dd/mm/yy
#Coded and Compiled in Python 3.6
#
#
#Purpose - To be able to successfully edit model and texture formats from the
#Budokai series including Budokai 1, Budokai 2, Budokai 3 and Infinite World
#Using a comfortable UI, the modding tool will give ease to a user and help 
#build a character, transformation or story to their favourite game!
#
#
#Extension purposes -
#1 - To edit, import, export model parts from compatible
#games into the Budokai Series and vice versa, these games could include
#Shin Budokai, Persona (PS2, PSP), Budokai Tenkachi
#
#2 - Create ideas and inspire modders to make certain models and characters
#using the tool itself with fusion, transformation and absorption
#sections to give to a user
#
#3 - Save and extract parts a user has used to use for next time, i.e.
#If a user has used a SSJ Goku hair model part it saves that file to
#a folder to user later
#
#4 - Reccommend models, model parts, textures, etc to a user when building
#a model to help and give a much easier experience
#
#
#Budokai Modding Tool - Main Program
#Sub-Programs below:
#
#AMT Editor - doing - discontinued
#AMT Creator - done
#AMB Combiner - done
#AMG Creator - doing - 4
#AMG Addition - doing - 3
#AMO0 Editor - doing - 1
#AMO0 Creator
#Model Part Editor - done
#Budokai 1 Importer - done
#Budokai 1 Exporter - done
#LGBT Tool
#Shin Budokai Importer
#Shin Budokai Exporter
#Model Viewer
#Texture Viewer - done (shin budokai texture viewer)
#Random Model Feature
#Random Texture Feature
#Tasks/Achievements
#Aura Editor - doing - 5
#Aura Creator
#
#
#Purpose of this Program - To be the main program to connect various
#functions, sub-programs and other parts of the tool
#
#
"""
    if x == "" or x == "":
        import
        .main()


Insert Code Below
"""
import random
import struct

#import __insert other function here__


func_list = ["AMT Editor", "AMT Creator", "AMB Combiner", "AMG Creator", "AMG Addition", "AMO Editor",
             "AMO Creator", "Model Part Editor", "Budokai 1 Importer", "Budokai 1 Exporter", "LGBT Tool",
             "Shin Budokai Importer", "Shin Budokai Exporter", "Model Viewer", "Texture Viewer",
             "Random Model Feature", "Random Texture Feature", "Tasks and Achievements", "Aura Editor", "Aura Creator"]


useable = ["Model Part Editor", "AMT Creator", "Budokai 1 Exporter",
           "Budokai 1 Importer", "AMB Combine", "SB2 AMT Edit",
           "AMG Addition", "AME Editing", "AMM Editing", "AMO Addition"]


#Main Function to load other ones

def main():
    print("Welcome to the Budokai Modding Tool!")
    print(useable)
    print("")
    print("Please select the function you would like to use: ")
    x = input("")
    #while x not in func_list:
    #    x = input("That is not valid, please select from above: ")
    if x == "Model Part Editor" or x == "mpe":
        import m_p_e
        m_p_e.main()
    if x == "Budokai 1 Exporter" or x == "b1e":
        import b_1_e
        b_1_e.main()
    if x == "Budokai 1 Importer" or x == "b1i":
        import b_1_i
        b_1_i.main()
    if x == "AMB Combine" or x == "amb":
        import amb_c
        amb_c.main()
    if x == "AMT Creator" or x == "amtc":
        import amt_c
        amt_c.main()
    if x == "SB2 AMT Edit" or x == "amtsb":
        import amt_sb.py
        amt_sb.py()
    if x == "AMO Addition" or x == "amoa":
        import amo_a
        amo_a.main()
    if x == "AMG Addition" or x == "amga":
        import amg_a
        amg_a.start()
    if x == "AME Editing" or x == "ammta":
        import amm_ta
        amm_ta.bsk_type()
    if x == "AMM Editing" or x == "ameae":
        import amm_ae
        amm_ae.aura_type()


    else:
        false_end()



def end():
    print("Thank you for using the modding tool!")
    exit()

def false_end():
    print("Error, please try again.")
    main()

main()
end()
