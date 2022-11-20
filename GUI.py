#!/usr/bin/python3
import os
global thisdir
thisdir = os.getcwd()
homedir = os.path.expanduser(r"~")

if(os.path.isfile(thisdir+"/programstate")) == False:
    os.mknod(thisdir+"/programstate")
    os.system('python3 get-pip.py')
    os.system('pip install opencv-python')
    os.system('pip install tk')
    os.system('rm get-pip.py')
    with open (thisdir+"/programstate", "w") as f:
        f.write(homedir)
import os
import glob
import pathlib
from pathlib import Path
from tkinter.ttk import Progressbar
import tkinter
import sys
import os.path
from tkinter import *
from tkinter import filedialog
import time
from multiprocessing import Queue, Process
import queue
from decimal import Decimal, getcontext
from datetime import datetime
import shutil
import subprocess
from subprocess import Popen, PIPE
from time import sleep
from threading import *
import socket
import json
from tkinter import ttk
import ntpath
from sys import exit
import glob
import os.path
import pathlib
import cv2
import csv
main_window = Tk()

cmd = 'ls -l'


# use threading
# create listbox object

listbox = Listbox(main_window, height=7,
                  width=10,
                  bg="grey",
                  activestyle='dotbox',
                  font="Helvetica",
                  selectmode=MULTIPLE,
                  fg="blue")



# insert elements by their
# index and names.
OPTIONS = ["2X","4X","8X","Rife-2","Rife-3","Rife-4","Rife-Anime"]
listbox.insert('end', *OPTIONS)


# Insert settings menu here
def settings_window():
    global settings_window
    settings_window = Tk()
    # Dumb problems require dumb solutions
    
    button_select_default_output = Button(settings_window,
                        text = "Select default output folder",
                        command = sel_default_output_folder)
    
    button_select_default_output.grid(column=0, row=0)
    
    f = open(thisdir+"/programstate", "r")
    f = csv.reader(f)
    for row in f:
        current_default_output_folder = row
    #displays current default output folder
    global default_output_label
    default_output_label = Label(settings_window, text="Default output folder: " + current_default_output_folder[0])
    default_output_label.grid(column=0, row=1)

    settings_window.geometry("600x200")
    settings_window.title('Settings')
    settings_window.resizable(False, False) 
    settings_window.mainloop()

def sel_default_output_folder():
    global select_default_output_folder
    select_default_output_folder = filedialog.askdirectory(initialdir = fr"{homedir}",
                                          title = "Select a Folder",)
    with open(thisdir+"/programstate", "w") as f:
        f.write(select_default_output_folder)

    f = open(thisdir+"/programstate", "r")
    f = csv.reader(f)
    for row in f:
        current_default_output_folder = row
    #displays current default output folder
    default_output_label.destroy()
    default_output_label_1 = Label(settings_window, text="Default output folder: " + current_default_output_folder[0])
    default_output_label_1.grid(column=0, row=1)
    #global outputdir
    #outputdir = current_default_output_folder[0]

settings_menu_button = Button(main_window,
                        text = "x",
                        command = settings_window)
# Sets the grid location of the settings menu button                        
settings_menu_button.grid(column=2, row=0)

def show():
    # These 2 variables are the defaults, will need to remove when make default selector.
    i = 1
    p = 3
    rifever=""
    for idx in listbox.curselection():
        
        if OPTIONS[idx] == "2X":
            i = 1
        elif OPTIONS[idx] == "4X":
            i = 2
        elif OPTIONS[idx] == "8X":
            i = 3

        if OPTIONS[idx] == "Rife-2":
            p = 1
        elif OPTIONS[idx] == "Rife-3":
            p = 2
        elif OPTIONS[idx] == "Rife-4":
            p = 3
        elif OPTIONS[idx] == "Rife-Anime":
            p = 4
    
    if p == 1:
            rifever = "-m rife-v2.4"
    if p == 2:
            rifever = "-m rife-v3.1"
    if p == 3:
            rifever = "-m rife-v4.6"
    if p == 4:
            rifever = "-m rife-anime"
    if i == 1:
            on_click(rifever)
    if i == 2:
            times4(rifever)
    if i == 3:
            times8(rifever)
    


def progressBar2x():
    i = 2
    amount_of_input_files = (len([name for name in os.listdir('input_frames/') if os.path.isfile(name)]))
    amount_of_output_files = amount_of_input_files * 2
    global progressbar
    progressbar = ttk.Progressbar(main_window,orient='horizontal', length=300, mode="determinate")
    progressbar.grid(column=3, row=20)
    # Add progressbar updater
    progressbar["maximum"]=100
    while i == 2:
        frames_processed = len(list(Path('output_frames/').glob('*')))
        amount_of_output_files = len(list(Path('input_frames/').glob('*'))) * 4
        e = frames_processed/amount_of_output_files
        e*= 100
        e = int(e)
        progressbar['value'] = e * 2
        progressbar.update()
# work on this later, it will change the progressbar based on the amount of interpolation.
'''def progressBar4x(): 
    i = 2
    amount_of_input_files = (len([name for name in os.listdir('input_frames/') if os.path.isfile(name)]))
    amount_of_output_files = amount_of_input_files * 4
    global progressbar
    progressbar = ttk.Progressbar(main_window,orient='horizontal', length=300, mode="determinate")
    progressbar.grid(column=3, row=20)
    # Add progressbar updater
    progressbar["maximum"]=100
    while i == 2:
        frames_processed = len(list(Path('output_frames/').glob('*')))
        amount_of_output_files = len(list(Path('input_frames/').glob('*'))) * 4
        e = frames_processed/amount_of_output_files
        e*= 100
        e = int(e)
        progressbar['value'] = e * 2
        progressbar.update()'''

#Calls respective function
def pbthread2x():
    # Call work function
    t1 = Thread(target=progressBar2x)
    t1.start()
def threading():
    # Call work function
    t1 = Thread(target=show)
    t1.start()
    
def exit_thread():
    # Call work function
    t1 = Thread(target=exi11)
    t1.start()
#Button

def browseFiles():

    global filename
    filename = filedialog.askopenfilename(initialdir = fr"{homedir}",
                                          title = "Select a File",
                                          filetypes = (("Video Files",
                                                        ['*.mp4','*.mov','*.avi','*.mkv']),
                                                        
                                                       ("all files",
                                                        "*.*")))

    global mp4name
    mp4name = ntpath.basename(filename)
    #change label contents
    label_file_explorer.configure(text="File Opened: " + mp4name,
                                  font=("Arial", 10)
                                 )
    global extension
    extension = (pathlib.Path(f'{filename}/{mp4name}').suffix)


def output():

    global outputdir
    outputdir = filedialog.askdirectory(initialdir = fr"{homedir}",
                                          title = "Select a Folder",)
    if os.path.isfile(thisdir+"/temp") == False and isinstance(outputdir, str) == True and len(outputdir) > 2:
        os.mknod(thisdir+"/temp")
        with open(thisdir+"/temp", "w") as f:
            f.write(outputdir)

# get output dir from programstate
def get_output_dir():
    f = open(thisdir+"/programstate", "r")
    f = csv.reader(f)
    for row in f:
        outputdir = row
    outputdir = outputdir[0]
    return outputdir

def get_fps():
    if os.path.isfile(thisdir+"/temp") == False:
        outputdir = get_output_dir()
    else:
        f = open(thisdir+"/temp")
        f = csv.reader(f)
        for row in f:
            outputdir = row
        outputdir = outputdir[0]
    cap=cv2.VideoCapture(fr'{filename}')
    global fps
    fps = cap.get(cv2.CAP_PROP_FPS)
    global done
    done = Label(main_window,
                 text=f"Done! Output File = {outputdir}/{mp4name}_{fps * 2}fps{extension}",
                 font=("Arial", 11),
                 fg="green")
    global Interpolation
    Interpolation = Label(main_window,
                          text=f"Interpolation Started!",
                          font=("Arial", 11),
                          fg="yellow")
    global extraction
    extraction = Label(main_window,
                       text=f"Extracting Frames",
                       font=("Arial", 11),
                       fg="yellow")






def get_fps2():
    if os.path.isfile(thisdir+"/temp") == False:
        outputdir = get_output_dir()
    else:
        f = open(thisdir+"/temp")
        f = csv.reader(f)
        for row in f:
            outputdir = row
        outputdir = outputdir[0]
    cap=cv2.VideoCapture(fr'{thisdir}/temp.mp4')
    global fps2

    fps2 = cap.get(cv2.CAP_PROP_FPS)
    done.destroy()
    global done2
    done2 = Label(main_window,
                 text=f"Done! Output File = {outputdir}/{mp4name}_{fps * 4}fps{extension}",
                 font=("Arial", 11),
                 fg="green")
    global Interpolation2
    Interpolation2 = Label(main_window,
                           text=f"Interpolation 4X Started!",
                           font=("Arial", 11),
                           fg="yellow")
def get_fps3():
    if os.path.isfile(thisdir+"/temp") == False:
        outputdir = get_output_dir()
    else:
        f = open(thisdir+"/temp")
        f = csv.reader(f)
        for row in f:
            outputdir = row
        outputdir = outputdir[0]
    cap=cv2.VideoCapture(fr'{thisdir}/temp2.mp4')
    global fps3
    fps3 = cap.get(cv2.CAP_PROP_FPS)
    done.destroy()
    done2.destroy()
    global done3
    done3 = Label(main_window,
                 text=f"Done! Output File = {outputdir}/{mp4name}_{fps * 8}fps{extension}",
                 font=("Arial", 11),
                 fg="green")
    global Interpolation3
    Interpolation3 = Label(main_window,
                           text=f"Interpolation 8X Started!",
                           font=("Arial", 11),
                           fg="yellow")



#create label
label_file_explorer = Label(main_window,
                            text = "",
                            fg = "yellow")


rife_vulkan = Label (main_window,
                            text = "               rife-ncnn-vulkan by nihui                    "
                                                           ,
                            font=("Arial", 25),
                            fg = "blue")
button_explore = Button(main_window,
                        text = "Input Video",
                        command = browseFiles)
button_output = Button(main_window,
                        text = "Output Folder",
                        command = output)
def exi11():
    os.system('pkill -f GUI.py')

button_exit = Button(main_window,
                        text = "EXIT",
                        command = exi11,
                        justify=CENTER )


button_explore.grid(column = 3, row = 3)
button_output.grid(column = 3, row = 4)
label_file_explorer.grid(column = 3, row = 8, columnspan = 4)
button_exit.grid(column=3, row=7)
listbox.grid(column = 3, row = 6)
rife_vulkan.grid(column=3, row=0)
#rifelist.grid(column=3,row=5)



def on_click(rifever):
    
    start_button = Button(main_window, text="Start!", command=threading, state=DISABLED).grid(row = 2, column = 3)
    button_output = Button(main_window,text = "Output Folder",command = output, state=DISABLED).grid(column = 3, row = 4)
    button_explore = Button(main_window,text = "Input Video",command = browseFiles, state=DISABLED).grid(column = 3, row = 3)
    # this if statement sets default output dir, may need to remove when add selector.
    if os.path.isfile(thisdir+"/temp") == False:
        outputdir = get_output_dir()
    
    else:
        f = open(thisdir+"/temp")
        f = csv.reader(f)
        for row in f:
            outputdir = row
        outputdir = outputdir[0]
    
    #def percent_done():
        #list_of_output_files = glob.glob(f'{thisdir}/output_frames/*')  # * means all if need specific format then *.csv
        #latest_output_file = max(list_of_output_files, key=os.path.getctime)
        #list_of_input_files = glob.glob(f'{thisdir}/input_frames/*')  # * means all if need specific format then *.csv
        #latest_input_file = max(list_of_input_files, key=os.path.getctime)
        #list_of_input_files * 2
        #percent_done = (list_of_input_files/list_of_output_files)
        #print(percent_done)
    get_fps()
    os.system('rm -rf input_frames')
    os.system('rm -rf output_frames ')
    os.system('mkdir input_frames')
    os.system('mkdir output_frames')
    os.system(f'ffprobe "{filename}"')
    os.system(f'ffmpeg -i "{filename}" -vn -acodec copy audio.m4a -y')
    extraction.grid(column=3,row=9)
    os.system(f'ffmpeg -i "{filename}" input_frames/frame_%08d.png')
    extraction.after(0, extraction.destroy())
    Interpolation.grid(column=3,row=9)
    pbthread2x()        # This is temperary until i can figure out how to have progressbar update based on interpolation selected.
    
    os.system(f'./rife-ncnn-vulkan {rifever} -i input_frames -o output_frames ')
    os.system(fr'ffmpeg -framerate {fps*2} -i "{thisdir}/output_frames/%08d.png" -i audio.m4a -c:a copy -crf 20 -c:v libx264 -pix_fmt yuv420p "{outputdir}/{mp4name}_{fps*2}fps{extension}" -y')# -y overwrites the file if it exists, delete this and check if file exists. If it does, add (1) to the file.
    Interpolation.after(0, Interpolation.destroy())
    done.grid(column=3, row=9)
    start_button = Button(main_window, text="Start!", command=threading).grid(row = 2, column = 3)
    button_output = Button(main_window,text = "Output Folder",command = output).grid(column = 3, row = 4)
    button_explore = Button(main_window,text = "Input Video",command = browseFiles).grid(column = 3, row = 3)
    os.system("rm -rf "+thisdir+"/temp")



start_button = Button(main_window, text="Start!", command=threading).grid(row = 2, column = 3)




def times4(rifever):
    
    start_button = Button(main_window, text="Start!", command=threading, state=DISABLED).grid(row = 2, column = 3)
    button_output = Button(main_window,text = "Output Folder",command = output, state=DISABLED).grid(column = 3, row = 4)
    button_explore = Button(main_window,text = "Input Video",command = browseFiles, state=DISABLED).grid(column = 3, row = 3)
        # this if statement sets default output dir, may need to remove when add selector.

    # this if statement sets default output dir, may need to remove when add selector.
    if os.path.isfile(thisdir+"/temp") == False:
        outputdir = get_output_dir()
    
    else:
        f = open(thisdir+"/temp")
        f = csv.reader(f)
        for row in f:
            outputdir = row
        outputdir = outputdir[0]
    
    on_click2(rifever)

    global timestwo
    timestwo = Label(main_window,
                     font=("Arial", 11),
                     text = f"Finished 2X interpolation. Generated temp.mp4.",
                     fg="blue")
    timestwo.grid(column=3,row=9)
    get_fps2()
    os.system('rm -rf input_frames')
    os.system('rm -rf output_frames ')
    os.system('mkdir input_frames')
    os.system('mkdir output_frames')
    os.system(f'ffprobe "{thisdir}/temp.mp4"')
    os.system(f'ffmpeg -i "{thisdir}/temp.mp4" -vn -acodec copy audio.m4a -y')
    os.system(f'ffmpeg -i "{thisdir}/temp.mp4" input_frames/frame_%08d.png')
    timestwo.after(0, timestwo.destroy())
    Interpolation2.grid(column=3,row=9)
    pbthread2x()        # This is temperary until i can figure out how to have progressbar update based on interpolation selected.
    os.system(f'./rife-ncnn-vulkan {rifever} -i input_frames -o output_frames ')
    os.system(fr'ffmpeg -framerate {fps2 * 2} -i "{thisdir}/output_frames/%08d.png" -i audio.m4a -c:a copy -crf 20 -c:v libx264 -pix_fmt yuv420p "{outputdir}/{mp4name}_{fps2 * 2}fps.{extension}" -y')
    os.system(fr'rm -rf "{thisdir}/temp.mp4"')
    Interpolation2.after(0, Interpolation2.destroy())
    done2.grid(column=3, row=9)
    start_button = Button(main_window, text="Start!", command=threading).grid(row = 2, column = 3)
    button_output = Button(main_window,text = "Output Folder",command = output).grid(column = 3, row = 4)
    button_explore = Button(main_window,text = "Input Video",command = browseFiles).grid(column = 3, row = 3)
    os.system("rm -rf "+thisdir+"/temp")

def on_click2(rifever):
    get_fps()
    
    os.system('rm -rf input_frames')
    os.system('rm -rf output_frames ')
    os.system('mkdir input_frames')
    os.system('mkdir output_frames')
    os.system(f'ffprobe "{filename}"')
    os.system(f'ffmpeg -i "{filename}" -vn -acodec copy audio.m4a -y')
    extraction.grid(column=3,row=9)
    os.system(f'ffmpeg -i "{filename}" input_frames/frame_%08d.png')
    extraction.after(0, extraction.destroy())
    Interpolation.grid(column=3,row=9)
    pbthread2x()        # This is temperary until i can figure out how to have progressbar update based on interpolation selected.
    os.system(f'./rife-ncnn-vulkan {rifever} -i input_frames -o output_frames ')
    os.system(fr'ffmpeg -framerate {fps * 2} -i "{thisdir}/output_frames/%08d.png" -i audio.m4a -c:a copy -crf 20 -c:v libx264 -pix_fmt yuv420p "{thisdir}/temp.mp4" -y')
    Interpolation.destroy()

def times8(rifever):
    
    start_button = Button(main_window, text="Start!", command=threading, state=DISABLED).grid(row = 2, column = 3)
    button_output = Button(main_window,text = "Output Folder",command = output, state=DISABLED).grid(column = 3, row = 4)
    button_explore = Button(main_window,text = "Input Video",command = browseFiles, state=DISABLED).grid(column = 3, row = 3)
        # this if statement sets default output dir, may need to remove when add selector.

    # this if statement sets default output dir, may need to remove when add selector.
    if os.path.isfile(thisdir+"/temp") == False:
        outputdir = get_output_dir()
    
    else:
        f = open(thisdir+"/temp")
        f = csv.reader(f)
        for row in f:
            outputdir = row
        outputdir = outputdir[0]

    on_click2(rifever)
    on_click3(rifever)
    global timestwo2
    timestwo2 = Label(main_window,
                     font=("Arial", 11),
                     text = f"Finished 4X interpolation. Generated temp.mp4.",
                     fg="blue")
    timestwo2.grid(column=3,row=9)
    get_fps3()
    os.system('rm -rf input_frames')
    os.system('rm -rf output_frames ')
    os.system('mkdir input_frames')
    os.system('mkdir output_frames')
    os.system(f'ffprobe "{thisdir}/temp2.mp4"')
    os.system(f'ffmpeg -i "{thisdir}/temp2.mp4" -vn -acodec copy audio.m4a -y')
    timestwo2.after(0, timestwo2.destroy())
    os.system(f'ffmpeg -i "{thisdir}/temp2.mp4" input_frames/frame_%08d.png')
    Interpolation3.grid(column=3,row=9)
    pbthread2x()        # This is temperary until i can figure out how to have progressbar update based on interpolation selected.
    os.system(f'./rife-ncnn-vulkan {rifever} -i input_frames -o output_frames ')
    os.system(fr'ffmpeg -framerate {fps3 * 2} -i "{thisdir}/output_frames/%08d.png" -i audio.m4a -c:a copy -crf 20 -c:v libx264 -pix_fmt yuv420p "{outputdir}/{mp4name}_{fps3 * 2}fps.{extension}" -y')
    os.system(fr'rm -rf "{thisdir}/temp2.mp4"')
    Interpolation3.after(0, Interpolation3.destroy())
    done3.grid(column=3, row=9)
    start_button = Button(main_window, text="Start!", command=threading).grid(row = 2, column = 3)
    button_output = Button(main_window,text = "Output Folder",command = output).grid(column = 3, row = 4)
    button_explore = Button(main_window,text = "Input Video",command = browseFiles).grid(column = 3, row = 3)
    os.system("rm -rf "+thisdir+"/temp")
def on_click3(rifever):
    get_fps2()
        # this if statement sets default output dir, may need to remove when add selector.

    
    global timestwo3
    timestwo3 = Label(main_window,
                      font=("Arial", 11),
                      text=f"Finished 2X interpolation. Generated temp.mp4.",
                      fg="blue")
    timestwo3.grid(column=3, row=9)
    os.system('rm -rf input_frames')
    os.system('rm -rf output_frames ')
    os.system('mkdir input_frames')
    os.system('mkdir output_frames')
    os.system(f'ffprobe "{thisdir}/temp.mp4"')
    os.system(f'ffmpeg -i "{thisdir}/temp.mp4" -vn -acodec copy audio.m4a -y')
    os.system(f'ffmpeg -i "{thisdir}/temp.mp4" input_frames/frame_%08d.png')
    timestwo3.after(0, timestwo3.destroy())
    Interpolation2.grid(column=3, row=9)
    pbthread2x()            # This is temperary until i can figure out how to have progressbar update based on interpolation selected.
    os.system(f'./rife-ncnn-vulkan {rifever} -i input_frames -o output_frames ')
    os.system(fr'ffmpeg -framerate {fps2 * 2} -i "{thisdir}/output_frames/%08d.png" -i audio.m4a -c:a copy -crf 20 -c:v libx264 -pix_fmt yuv420p "{thisdir}/temp2.mp4" -y')
    Interpolation2.after(0, Interpolation2.destroy())
    os.system(fr'rm -rf "{thisdir}/temp.mp4"')

main_window.geometry("700x500")
main_window.title('rife-ncnn-vulkan')
main_window.resizable(False, False) 
main_window.mainloop()






