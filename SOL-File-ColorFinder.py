import os

from tkinter import *
from math import *
from itertools import cycle
from tkinter import filedialog
from time import sleep

def pack_button():
    button = Button(window,text="Choose SOL File",command=choose_file)
    button.pack()
    
def choose_file():
    global file_path
    
    window.title("Which file to choose?")
    file_path = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select SOL File", filetype=(('SOL file', '*.sol'),("ALL file",'*.*')))

    if len(str(file_path)) != 0:
        color_find()
    else:
        window.title("No File Selected")

def color_find():
    global color_result
    global global_num
    global button

    if global_num != 0:
        for label in window.winfo_children():
            label.destroy()
        pack_button()
        
    file_target = open(file_path, "r", encoding='ANSI')
    file_target = file_target.read()

    if "ColoringWidget" in file_target[18:33] and "grid" in file_target[37:42]:            

        color_list= []
        color_result= []

        solo_file_name = ""
            
        n = len(file_path) - 1
        while n!= 0 and file_path[n] != '/':
            solo_file_name = file_path[n] + solo_file_name
            n -= 1
            
        Label(window, height= 1, text=solo_file_name, font = "Verdana 12 bold", fg='black').pack()
 
        path_output_short = file_path[:n]
        file_path_output = path_output_short + '/' + solo_file_name + ".txt"

        file_target= file_target[44:]
        number = ""
        for n in range (0, len(file_target)):
            if file_target[n] != "," and file_target[n] != ".":
                number += file_target[n]
            else:
                if len(number) > 8:
                    n += len(file_target)-1
                else:
                    if not number in color_list:
                        color_list.append(number)
                    n += 1
                    number= ""

        global_num += len(color_list)
 
        for n in range (0, len(color_list)):
            DecColor = int(color_list[n])
            R = DecColor // 256 // 256 % 256
            G = DecColor // 256 % 256
            B = DecColor % 256

            Hex= "#%02x%02x%02x" % (R,G,B)

            Aver = ( R + G + B ) // 3

            R = str(R)
            G = str(G)
            B = str(B)

            result = str(str(color_list[n]) + str((8 - len(color_list[n])) * " ") + " > RGB(" + R + "," + G + "," + B + ") Hex-Data: " + Hex.upper())
            if n < 43 or global_num < 43:
                if Aver < 126:
                    l = Label(window, bg=Hex, height= 1, text=result, font = ("Verdana", 10), fg='white')
                else:
                    l = Label(window, bg=Hex, height= 1, text=result, font = ("Verdana", 10), fg='black')
                l.pack()
            color_result.append(result)

        for n in range(0, len(color_result)-1):
            color_result[n] = color_result[n] + "\n"

        out_file = open(file_path_output, "w+")

        out_file.write(solo_file_name + "\n")
        out_file.write("Nb of Colors: " + str(len(color_list)) + "\n")
            
        for n in range(0, len(color_result)):
            out_file.write(color_result[n])

        out_file.close()

        if len(color_list) > 43 :
            window.title("Wow! That's a lotsa colors")
            sleep(5)

        window.title("Done! Check the txt file!")

    else:
        window.title("Are you sure this is a Coloring Widget SOL File?")

file_path = ""
global_num = 0

window=Tk()
window.geometry("600x900")
window.title("Welcome to Coloring Widget Color Finder. Please choose a SOL File.")
window.iconbitmap("DA Pixel Maker Tool Ico.ico")
pack_button()

window.mainloop()
