#!/usr/bin/python3
# have to edit GUI.py for everything to update
import os 
global thisdir
thisdir = os.getcwd()
homedir = os.path.expanduser(r"~")
if os.path.exists(f"{thisdir}/files/") == False:
    os.mkdir(f"{thisdir}/files/")
if os.path.isfile(f"{thisdir}/files/isInstalled") == False:
    os.mknod(f"{thisdir}/files/isInstalled")
    with open(f"{thisdir}/files/isInstalled", "w") as f:
        f.write("False")
if(os.path.isfile(thisdir+"/programstate")) == False:
    os.chdir(f"{thisdir}/files")
    os.system("wget https://bootstrap.pypa.io/get-pip.py")
    os.chdir(f"{thisdir}")
    os.mknod(thisdir+"/programstate")
    os.system('python3 files/get-pip.py install')
    os.system('python3 -m pip install opencv-python')
    os.system('python3 -m pip install tk')
    os.system('python3 -m pip install requests')
    os.system('rm files/get-pip.py')
    with open (thisdir+"/programstate", "w") as f:
        f.write(homedir)
if os.path.isfile(f'{thisdir}/Start') == False:
    os.system(f"wget https://raw.githubusercontent.com/TNTwise/Rife-Vulkan-GUI-Linux/main/Start")
    
if(os.path.isfile(thisdir+"/theme")) == False:
    os.mknod(thisdir+"/theme")
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
from functools import partial
import getpass
import requests
import re
from zipfile import ZipFile
def check_theme():
    
    # This code reads the theme file and stores its data in a theme variable
    f = open(thisdir+"/theme", "r")
    global theme
    for row in f:
        theme = row
    return theme
filename = ""
main_window = Tk()
tabControl = ttk.Notebook(main_window)
if check_theme() == "Light":
    tab1 = ttk.Frame(tabControl)
    tab2 = ttk.Frame(tabControl)
    tab3 = ttk.Frame(tabControl)
    s = ttk.Style()
# Create style used by default for all Frames
    s.configure('TFrame', background='White')

# Create style for the first frame
    s.configure('Frame1.TFrame', background='White', foreground='Black')
if check_theme() == "Dark":
    tab1 = ttk.Frame(tabControl)
    tab2 = ttk.Frame(tabControl)
    tab3 = ttk.Frame(tabControl)
    s = ttk.Style()
# Create style used by default for all Frames
    s.configure('TFrame', background='#4C4E52',foreground='#4C4E52')

# Create style for the first frame
    s.configure('Frame1.TFrame', background='red')
#Create tabs
tabControl.add(tab1, text='Rife')
tabControl.add(tab2, text='Real-ESRGAN')

tabControl.add(tab3, text='Settings')
tabControl.grid(row=0,column=0)
if check_theme() == "Light":
    main_window.config(bg="white")
    
    fg="black"
    bg="White"
    bg_button="white"
if check_theme() == "Dark":
    main_window.config(bg="#4C4E52")
    
    fg="white"
    
    bg_button="#4C4E52"

if os.path.isfile(f"{thisdir}/files/videoQuality") == False:
    os.mknod(f"{thisdir}/files/videoQuality")
    with open(f"{thisdir}/files/videoQuality", 'w') as f:
        f.write("9")

f = open(thisdir+"/programstate", "r")
f = csv.reader(f)
for row in f:
    current_default_output_folder = row
if os.path.exists(current_default_output_folder[0]) == False:
    with open(thisdir+"/programstate", 'w') as f:
        f.write(homedir)
with open(f"{thisdir}/files/isAnime", 'w') as f:
                    f.write("False")
def getVidQuality():
    with open(f"{thisdir}/files/videoQuality", 'r') as f:
            f = csv.reader(f)
            for row in f:
                vidQuality = row

    vidQuality = vidQuality[0]
    return vidQuality

def latest():
    # this code gets the latest versaion of rife vulkan
            

            latest = requests.get('https://github.com/nihui/rife-ncnn-vulkan/releases/latest/') 
            latest = latest.url
            latest = re.findall(r'[\d]*$', latest)
            latest = latest[0]
            if os.path.isfile(f"{thisdir}/files/version") == False:
                os.mknod(f"{thisdir}/files/version")
                with open(f'{thisdir}/files/version', 'w') as f:
                    f.write("20220728")
                current = "20220728"
            else:
                f = open(f"{thisdir}/files/version")
                f = csv.reader(f)
                for row in f:
                    current = row
                current = current[0]
                with open(f"{thisdir}/files/version", 'w') as f:
                    f.write(latest)
            return(latest,current)
# this checks for updates
# it makes a temp folder, and gets the latest GUI.py from github
# It compares the files, and if the files are different, replaces the old GUI.py with the one from github
# Ive changed it to the Stable branch which created, this helps prevent unintended bugs from getting in the updates 
def check_for_updates():
    is_updated = 0
    os.system(f'mkdir "{thisdir}/temp/"')
    os.chdir(f"{thisdir}/temp/")
    
    with open(f"{thisdir}/files/repository", 'r') as f:
        f = csv.reader(f)
        for row in f:
            repo = row
    repo = repo[0]
    if repo =="Stable":
        os.system(f"wget https://raw.githubusercontent.com/TNTwise/Rife-Vulkan-GUI-Linux/Stable/GUI.py")
        os.system(f"wget https://raw.githubusercontent.com/TNTwise/Rife-Vulkan-GUI-Linux/Stable/files/start.py")
        os.system(f"wget https://raw.githubusercontent.com/TNTwise/Rife-Vulkan-GUI-Linux/Stable/Start")
    if repo =="Testing":
        os.system(f"wget https://raw.githubusercontent.com/TNTwise/Rife-Vulkan-GUI-Linux/main/GUI.py")
        os.system(f"wget https://raw.githubusercontent.com/TNTwise/Rife-Vulkan-GUI-Linux/main/files/start.py")
        os.system(f"wget https://raw.githubusercontent.com/TNTwise/Rife-Vulkan-GUI-Linux/main/Start")
        os.chdir(f"{thisdir}")
    file1 = open(f"{thisdir}/temp/GUI.py")
    file2 = open(f"{thisdir}/GUI.py")
    file1_lines = file1.readlines()
    file2_lines = file2.readlines()
    version = latest() # calls latest function which gets the latest version release of rife and returns the latest and the current, if the version file doesnt exist, it updates and creates the file
    latest_ver = version[0]
    current = version[1]
    
    if len(file1_lines) != len(file2_lines):
            is_updated = 1
            os.system(f'rm -rf "{thisdir}/GUI.py"')
            os.system(f'mv "{thisdir}/temp/GUI.py" "{thisdir}/"')
            os.system(f'rm -rf "{thisdir}/start.py"')
            os.system(f'mv "{thisdir}/temp/start.py" "{thisdir}/files/"')
            os.system(f'rm -rf "{thisdir}/Start"')
            os.system(f'mv "{thisdir}/temp/Start" "{thisdir}/"')
            os.system(f'chmod +x "{thisdir}/Start"')
            os.system(f'rm -rf "{thisdir}/temp/"')
            
    os.system(f'rm -rf "{thisdir}/temp/"')
            
    
        
            
    if latest_ver > current:
                is_updated = 1
                os.chdir(f"{thisdir}/files/")
                os.system(f"wget https://github.com/nihui/rife-ncnn-vulkan/releases/download/{latest_ver}/rife-ncnn-vulkan-{latest_ver}-ubuntu.zip")
                with ZipFile(f'rife-ncnn-vulkan-{latest_ver}-ubuntu.zip','r') as f:
                    f.extractall()
                os.chdir(f"{thisdir}")
                os.system(f'rm -rf "{thisdir}/files/rife-ncnn-vulkan"')
                os.system(f'mv "{thisdir}/rife-ncnn-vulkan-{latest_ver}-ubuntu" "{thisdir}/files/"')
                os.system(f'mv "{thisdir}/files/rife-ncnn-vulkan-{latest_ver}-ubuntu/"* "{thisdir}/rife-vulkan-models/"')
                os.system(f'chmod +x "{thisdir}/files/rife-ncnn-vulkan"')
                with open(f"{thisdir}/files/version", 'w') as f:
                    f.write(latest_ver)
                os.system(f'rm -rf "{thisdir}/files/rife-ncnn-vulkan-{latest_ver}-ubuntu.zip"')
                os.system(f'rm -rf "{thisdir}/files/rife-ncnn-vulkan-{latest_ver}-ubuntu"')

    if is_updated == 1:
        return 1
    else:
        return

def get_all_models():
    if os.path.exists(f"{thisdir}/rife-vulkan-models/") == False:
        os.mkdir(f"{thisdir}/rife-vulkan-models/")
    if os.path.exists(f"{thisdir}/rife-vulkan-models/rife-HD/") != True:
        version = latest() # calls latest function which gets the latest version release of rife and returns the latest and the current, if the version file doesnt exist, it updates and creates the file
        latest_ver = version[0]
        os.chdir(f"{thisdir}/files/")
        os.system(f"wget https://github.com/nihui/rife-ncnn-vulkan/releases/download/{latest_ver}/rife-ncnn-vulkan-{latest_ver}-ubuntu.zip")
        with ZipFile(f'rife-ncnn-vulkan-{latest_ver}-ubuntu.zip','r') as f:
            f.extractall()
        os.chdir(f"{thisdir}")
        os.system(f'rm -rf "{thisdir}/rife-ncnn-vulkan"')
        os.system(f'mv "{thisdir}/rife-ncnn-vulkan-{latest_ver}-ubuntu" "{thisdir}/files/"')
        os.system(f'mv "{thisdir}/files/rife-ncnn-vulkan-{latest_ver}-ubuntu/"* "{thisdir}/rife-vulkan-models/"')
        with open(f"{thisdir}/files/version", 'w') as f:
            f.write(latest_ver)
        os.system(f'rm -rf "{thisdir}/files/rife-ncnn-vulkan-{latest_ver}-ubuntu.zip"')
        os.system(f'rm -rf "{thisdir}/files/rife-ncnn-vulkan-{latest_ver}-ubuntu"')
        os.system(f'chmod +x "{thisdir}/rife-vulkan-models/rife-ncnn-vulkan"')
                
    os.system(f'rm -rf "{thisdir}/temp/"')
get_all_models()


    
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

def pass_dialog_box():
    
    global pass_window
    pass_window = Tk()
    global pass_box
    pass_box = Entry(pass_window, width = 25,show='*')
    pass_label = Label(pass_window, text="Enter your password:")
    pass_button = Button(pass_window, text="Enter",command=install)

    pass_label.grid(column=0,row=0)
    pass_box.grid(column=0,row=1)
    pass_button.grid(column=0,row=2)
    pass_window.geometry("200x100")
    pass_window.resizable(False, False)
    
    pass_window.mainloop()

def pass_dialog_box_err():
    global pass_window1
    pass_window1 = Tk()
    global pass_box1
    pass_box1 = Entry(pass_window1, width = 25,show='*')
    pass_label1 = Label(pass_window1, text="Enter your password:")
    pass_button1 = Button(pass_window1, text="Enter",command=install1)
    err_lbl = Label(pass_window1, text="Wrong password", fg="red")
    pass_label1.grid(column=0,row=0)
    pass_box1.grid(column=0,row=1)
    pass_button1.grid(column=0,row=2)
    err_lbl.grid(column=0,row=3)
    pass_window1.geometry("200x100")
    pass_window1.resizable(False, False)
    
def install():
    with open(f"{thisdir}/files/isInstalled", "w") as f:
        f.write("False")
    passwd = pass_box.get()
    pass_window.destroy()
    
    p = subprocess.Popen((f'echo {passwd} | sudo -S cp "{thisdir}/install/rife-gui" /usr/bin/rife-gui'),shell=TRUE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, error = p.communicate()
    os.system(f'echo {passwd} | sudo -S cp "{thisdir}/icons/Icon.svg" /usr/share/icons/hicolor/scalable/apps/Rife.svg')
    if str(error) != f"b'[sudo] password for {getpass.getuser()}: '":# Add different pop up window here and in other install function that says it completed successfully
        pass_dialog_box_err()
    else:
        os.system(f"echo {passwd} | sudo -S chmod +x /usr/bin/rife-gui")
        passwd=""
        with open(f"{thisdir}/files/isInstalled", "w") as f:
            f.write("True")
        os.system(f'cp "{thisdir}/install/Rife-Vulkan-GUI.desktop" /home/$USER/.local/share/applications/')
        os.system("mkdir /home/$USER/Rife-Vulkan-GUI")
        os.system(f"echo {passwd} | sudo -S rm -rf {thisdir}/.git/")
        os.system(f"cp -r * /home/$USER/Rife-Vulkan-GUI")
        os.chdir(f"{thisdir}")
        
def install1():
    with open(f"{thisdir}/files/isInstalled", "w") as f:
        f.write("False")
    passwd = pass_box1.get()
    pass_window1.destroy()
    os.system(f'chmod +x "{thisdir}/install/rife-gui"')
    p = subprocess.Popen((f'echo {passwd} | sudo -S cp "{thisdir}/install/rife-gui" /usr/bin/rife-gui'),shell=TRUE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, error = p.communicate()
    os.system(f'echo {passwd} | sudo -S cp "{thisdir}/icons/Icon.svg" /usr/share/icons/hicolor/scalable/apps/Rife.svg')
    if str(error) != f"b'[sudo] password for {getpass.getuser()}: '":
        pass_dialog_box_err()
    else:
        os.system(f"echo {passwd} | sudo -S chmod +x /usr/bin/rife-gui")
        passwd=""
        with open(f"{thisdir}/files/isInstalled", "w") as f:
            f.write("True")
        os.system(f'cp "{thisdir}/install/Rife-Vulkan-GUI.desktop" /home/$USER/.local/share/applications/')
        os.system("mkdir /home/$USER/Rife-Vulkan-GUI")
        os.system(f"echo {passwd} | sudo -S rm -rf {thisdir}/.git/")
        os.system(f"cp -r * /home/$USER/Rife-Vulkan-GUI")
        os.chdir(f"{thisdir}")
    
# use threading
# create listbox object

listbox = Listbox(tab1, height=7,
                  width=10,
                  bg="grey",
                  activestyle='dotbox',
                  font="Helvetica",
                  selectmode=MULTIPLE)



# insert elements by their
# index and names.

# Insert settings menu here


def settings_window():
    
    
    button_select_default_output = Button(tab3,
                        text = "Select default output folder",
                        command = sel_default_output_folder, bg=bg_button,fg=fg)
    
    # just writes 'stable' to file repository to be able to change where the program is taken from
    if os.path.isfile(f"{thisdir}/files/repository") == False:
        os.mknod(f"{thisdir}/files/repository")
        with open(f"{thisdir}/files/repository", "w") as f:
            f.write("stable")
    
    f = open(thisdir+"/programstate", "r")
    f = csv.reader(f)
    for row in f:
        current_default_output_folder = row
    #displays current default output folder
    
    global default_output_label
    default_output_label = Label(tab3, text=current_default_output_folder[0],bg=bg,fg=fg, width=25, anchor="w")
    # This code just creates the theme file if it doesnt txist
    if os.path.isfile(thisdir+"/theme") == False:
        os.mknod(thisdir+"/theme")
        with open(thisdir+"/theme", "w") as f:
            f.write("Light")
    # creates theme button and calls check_theme which returns the theme that is currently on
    global repo
    with open(f"{thisdir}/files/repository", 'r') as f: # gets the repo stored in repository file
        f = csv.reader(f)
        for row in f:
            repo = row
    repo = repo[0]
    if repo == "stable": # capitolizes repo first char
        repo = "Stable"
    if repo == "testing":
        repo = "Testing"
    global theme_button
    theme = check_theme()
    if theme == "Light":
            theme_button = Button(tab3,text="Light",command=darkTheme,bg="white",fg=fg)
    if theme == "Dark":
            theme_button = Button(tab3,text="Dark",command=lightTheme,bg=bg,fg=fg)
    theme_label = Label(tab3,text=" Theme: ",bg=bg,fg=fg)
    spacer_label = Label(tab3,text="            ",bg=bg) # This spaces the middle
    spacer_label1 = Label(tab3,text="            ",bg=bg) # this spaces the end
    spacer_label2 = Label(tab3,text="",bg=bg) # this is at the start of the gui
    global check_updates_button
    check_updates_button = Button(tab3,text="Check For Updates", command=start_update_check_thread, bg=bg,fg=fg)
    install_button = Button(tab3, text="Install", command=pass_dialog_box,bg=bg,fg=fg)
    global  update_spacer_label
    update_spacer_label = Label(tab3,text = " ", bg=bg)
    
    def show_dropdown():
        update_branch_label = Label(tab3,text="Update channel:",bg=bg,fg=fg)
        
        variable = StringVar(tab3)
        repo_options = ['Testing', 'Stable']
        variable.set(repo)
        opt = OptionMenu(tab3, variable, *repo_options)
        opt.config(width=9, font=('Helvetica', 12))
        opt.config(bg=bg)
        opt.config(fg=fg)
        update_branch_label.grid(column=6,row=0)
        opt.grid(column=6,row=1)
        def callback(*args):
            with open(f"{thisdir}/files/repository", 'w') as f: # gets the repo stored in repository file
                f.write(variable.get())
                
        variable.trace("w", callback)

    with open(f"{thisdir}/files/isInstalled", "r") as f:
        f = csv.reader(f)
        for row in f:
            is_installed = row
    is_installed = is_installed[0]
    show_dropdown()
    def video_quality_drop_down():
        vid_quality_label = Label(tab3,text="Video quality:", bg=bg,fg=fg).grid(column=1,row=2)
        vidQuality = getVidQuality()
        if vidQuality == "25":
            vidQuality1 = "Low"
        if vidQuality == "20":
            vidQuality1 = "Medium"
        if vidQuality == "13":
            vidQuality1 = "High"
        if vidQuality == "3":
            vidQuality1 = "Lossless"
        variable = StringVar(tab3)
        repo_options = ['Lossless','High', 'Medium', 'Low']
        variable.set(vidQuality1)
        opt = OptionMenu(tab3, variable, *repo_options)
        opt.config(width=9, font=('Helvetica', 12))
        opt.config(bg=bg)
        opt.config(fg=fg)
        
        opt.grid(column=1,row=3)
        def callback(*args):
            with open(f"{thisdir}/files/videoQuality", 'w') as f: # gets the repo stored in repository file
                # Converts these to cfv format
                if variable.get() == "Low":
                    f.write("22")
                if variable.get() == "Medium":
                    f.write("18")
                if variable.get() == "High":
                    f.write("9")
                if variable.get() == "Lossless":
                    f.write("3")
                
        variable.trace("w", callback)
    video_quality_drop_down()
    with open(f"{thisdir}/files/isInstalled", "r") as f:
        f = csv.reader(f)
        for row in f:
            is_installed = row
     # lays out the menu
    spacer_label2.grid(column=0,row=0)
    spacer_label2.config(padx=30)
    button_select_default_output.grid(column=1, row=0)
    default_output_label.grid(column=1, row=1)
    if os.path.exists(f"{homedir}/Rife-Vulkan-GUI/") == False:
        is_installed = False
    else:
        is_installed = True
    if is_installed == False:
        install_button.grid(column=4,row=4)
    spacer_label.grid(column=2,row=0)
    theme_label.grid(column=4,row=0)
    theme_button.grid(column=4, row=1)
    spacer_label1.grid(column=5,row=0)
    check_updates_button.grid(column=6,row=3)
    update_spacer_label.grid(column=6,row=2)
    #change_repo_dropdown.grid(column=5,row=2)



# this will show if updates exist
def start_update_check():
    global update_check_label
    if check_for_updates() == 1:
        update_check_label = Label(tab3,text="Updated, restart to apply.",bg=bg,fg=fg)
        check_updates_button = Button(tab3,text="Check For Updates", command=start_update_check_thread, bg=bg,fg=fg).grid(column=5,row=3)
        restart_window("Updated, re-launch the program to apply.")
    else:
        update_check_label = Label(tab3,text="No Updates",bg=bg,fg=fg)
        check_updates_button = Button(tab3,text="Check For Updates", command=start_update_check_thread, bg=bg,fg=fg).grid(column=5,row=3)
    update_check_label.grid(column=5,row=5)
# restarts the program


def restart():
    os.system("pkill -f GUI.py && python3 start.py")
def restart_thread():
    t1 = Thread(target=restart_window)
    t1.start()



# restart window, this allows the program to restart after a application settings changes. call this with a message to confirm restart of program.   
def restart_window(message):
    restart_window = Tk()
    centering_label = Label(restart_window, text="                                                                         ")
    restart_label = Label(restart_window, text=message, justify=CENTER)
    exit_button = Button(restart_window, text="Exit", command=exi11,justify=CENTER)
    #restart_button = Button(restart_window, text="Restart", command=restart_thread,justify=CENTER)
    # lays out restart window 
    centering_label.grid(column=0,row=0)
    #restart_button.grid(column=0,row=1)
    exit_button.grid(column=0,row=1)
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
    theme_button = Button(tab3,text="Dark",command=lightTheme,bg=bg,fg=fg)
    theme_button.grid(column = 3, row = 1)
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
    theme_button = Button(tab3,text="Light",command=darkTheme,bg="white",fg=fg)
    theme_button.grid(column = 3, row = 1)
    restart_window("Changing theme requires restart.")
    
    
def sel_default_output_folder():
    global select_default_output_folder
    select_default_output_folder = filedialog.askdirectory(initialdir = fr"{homedir}",
                                          title = "Select a Folder",)
    if isinstance(select_default_output_folder, str) == True and len(select_default_output_folder) > 0:
        with open(thisdir+"/programstate", "w") as f:
            f.write(select_default_output_folder)

    f = open(thisdir+"/programstate", "r")
    f = csv.reader(f)
    for row in f:
        current_default_output_folder = row
    #displays current default output folder
    default_output_label.destroy()
    default_output_label_1 = Label(tab3, text=current_default_output_folder[0],bg=bg,fg=fg, width=25, anchor="w")
    default_output_label_1.grid(column=1, row=1)
    



def show(program):
    # These 2 variables are the defaults, will need to remove when make default selector.
    if program == "rife":
        rifever = ""
    
        if os.path.isfile(f"{thisdir}/files/temp_interp_opt") == True:
            with open(f"{thisdir}/files/temp_interp_opt" , 'r') as f:
                f = csv.reader(f)
                for row in f:
                    interpolation_option = row
            interpolation_option = interpolation_option[0]
        if os.path.isfile(f"{thisdir}/files/temp_rife_ver") == False:
            rifever1 = "4.6"
        else: 
            with open(f"{thisdir}/files/temp_rife_ver" , 'r') as f:
                f = csv.reader(f)
                for row in f:
                    rifever1 = row
            rifever1 = rifever1[0]
        if os.path.isfile(f"{thisdir}/files/isAnime") == False: # temp solution to not selecting anime after interpolating video.
                os.mknod(f"{thisdir}/files/isAnime")
        with open(f"{thisdir}/files/isAnime", 'r') as f:
            f = csv.reader(f)
            for row in f:
                isAnime = row
        isAnime = isAnime[0]
    #print(isAnime + "\n\n\n\n\n\n")
    #print(rifever1)

    #print(rifever1)
        if isAnime != "True":
            if rifever1 == "Rife":
                rifever = "-m rife"
            if rifever1 == "HD":
                rifever = "-m rife-HD"
            if rifever1 == "UHD":
                rifever = "-m rife-UHD"
            if rifever1 == "2.0":
                rifever = "-m rife-v2"
            if rifever1 == "2.3":
                rifever = "-m rife-v2.3"
            if rifever1 == "3.0":
                rifever = "-m rife-v3.0"
            if rifever1 == "4.0":
                rifever = "-m rife-v4"
            if rifever1 == "2.4":
                rifever = "-m rife-v2.4"
            if rifever1 == "3.1":
                rifever = "-m rife-v3.1"
            if rifever1 == "4.6":
                rifever = "-m rife-v4.6"
            if rifever1 == "Anime":
                rifever = "-m rife-anime"
            if interpolation_option == "2X":
                on_click(rifever)
            if interpolation_option == "4X":
                times4(rifever)
            if interpolation_option == "8X":
                times8(rifever)
        else:
            AnimeInterpolation()

# This code allows for the dropdown selector for the rife versions and interpolation option.  
# This was a very desprate debugging technique i used, apologize for the mess.
# The solution was me not being an idiot
def show_interp_opt():
    if os.path.isfile(f"{thisdir}/files/temp_interp_opt") == False: 
       os.mknod(f"{thisdir}/files/temp_interp_opt")
    with open(f"{thisdir}/files/temp_interp_opt", 'w') as f: # gets the repo stored in repository file
        f.write("2X")
    global iterp_opt_variable
    iterp_opt_variable = StringVar(tab1)
    interpolation_options = ['2X', '4X', '8X']
    iterp_opt_variable.set('2X')
    global interpOptDropDown
    interpOptDropDown = OptionMenu(tab1, iterp_opt_variable, *interpolation_options)
    interpOptDropDown.config(width=2, font=('Helvetica', 12))
    interpOptDropDown.config(bg=bg)
    interpOptDropDown.config(fg=fg)
    interpOptDropDown.grid(column=4,row=6)
    if os.path.isfile(f"{thisdir}/files/temp_interp_opt") == False: 
            os.mknod(f"{thisdir}/files/temp_interp_opt")
    def callback(*args):
        if os.path.isfile(f"{thisdir}/files/temp_interp_opt") == False: 
            os.mknod(f"{thisdir}/files/temp_interp_opt")
        with open(f"{thisdir}/files/temp_interp_opt", 'w') as f: # gets the repo stored in repository file
            f.write(iterp_opt_variable.get())
                
    iterp_opt_variable.trace("w", callback)
show_interp_opt()

def show_rife_ver():
    if os.path.isfile(f"{thisdir}/files/temp_rife_ver") == False: 
       os.mknod(f"{thisdir}/files/temp_rife_ver")
    with open(f"{thisdir}/files/temp_rife_ver", 'w') as f: # gets the repo stored in repository file
        f.write("2.3")
    global rife_ver_variable
    rife_ver_variable = StringVar(tab1)
    interpolation_options = ['Rife', 'Rife-HD','Rife-UHD','Rife Anime','Rife 2.0','Rife 2.3', 'Rife 2.4','Rife 3.0', 'Rife 3.1','Rife 4.0', 'Rife 4.6']
    rife_ver_variable.set('Rife 2.3')
    global rifeVerDropDown
    rifeVerDropDown = OptionMenu(tab1, rife_ver_variable, *interpolation_options)
    rifeVerDropDown.config(width=10, font=('Helvetica', 12))
    rifeVerDropDown.config(bg=bg)
    rifeVerDropDown.config(fg=fg)
    rifeVerDropDown.grid(column=4,row=7)
    
    def callback(*args):
        if os.path.isfile(f"{thisdir}/files/temp_rife_ver") == False: 
            os.mknod(f"{thisdir}/files/temp_rife_ver")
        with open(f"{thisdir}/files/temp_rife_ver", 'w') as f: # gets the repo stored in repository file
            if rife_ver_variable.get() == "Rife":
                f.write("Rife")
            if rife_ver_variable.get() == "Rife-HD":
                f.write("HD")
            if rife_ver_variable.get() == "Rife Anime":
                f.write("Anime")
            if rife_ver_variable.get() == "Rife-UHD":
                f.write("UHD")
            if rife_ver_variable.get() == "Rife 4.0":
                f.write("4.0")
            if rife_ver_variable.get() == "Rife 3.0":
                f.write("3.0")
            if rife_ver_variable.get() == "Rife 2.0":
                f.write("2.0")
            if rife_ver_variable.get() == "Rife 2.3":
                f.write("2.3")
            if rife_ver_variable.get() == "Rife 2.4":
                f.write("2.4")
            if rife_ver_variable.get() == "Rife 3.1":
                f.write("3.1")
            if rife_ver_variable.get() == "Rife 4.6":
                f.write("4.6")
                
    rife_ver_variable.trace("w", callback)
show_rife_ver()

# The 8x and 4x progressbars are split into sections
# The 2x portion of the 4x takes up 1/3 of the progressbar, while the 4x takes up the rest 2/3s.
# the 8x portion is split into 7ths.
# the 2x portion is 0/7 - 1/7
# The 4x portion is 1/7-3/7
# the 8x protion is 3/7-7/7
def progressBar2x():
    i = 2
    amount_of_input_files = (len([name for name in os.listdir('input_frames/') if os.path.isfile(name)]))
    amount_of_output_files = amount_of_input_files * 2
    global progressbar
    progressbar = ttk.Progressbar(tab1,orient='horizontal', length=500, mode="determinate")
    progressbar.grid(column=4, row=22)
    # Add progressbar updater
    progressbar["maximum"]=100
    while i == 2:
        frames_processed = len(list(Path('output_frames/').glob('*')))
        amount_of_output_files = len(list(Path('input_frames/').glob('*'))) * 2
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
    progressbar_1 = ttk.Progressbar(tab1,orient='horizontal', length=500, mode="determinate",value=50,maximum=150)
    progressbar_1.grid(column=4, row=22)
    # Add progressbar updater
    #sleep(1) # wont update unless we sleep for 1 second?????????
    while i == 4:
        
        frames_processed_1 = len(list(Path('output_frames/').glob('*')))
        amount_of_output_files_1 = len(list(Path('input_frames/').glob('*'))) *2
        e_1 = frames_processed_1/amount_of_output_files_1
        e_1*= 100
        e_1 = int(e_1) + 50 # Has to add 50 to make progress bar save state from other end
        progressbar_1['value'] = e_1
        progressbar_1.update()
        if progressbar_1['value'] == 150:
            progressbar_1 = ttk.Progressbar(tab1,orient='horizontal', length=500, mode="determinate",value=150,maximum=150)
            progressbar_1.grid(column=4, row=22)
            break
            
# work on this later, it will change the progressbar based on the amount of interpolation.
def progressBar4x(): # makes first progressbar in 4x 
    
    i = 2
    
    amount_of_input_files = (len([name for name in os.listdir('input_frames/') if os.path.isfile(name)]))
    amount_of_output_files = amount_of_input_files * 2
    
    progressbar = ttk.Progressbar(tab1,orient='horizontal', length=500, mode="determinate",maximum=300)
    progressbar.grid(column=4, row=22)
    sleep(1) # Helps progressbar be more consistant
    # Add progressbar updater
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
   
    progressbar_5 = ttk.Progressbar(tab1,orient='horizontal', length=500, mode="determinate",value=73,maximum=170)
    
    progressbar_5.grid(column=4, row=22)
    progressbar_5.update()
    # Add progressbar updater
    #sleep(1) # wont update unless we sleep for 1 second?????????
    while p == 5:
        
        frames_processed_5 = len(list(Path('output_frames/').glob('*')))
        amount_of_output_files_5 = len(list(Path('input_frames/').glob('*'))) *2
        e_5 = frames_processed_5/amount_of_output_files_5
        e_5*= 100
        e_5 = int(e_5) + 73 # has to add 43 to the value because the progress bar only updates with the current files interpolated
        progressbar_5['value'] = e_5
        progressbar_5.update()
        if progressbar_5['value'] == 170:
            progressbar_5 = ttk.Progressbar(tab1,orient='horizontal', length=500, mode="determinate",value=700,maximum=700)
            progressbar_5.grid(column=4, row=22)
            break

def progressBar8xSecond(): # calls this second, this is called by onclick3
    
    p = 4
    amount_of_input_files_2 = (len([name for name in os.listdir('input_frames/') if os.path.isfile(name)]))
    amount_of_output_files_2 = amount_of_input_files_2 * 2
    global progressbar_2 # creates new progressbar
    progressbar_2 = ttk.Progressbar(tab1,orient='horizontal', length=500, mode="determinate", value=43, maximum=300)
    progressbar_2.grid(column=4, row=22)
    # Add progressbar updater
    #progressbar_2["maximum"]= 800
    #sleep(1) # wont update unless we sleep for 1 second?????????
    while p == 4:
        if int(progressbar_2['value']) == 128:
            
            progressbar_2 = ttk.Progressbar(tab1,orient='horizontal', length=500, mode="determinate",value=128,maximum=300)
            progressbar_2.grid(column=4, row=22)
            break
        frames_processed_2 = len(list(Path('output_frames/').glob('*')))
        amount_of_output_files_2 = len(list(Path('input_frames/').glob('*'))) *2
        e_2 = frames_processed_2/amount_of_output_files_2
        e_2*= 100 
        e_2 = int(e_2) +43
        e_2 = e_2 * 0.9
        progressbar_2['value'] = e_2 # this times it by .9 so that the progressbar goes up to 3/7 of 300 which is 128.7
        progressbar_2.update()
        
        
def progressBar8x(): # this is called first.
    i = 2
    amount_of_input_files = (len([name for name in os.listdir('input_frames/') if os.path.isfile(name)]))
    amount_of_output_files = amount_of_input_files * 2
    
    progressbar = ttk.Progressbar(tab1,orient='horizontal', length=500, mode="determinate",maximum=700)
    progressbar.grid(column=4, row=22)
    sleep(1) #Helps keep consistancy.
    # Add progressbar updater
    while i == 2: # all this adds up to 100, i change the maximum so that it will even out the progressbar for different rendering times.
        frames_processed = len(list(Path('output_frames/').glob('*')))
        amount_of_output_files = len(list(Path('input_frames/').glob('*'))) *2
        e = frames_processed/amount_of_output_files
        e*= 100 # converts e to percentage
        e = int(e) # converts e to integer
        progressbar['value'] = e # sets the progressbar value to e
        progressbar.update()
        if progressbar['value'] == 100:
            progressbar = ttk.Progressbar(tab1,orient='horizontal', length=500, mode="determinate",value=100,maximum=700)
            progressbar.grid(column=4, row=22)
            break
        

# anime progress bars
def Anime8xPb4():
    i = 2
    amount_of_input_files = (len([name for name in os.listdir('input_frames/') if os.path.isfile(name)]))
    amount_of_output_files = amount_of_input_files * 2
    
    progressbar = ttk.Progressbar(tab1,orient='horizontal', length=500, mode="determinate",value=300,maximum=400)
    progressbar.grid(column=4, row=22)
    
    # Add progressbar updater
    while i == 2: # all this adds up to 100, i change the maximum so that it will even out the progressbar for different rendering times.
        frames_processed = len(list(Path('output_frames/').glob('*')))
        amount_of_output_files = len(list(Path('input_frames/').glob('*'))) *2
        e = frames_processed/amount_of_output_files
        e*= 100 # converts e to percentage
        e = int(e) + 300 # converts e to integer
        progressbar['value'] = e # sets the progressbar value to e
        progressbar.update()
        if progressbar['value'] == 399:
            progressbar = ttk.Progressbar(tab1,orient='horizontal', length=500, mode="determinate",value=400,maximum=400)
            progressbar.grid(column=4, row=22)
            break
def Anime8xPb3():# called 3nd 8x
    i = 2
    amount_of_input_files = (len([name for name in os.listdir('input_frames/') if os.path.isfile(name)]))
    amount_of_output_files = amount_of_input_files * 2
    
    progressbar = ttk.Progressbar(tab1,orient='horizontal', length=500, mode="determinate",value=200,maximum=400)
    progressbar.grid(column=4, row=22)
    
    # Add progressbar updater
    while i == 2: # all this adds up to 100, i change the maximum so that it will even out the progressbar for different rendering times.
        frames_processed = len(list(Path('output_frames/').glob('*')))
        amount_of_output_files = len(list(Path('input_frames/').glob('*'))) *2
        e = frames_processed/amount_of_output_files
        e*= 100 # converts e to percentage
        e = int(e) + 200 # converts e to integer
        progressbar['value'] = e # sets the progressbar value to e
        progressbar.update()
        if progressbar['value'] == 299:
            progressbar = ttk.Progressbar(tab1,orient='horizontal', length=500, mode="determinate",value=300,maximum=400)
            progressbar.grid(column=4, row=22)
            break
def Anime8xPb2():# called 2nd 8x
    i = 2
    amount_of_input_files = (len([name for name in os.listdir('input_frames/') if os.path.isfile(name)]))
    amount_of_output_files = amount_of_input_files * 2
    
    progressbar = ttk.Progressbar(tab1,orient='horizontal', length=500, mode="determinate",value=200,maximum=400)
    progressbar.grid(column=4, row=22)
    
    # Add progressbar updater
    while i == 2: # all this adds up to 100, i change the maximum so that it will even out the progressbar for different rendering times.
        frames_processed = len(list(Path('output_frames/').glob('*')))
        amount_of_output_files = len(list(Path('input_frames/').glob('*'))) *2
        e = frames_processed/amount_of_output_files
        e*= 100 # converts e to percentage
        e = int(e) + 100 # converts e to integer
        progressbar['value'] = e # sets the progressbar value to e
        progressbar.update()
        if progressbar['value'] == 199:
            progressbar = ttk.Progressbar(tab1,orient='horizontal', length=500, mode="determinate",value=200,maximum=400)
            progressbar.grid(column=4, row=22)
            break
def Anime8xPb1(): # called first 8x
    i = 2
    amount_of_input_files = (len([name for name in os.listdir('input_frames/') if os.path.isfile(name)]))
    amount_of_output_files = amount_of_input_files * 2
    
    progressbar = ttk.Progressbar(tab1,orient='horizontal', length=500, mode="determinate",maximum=400)
    progressbar.grid(column=4, row=22)
    
    # Add progressbar updater
    sleep(1)
    while i == 2: # all this adds up to 100, i change the maximum so that it will even out the progressbar for different rendering times.
        frames_processed = len(list(Path('output_frames/').glob('*')))
        amount_of_output_files = len(list(Path('input_frames/').glob('*'))) *2
        e = frames_processed/amount_of_output_files
        e*= 100 # converts e to percentage
        e = int(e) # converts e to integer
        progressbar['value'] = e # sets the progressbar value to e
        progressbar.update()
        if progressbar['value'] == 99:
            
            progressbar = ttk.Progressbar(tab1,orient='horizontal', length=500, mode="determinate",value=100,maximum=400)
            progressbar.grid(column=4, row=22)
            break
def Anime16xPb1(): # called first 16x

    i = 2
    amount_of_input_files = (len([name for name in os.listdir('input_frames/') if os.path.isfile(name)]))
    amount_of_output_files = amount_of_input_files * 2
    
    progressbar = ttk.Progressbar(tab1,orient='horizontal', length=500, mode="determinate",maximum=600)
    progressbar.grid(column=4, row=22)
    sleep(1)
    # Add progressbar updater
    while i == 2: # all this adds up to 100, i change the maximum so that it will even out the progressbar for different rendering times.
        frames_processed = len(list(Path('output_frames/').glob('*')))
        amount_of_output_files = len(list(Path('input_frames/').glob('*'))) *2
        e = frames_processed/amount_of_output_files
        e*= 100 # converts e to percentage
        e = int(e) # converts e to integer
        progressbar['value'] = e # sets the progressbar value to e
        progressbar.update()
        if progressbar['value'] == 99:
            
            progressbar = ttk.Progressbar(tab1,orient='horizontal', length=500, mode="determinate",value=100,maximum=600)
            progressbar.grid(column=4, row=22)
            break
def Anime16xPb2(): # called first 16x
    i = 2
    amount_of_input_files = (len([name for name in os.listdir('input_frames/') if os.path.isfile(name)]))
    amount_of_output_files = amount_of_input_files * 2
    
    progressbar = ttk.Progressbar(tab1,orient='horizontal', length=500, mode="determinate",maximum=600)
    progressbar.grid(column=4, row=22)
    
    # Add progressbar updater
    while i == 2: # all this adds up to 100, i change the maximum so that it will even out the progressbar for different rendering times.
        frames_processed = len(list(Path('output_frames/').glob('*')))
        amount_of_output_files = len(list(Path('input_frames/').glob('*'))) *2
        e = frames_processed/amount_of_output_files
        e*= 100 # converts e to percentage
        e = int(e) + 100 # converts e to integer
        progressbar['value'] = e # sets the progressbar value to e
        progressbar.update()
        if progressbar['value'] == 199:
            
            progressbar = ttk.Progressbar(tab1,orient='horizontal', length=500, mode="determinate",value=200,maximum=600)
            progressbar.grid(column=4, row=22)
            break
def Anime16xPb3(): # called first 16x
    i = 2
    amount_of_input_files = (len([name for name in os.listdir('input_frames/') if os.path.isfile(name)]))
    amount_of_output_files = amount_of_input_files * 2
    
    progressbar = ttk.Progressbar(tab1,orient='horizontal', length=500, mode="determinate",maximum=600)
    progressbar.grid(column=4, row=22)
    
    # Add progressbar updater
    while i == 2: # all this adds up to 100, i change the maximum so that it will even out the progressbar for different rendering times.
        frames_processed = len(list(Path('output_frames/').glob('*')))
        amount_of_output_files = len(list(Path('input_frames/').glob('*'))) *2
        e = frames_processed/amount_of_output_files
        e*= 100 # converts e to percentage
        e = int(e) + 200 # converts e to integer
        progressbar['value'] = e # sets the progressbar value to e
        progressbar.update()
        if progressbar['value'] == 299:
            
            progressbar = ttk.Progressbar(tab1,orient='horizontal', length=500, mode="determinate",value=300,maximum=600)
            progressbar.grid(column=4, row=22)
            break
def Anime16xPb4(): # called first 16x
    i = 2
    amount_of_input_files = (len([name for name in os.listdir('input_frames/') if os.path.isfile(name)]))
    amount_of_output_files = amount_of_input_files * 2
    
    progressbar = ttk.Progressbar(tab1,orient='horizontal', length=500, mode="determinate",maximum=600)
    progressbar.grid(column=4, row=22)
    
    # Add progressbar updater
    while i == 2: # all this adds up to 100, i change the maximum so that it will even out the progressbar for different rendering times.
        frames_processed = len(list(Path('output_frames/').glob('*')))
        amount_of_output_files = len(list(Path('input_frames/').glob('*'))) *2
        e = frames_processed/amount_of_output_files
        e*= 100 # converts e to percentage
        e = int(e) + 300 # converts e to integer
        progressbar['value'] = e # sets the progressbar value to e
        progressbar.update()
        if progressbar['value'] == 399:
            
            progressbar = ttk.Progressbar(tab1,orient='horizontal', length=500, mode="determinate",value=400,maximum=600)
            progressbar.grid(column=4, row=22)
            break
def Anime16xPb5(): # called first 16x
    i = 2
    amount_of_input_files = (len([name for name in os.listdir('input_frames/') if os.path.isfile(name)]))
    amount_of_output_files = amount_of_input_files * 2
    
    progressbar = ttk.Progressbar(tab1,orient='horizontal', length=500, mode="determinate",maximum=600)
    progressbar.grid(column=4, row=22)
    
    # Add progressbar updater
    while i == 2: # all this adds up to 100, i change the maximum so that it will even out the progressbar for different rendering times.
        frames_processed = len(list(Path('output_frames/').glob('*')))
        amount_of_output_files = len(list(Path('input_frames/').glob('*'))) *2
        e = frames_processed/amount_of_output_files
        e*= 100 # converts e to percentage
        e = int(e) + 400 # converts e to integer
        progressbar['value'] = e # sets the progressbar value to e
        progressbar.update()
        if progressbar['value'] == 499:
            
            progressbar = ttk.Progressbar(tab1,orient='horizontal', length=500, mode="determinate",value=500,maximum=600)
            progressbar.grid(column=4, row=22)
            break
def Anime16xPb6(): # called first 16x
    i = 2
    amount_of_input_files = (len([name for name in os.listdir('input_frames/') if os.path.isfile(name)]))
    amount_of_output_files = amount_of_input_files * 2
    
    progressbar = ttk.Progressbar(tab1,orient='horizontal', length=500, mode="determinate",maximum=600)
    progressbar.grid(column=4, row=22)
    
    # Add progressbar updater
    while i == 2: # all this adds up to 100, i change the maximum so that it will even out the progressbar for different rendering times.
        frames_processed = len(list(Path('output_frames/').glob('*')))
        amount_of_output_files = len(list(Path('input_frames/').glob('*'))) *2
        e = frames_processed/amount_of_output_files
        e*= 100 # converts e to percentage
        e = int(e) + 500# converts e to integer
        progressbar['value'] = e # sets the progressbar value to e
        progressbar.update()
        if progressbar['value'] == 599:
            
            progressbar = ttk.Progressbar(tab1,orient='horizontal', length=500, mode="determinate",value=600,maximum=600)
            progressbar.grid(column=4, row=22)
            break

#Calls respective function, creates new thread for progressbar and other things, will only execute if called.
def Anime16xPb1Thread():
    t1 = Thread(target=Anime16xPb1)
    t1.start()
def Anime16xPb2Thread():
    t1 = Thread(target=Anime16xPb2)
    t1.start()
def Anime16xPb3Thread():
    t1 = Thread(target=Anime16xPb3)
    t1.start()
def Anime16xPb4Thread():
    t1 = Thread(target=Anime16xPb4)
    t1.start()
def Anime16xPb5Thread():
    t1 = Thread(target=Anime16xPb5)
    t1.start()
def Anime16xPb6Thread():
    t1 = Thread(target=Anime16xPb6)
    t1.start()




def Anime8xPb1Thread():
    # Call work function
    t1 = Thread(target=Anime8xPb1)
    t1.start()
def Anime8xPb2Thread():
    # Call work function
    t1 = Thread(target=Anime8xPb2)
    t1.start()
def Anime8xPb3Thread():
    # Call work function
    t1 = Thread(target=Anime8xPb3)
    t1.start()
def Anime8xPb4Thread():
    # Call work function
    t1 = Thread(target=Anime8xPb4)
    t1.start()
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
def threading(program):
    # Call work function
    t1 = Thread(target=lambda: show(program))
    t1.start()
def start_update_check_thread():
    t1 = Thread(target=start_update_check)
    t1.start()
    check_updates_button = Button(tab3,text="Check For Updates", command=start_update_check_thread, bg=bg,fg=fg, state=DISABLED).grid(column=5,row=3)
def anime_thread():
    t1 = Thread(target=AnimeInterpolation)
    t1.start()

def exit_thread():
    # Call work function
    t1 = Thread(target=exi11)
    t1.start()
#Button
settings_window()
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
    Interpolation = Label(tab1,
                          text=f"Interpolation Started!",
                          font=("Arial", 11),
                          fg=fg,bg=bg)
    global extraction
    extraction = Label(tab1,
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
    Interpolation2 = Label(tab1,
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
    Interpolation3 = Label(tab1,
                           text=f"Interpolation 8X Started!",
                           font=("Arial", 11),
                           fg=fg,bg=bg)
    

#def show_term():
#    termf = Frame(tab1, height=100, width=500)
#
#    termf.grid(column=4,row=10)
#    wid = termf.winfo_id()
#    os.system('xterm -into %d -geometry 80x10 -sb &' % wid)
#show_term()
#create labels
def Anime():
    #if os.path.isfile(f"{thisdir}/files/isAnime") == False: 
    #   os.mknod(f"{thisdir}/files/isAnime")
    #with open(f"{thisdir}/files/isAnime", 'w') as f: # gets the repo stored in repository file
    #    f.write("Default")
    variable2 = StringVar(tab1)
    video_options = ['Default', 'Animation (Uneven Framerate)']
    variable2.set('Default')
    opt1 = OptionMenu(tab1, variable2, *video_options)
    opt1.config(width=30, font=('Helvetica', 12))
    opt1.config(bg=bg)
    opt1.config(fg=fg)
    opt1.grid(column=4,row=8)
    #if os.path.isfile(f"{thisdir}/files/isAnime") == False: 
    #        os.mknod(f"{thisdir}/files/isAnime")
    def callback(*args):
        #print(variable2.get())
        if variable2.get() == 'Default':
            start_button = Button(tab1, text="Start!", command=lambda: threading('rife'),bg=bg_button,fg=fg,width=10,height=4).grid(row = 22, column = 0)
            # UNGREY inter_opt and rive_ver buttons
            rifeVerDropDown.config(state="normal")
            global iterp_opt_variable2
            iterp_opt_variable2 = StringVar(tab1)
            interpolation_options = ['2X','4X', '8X']
            interpOptDropDown2 = OptionMenu(tab1, iterp_opt_variable2, *interpolation_options)
            interpOptDropDown2.config(width=2, font=('Helvetica', 12))
            iterp_opt_variable2.set('2X')
            interpOptDropDown2.config(bg=bg)
            interpOptDropDown2.config(fg=fg)
            with open(f"{thisdir}/files/temp_interp_opt", 'w') as f: # gets the repo stored in repository file
                    f.write("2X")
            with open(f"{thisdir}/files/isAnime", 'w') as f:
                    f.write("False")
            interpOptDropDown2.grid(column=4,row=6)
            if os.path.isfile(f"{thisdir}/files/temp_interp_opt") == False: 
                os.mknod(f"{thisdir}/files/temp_interp_opt")
            def callback(*args):
                if os.path.isfile(f"{thisdir}/files/temp_interp_opt") == False: 
                    os.mknod(f"{thisdir}/files/temp_interp_opt")
                with open(f"{thisdir}/files/temp_interp_opt", 'w') as f: # gets the repo stored in repository file
                    f.write(iterp_opt_variable2.get())

                
                
                if os.path.isfile(f"{thisdir}/files/isAnime") == False: # temp solution to not selecting anime after interpolating video.
                    os.mknod(f"{thisdir}/files/isAnime")
                with open(f"{thisdir}/files/isAnime", 'w') as f:
                    f.write("False")
            iterp_opt_variable2.trace("w", callback)
        else:
            Button(tab1, text="Start!", command=anime_thread,bg=bg_button,fg=fg,width=10,height=4).grid(row = 22, column = 0)
            # Grey out inter_opt and rive_ver buttons
            rife_ver_variable.set("Rife 2.3")
            
            #interpOptDropDown.config(state=DISABLED)
            rifeVerDropDown.config(state=DISABLED)
            if os.path.isfile(f"{thisdir}/files/isAnime") == False: # temp solution to not selecting anime after interpolating video.
                os.mknod(f"{thisdir}/files/isAnime")
            with open(f"{thisdir}/files/isAnime", 'w') as f:
                f.write("True")
            global iterp_opt_variable1
            iterp_opt_variable1 = StringVar(tab1)
            interpolation_options = ['4X', '8X', '16X']
            iterp_opt_variable1.set('4X')
            interpOptDropDown1 = OptionMenu(tab1, iterp_opt_variable1, *interpolation_options)
            interpOptDropDown1.config(width=2, font=('Helvetica', 12))
            interpOptDropDown1.config(bg=bg)
            interpOptDropDown1.config(fg=fg)
            interpOptDropDown1.grid(column=4,row=6)
            with open(f"{thisdir}/files/temp_interp_opt", 'w') as f: # gets the repo stored in repository file
                    f.write("4X")
            if os.path.isfile(f"{thisdir}/files/temp_interp_opt") == False: 
                os.mknod(f"{thisdir}/files/temp_interp_opt")
            def callback(*args):
                if os.path.isfile(f"{thisdir}/files/temp_interp_opt") == False: 
                    os.mknod(f"{thisdir}/files/temp_interp_opt")
                with open(f"{thisdir}/files/temp_interp_opt", 'w') as f: # gets the repo stored in repository file
                    f.write(iterp_opt_variable1.get())
            iterp_opt_variable1.trace("w", callback)
    variable2.trace("w", callback)

Anime()
rife_vulkan = Label (tab1,
                            text = "Rife Vulkan"
                                                           ,
                            font=("Arial", 23),
                            bg=bg,fg=fg,padx='0')# adjust this padx
button_explore = Button(tab1,
                        text = "Input Video",
                        command = browseFiles, bg=bg_button,fg=fg)
button_output = Button(tab1,
                        text = "Output Folder",
                        command = output, bg=bg_button,fg=fg)
def exi11(): # this funtion kills the program.
    os.system('pkill -f GUI.py')

button_exit = Button(tab1,
                        text = "EXIT",
                        command = exi11,
                        justify=CENTER,bg=bg_button,fg=fg)
                                                                                                                                                     
settings_menu_button = Label(tab1,padx='500',bg=bg,fg=fg)
start_button = Button(tab1, text="Start!", command=lambda: threading('rife'),bg=bg_button,fg=fg,width=9,height=4).grid(row = 22, column = 0)

# Last column is 22
spacer= Label(tab1, padx='0',
                 fg=fg,bg=bg)
spacer.grid(column=4, row=10)
progressbar = ttk.Progressbar(tab1,orient='horizontal', length=500, mode="determinate",maximum=700)
progressbar.grid(column=4, row=22)
# Sets the grid location of the settings menu button                        
settings_menu_button.grid(column=5, row=0)
# Sets start button away from everything else
start_button_spacer = Label(tab1,pady=55,bg=bg,fg=fg).grid(column=0,row=21)# Adjust this padY for start button.
# this is where i layout the stuff on the gui
button_explore.grid(column = 4, row = 3)
button_output.grid(column = 4, row = 4)
button_exit.grid(column=4,row=9)
rife_vulkan.grid(column=4, row=0)
def AnimeInterpolation():
    with open(f"{thisdir}/files/temp_interp_opt", 'r') as f:
        f = csv.reader(f)
        for row in f:
            interp_opt = row
    interp_opt = interp_opt[0]
    if interp_opt == "4X":
        anime4X(False,False)

    if interp_opt == "8X":
        anime8X(False)
    if interp_opt == "16X":
        anime4X(True, False)
        
def anime4X(is16x, is8x): 
    if is8x == True and is16x == False:
        X4_loop = 2
    if is8x == False and is16x == False:
        X4_loop = 1
    if is8x == False and is16x == True:
        X4_loop = 3
    for i in range(X4_loop): # loops through it twice for 8x, 3 times for 16x
        vidQuality = getVidQuality()
        os.chdir("rife-vulkan-models")
        global done
        
        start_button = Button(tab1, text="Start!", command=lambda: threading('rife'),bg=bg_button,fg=fg,width=10,height=4, state=DISABLED).grid(row = 22, column = 0)
        button_output = Button(tab1,text = "Output Folder",command = output, state=DISABLED,bg=bg,fg=fg).grid(column = 4, row = 4)
        button_explore = Button(tab1,text = "Input Video",command = browseFiles, state=DISABLED,bg=bg,fg=fg).grid(column = 4, row = 3)
        # this if statement sets default output dir, may need to remove when add selector.

        if os.path.isfile(thisdir+"/temp") == False:
            outputdir = get_output_dir()
    
        else:
            f = open(thisdir+"/temp")
            f = csv.reader(f)
            for row in f:
                outputdir = row
            outputdir = outputdir[0]
        if os.path.exists(outputdir) == False:
            outputdir = homedir
        if i == 0:
            on_click2_anime(i,is16x, False)
        if i == 1 and is16x == False:
            on_click2_anime(i,is16x, True)
        if i == 1 and is16x == True:
            on_click2_anime(i,is16x, False)
        if i == 2:
            on_click2_anime(i,is16x, True)
        
        os.system(f'ffmpeg -i {thisdir}/temp1.mp4  -vf mpdecimate,fps=30 -vsync vfr -vcodec libx264 -preset veryslow -qp 0 -profile:v high444 -crf 0 -c:a copy {thisdir}/temp.mp4 -y')
        os.chdir(f"{thisdir}")
        os.system('rm temp1.mp4')
        os.chdir("rife-vulkan-models")
        global timestwo
        timestwo = Label(tab1,
                     font=("Arial", 11),
                     text = f"Finished 2X interpolation. Generated temp.mp4.",
                     fg=fg,bg=bg)
        timestwo.grid(column=4,row=10)
        get_fps2()
        os.system('rm -rf input_frames')
        os.system('rm -rf output_frames ')
        os.system('mkdir input_frames')
        os.system('mkdir output_frames')
        os.system(f'ffprobe "{thisdir}/temp.mp4"')
    
        os.system(f'ffmpeg -i "{thisdir}/temp.mp4" input_frames/frame_%08d.png')
        if is16x == True and is8x == False:
            if i == 0:
                Anime16xPb2Thread()
            if i == 1:
                Anime16xPb4Thread()
            if i == 2:
                Anime16xPb6Thread()
            
        if is8x == True and is16x == False:
            if i == 0:
                Anime8xPb2Thread()
            if i == 1:
                Anime8xPb4Thread()
        if is8x == False and is16x == False:
                pb4x2()
            
        timestwo.after(0, timestwo.destroy())
        Interpolation2.grid(column=4,row=10)
        global done2
        if os.path.isfile(fr"{outputdir}/{mp4name}_{fps2 * 2}fps{extension}") == True:
            done2 = Label(tab1,
                 text=f"Done! Output File = {outputdir}/{mp4name}_60fps(1){extension}",
                 font=("Arial", 11), width=57, anchor="w",
                 fg=fg,bg=bg)
        else:
            done2 = Label(tab1,
                 text=f"Done! Output File = {outputdir}/{mp4name}_60fps{extension}",
                 font=("Arial", 11), width=57, anchor="w",
                 fg=fg,bg=bg)
    
        os.system(f'./rife-ncnn-vulkan -i input_frames -o output_frames ')
        if is16x == False and is8x == False:# Exports video based on interpolation option
            if os.path.isfile(fr"{outputdir}/{mp4name}_60fps.{extension}") == True:
                os.system(fr'ffmpeg -framerate 60 -i "{thisdir}/rife-vulkan-models/output_frames/%08d.png" -i "{thisdir}/rife-vulkan-models/audio.m4a"  -crf {vidQuality} -c:a copy  "{outputdir}/{mp4name}_60fps(1){extension}" -y')
            else:
                os.system(fr'ffmpeg -framerate 60 -i "{thisdir}/rife-vulkan-models/output_frames/%08d.png" -i "{thisdir}/rife-vulkan-models/audio.m4a"  -crf {vidQuality} -c:a copy "{outputdir}/{mp4name}_60fps{extension}" -y')
            os.system(fr'rm -rf "{thisdir}/temp.mp4"')
        if is8x == True and is16x == False:
            if i == 0:
                os.system(fr'ffmpeg -framerate 60 -i "{thisdir}/rife-vulkan-models/output_frames/%08d.png" -i "{thisdir}/rife-vulkan-models/audio.m4a" -vcodec copy -crf 0 -c:a copy "{thisdir}/temp.mp4" -y')
            else:
                os.system(fr'ffmpeg -framerate 60 -i "{thisdir}/rife-vulkan-models/output_frames/%08d.png" -i "{thisdir}/rife-vulkan-models/audio.m4a"  -crf {vidQuality} -c:a copy "{outputdir}/{mp4name}_60fps{extension}" -y')
        if is16x == True and is8x == False:
            if i != 2:
                os.system(fr'ffmpeg -framerate 60 -i "{thisdir}/rife-vulkan-models/output_frames/%08d.png" -i "{thisdir}/rife-vulkan-models/audio.m4a" -vcodec copy -crf 0 -c:a copy "{thisdir}/temp.mp4" -y')
                
            else:
                os.system(fr'ffmpeg -framerate 60 -i "{thisdir}/rife-vulkan-models/output_frames/%08d.png" -i "{thisdir}/rife-vulkan-models/audio.m4a"  -crf {vidQuality} -c:a copy "{outputdir}/{mp4name}_60fps{extension}" -y')
                os.system(fr'rm -rf "{thisdir}/temp.mp4"')
        Interpolation2.after(0, Interpolation2.destroy())
        done2.grid(column=4,row=10)# maybe change done label location in code, edit what row it shows up on
    
        start_button = Button(tab1, text="Start!", command=lambda: threading('rife'),bg=bg_button,fg=fg,width=10,height=4).grid(row = 22, column = 0)
        button_output = Button(tab1,text = "Output Folder",command = output, bg=bg_button,fg=fg).grid(column = 4, row = 4)
        button_explore = Button(tab1,text = "Input Video",command = browseFiles, bg=bg_button,fg=fg).grid(column = 4, row = 3)
        os.system('rm -rf input_frames')
        os.system('rm -rf output_frames ')    
        os.chdir(f"{thisdir}")
        
    if is16x == False and is8x == False:
            os.system('rm -rf "'+thisdir+'/temp"')
            os.chdir(f"{thisdir}")
            os.system('rm temp*')
            os.chdir("rife-vulkan-models")
    os.chdir(f"{thisdir}")
    if i == X4_loop - 1:
        os.system('rm temp*')
def anime8X(is16x):
        if is16x == False:
            anime4X(False,True)# this sets is8x to true, which loops the program twice for 8x.
        else:
            anime4X(True,False) # sets 8x and 16x to true, for looping
            

# different modes of interpolation
def on_click(rifever):
    vidQuality = getVidQuality()
    if filename != "":
        os.chdir("rife-vulkan-models")
        global done
        #done = Label(tab1,text="                                                                                                                                                                ",bg=bg)
        #done.grid(column=4, row=10)
        start_button = Button(tab1, text="Start!", command=anime_thread,bg=bg_button,fg=fg,width=10,height=4, state=DISABLED).grid(row = 22, column = 0)
        button_output = Button(tab1,text = "Output Folder",command = output, state=DISABLED,bg=bg,fg=fg).grid(column = 4, row = 4)
        button_explore = Button(tab1,text = "Input Video",command = browseFiles, state=DISABLED,bg=bg,fg=fg).grid(column = 4, row = 3)
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
        extraction.grid(column=4,row=10)
        os.system(f'ffmpeg -i "{filename}" input_frames/frame_%08d.png')
        extraction.after(0, extraction.destroy())
        Interpolation.grid(column=4,row=10)
        pbthread2x()        # progressbar is fixed, may want to make it more accurate and not just split into even secitons. 
        if os.path.exists(outputdir) == False:
            outputdir = homedir
        if os.path.isfile(fr"{outputdir}/{mp4name}_{fps * 2}fps{extension}") == True:
            done = Label(tab1,
                 text=f"Done! Output File = {outputdir}/{mp4name}_{int(fps * 2)}fps(1){extension}",
                 font=("Arial", 11), width=57, anchor="w",
                 fg=fg,bg=bg)
        else:
           done = Label(tab1,
                 text=f"Done! Output File = {outputdir}/{mp4name}_{int(fps * 2)}fps{extension}",
                 font=("Arial", 11), width=57, anchor="w",
                 fg=fg,bg=bg)
        os.system(f'./rife-ncnn-vulkan {rifever} -i input_frames -o output_frames ')
        if os.path.isfile(fr"{outputdir}/{mp4name}_{fps * 2}fps.{extension}") == True:
            os.system(fr'ffmpeg -framerate {fps * 2} -i "{thisdir}/rife-vulkan-models/output_frames/%08d.png" -i {thisdir}/rife-vulkan-models/audio.m4a -c:a copy -crf {vidQuality} -c:v libx264 -preset slow -pix_fmt yuv420p "{outputdir}/{mp4name}_{int(fps * 2)}fps(1).{extension}" -y')
        else:
            os.system(fr'ffmpeg -framerate {fps * 2} -i "{thisdir}/rife-vulkan-models/output_frames/%08d.png" -i {thisdir}/rife-vulkan-models/audio.m4a -c:a copy -crf {vidQuality} -c:v libx264 -preset slow -pix_fmt yuv420p "{outputdir}/{mp4name}_{int(fps * 2)}fps.{extension}" -y')
        Interpolation.after(0, Interpolation.destroy())
        done.grid(column=4,row=10)
        # these re-enable the start, input, and output buttons
        start_button = Button(tab1, text="Start!", command=lambda: threading('rife'),bg=bg_button,fg=fg,width=10,height=4).grid(row = 22, column = 0)
        button_output = Button(tab1,text = "Output Folder",command = output,bg=bg,fg=fg).grid(column = 4, row = 4)
        button_explore = Button(tab1,text = "Input Video",command = browseFiles,bg=bg,fg=fg).grid(column = 4, row = 3)
        os.system('rm -rf "'+thisdir+'/temp"') # removes the temp file, this is after every times function, not on onclick functions as they do not require the outputdir variable.
        os.system('rm -rf input_frames')
        os.system('rm -rf output_frames ')
        os.chdir(f"{thisdir}")






def times4(rifever):
    os.chdir("rife-vulkan-models")
    global done
    #done = Label(tab1,text="                                                                                                                                                                ",bg=bg)
    #done.grid(column=4,row=10)
    start_button = Button(tab1, text="Start!", command=lambda: threading('rife'),bg=bg_button,fg=fg,width=10,height=4, state=DISABLED).grid(row = 22, column = 0)
    button_output = Button(tab1,text = "Output Folder",command = output, state=DISABLED,bg=bg,fg=fg).grid(column = 4, row = 4)
    button_explore = Button(tab1,text = "Input Video",command = browseFiles, state=DISABLED,bg=bg,fg=fg).grid(column = 4, row = 3)
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
    timestwo = Label(tab1,
                     font=("Arial", 11),
                     text = f"Finished 2X interpolation. Generated temp.mp4.",
                     fg=fg,bg=bg)
    timestwo.grid(column=4,row=10)
    get_fps2()
    os.system('rm -rf input_frames')
    os.system('rm -rf output_frames ')
    os.system('mkdir input_frames')
    os.system('mkdir output_frames')
    os.system(f'ffprobe "{thisdir}/temp.mp4"')
    os.system(f'ffmpeg -i "{thisdir}/temp.mp4" -vn -acodec copy audio.m4a -y')
    os.system(f'ffmpeg -i "{thisdir}/temp.mp4" input_frames/frame_%08d.png')
    pb4x2() # calls the second 4x progressbar, ik this is dumb, but live with it. This happens after onclick executes Should be called after the ffmpeg extracts the frames
    if os.path.exists(outputdir) == False:
            outputdir = homedir
    timestwo.after(0, timestwo.destroy())
    Interpolation2.grid(column=4,row=10)
    global done2
    if os.path.isfile(fr"{outputdir}/{mp4name}_{fps2 * 2}fps{extension}") == True:
        done2 = Label(tab1,
                 text=f"Done! Output File = {outputdir}/{mp4name}_{int(fps * 4)}fps(1){extension}",
                 font=("Arial", 11), width=57, anchor="w",
                 fg=fg,bg=bg)
    else:
        done2 = Label(tab1,
                 text=f"Done! Output File = {outputdir}/{mp4name}_{int(fps * 4)}fps{extension}",
                 font=("Arial", 11), width=57, anchor="w",
                 fg=fg,bg=bg)
    
    os.system(f'./rife-ncnn-vulkan {rifever} -i input_frames -o output_frames ')
    if os.path.isfile(fr"{outputdir}/{mp4name}_{fps2 * 2}fps.{extension}") == True:
            os.system(fr'ffmpeg -framerate {fps2 * 2} -i "{thisdir}/rife-vulkan-models/output_frames/%08d.png" -i {thisdir}/rife-vulkan-models/audio.m4a -c:a copy -crf {getVidQuality()}  -pix_fmt yuv420p "{outputdir}/{mp4name}_{int(fps2 * 2)}fps(1).{extension}" -y')
    else:
        os.system(fr'ffmpeg -framerate {fps2 * 2} -i "{thisdir}/rife-vulkan-models/output_frames/%08d.png" -i {thisdir}/rife-vulkan-models/audio.m4a -c:a copy -crf {getVidQuality()}  -pix_fmt yuv420p "{outputdir}/{mp4name}_{int(fps2 * 2)}fps.{extension}" -y')
    os.system(fr'rm -rf "{thisdir}/temp.mp4"')
    Interpolation2.after(0, Interpolation2.destroy())
    done2.grid(column=4,row=10)# maybe change done label location in code, edit what row it shows up on
    
    start_button = Button(tab1, text="Start!", command=lambda: threading('rife'),bg=bg_button,fg=fg,width=10,height=4).grid(row = 22, column = 0)
    button_output = Button(tab1,text = "Output Folder",command = output, bg=bg_button,fg=fg).grid(column = 4, row = 4)
    button_explore = Button(tab1,text = "Input Video",command = browseFiles, bg=bg_button,fg=fg).grid(column = 4, row = 3)
    os.system('rm -rf "'+thisdir+'/temp"')
    os.system('rm -rf input_frames')
    os.system('rm -rf output_frames ')    
    os.chdir(f"{thisdir}")

def on_click2(rifever):
    get_fps()
    
    os.system('rm -rf input_frames')
    os.system('rm -rf output_frames ')
    os.system('mkdir input_frames')
    os.system('mkdir output_frames')
    os.system(f'ffprobe "{filename}"')
    os.system(f'ffmpeg -i "{filename}" -vn -acodec copy audio.m4a -y')
    extraction.grid(column=4,row=10)
    os.system(f'ffmpeg -i "{filename}" input_frames/frame_%08d.png')
    extraction.after(0, extraction.destroy())
    Interpolation.grid(column=4,row=10)
    pbthread4x() # calls the first 4x progressbar.
            # This is temperary until i can figure out how to have progressbar update based on interpolation selected.
    os.system(f'./rife-ncnn-vulkan {rifever} -i input_frames -o output_frames ')
    os.system(fr'ffmpeg -framerate {fps * 2} -i "{thisdir}/rife-vulkan-models/output_frames/%08d.png" -i {thisdir}/rife-vulkan-models/audio.m4a -c:a copy -crf 0 -vcodec copy -pix_fmt yuv420p "{thisdir}/temp.mp4" -y')
    Interpolation.destroy()
def on_click2_anime(round, is16x, is8x):
    get_fps()
    if round != 0:
        os.system(f'ffmpeg -i {thisdir}/temp.mp4  -vf mpdecimate,fps=30 -vsync vfr -vcodec libx264 -preset veryslow -qp 0 -profile:v high444 -crf 0 -c:a copy {thisdir}/temp2.mp4 -y')
    if is8x == True or is16x == True and round != 0:
        filename1 = f'"{thisdir}/temp2.mp4"'
    else:
        filename1 = filename
    os.system('rm -rf input_frames')
    os.system('rm -rf output_frames ')
    os.system('mkdir input_frames')
    os.system('mkdir output_frames')
    os.system(f'ffprobe "{filename1}"')
    os.system(f'ffmpeg -i "{filename1}" -vn -acodec copy audio.m4a -y')
    extraction.grid(column=4,row=10)
    os.system(f'ffmpeg -i "{filename1}" input_frames/frame_%08d.png')
    extraction.after(0, extraction.destroy())
    Interpolation.grid(column=4,row=10)
    if is16x == False and is8x == False:
        sleep(1)
        pbthread4x() # calls the first 4x progressbar.
    if is16x == True and is8x == False:
        if round == 0:
            Anime16xPb1Thread()
        if round == 1:
            Anime16xPb3Thread()
        if round == 2:
            Anime16xPb5Thread()
            
    if is8x == True and is16x == False:
        if round == 0:
            Anime8xPb1Thread()
        if round == 1:
            Anime8xPb3Thread()
        
    os.system(f'./rife-ncnn-vulkan -i input_frames -o output_frames ')
    if round == 0:
        os.system(fr'ffmpeg -framerate {fps * 2} -i "{thisdir}/rife-vulkan-models/output_frames/%08d.png" -i {thisdir}/rife-vulkan-models/audio.m4a -c:a copy -crf 0 -vcodec copy  "{thisdir}/temp1.mp4" -y')
    else:
        os.system(fr'ffmpeg -framerate 60 -i "{thisdir}/rife-vulkan-models/output_frames/%08d.png" -i {thisdir}/rife-vulkan-models/audio.m4a -c:a copy -crf 0 -vcodec copy  "{thisdir}/temp1.mp4" -y')
    Interpolation.destroy()
def on_click2_anime_8x(is16x):# generates temp2 file witch is 30fps
    get_fps()
    
    os.system('rm -rf input_frames')
    os.system('rm -rf output_frames ')
    os.system('mkdir input_frames')
    os.system('mkdir output_frames')
    if is16x == False:
        os.system(f'ffprobe "{filename}"')
        os.system(f'ffmpeg -i "{filename}" -vn -acodec copy audio.m4a -y')
        extraction.grid(column=4,row=10)
        os.system(f'ffmpeg -i "{filename}" input_frames/frame_%08d.png')
    else:
        os.system(f'ffprobe "{thisdir}/temp.mp4"')
        os.system(f'ffmpeg -i "{thisdir}/temp.mp4" -vn -acodec copy audio.m4a -y')
        extraction.grid(column=4,row=10)
        os.system(f'ffmpeg -i "{thisdir}/temp.mp4" input_frames/frame_%08d.png')
    extraction.after(0, extraction.destroy())
    Interpolation.grid(column=4,row=10)
    if is16x == False:
        Anime8xPb1Thread() # calls the first 4x progressbar.
    else:
        Anime16xPb3Thread() # calls the first 4x progressbar.
            # This is temperary until i can figure out how to have progressbar update based on interpolation selected.
    os.system(f'./rife-ncnn-vulkan -i input_frames -o output_frames ')
    os.chdir(f"{thisdir}")
    os.system('rm temp*')
    os.chdir("rife-vulkan-models")
    if is16x == False:
        os.system(fr'ffmpeg -framerate {fps * 2} -i "{thisdir}/rife-vulkan-models/output_frames/%08d.png" -i {thisdir}/rife-vulkan-models/audio.m4a -c:a copy -crf 0 -vcodec copy -pix_fmt yuv420p "{thisdir}/temp1.mp4" -y')
    else:
        os.system(fr'ffmpeg -framerate 120 -i "{thisdir}/rife-vulkan-models/output_frames/%08d.png" -i {thisdir}/rife-vulkan-models/audio.m4a -c:a copy -crf 0 -vcodec copy -pix_fmt yuv420p "{thisdir}/temp1.mp4" -y')
    os.system(f'ffmpeg -i {thisdir}/temp1.mp4  -vf mpdecimate,fps=30 -vcodec libx264 -preset veryslow -qp 0 -profile:v high444 -vsync vfr -crf 0 -c:a copy {thisdir}/temp2.mp4 -y')
    os.chdir(f"{thisdir}")
    os.system('rm temp1.mp4')
    os.chdir("rife-vulkan-models")
def on_click2_8(rifever): # the 8x interpolation of on_click, has to set so different progress bars work. Ik i can do this better, but i dont feel like it.
    get_fps()
    
    os.system('rm -rf input_frames')
    os.system('rm -rf output_frames ')
    os.system('mkdir input_frames')
    os.system('mkdir output_frames')
    os.system(f'ffprobe "{filename}"')
    os.system(f'ffmpeg -i "{filename}" -vn -acodec copy audio.m4a -y')
    extraction.grid(column=4,row=10)
    os.system(f'ffmpeg -i "{filename}" input_frames/frame_%08d.png')
    extraction.after(0, extraction.destroy())
    Interpolation.grid(column=4,row=10)
    pbthread8x() #Set this to 8x, this is the first of 3 progressbars
    os.system(f'./rife-ncnn-vulkan {rifever} -i input_frames -o output_frames ')
    os.system(fr'ffmpeg -framerate {fps * 2} -i "{thisdir}/rife-vulkan-models/output_frames/%08d.png" -i {thisdir}/rife-vulkan-models/audio.m4a -c:a copy -crf 0 -vcodec copy -pix_fmt yuv420p "{thisdir}/temp.mp4" -y')
    Interpolation.destroy()

def on_click3(rifever):
    get_fps2()
        # this if statement sets default output dir, may need to remove when add selector.
    

    
    global timestwo3
    timestwo3 = Label(tab1,
                      font=("Arial", 11),
                      text=f"Finished 2X interpolation. Generated temp.mp4.",
                      fg=fg,bg=bg)
    timestwo3.grid(column=4,row=10)
    os.system('rm -rf input_frames')
    os.system('rm -rf output_frames ')
    os.system('mkdir input_frames')
    os.system('mkdir output_frames')
    os.system(f'ffprobe "{thisdir}/temp.mp4"')
    os.system(f'ffmpeg -i "{thisdir}/temp.mp4" -vn -acodec copy audio.m4a -y')
    os.system(f'ffmpeg -i "{thisdir}/temp.mp4" input_frames/frame_%08d.png')
    timestwo3.after(0, timestwo3.destroy())
    Interpolation2.grid(column=4,row=10)
    pb8x2()            # This calls it for the second time, initiates second progressbar 
    os.system(f'./rife-ncnn-vulkan {rifever} -i input_frames -o output_frames ')
    os.system(fr'ffmpeg -framerate {fps2 * 2} -i "{thisdir}/rife-vulkan-models/output_frames/%08d.png" -i {thisdir}/rife-vulkan-models/audio.m4a -c:a copy -crf 0 -vcodec copy -pix_fmt yuv420p "{thisdir}/temp2.mp4" -y')
    Interpolation2.after(0, Interpolation2.destroy())
    os.system(fr'rm -rf "{thisdir}/temp.mp4"')

def times8(rifever):
    os.chdir("rife-vulkan-models")
    global done
    #done = Label(tab1,text="                                                                                                                                                                ",bg=bg)
    #done.grid(column=4,row=10)
    start_button = Button(tab1, text="Start!", command=lambda: threading('rife'),bg=bg_button,fg=fg,width=10,height=4, state=DISABLED).grid(row = 22, column = 0)

    button_output = Button(tab1,text = "Output Folder",command = output, state=DISABLED,bg=bg,fg=fg).grid(column = 4, row = 4)
    button_explore = Button(tab1,text = "Input Video",command = browseFiles, state=DISABLED,bg=bg,fg=fg).grid(column = 4, row = 3)
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
    timestwo2 = Label(tab1,
                     font=("Arial", 11),
                     text = f"Finished 4X interpolation. Generated temp.mp4.",
                     bg=bg,
                     fg=fg)
    timestwo2.grid(column=4,row=10)
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
    if os.path.exists(outputdir) == False:
            outputdir = homedir
    Interpolation3.grid(column=4,row=10)
    global done3
    if os.path.isfile(fr"{outputdir}/{mp4name}_{fps2 * 2}fps.{extension}") == True:
        done3 = Label(tab1,
                 text=f"Done! Output File = {outputdir}/{mp4name}_{int(fps * 8)}fps(1){extension}",
                 font=("Arial", 11), width=57, anchor="w",
                 fg=fg,bg=bg)
    else:
        done3 = Label(tab1,
                 text=f"Done! Output File = {outputdir}/{mp4name}_{int(fps * 8)}fps{extension}",
                 font=("Arial", 11), width=57, anchor="w",
                 fg=fg,bg=bg)

    os.system(f'./rife-ncnn-vulkan {rifever} -i input_frames -o output_frames ')
    if os.path.isfile(fr"{outputdir}/{mp4name}_{fps3 * 2}fps.{extension}") == True:
            os.system(fr'ffmpeg -framerate {fps3 * 2} -i "{thisdir}/rife-vulkan-models/output_frames/%08d.png" -i {thisdir}/rife-vulkan-models/audio.m4a -c:a copy -crf {getVidQuality()}  -pix_fmt yuv420p "{outputdir}/{mp4name}_{int(fps3 * 2)}fps(1).{extension}" -y')
    else:
        os.system(fr'ffmpeg -framerate {fps3 * 2} -i "{thisdir}/rife-vulkan-models/output_frames/%08d.png" -i {thisdir}/rife-vulkan-models/audio.m4a -c:a copy -crf {getVidQuality()}  -pix_fmt yuv420p "{outputdir}/{mp4name}_{int(fps3 * 2)}fps.{extension}" -y')
    
    os.system(fr'rm -rf "{thisdir}/temp2.mp4"')
    Interpolation3.after(0, Interpolation3.destroy())
    done3.grid(column=4,row=10)
    start_button = Button(tab1, text="Start!", command=lambda: threading('rife'),bg=bg_button,fg=fg,width=10,height=4).grid(row = 22, column = 0)
    button_output = Button(tab1,text = "Output Folder",command = output, bg=bg_button,fg=fg).grid(column = 4, row = 4)
    button_explore = Button(tab1,text = "Input Video",command = browseFiles, bg=bg_button,fg=fg).grid(column = 4, row = 3)
    os.system('rm -rf input_frames')
    os.system('rm -rf output_frames ')
    os.system('rm -rf "'+thisdir+'/temp"')
    os.chdir(f"{thisdir}")
main_window.geometry("680x490")
main_window.title(' ')
main_window.resizable(False, False) 
main_window.mainloop()

#Help me
