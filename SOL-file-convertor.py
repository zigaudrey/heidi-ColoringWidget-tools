# Dislcaimer: The script is unfinished. The byte2 is far from knowing how it work. I need some help.

import os
import struct
from tkinter import filedialog
from PIL import Image
from itertools import cycle

print("Welcome to SOL Convertor!")
print("Please choose a file")

file_path=""
file_path=filedialog.askopenfilename(initialdir=os.getcwd(), title="Select Image", filetype=(('PNG file', '*.png'),("ALL file",'*.*')))

if len(file_path) != 0:

    openpic = Image.open(file_path)
    h,w = openpic.size

    if 545 < w and w < 565 and 545 < h and h < 565:
        
        if len(file_path) != 0:
            n=len(file_path)-1
            solo_file_name = ""
            while n!= 0 and file_path[n] != '/':
                solo_file_name = file_path[n] + solo_file_name
                n -= 1
            out_folder_path = file_path[:len(file_path) - len(solo_file_name)]

            sol_size=bytearray(4)
            byte2=bytearray(2) # Not find yet
            
            sol_header = b'\x00\xBF' + sol_size + b'TCSO\x00\x04' + bytearray(5) +  b'\x0EColoringWidget' + bytearray(3) + b'\x03\x09grid\x06' + byte2
            sol_body= bytearray()

            picture_color = []

            for y in range(1,12):
                for x in range (1,12):
                    red , green, blue = openpic.getpixel((x*45,y*45))
                    DecColor = (red * 256 * 256) + (green * 256) + blue
                    picture_color.append(str(DecColor))
            
            for i in range(len(picture_color)):
                sol_body += picture_color[i].encode("utf-8")
                if i != len(picture_color)-1:
                    sol_body += b','

            sol_body += b'\x00'

            sol_size= struct.pack(">L", len(sol_header) - 6 +len(sol_body)) ## Size of SOL File starting at TCSO

            sol_header = sol_header[:2] + sol_size + sol_header[6:]

            new_folder_path = out_folder_path + "NewColoringWidget" + solo_file_name[:-4] + ".sol"
                
            new_sol_file = sol_header + sol_body

            if picture_color.count("0") == 121 or picture_color.count("16777215") == 121 :
                if "0" in picture_color:
                    print("This is easy to achieve! No need to create a SOL file!")
                else:
                    print("Just click the Clear button in the App and you got it!")

            else:
                out_file = open(new_folder_path, "wb+")
                out_file.write(new_sol_file)
                out_file.close()
                print("SOL File has been created! Check the file!")

    else:
        window.title("Picture should be around 550 x 550.")
        
else:
    window.title("There is nothing to convert!")
