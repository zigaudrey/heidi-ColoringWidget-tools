import os

from tkinter import *
from math import *
from itertools import cycle
from tkinter import filedialog
from time import sleep

def destroy_all():
    for label in window.winfo_children():
        label.destroy()

def pack_button():
    button = Button(window,text="Choose SOL File",command=choose_file)
    button.pack()

def page_button_pack(End):  
    page_frame= Frame()
    page_frame.pack()
    if page != 0 :
        prev_button = Button(page_frame,text="Prev",command=prev_page)
        prev_button.grid(row=0,column=0)
    if page == 0 or End ==  False:
        next_button = Button(page_frame,text="Next",command=next_page)
        next_button.grid(row=0,column=1)
        
def next_page():
    global page
    global end

    end = False
    
    if page < len(result) % 36 or page < 5:
        destroy_all()
        page += 1
        pack_button()
        Label(window, height= 1, text=solo_file_name, font = "Verdana 12 bold", fg='black').pack()
        for n in range (35 * page , 35 * page + 36):
            if n < len(color_result):
                Hex = color_result[n][-7:]
                R = int(color_result[n][-6:-4] , 16)
                G = int(color_result[n][-4:-2] , 16)
                B = int(color_result[n][-2:] , 16)
                Aver = ( R + G + B ) // 3

                print( "RGB(" + R + "," + G + "," + B + ")" )              
                if Aver < 126:
                    l = Label(window, bg=Hex, height= 1, text=color_result[n], font = ("Verdana", 10), fg='white')
                else:
                    l = Label(window, bg=Hex, height= 1, text=color_result[n], font = ("Verdana", 10), fg='black')
            else:
                l = Label(window, height= 1, text="", font = ("Verdana", 10), fg='white')
                end = True
            l.pack()
        page_button_pack(end)
        p = Label(window, height= 1, text= "Page " + str(page+1), font = ("Verdana", 8))
        p.pack()
            
def prev_page():
    global page
    global end

    end = False
    
    if page > 0:
        destroy_all()
        page -= 1
        pack_button()
        Label(window, height= 1, text=solo_file_name, font = "Verdana 12 bold", fg='black').pack()
        for n in range (35 * page , 35 * page + 36):
            Hex = color_result[n][-7:]
            R = int(color_result[n][-6:-4] , 16)
            G = int(color_result[n][-4:-2] , 16)
            B = int(color_result[n][-2:] , 16)
            Aver = ( R + G + B ) // 3
            
            if Aver < 126:
                l = Label(window, bg=Hex, height= 1, text=color_result[n], font = ("Verdana", 10), fg='white')
            else:
                l = Label(window, bg=Hex, height= 1, text=color_result[n], font = ("Verdana", 10), fg='black')
            l.pack()
        page_button_pack(end)
        p = Label(window, height= 1, text= "Page " + str(page+1), font = ("Verdana", 8))
        p.pack()
        
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
    global result
    global solo_file_name
    global page
    global end

    end = False

    if global_num != 0:
        destroy_all()
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
            if n <= 35 or global_num <= 35:
                if Aver < 126:
                    l = Label(window, bg=Hex, height= 1, text=result, font = ("Verdana", 10), fg='white')
                else:
                    l = Label(window, bg=Hex, height= 1, text=result, font = ("Verdana", 10), fg='black')
                l.pack()
            color_result.append(result)

        if len(color_list) == 1 and (color_list.count("0") == 1 or color_list.count("16777215") == 1) :
            if "0" in color_list:
                window.title("That's it?This is just a black picture.")
            else:
                window.title("You choose a blank SOL file!")

        else:

            out_file = open(file_path_output, "w+")

            out_file.write(solo_file_name + "\n")
            out_file.write("Nb of Colors: " + str(len(color_list)) + "\n")
            
            for n in range(0, len(color_result)-1):
                out_file.write(color_result[n] + "\n" )

            out_file.write(color_result[len(color_result)-1])

            out_file.close()

            if len(color_list) > 35 :
                window.geometry("600x900")
                page_button_pack(end)
                p = Label(window, height= 1, text= "Page " + str(page+1), font = ("Verdana", 8))
                p.pack()
                window.title("Done! Check the txt file! Don't forget to scroll page!")
            else:
                window.geometry("600x800")
                window.title("Done! Check the txt file!")

    else:
        window.title("Are you sure this is a Coloring Widget SOL File?")

file_path = ""
global_num = 0
page = 0

window=Tk()
window.geometry("600x800")
window.title("Welcome to Coloring Widget Color Finder. Please choose a SOL File.")
window.iconbitmap("DA Pixel Maker Tool Ico.ico")
pack_button()

window.mainloop()
