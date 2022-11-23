#!/usr/bin/python3
import os
global thisdir
thisdir = os.getcwd()
homedir = os.path.expanduser(r"~")

if(os.path.isfile(thisdir+"/programstate")) == False:
    os.mknod(thisdir+"/programstate")
    os.mknod(thisdir+"/theme")
    os.system('python3 get-pip.py')
    os.system('pip install opencv-python')
    os.system('pip install tk')
    os.system('pip install pillow')
    os.system('rm get-pip.py')
    with open (thisdir+"/programstate", "w") as f:
        f.write(homedir)
    with open(thisdir+"/theme", "w") as f:
        f.write("Light")
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
from tkinter import *
main_window = Tk()
def check_for_updates():
    os.system(f"mkdir {thisdir}/temp/")
    os.chdir(f"{thisdir}/temp/")
    os.system(f"wget https://raw.githubusercontent.com/TNTwise/Rife-Vulkan-GUI-Linux/main/GUI.py")
    os.chdir(f"{thisdir}")
    file1 = open(f"{thisdir}/temp/GUI.py")
    file2 = open(f"{thisdir}/GUI.py")
    file1_lines = file1.readlines()
    file2_lines = file2.readlines()
    for i in range(len(file1_lines)):
        if file1_lines[i] != file2_lines[i]:
            os.system(f"rm -rf {thisdir}/GUI.py")
            os.system(f"mv {thisdir}/temp/GUI.py {thisdir}/")
            os.system(f"rm -rf {thisdir}/temp/")
            return 1
    os.system(f"rm -rf {thisdir}/temp/")


def check_theme():
    # This code reads the theme file and stores its data in a theme variable
    f = open(thisdir+"/theme", "r")
    global theme
    for row in f:
        theme = row
    
    return theme
# set theme on launch, this sets bg and bg_background, this is set throughout the entire script
if check_theme() == "Light":
    main_window.config(bg="white")
    fg="black"
    bg="white"
    bg_button="white"
if check_theme() == "Dark":
    main_window.config(bg="#4C4E52")
    fg="white"
    bg="#4C4E52"
    bg_button="#4C4E52"


cmd = 'ls -l'


# use threading
# create listbox object

listbox = Listbox(main_window, height=7,
                  width=10,
                  bg="grey",
                  activestyle='dotbox',
                  font="Helvetica",
                  selectmode=MULTIPLE)



# insert elements by their
# index and names.
OPTIONS = ["2X","4X","8X","Rife-2","Rife-3","Rife-4","Rife-Anime"]
listbox.insert('end', *OPTIONS)
# Insert settings menu here


def settings_window():
    global settings_window
    settings_window = Tk()
    # sets colors for window
    if check_theme() == "Light":

        settings_window.config(bg="white")

    if check_theme() == "Dark":

        settings_window.config(bg="#4C4E52")

    button_select_default_output = Button(settings_window,
                        text = "Select default output folder",
                        command = sel_default_output_folder, bg=bg_button,fg=fg)
    
    
    
    f = open(thisdir+"/programstate", "r")
    f = csv.reader(f)
    for row in f:
        current_default_output_folder = row
    #displays current default output folder
    global default_output_label
    default_output_label = Label(settings_window, text="Default output folder: " + current_default_output_folder[0],bg=bg,fg=fg)
    # This code just creates the theme file if it doesnt txist
    if os.path.isfile(thisdir+"/theme") == False:
        os.mknod(thisdir+"/theme")
        with open(thisdir+"/theme", "w") as f:
            f.write("Light")
    # creates theme button and calls check_theme which returns the theme that is currently on
    global theme_button
    theme = check_theme()
    if theme == "Light":
            theme_button = Button(settings_window,text="Dark",command=darkTheme,bg="white",fg=fg)
    if theme == "Dark":
            theme_button = Button(settings_window,text="Light",command=lightTheme,bg=bg,fg=fg)
    theme_label = Label(settings_window,text=" Theme: ",bg=bg,fg=fg)
    spacer_label = Label(settings_window,text="            ",bg=bg)
    check_updates_button = Button(settings_window,text="Check For Updates", command=start_update_check, bg=bg,fg=fg)
     # lays out the menu
    
    spacer_label.grid(column=1,row=0)
    button_select_default_output.grid(column=0, row=0)
    default_output_label.grid(column=0, row=1)
    theme_label.grid(column=2,row=0)
    theme_button.grid(column=2, row=1)
    check_updates_button.grid(column=2,row=2)
    settings_window.geometry("600x200")
    settings_window.title('Settings')
    settings_window.resizable(False, False) 
    settings_window.mainloop()

def start_update_check():
    global update_check_label
    
    if check_for_updates() == 1:
        update_check_label = Label(settings_window,text="Updated, restart to apply.",bg=bg,fg=fg)
    if check_for_updates() != 1:
        update_check_label = Label(settings_window,text="No Updates",bg=bg,fg=fg)
    update_check_label.grid(column=2,row=3)
# restart window, this allows the program to restart after a application settings changes. call this with a message to confirm restart of program. 
def restart_window(message):
    restart_window = Tk()
    centering_label = Label(restart_window, text="                                                                         ")
    restart_label = Label(restart_window, text=message, justify=CENTER)
    restart_button = Button(restart_window, text="Exit", command=exi11,justify=CENTER)

    # lays out restart window 
    centering_label.grid(column=0,row=0)
    restart_button.grid(column=0,row=1)
    restart_label.grid(column=0,row=2)
    # sets window values
    restart_window.title("")
    restart_window.geometry("300x200")
    restart_window.resizable(False, False)
    restart_window.mainloop()
# Switches themes for tkinter

def darkTheme():
    with open(thisdir+"/theme", "w") as f:
        f.write("Dark")
    global bg
    global bg_button
    global fg
    bg="#4C4E52"
    fg="white"
    bg_button="#4C4E52"
    global theme_button
    theme_button.destroy()
    theme_button = Button(settings_window,text="Light",command=lightTheme,bg=bg,fg=fg)
    theme_button.grid(column = 1, row = 1)
    restart_window("Changing theme requires restart.")
    

def lightTheme():
    with open(thisdir+"/theme", "w") as f:
        f.write("Light")
    
    global bg
    global bg_button
    global fg
    bg="white"
    bg_button="white" 
    fg="black"
    global theme_button
    theme_button.destroy()
    theme_button = Button(settings_window,text="Dark",command=darkTheme,bg="white",fg=fg)
    theme_button.grid(column = 1, row = 1)
    restart_window("Changing theme requires restart.")
    
    
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
    
settings_icon = PhotoImage(file = thisdir+"/icons/settings_icon.png")




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
        amount_of_output_files = len(list(Path('input_frames/').glob('*'))) *2
        e = frames_processed/amount_of_output_files
        e*= 100
        e = int(e)
        progressbar['value'] = e
        progressbar.update()
def progressBar4xSecond(): # makes second progressbar in 4x
    i = 4
    amount_of_input_files_1 = (len([name for name in os.listdir('input_frames/') if os.path.isfile(name)]))
    amount_of_output_files_1 = amount_of_input_files_1 * 2
    global progressbar_1 # creates new progressbar
    progressbar_1 = ttk.Progressbar(main_window,orient='horizontal', length=300, mode="determinate", value=100)
    progressbar_1.grid(column=3, row=20)
    # Add progressbar updater
    progressbar_1["maximum"]=200
    sleep(1) # wont update unless we sleep for 1 second?????????
    while i == 4:
        
        frames_processed_1 = len(list(Path('output_frames/').glob('*')))
        amount_of_output_files_1 = len(list(Path('input_frames/').glob('*'))) *2
        e_1 = frames_processed_1/amount_of_output_files_1
        e_1*= 100
        e_1 = int(e_1) + 100 # Has to add 100 to make progress bar work
        progressbar_1['value'] = e_1
        progressbar_1.update()
            
# work on this later, it will change the progressbar based on the amount of interpolation.
def progressBar4x(): # makes first progressbar in 4x 
    
    i = 2
    
    amount_of_input_files = (len([name for name in os.listdir('input_frames/') if os.path.isfile(name)]))
    amount_of_output_files = amount_of_input_files * 2
    
    progressbar = ttk.Progressbar(main_window,orient='horizontal', length=300, mode="determinate")
    progressbar.grid(column=3, row=20)
    
    # Add progressbar updater
    progressbar["maximum"]=200
    while i == 2:
        frames_processed = len(list(Path('output_frames/').glob('*')))
        amount_of_output_files = len(list(Path('input_frames/').glob('*'))) *2
        e = frames_processed/amount_of_output_files
        e*= 100 # converts e to percentage
        e = int(e) # converts e to integer
        progressbar['value'] = e # sets the progressbar value to e
        progressbar.update()
        if os.path.isfile(thisdir+"/temp.mp4") == True:
            i = 3


def progressBar8xThird(): # this is called third, makes 3rd progressbar
    p = 5
    amount_of_input_files_5 = (len([name for name in os.listdir('input_frames/') if os.path.isfile(name)]))
    amount_of_output_files_5 = amount_of_input_files_5 * 2
    global progressbar_5 # creates new progressbar
   
    progressbar_5 = ttk.Progressbar(main_window,orient='horizontal', length=300, mode="determinate",value=180)
    progressbar_5.grid(column=3, row=20)
    progressbar_5["maximum"]=300
    # Add progressbar updater
    
    sleep(1) # wont update unless we sleep for 1 second?????????
    while p == 5:
        
        frames_processed_5 = len(list(Path('output_frames/').glob('*')))
        amount_of_output_files_5 = len(list(Path('input_frames/').glob('*'))) *2
        e_5 = frames_processed_5/amount_of_output_files_5
        e_5*= 100
        e_5 = int(e_5) + 200 # has to add 200 to the value because the progress bar only updates with the current files interpolated
        progressbar_5['value'] = e_5
        progressbar_5.update()

def progressBar8xSecond(): # calls this second, this is called by onclick3
    
    p = 4
    amount_of_input_files_2 = (len([name for name in os.listdir('input_frames/') if os.path.isfile(name)]))
    amount_of_output_files_2 = amount_of_input_files_2 * 2
    global progressbar_2 # creates new progressbar
    progressbar_2 = ttk.Progressbar(main_window,orient='horizontal', length=300, mode="determinate", value=100)
    progressbar_2.grid(column=3, row=20)
    # Add progressbar updater
    progressbar_2["maximum"]=300
    sleep(1) # wont update unless we sleep for 1 second?????????
    while p == 4:
        
        frames_processed_2 = len(list(Path('output_frames/').glob('*')))
        amount_of_output_files_2 = len(list(Path('input_frames/').glob('*'))) *2
        e_2 = frames_processed_2/amount_of_output_files_2
        e_2*= 100
        e_2 = int(e_2) + 100
        progressbar_2['value'] = e_2
        progressbar_2.update()
def progressBar8x(): # this is called first.
    i = 2
    amount_of_input_files = (len([name for name in os.listdir('input_frames/') if os.path.isfile(name)]))
    amount_of_output_files = amount_of_input_files * 2
    
    progressbar = ttk.Progressbar(main_window,orient='horizontal', length=300, mode="determinate")
    progressbar.grid(column=3, row=20)
    
    # Add progressbar updater
    progressbar["maximum"]=300
    while i == 2:
        frames_processed = len(list(Path('output_frames/').glob('*')))
        amount_of_output_files = len(list(Path('input_frames/').glob('*'))) *2
        e = frames_processed/amount_of_output_files
        e*= 100 # converts e to percentage
        e = int(e) # converts e to integer
        progressbar['value'] = e # sets the progressbar value to e
        progressbar.update()
        
    
        


#Calls respective function, creates new thread for progressbar and other things, will only execute if called.
def pbthread2x():
    # Call work function
    t1 = Thread(target=progressBar2x)
    t1.start()
def pbthread4x():
    t1 = Thread(target=progressBar4x)
    t1.start()
def pb4x2():
    t1 = Thread(target=progressBar4xSecond)
    t1.start()
def pbthread8x():
    t1 = Thread(target=progressBar8x)
    t1.start()
def pb8x2():
    t1 = Thread(target=progressBar8xSecond)
    t1.start()
def pb8x3():
    t1 = Thread(target=progressBar8xThird)
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
    global extension
    extension = (pathlib.Path(f'{filename}/{mp4name}').suffix)


def output(): # this function gets the output directory and writes outputdir to temp if the file doest exist, and if other conditions are met. 
    #This is only used if the Select Output folder is selected, otherwise it will use the default folder set in the settings menu

    global outputdir
    outputdir = filedialog.askdirectory(initialdir = fr"{homedir}",
                                          title = "Select a Folder",)
    if os.path.isfile(thisdir+"/temp") == False and isinstance(outputdir, str) == True and len(outputdir) > 0: # checks if requirements are ment to write the temp file, 
        #and if the temp file exists, the program will use the temp file for the output directory.
        os.mknod(thisdir+"/temp")
        with open(thisdir+"/temp", "w") as f:
            f.write(outputdir)

# get output dir from programstate, this will only happen if temp file doesnt exist.
def get_output_dir():
    f = open(thisdir+"/programstate", "r")
    f = csv.reader(f)
    for row in f:
        outputdir = row
    outputdir = outputdir[0]
    return outputdir
# gets fps of video, for all get_fps methods.
def get_fps():
    if os.path.isfile(thisdir+"/temp") == False: # same if statement to check what outputdir to get. Checks if temp file exists or not
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
    # putting these here so it can get referenced every time an interpolation runs.
    global Interpolation
    Interpolation = Label(main_window,
                          text=f"Interpolation Started!",
                          font=("Arial", 11),
                          fg=fg,bg=bg)
    global extraction
    extraction = Label(main_window,
                       text=f"Extracting Frames",
                       font=("Arial", 11),
                       fg=fg,bg=bg)

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
    # putting these here so it can get referenced every time an interpolation runs.
    
    global Interpolation2
    Interpolation2 = Label(main_window,
                           text=f"Interpolation 4X Started!",
                           font=("Arial", 11),
                           fg=fg,bg=bg)
    
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
    # putting these here so it can get referenced every time an interpolation runs.
    global Interpolation3
    Interpolation3 = Label(main_window,
                           text=f"Interpolation 8X Started!",
                           font=("Arial", 11),
                           fg=fg,bg=bg)
    



#create labels

rife_vulkan = Label (main_window,
                            text = "Rife Vulkan GUI"
                                                           ,
                            font=("Arial", 25),
                            bg=bg,fg=fg)
button_explore = Button(main_window,
                        text = "Input Video",
                        command = browseFiles, bg=bg_button,fg=fg)
button_output = Button(main_window,
                        text = "Output Folder",
                        command = output, bg=bg_button,fg=fg)
def exi11(): # this funtion kills the program.
    os.system('pkill -f GUI.py')

button_exit = Button(main_window,
                        text = "EXIT",
                        command = exi11,
                        justify=CENTER,bg=bg_button,fg=fg)
centering_label = Label(main_window, text="                                                                                                                                                                ",
                        bg=bg,fg=fg)
settings_menu_button = Button(main_window,
                        image=settings_icon, # sets settings icon image for button
                        command = settings_window,bg=bg_button)
start_button = Button(main_window, text="Start!", command=threading,bg=bg_button,fg=fg).grid(row = 2, column = 3)

# Sets the grid location of the settings menu button                        
settings_menu_button.grid(column=2, row=0)
centering_label.grid(column=3,row=1)

# this is where i layout the stuff on the gui
button_explore.grid(column = 3, row = 3)
button_output.grid(column = 3, row = 4)
button_exit.grid(column=3, row=7)
listbox.grid(column = 3, row = 6)
rife_vulkan.grid(column=3, row=0)
rife_vulkan.config(anchor=CENTER)
#rifelist.grid(column=3,row=5)


# different modes of interpolation
def on_click(rifever):
    global done
    done = Label(main_window,text="                                                                                                                                                                ",bg=bg)
    done.grid(column=3, row=9)
    start_button = Button(main_window, text="Start!", command=threading, state=DISABLED).grid(row = 2, column = 3)
    button_output = Button(main_window,text = "Output Folder",command = output, state=DISABLED).grid(column = 3, row = 4)
    button_explore = Button(main_window,text = "Input Video",command = browseFiles, state=DISABLED).grid(column = 3, row = 3)
    # this if statement sets default output dir, may need to remove when add selector.
    # this checks if the temp file exists, which the temp file holds the temp directory if you choose an outputdir manually.
    # This is for all modes of interpolation
    if os.path.isfile(thisdir+"/temp") == False:
        outputdir = get_output_dir()
    
    else:
        f = open(thisdir+"/temp")
        f = csv.reader(f)
        for row in f:
            outputdir = row
        outputdir = outputdir[0]
    
    # Calls get_fps function
    get_fps()
    #this runs through basic rife steps, this is straight from rife vulkan ncnn github.
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
    pbthread2x()        # progressbar is fixed, may want to make it more accurate and not just split into even secitons. 
    
    if os.path.isfile(fr"{outputdir}/{mp4name}_{fps * 2}fps{extension}") == True:
        done = Label(main_window,
                 text=f"Done! Output File = {outputdir}/{mp4name}_{fps * 2}fps(1){extension}",
                 font=("Arial", 7),
                 fg=fg,bg=bg)
    else:
        done = Label(main_window,
                 text=f"Done! Output File = {outputdir}/{mp4name}_{fps * 2}fps{extension}",
                 font=("Arial", 7),
                 fg=fg,bg=bg)
    os.system(f'./rife-ncnn-vulkan {rifever} -i input_frames -o output_frames ')
    if os.path.isfile(fr"{outputdir}/{mp4name}_{fps * 2}fps.{extension}") == True:
            os.system(fr'ffmpeg -framerate {fps * 2} -i "{thisdir}/output_frames/%08d.png" -i audio.m4a -c:a copy -crf 20 -c:v libx264 -pix_fmt yuv420p "{outputdir}/{mp4name}_{fps * 2}fps(1).{extension}" -y')
    else:
        os.system(fr'ffmpeg -framerate {fps * 2} -i "{thisdir}/output_frames/%08d.png" -i audio.m4a -c:a copy -crf 20 -c:v libx264 -pix_fmt yuv420p "{outputdir}/{mp4name}_{fps * 2}fps.{extension}" -y')
    Interpolation.after(0, Interpolation.destroy())
    done.grid(column=3, row=9)
    # these re-enable the start, input, and output buttons
    start_button = Button(main_window, text="Start!", command=threading,bg=bg,fg=fg).grid(row = 2, column = 3)
    button_output = Button(main_window,text = "Output Folder",command = output,bg=bg,fg=fg).grid(column = 3, row = 4)
    button_explore = Button(main_window,text = "Input Video",command = browseFiles,bg=bg,fg=fg).grid(column = 3, row = 3)
    os.system("rm -rf "+thisdir+"/temp") # removes the temp file, this is after every times function, not on onclick functions as they do not require the outputdir variable.







def times4(rifever):
    global done
    done = Label(main_window,text="                                                                                                                                                                ",bg=bg)
    done.grid(column=3, row=9)
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
                     fg=fg,bg=bg)
    timestwo.grid(column=3,row=9)
    get_fps2()
    os.system('rm -rf input_frames')
    os.system('rm -rf output_frames ')
    os.system('mkdir input_frames')
    os.system('mkdir output_frames')
    os.system(f'ffprobe "{thisdir}/temp.mp4"')
    os.system(f'ffmpeg -i "{thisdir}/temp.mp4" -vn -acodec copy audio.m4a -y')
    os.system(f'ffmpeg -i "{thisdir}/temp.mp4" input_frames/frame_%08d.png')
    pb4x2() # calls the second 4x progressbar, ik this is dumb, but live with it. This happens after onclick executes Should be called after the ffmpeg extracts the frames

    timestwo.after(0, timestwo.destroy())
    Interpolation2.grid(column=3,row=9)
    global done2
    if os.path.isfile(fr"{outputdir}/{mp4name}_{fps2 * 2}fps.{extension}") == True:
        done2 = Label(main_window,
                 text=f"Done! Output File = {outputdir}/{mp4name}_{fps * 4}fps(1){extension}",
                 font=("Arial", 7),
                 fg=fg,bg=bg)
    else:
        done2 = Label(main_window,
                 text=f"Done! Output File = {outputdir}/{mp4name}_{fps * 4}fps{extension}",
                 font=("Arial", 7),
                 fg=fg,bg=bg)
    
    os.system(f'./rife-ncnn-vulkan {rifever} -i input_frames -o output_frames ')
    if os.path.isfile(fr"{outputdir}/{mp4name}_{fps2 * 2}fps.{extension}") == True:
            os.system(fr'ffmpeg -framerate {fps2 * 2} -i "{thisdir}/output_frames/%08d.png" -i audio.m4a -c:a copy -crf 20 -c:v libx264 -pix_fmt yuv420p "{outputdir}/{mp4name}_{fps2 * 2}fps(1).{extension}" -y')
    else:
        os.system(fr'ffmpeg -framerate {fps2 * 2} -i "{thisdir}/output_frames/%08d.png" -i audio.m4a -c:a copy -crf 20 -c:v libx264 -pix_fmt yuv420p "{outputdir}/{mp4name}_{fps2 * 2}fps.{extension}" -y')
    os.system(fr'rm -rf "{thisdir}/temp.mp4"')
    Interpolation2.after(0, Interpolation2.destroy())
    done2.grid(column=3, row=9)# maybe change done label location in code, edit what row it shows up on
    
    start_button = Button(main_window, text="Start!", command=threading, bg=bg_button,fg=fg).grid(row = 2, column = 3)
    button_output = Button(main_window,text = "Output Folder",command = output, bg=bg_button,fg=fg).grid(column = 3, row = 4)
    button_explore = Button(main_window,text = "Input Video",command = browseFiles, bg=bg_button,fg=fg).grid(column = 3, row = 3)
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
    pbthread4x() # calls the first 4x progressbar.
            # This is temperary until i can figure out how to have progressbar update based on interpolation selected.
    os.system(f'./rife-ncnn-vulkan {rifever} -i input_frames -o output_frames ')
    os.system(fr'ffmpeg -framerate {fps * 2} -i "{thisdir}/output_frames/%08d.png" -i audio.m4a -c:a copy -crf 20 -c:v libx264 -pix_fmt yuv420p "{thisdir}/temp.mp4" -y')
    Interpolation.destroy()

def on_click2_8(rifever): # the 8x interpolation of on_click, has to set so different progress bars work. Ik i can do this better, but i dont feel like it.
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
    pbthread8x() #Set this to 8x, this is the first of 3 progressbars
    os.system(f'./rife-ncnn-vulkan {rifever} -i input_frames -o output_frames ')
    os.system(fr'ffmpeg -framerate {fps * 2} -i "{thisdir}/output_frames/%08d.png" -i audio.m4a -c:a copy -crf 20 -c:v libx264 -pix_fmt yuv420p "{thisdir}/temp.mp4" -y')
    Interpolation.destroy()

def on_click3(rifever):
    get_fps2()
        # this if statement sets default output dir, may need to remove when add selector.
    

    
    global timestwo3
    timestwo3 = Label(main_window,
                      font=("Arial", 11),
                      text=f"Finished 2X interpolation. Generated temp.mp4.",
                      fg=fg,bg=bg)
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
    pb8x2()            # This calls it for the second time, initiates second progressbar 
    os.system(f'./rife-ncnn-vulkan {rifever} -i input_frames -o output_frames ')
    os.system(fr'ffmpeg -framerate {fps2 * 2} -i "{thisdir}/output_frames/%08d.png" -i audio.m4a -c:a copy -crf 20 -c:v libx264 -pix_fmt yuv420p "{thisdir}/temp2.mp4" -y')
    Interpolation2.after(0, Interpolation2.destroy())
    os.system(fr'rm -rf "{thisdir}/temp.mp4"')

def times8(rifever):
    global done
    done = Label(main_window,text="                                                                                                                                                                ",bg=bg)
    done.grid(column=3, row=9)
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

    on_click2_8(rifever)
    on_click3(rifever)
    global timestwo2
    timestwo2 = Label(main_window,
                     font=("Arial", 11),
                     text = f"Finished 4X interpolation. Generated temp.mp4.",
                     bg=bg,
                     fg=fg)
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
    pb8x3() # should be called after ffmpeg extracts the frames

    Interpolation3.grid(column=3,row=9)
    global done3
    if os.path.isfile(fr"{outputdir}/{mp4name}_{fps2 * 2}fps.{extension}") == True:
        done3 = Label(main_window,
                 text=f"Done! Output File = {outputdir}/{mp4name}_{fps * 8}fps(1){extension}",
                 font=("Arial", 7),
                 fg=fg,bg=bg)
    else:
        done3 = Label(main_window,
                 text=f"Done! Output File = {outputdir}/{mp4name}_{fps * 8}fps{extension}",
                 font=("Arial", 7),
                 fg=fg,bg=bg)

    os.system(f'./rife-ncnn-vulkan {rifever} -i input_frames -o output_frames ')
    if os.path.isfile(fr"{outputdir}/{mp4name}_{fps3 * 2}fps.{extension}") == True:
            os.system(fr'ffmpeg -framerate {fps3 * 2} -i "{thisdir}/output_frames/%08d.png" -i audio.m4a -c:a copy -crf 20 -c:v libx264 -pix_fmt yuv420p "{outputdir}/{mp4name}_{fps3 * 2}fps(1).{extension}" -y')
    else:
        os.system(fr'ffmpeg -framerate {fps3 * 2} -i "{thisdir}/output_frames/%08d.png" -i audio.m4a -c:a copy -crf 20 -c:v libx264 -pix_fmt yuv420p "{outputdir}/{mp4name}_{fps3 * 2}fps.{extension}" -y')
    
    
    os.system(fr'rm -rf "{thisdir}/temp2.mp4"')
    Interpolation3.after(0, Interpolation3.destroy())
    done3.grid(column=3, row=9)
    start_button = Button(main_window, text="Start!", command=threading, bg=bg_button,fg=fg).grid(row = 2, column = 3)
    button_output = Button(main_window,text = "Output Folder",command = output, bg=bg_button,fg=fg).grid(column = 3, row = 4)
    button_explore = Button(main_window,text = "Input Video",command = browseFiles, bg=bg_button,fg=fg).grid(column = 3, row = 3)
    os.system("rm -rf "+thisdir+"/temp")








main_window.geometry("700x500")
main_window.title(' ')
main_window.resizable(False, False) 
main_window.mainloop()






