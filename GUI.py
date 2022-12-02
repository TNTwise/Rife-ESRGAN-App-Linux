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
    os.system('python3 -m pip install distro')
    os.system('rm files/get-pip.py')
    with open (thisdir+"/programstate", "w") as f:
        f.write(homedir)
    
    
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
import distro
filename = ""
main_window = Tk()

f = open(thisdir+"/programstate", "r")
f = csv.reader(f)
for row in f:
    current_default_output_folder = row
if os.path.exists(current_default_output_folder[0]) == False:
    with open(thisdir+"/programstate", 'w') as f:
        f.write(homedir)

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
    for i in range(len(file1_lines)):
        if file1_lines[i] != file2_lines[i]:
            is_updated = 1
            os.system(f'rm -rf "{thisdir}/GUI.py"')
            os.system(f'mv "{thisdir}/temp/GUI.py" "{thisdir}/"')
            os.system(f'rm -rf "{thisdir}/start.py"')
            os.system(f'mv "{thisdir}/temp/start.py" "{thisdir}/files/"')
            os.system(f'rm -rf "{thisdir}/Start"')
            os.system(f'mv "{thisdir}/temp/Start" "{thisdir}/"')
            os.system(f'chmod +x "{thisdir}/Start"')
            os.system(f'rm -rf "{thisdir}/temp/"')
            break
    os.system(f'rm -rf "{thisdir}/temp/"')
            
    
        
            
    if latest_ver > current:
                is_updated = 1
                os.chdir(f"{thisdir}/files/")
                os.system(f"wget https://github.com/nihui/rife-ncnn-vulkan/releases/download/{latest_ver}/rife-ncnn-vulkan-{latest_ver}-ubuntu.zip")
                with ZipFile(f'rife-ncnn-vulkan-{latest_ver}-ubuntu.zip','r') as f:
                    f.extractall()
                os.chdir(f"{thisdir}")
                os.system(f'mv "rife-ncnn-vulkan-{latest_ver}-ubuntu" "{thisdir}/files/"')
                os.system(f'rm -rf "{thisdir}/rife-anime/"')
                os.system(f'mv "{thisdir}/files/rife-ncnn-vulkan-{latest_ver}-ubuntu/rife-anime/" "{thisdir}/"')
                os.system(f'rm -rf "{thisdir}/rife-v2.4/"')
                os.system(f'mv "{thisdir}/files/rife-ncnn-vulkan-{latest_ver}-ubuntu/rife-v2.4/" "{thisdir}/"')
                os.system(f'rm -rf "{thisdir}/rife-v3.1/"')
                os.system(f'mv "{thisdir}/files/rife-ncnn-vulkan-{latest_ver}-ubuntu/rife-v3.1/" "{thisdir}/"')
                os.system(f'rm -rf "{thisdir}/rife-v4.6/"')
                os.system(f'mv "{thisdir}/files/rife-ncnn-vulkan-{latest_ver}-ubuntu/rife-v4.6/" "{thisdir}/"')
                with open(f"{thisdir}/files/version", 'w') as f:
                    f.write(latest_ver)
                os.system(f'rm -rf "{thisdir}/files/rife-ncnn-vulkan-{latest_ver}-ubuntu.zip"')
                os.system(f'rm -rf "{thisdir}/files/rife-ncnn-vulkan-{latest_ver}-ubuntu"')
                
    if is_updated == 1:
        return 1
    else:
        return
                
                
                
    os.system(f'rm -rf "{thisdir}/temp/"')

def get_distro():
    global distro
    distro = distro.id()
    return distro

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
    default_output_label = Label(settings_window, text=current_default_output_folder[0],bg=bg,fg=fg, width=25, anchor="w")
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
            theme_button = Button(settings_window,text="Light",command=darkTheme,bg="white",fg=fg)
    if theme == "Dark":
            theme_button = Button(settings_window,text="Dark",command=lightTheme,bg=bg,fg=fg)
    theme_label = Label(settings_window,text=" Theme: ",bg=bg,fg=fg)
    spacer_label = Label(settings_window,text="            ",bg=bg) # This spaces the middle
    spacer_label1 = Label(settings_window,text="            ",bg=bg) # this spaces the end
    spacer_label2 = Label(settings_window,text="        ",bg=bg) # this is at the start of the gui
    global check_updates_button
    check_updates_button = Button(settings_window,text="Check For Updates", command=start_update_check_thread, bg=bg,fg=fg)
    install_button = Button(settings_window, text="Install", command=pass_dialog_box,bg=bg,fg=fg)
    global  update_spacer_label
    update_spacer_label = Label(settings_window,text = " ", bg=bg)
    
    def show_dropdown():
        update_branch_label = Label(settings_window,text="Update channel:",bg=bg,fg=fg)
        
        variable = StringVar(settings_window)
        repo_options = ['Testing', 'Stable']
        variable.set(repo)
        opt = OptionMenu(settings_window, variable, *repo_options)
        opt.config(width=9, font=('Helvetica', 12))
        opt.config(bg=bg)
        opt.config(fg=fg)
        update_branch_label.grid(column=5,row=0)
        opt.grid(column=5,row=1)
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
     # lays out the menu
    spacer_label2.grid(column=0,row=0)
    button_select_default_output.grid(column=1, row=0)
    default_output_label.grid(column=1, row=1)
    if is_installed == "False":
        install_button.grid(column=1,row=2)
    spacer_label.grid(column=2,row=0)
    theme_label.grid(column=3,row=0)
    theme_button.grid(column=3, row=1)
    spacer_label1.grid(column=4,row=0)
    check_updates_button.grid(column=5,row=3)
    update_spacer_label.grid(column=5,row=2)
    #change_repo_dropdown.grid(column=5,row=2)
    settings_window.geometry("600x200")
    settings_window.title('             Settings')
    settings_window.resizable(False, False) 
    settings_window.mainloop()


# this will show if updates exist
def start_update_check():
    global update_check_label
    if check_for_updates() == 1:
        update_check_label = Label(settings_window,text="Updated, restart to apply.",bg=bg,fg=fg)
        check_updates_button = Button(settings_window,text="Check For Updates", command=start_update_check_thread, bg=bg,fg=fg).grid(column=5,row=3)
        restart_window("Updated, re-launch the program to apply.")
    else:
        update_spacer_label.destroy()
        update_check_label = Label(settings_window,text="No Updates",bg=bg,fg=fg)
        check_updates_button = Button(settings_window,text="Check For Updates", command=start_update_check_thread, bg=bg,fg=fg).grid(column=5,row=3)
    update_check_label.grid(column=5,row=1)
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
    theme_button = Button(settings_window,text="Dark",command=lightTheme,bg=bg,fg=fg)
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
    theme_button = Button(settings_window,text="Light",command=darkTheme,bg="white",fg=fg)
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
    default_output_label_1 = Label(settings_window, text=current_default_output_folder[0],bg=bg,fg=fg, width=25, anchor="w")
    default_output_label_1.grid(column=1, row=1)
    
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
    progressbar = ttk.Progressbar(main_window,orient='horizontal', length=300, mode="determinate")
    progressbar.grid(column=3, row=20)
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
    progressbar_1 = ttk.Progressbar(main_window,orient='horizontal', length=300, mode="determinate",value=50,maximum=150)
    progressbar_1.grid(column=3, row=20)
    # Add progressbar updater
    #sleep(1) # wont update unless we sleep for 1 second?????????
    while i == 4:
        
        frames_processed_1 = len(list(Path('output_frames/').glob('*')))
        amount_of_output_files_1 = len(list(Path('input_frames/').glob('*'))) *2
        e_1 = frames_processed_1/amount_of_output_files_1
        e_1*= 100
        e_1 = int(e_1) + 50 # Has to add 100 to make progress bar work
        progressbar_1['value'] = e_1
        progressbar_1.update()
            
# work on this later, it will change the progressbar based on the amount of interpolation.
def progressBar4x(): # makes first progressbar in 4x 
    
    i = 2
    
    amount_of_input_files = (len([name for name in os.listdir('input_frames/') if os.path.isfile(name)]))
    amount_of_output_files = amount_of_input_files * 2
    
    progressbar = ttk.Progressbar(main_window,orient='horizontal', length=300, mode="determinate",maximum=300)
    progressbar.grid(column=3, row=20)
    #sleep(1)
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
   
    progressbar_5 = ttk.Progressbar(main_window,orient='horizontal', length=300, mode="determinate",value=73,maximum=170)
    progressbar_5.update()
    progressbar_5.grid(column=3, row=20)
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

def progressBar8xSecond(): # calls this second, this is called by onclick3
    
    p = 4
    amount_of_input_files_2 = (len([name for name in os.listdir('input_frames/') if os.path.isfile(name)]))
    amount_of_output_files_2 = amount_of_input_files_2 * 2
    global progressbar_2 # creates new progressbar
    progressbar_2 = ttk.Progressbar(main_window,orient='horizontal', length=300, mode="determinate", value=43, maximum=300)
    progressbar_2.grid(column=3, row=20)
    # Add progressbar updater
    #progressbar_2["maximum"]= 800
    #sleep(1) # wont update unless we sleep for 1 second?????????
    while p == 4:
        
        frames_processed_2 = len(list(Path('output_frames/').glob('*')))
        amount_of_output_files_2 = len(list(Path('input_frames/').glob('*'))) *2
        e_2 = frames_processed_2/amount_of_output_files_2
        e_2*= 100 
        e_2 = int(e_2) +43
        e_2 = e_2 * 0.9
        progressbar_2['value'] = e_2 # this times it by .9 so that the progressbar goes up to 3/7 of 300 which is 128.7
        progressbar_2.update()
        if progressbar_2 ['value'] == 128:
            progressbar_2 ['value'] = 128
            break
def progressBar8x(): # this is called first.
    i = 2
    amount_of_input_files = (len([name for name in os.listdir('input_frames/') if os.path.isfile(name)]))
    amount_of_output_files = amount_of_input_files * 2
    
    progressbar = ttk.Progressbar(main_window,orient='horizontal', length=300, mode="determinate",maximum=700)
    progressbar.grid(column=3, row=20)
    
    # Add progressbar updater
    while i == 2: # all this adds up to 100, i change the maximum so that it will even out the progressbar for different rendering times.
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
def start_update_check_thread():
    t1 = Thread(target=start_update_check)
    t1.start()
    check_updates_button = Button(settings_window,text="Check For Updates", command=start_update_check_thread, bg=bg,fg=fg, state=DISABLED).grid(column=5,row=2)


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
if get_distro() != "ubuntu":
    centering_label = Label(main_window, text="                                                                                                                                                                "
    ,bg=bg,fg=fg,font=("Ariel", "12"))
else:
    centering_label = Label(main_window, text="                                                                                                                                                                ",bg=bg,fg=fg)

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
    if filename != "":
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
        if os.path.exists(outputdir) == False:
            outputdir = homedir
        if os.path.isfile(fr"{outputdir}/{mp4name}_{fps * 2}fps{extension}") == True:
            done = Label(main_window,
                 text=f"Done! Output File = {outputdir}/{mp4name}_{int(fps * 2)}fps(1){extension}",
                 font=("Arial", 11), width=80, anchor="w",
                 fg=fg,bg=bg)
        else:
           done = Label(main_window,
                 text=f"Done! Output File = {outputdir}/{mp4name}_{int(fps * 2)}fps{extension}",
                 font=("Arial", 11), width=80, anchor="w",
                 fg=fg,bg=bg)
        os.system(f'./rife-ncnn-vulkan {rifever} -i input_frames -o output_frames ')
        if os.path.isfile(fr"{outputdir}/{mp4name}_{fps * 2}fps.{extension}") == True:
            os.system(fr'ffmpeg -framerate {fps * 2} -i "{thisdir}/output_frames/%08d.png" -i audio.m4a -c:a copy -crf 20 -c:v libx264 -pix_fmt yuv420p "{outputdir}/{mp4name}_{int(fps * 2)}fps(1).{extension}" -y')
        else:
            os.system(fr'ffmpeg -framerate {fps * 2} -i "{thisdir}/output_frames/%08d.png" -i audio.m4a -c:a copy -crf 20 -c:v libx264 -pix_fmt yuv420p "{outputdir}/{mp4name}_{int(fps * 2)}fps.{extension}" -y')
        Interpolation.after(0, Interpolation.destroy())
        done.grid(column=3, row=9)
        # these re-enable the start, input, and output buttons
        start_button = Button(main_window, text="Start!", command=threading,bg=bg,fg=fg).grid(row = 2, column = 3)
        button_output = Button(main_window,text = "Output Folder",command = output,bg=bg,fg=fg).grid(column = 3, row = 4)
        button_explore = Button(main_window,text = "Input Video",command = browseFiles,bg=bg,fg=fg).grid(column = 3, row = 3)
        os.system('rm -rf "'+thisdir+'/temp"') # removes the temp file, this is after every times function, not on onclick functions as they do not require the outputdir variable.







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
    if os.path.exists(outputdir) == False:
            outputdir = homedir
    timestwo.after(0, timestwo.destroy())
    Interpolation2.grid(column=3,row=9)
    global done2
    if os.path.isfile(fr"{outputdir}/{mp4name}_{fps2 * 2}fps{extension}") == True:
        done2 = Label(main_window,
                 text=f"Done! Output File = {outputdir}/{mp4name}_{int(fps * 4)}fps(1){extension}",
                 font=("Arial", 11), width=80, anchor="w",
                 fg=fg,bg=bg)
    else:
        done2 = Label(main_window,
                 text=f"Done! Output File = {outputdir}/{mp4name}_{int(fps * 4)}fps{extension}",
                 font=("Arial", 11), width=80, anchor="w",
                 fg=fg,bg=bg)
    
    os.system(f'./rife-ncnn-vulkan {rifever} -i input_frames -o output_frames ')
    if os.path.isfile(fr"{outputdir}/{mp4name}_{fps2 * 2}fps.{extension}") == True:
            os.system(fr'ffmpeg -framerate {fps2 * 2} -i "{thisdir}/output_frames/%08d.png" -i audio.m4a -c:a copy -crf 20 -c:v libx264 -pix_fmt yuv420p "{outputdir}/{mp4name}_{int(fps2 * 2)}fps(1).{extension}" -y')
    else:
        os.system(fr'ffmpeg -framerate {fps2 * 2} -i "{thisdir}/output_frames/%08d.png" -i audio.m4a -c:a copy -crf 20 -c:v libx264 -pix_fmt yuv420p "{outputdir}/{mp4name}_{int(fps2 * 2)}fps.{extension}" -y')
    os.system(fr'rm -rf "{thisdir}/temp.mp4"')
    Interpolation2.after(0, Interpolation2.destroy())
    done2.grid(column=3, row=9)# maybe change done label location in code, edit what row it shows up on
    
    start_button = Button(main_window, text="Start!", command=threading, bg=bg_button,fg=fg).grid(row = 2, column = 3)
    button_output = Button(main_window,text = "Output Folder",command = output, bg=bg_button,fg=fg).grid(column = 3, row = 4)
    button_explore = Button(main_window,text = "Input Video",command = browseFiles, bg=bg_button,fg=fg).grid(column = 3, row = 3)
    os.system('rm -rf "'+thisdir+'/temp"')

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
    if os.path.exists(outputdir) == False:
            outputdir = homedir
    Interpolation3.grid(column=3,row=9)
    global done3
    if os.path.isfile(fr"{outputdir}/{mp4name}_{fps2 * 2}fps.{extension}") == True:
        done3 = Label(main_window,
                 text=f"Done! Output File = {outputdir}/{mp4name}_{int(fps * 8)}fps(1){extension}",
                 font=("Arial", 11), width=80, anchor="w",
                 fg=fg,bg=bg)
    else:
        done3 = Label(main_window,
                 text=f"Done! Output File = {outputdir}/{mp4name}_{int(fps * 8)}fps{extension}",
                 font=("Arial", 11), width=80, anchor="w",
                 fg=fg,bg=bg)

    os.system(f'./rife-ncnn-vulkan {rifever} -i input_frames -o output_frames ')
    if os.path.isfile(fr"{outputdir}/{mp4name}_{fps3 * 2}fps.{extension}") == True:
            os.system(fr'ffmpeg -framerate {fps3 * 2} -i "{thisdir}/output_frames/%08d.png" -i audio.m4a -c:a copy -crf 20 -c:v libx264 -pix_fmt yuv420p "{outputdir}/{mp4name}_{int(fps3 * 2)}fps(1).{extension}" -y')
    else:
        os.system(fr'ffmpeg -framerate {fps3 * 2} -i "{thisdir}/output_frames/%08d.png" -i audio.m4a -c:a copy -crf 20 -c:v libx264 -pix_fmt yuv420p "{outputdir}/{mp4name}_{int(fps3 * 2)}fps.{extension}" -y')
    
    
    os.system(fr'rm -rf "{thisdir}/temp2.mp4"')
    Interpolation3.after(0, Interpolation3.destroy())
    done3.grid(column=3, row=9)
    start_button = Button(main_window, text="Start!", command=threading, bg=bg_button,fg=fg).grid(row = 2, column = 3)
    button_output = Button(main_window,text = "Output Folder",command = output, bg=bg_button,fg=fg).grid(column = 3, row = 4)
    button_explore = Button(main_window,text = "Input Video",command = browseFiles, bg=bg_button,fg=fg).grid(column = 3, row = 3)
    os.system('rm -rf "'+thisdir+'/temp"')








main_window.geometry("700x500")
main_window.title(' ')
main_window.resizable(False, False) 
main_window.mainloop()





