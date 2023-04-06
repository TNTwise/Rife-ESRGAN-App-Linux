#!/usr/bin/python3
#version=4.0
#Implementing a version update system, instead of checking if file length is different.
import os 
global thisdir
import requests
import re
import sys
import csv
import PIL.Image
#This will replace wget
def wget(URL,name):
    response = requests.get(URL)
    open(f"{name}", 'wb').write(response.content)
global onefile_dir
thisdir = os.getcwd()
onefile_dir = thisdir
global ffmpeg_command
ffmpeg_command = 'ffmpeg'
homedir = os.path.expanduser(r"~")

if len(sys.argv) > 1: 
    if sys.argv[1] == '--compile-appimage':
        GUI_List = []
        with open('GUI.py', 'r') as f:
            for line in f:
                GUI_List.append(line)
                if line == '#ffmpeg_command = ../ffmpeg\n':
                    line_index = GUI_List.index(line)
                    GUI_List[line_index] = 'ffmpeg_command = "../ffmpeg"\n'
                    print(GUI_List[line_index])
                if line == '#thisdir = f{homedir}/.Rife-Vulkan-GUI\n':
                    line_index = GUI_List.index(line)
                    GUI_List[line_index] ='thisdir = f\'{homedir}/.Rife-Vulkan-GUI\'\n'
                    print(GUI_List[line_index])
                if line == '#onefile_dir = sys._MEIPASS\n':
                    line_index = GUI_List.index(line)
                    GUI_List[line_index] = 'onefile_dir = sys._MEIPASS\n'
                    print(GUI_List[line_index])
                if line =='get_all_models()\n':
                    line_index = GUI_List.index(line)
                    GUI_List[line_index] = '#get_all_models()\n'
                    print(GUI_List[line_index])
                
    if os.path.isfile('GUIPortable.py') == False:
        os.mknod('GUIPortable.py')
    with open ('GUIPortable.py', 'w') as f:
        for i in GUI_List:
            f.write(i)
    print('Completed')
    exit()
#do not edit these lines.

#ffmpeg_command = ../ffmpeg
#thisdir = f{homedir}/.Rife-Vulkan-GUI
#onefile_dir = sys._MEIPASS
#you can edit from down here on
if os.path.exists(f'{homedir}/.Rife-Vulkan-GUI') == False:
    os.mkdir(f'{homedir}/.Rife-Vulkan-GUI')

if os.path.exists(f"{thisdir}/files/") == False:
    os.mkdir(f"{thisdir}/files/")



if(os.path.isfile(thisdir+"/files/settings.txt")) == False and ffmpeg_command == 'ffmpeg':
    os.chdir(f"{thisdir}/files")
    os.system(f'curl -O "https://bootstrap.pypa.io/get-pip.py" > get-pip.py')
    os.system(f'python3 -m pip install requests')
    
    os.chdir(f"{thisdir}")
    
    os.system(f'python3 files/get-pip.py install')
    os.system(f'python3 -m pip install opencv-python')
    os.system(f'python3 -m pip install tk')
    os.system(f'python3 -m pip install psutil')
    
    os.system(f'rm files/get-pip.py')
    

import getpass
from pathlib import Path
import pathlib
import os
import glob
from tkinter.ttk import Progressbar
import sys
import os.path
from tkinter import *
from tkinter import filedialog
from multiprocessing import Queue, Process
import subprocess
from subprocess import Popen, PIPE
from time import sleep
from threading import *
from tkinter import ttk
import ntpath
from sys import exit
import glob
import os.path
import cv2
from tkinter import *
import psutil
from zipfile import ZipFile
from PIL import ImageTk


# These change the settings file
def write_to_settings_file(description, option):
    
    with open(f'{thisdir}/files/settings.txt', 'a') as f:
        f.write(description + ","+option + "\n")


def read_settings():
    global settings_dict
    settings_dict = {}

    with open(f'{thisdir}/files/settings.txt', 'r') as f:
        f = csv.reader(f)
        for row in f:
            try:
                settings_dict[row[0]] = row[1]
            except:
                pass
    try:
        global Rife_Option
        Rife_Option = settings_dict['Rife_Option']
        global Interpolation_Option
        Interpolation_Option = settings_dict['Interpolation_Option']
        global Repository
        Repository = settings_dict['Repository']
        global Image_Type
        Image_Type = settings_dict['Image_Type']
        global IsAnime
        IsAnime = settings_dict['IsAnime']
        global rifeversion
        rifeversion = settings_dict['rifeversion']
        global esrganversion
        esrganversion = settings_dict['esrganversion']
        global videoQuality
        videoQuality = settings_dict['videoQuality']
        global Theme
        Theme = settings_dict['Theme']
        global OutputDir
        OutputDir = settings_dict['OutputDir']
        global GPUUsage
        GPUUsage = settings_dict['GPUUsage']
        global RenderDevice
        RenderDevice = settings_dict['RenderDevice']
        global RenderDir
        RenderDir = settings_dict['RenderDir']
        global ExtractionImageType
        ExtractionImageType=settings_dict['ExtractionImageType']
        global SceneChangeDetection
        SceneChangeDetection=settings_dict['SceneChangeDetection']

    except:
        os.system(f'rm -rf "{thisdir}/files/settings.txt"')
        os.mknod(f'{thisdir}/files/settings.txt')
        write_to_settings_file("Image_Type", "webp")
        write_to_settings_file("IsAnime", "False")
        write_to_settings_file("Repository", "stable")
        write_to_settings_file("rifeversion", "20221029")
        write_to_settings_file("esrganversion", "0.2.0")
        write_to_settings_file("videoQuality", "14")
        write_to_settings_file("Theme", "Light")
        write_to_settings_file("OutputDir", f"{homedir}")
        write_to_settings_file("Interpolation_Option", f"2X")
        write_to_settings_file("Rife_Option" ,'2.3')
        write_to_settings_file("GPUUsage" ,'Default')
        write_to_settings_file("RenderDevice" ,'GPU')
        write_to_settings_file("RenderDir" ,f"{thisdir}")
        write_to_settings_file("ExtractionImageType" ,"jpg")
        write_to_settings_file('SceneChangeDetection','0.4')

        settings_dict = {}
        with open(f'{thisdir}/files/settings.txt', 'r') as f:
            f = csv.reader(f)
            for row in f:
                settings_dict[row[0]] = row[1]
        Rife_Option = settings_dict['Rife_Option']
        
        Interpolation_Option = settings_dict['Interpolation_Option']
        
        Repository = settings_dict['Repository']
        
        Image_Type = settings_dict['Image_Type']
        
        IsAnime = settings_dict['IsAnime']
        rifeversion = settings_dict['rifeversion']
        esrganversion = settings_dict['esrganversion']
        videoQuality = settings_dict['videoQuality']
        Theme = settings_dict['Theme']
        OutputDir = settings_dict['OutputDir']
        GPUUsage = settings_dict['GPUUsage']
        RenderDevice = settings_dict['RenderDevice']
        RenderDir = settings_dict['RenderDir']
        

        
def write_defaults():
    write_to_settings_file("Image_Type", "webp")
    write_to_settings_file("IsAnime", "False")
    write_to_settings_file("Repository", "stable")
    write_to_settings_file("rifeversion", "20221029")
    write_to_settings_file("esrganversion", "0.2.0")
    write_to_settings_file("videoQuality", "14")
    write_to_settings_file("Theme", "Light")
    write_to_settings_file("OutputDir", f"{homedir}")
    write_to_settings_file("Interpolation_Option", f"2X")
    write_to_settings_file("Rife_Option" ,'2.3')
    write_to_settings_file("GPUUsage" ,'Default')
    write_to_settings_file("RenderDevice" ,'GPU')
    write_to_settings_file("RenderDir" ,f"{thisdir}")
    write_to_settings_file("ExtractionImageType" ,"jpg")
    write_to_settings_file('SceneChangeDetection','0.4')
    try:
        read_settings()
    except:
        pass

if os.path.isfile(f'{thisdir}/files/settings.txt') == False:
    os.mknod(f'{thisdir}/files/settings.txt')
    write_defaults()
def write_temp(): # im doing this because i am lazy
    change_setting("Interpolation_Option", f"2X")
    change_setting("Rife_Option", f"2.3")
    change_setting("IsAnime", "False")


read_settings()
def change_setting(setting,svalue):
    original_settings = {}
    with open(f'{thisdir}/files/settings.txt', 'r') as f:
        f = csv.reader(f)
        for row in f:
            original_settings[row[0]] = row[1]
        
        original_settings[setting] = svalue
        os.system(f'rm -rf "{thisdir}/files/settings.txt" && touch "{thisdir}/files/settings.txt"')
        for key,value in original_settings.items():
            with open(f'{thisdir}/files/settings.txt', 'a') as f:
                f.write(key + ',' + value+'\n')
    read_settings()
write_temp()

def check_output_dir():
    if os.path.exists(f'{OutputDir}') == False:
        change_setting('OutputDir', f'{homedir}')
    if os.path.exists(f'{RenderDir}') == False:
        change_setting('RenderDir', f'{thisdir}')
check_output_dir()



global realsr_model
realsr_model = '-n realesrgan-x4plus -s 4'




os.system(f'chmod +x "{thisdir}/rife-vulkan-models/rife-ncnn-vulkan"')
def check_theme():
    
    # This code reads the theme file and stores its data in a theme variable
    return Theme
videopath = ""
main_window = Tk()
tabControl = ttk.Notebook(main_window)
if check_theme() == "Light":
    tab1 = ttk.Frame(tabControl)
    tab2 = ttk.Frame(tabControl)
    tab3 = ttk.Frame(tabControl)
    tab4 = ttk.Frame(tabControl)
    s = ttk.Style()
# Create style used by default for all Frames
    s.configure('TFrame', background='White')

# Create style for the first frame
    s.configure('Frame1.TFrame', background='White', foreground='Black')
if check_theme() == "Dark":
    tab1 = ttk.Frame(tabControl)
    tab2 = ttk.Frame(tabControl)
    tab3 = ttk.Frame(tabControl)
    tab4 = ttk.Frame(tabControl)
    s = ttk.Style()
# Create style used by default for all Frames
    s.configure('TFrame', background='#4C4E52',foreground='#4C4E52')

# Create style for the first frame
    s.configure('Frame1.TFrame', background='red')
#Create tabs
tabControl.add(tab1, text='Rife')
tabControl.add(tab2, text='Real-ESRGAN')
tabControl.add(tab3, text='Preview')
tabControl.add(tab4, text='Settings')
tabControl.grid(row=0,column=0)


def grayout_tabs(mode):
    if mode == 'rife':
        tabControl.tab(tab2, state='disabled')
        
    if mode == 'realsr':
        tabControl.tab(tab1, state='disabled')  
    tabControl.tab(tab4, state='disabled')
def enable_tabs():
     tabControl.tab(tab1, state='normal')  
     tabControl.tab(tab2, state='normal')  
     tabControl.tab(tab4, state='normal')  


if check_theme() == "Light":
    main_window.config(bg="white")
    
    fg="black"
    bg="White"
    bg_button="white"
if check_theme() == "Dark":
    main_window.config(bg="#4C4E52")
    
    fg="white"
    
    bg_button="#4C4E52"




       
    

def latest_ESRGAN():
    # this code gets the latest versaion of rife vulkan
            

            latest = requests.get('https://github.com/xinntao/Real-ESRGAN-ncnn-vulkan/releases/latest') 
            latest = latest.url
            latest = re.findall(r'v[\d].[\d].[\d]*$', latest)
            latest = latest[0]
            current = esrganversion
            return(latest,current)

# this checks for updates
# it makes a temp folder, and gets the latest GUI.py from github
# It compares the files, and if the files are different, replaces the old GUI.py with the one from github
# Ive changed it to the Stable branch which created, this helps prevent unintended bugs from getting in the updates 
def check_for_updates():
    is_updated = 0
    os.system(f'mkdir -p "{thisdir}/temp/"')
    os.chdir(f"{thisdir}/temp/")
    
    
    
    if repo =="Stable":
        wget('https://raw.githubusercontent.com/TNTwise/Rife-Vulkan-GUI-Linux/Stable/GUI.py', 'GUI.py')
        wget('https://raw.githubusercontent.com/TNTwise/Rife-Vulkan-GUI-Linux/Stable/start.py', 'start.py')
        wget('https://raw.githubusercontent.com/TNTwise/Rife-Vulkan-GUI-Linux/Stable/Start', 'Start')
    if repo =="Testing":
        wget('https://raw.githubusercontent.com/TNTwise/Rife-Vulkan-GUI-Linux/main/GUI.py', 'GUI.py')
        wget('https://raw.githubusercontent.com/TNTwise/Rife-Vulkan-GUI-Linux/main/start.py', 'start.py')
        wget('https://raw.githubusercontent.com/TNTwise/Rife-Vulkan-GUI-Linux/main/Start', 'Start')
        os.chdir(f"{thisdir}")
    file1 = open(f"{thisdir}/temp/GUI.py")
    file2 = open(f"{thisdir}/GUI.py")
    file1_lines = file1.readlines()
    file2_lines = file2.readlines()
    version = latest_rife() # calls latest function which gets the latest version release of rife and returns the latest and the current, if the version file doesnt exist, it updates and creates the file
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
                wget(f"https://github.com/nihui/rife-ncnn-vulkan/releases/download/{latest_ver}/rife-ncnn-vulkan-{latest_ver}-ubuntu.zip", f"rife-ncnn-vulkan-{latest_ver}-ubuntu.zip")
                with ZipFile(f'rife-ncnn-vulkan-{latest_ver}-ubuntu.zip','r') as f:
                    f.extractall()
                os.chdir(f"{thisdir}")
                os.system(f'rm -rf "{thisdir}/files/rife-ncnn-vulkan"')
                os.system(f'mv "{thisdir}/rife-ncnn-vulkan-{latest_ver}-ubuntu" "{thisdir}/files/"')
                os.system(f'mv "{thisdir}/files/rife-ncnn-vulkan-{latest_ver}-ubuntu/"* "{thisdir}/rife-vulkan-models/"')
                os.system(f'chmod +x "{thisdir}/files/rife-ncnn-vulkan"')
                change_setting('rifeversion',f'{latest_ver}')
                os.system(f'rm -rf "{thisdir}/files/rife-ncnn-vulkan-{latest_ver}-ubuntu.zip"')
                os.system(f'rm -rf "{thisdir}/files/rife-ncnn-vulkan-{latest_ver}-ubuntu"')

    if is_updated == 1:
        return 1
    else:
        return




    
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



    

# insert elements by their
# index and names.

# Insert settings menu here


def settings_window():
    
    
    button_select_default_output = Button(tab4,
                        text = "Select default output folder",
                        command = sel_default_output_folder, bg=bg_button,fg=fg)
    
    # just writes 'stable' to file repository to be able to change where the program is taken from
    
    
    current_default_output_folder = OutputDir
    #displays current default output folder
    
    global default_output_label
    default_output_label = Label(tab4, text=current_default_output_folder,bg=bg,fg=fg, width=25, anchor="w")
    
    # creates theme button and calls check_theme which returns the theme that is currently on
    global repo
    repo = Repository
    if repo == "stable": # capitolizes repo first char
        repo = "Stable"
    if repo == "testing":
        repo = "Testing"
    global theme_button
    theme = check_theme()
    if theme == "Light":
            theme_button = Button(tab4,text="Light",command=darkTheme,bg="white",fg=fg)
    if theme == "Dark":
            theme_button = Button(tab4,text="Dark",command=lightTheme,bg=bg,fg=fg)
    theme_label = Label(tab4,text=" Theme: ",bg=bg,fg=fg)
    spacer_label = Label(tab4,text="            ",bg=bg) # This spaces the middle
    spacer_label1 = Label(tab4,text="            ",bg=bg) # this spaces the end
    spacer_label2 = Label(tab4,text="",bg=bg) # this is at the start of the gui
    global default_render_label
    default_render_label = Label(tab4,text=RenderDir,bg=bg,fg=fg,width=25,anchor='w')
    default_render_label.grid(column=6,row=1)
    global check_updates_button
    check_updates_button = Button(tab4,text="Check For Updates", command=start_update_check_thread, bg=bg,fg=fg)
    global  update_spacer_label
    update_spacer_label = Label(tab4,text = " ", bg=bg)
    
    button_select_default_render = Button(tab4,
                        text = "Select default render folder",
                        command = sel_default_render_folder, bg=bg_button,fg=fg).grid(column=6, row=0)
        
    def video_image_dropdown():
        update_branch_label = Label(tab4,text="Render Image Type: ",bg=bg,fg=fg)
        update_branch_label.grid(column=1,row=5)
        variable = StringVar(tab4)
        repo_options = ['webp            (smaller size, lossless)', 'png            (lossless)', 'jpg            (lossy)']
        variable.set(Image_Type)
        opt = OptionMenu(tab4, variable, *repo_options)
        opt.config(width=4,font=('Ariel', '12'))
        
        opt.config(bg=bg)
        opt.config(fg=fg)
        opt.config(anchor="w")
        opt.grid(column=1,row=6)
        def callback(*args):
            
            if variable.get() == 'webp            (smaller size, lossless)':
                change_setting('Image_Type', 'webp')
                global Image_Type
                Image_Type = 'webp'
                read_settings()
            if variable.get() == 'png            (lossless)':
                
                Image_Type = 'png'
                change_setting('Image_Type', 'png')
                read_settings()
            if variable.get() == 'jpg            (lossy)':
                change_setting('Image_Type', 'jpg')
                Image_Type = 'jpg'
                read_settings()
        variable.trace("w", callback)

    

    def gpu_usage_dropdown():
        update_branch_label = Label(tab4,text="System Load:",bg=bg,fg=fg)
        update_branch_label.grid(column=4,row=5)
        variable = StringVar(tab4)
        repo_options = ['Default', 'Low', 'High', 'Very High', 'Custom']
        if GPUUsage == 'Default' or GPUUsage == 'Low' or GPUUsage == 'High' or GPUUsage == 'Very High':
            variable.set(GPUUsage)
        else:
            variable.set('Custom')
            global save_button
            global custom_box1
            custom_box1 = Text(tab4,width=10,height=1)
            custom_box1.insert("end-1c", GPUUsage)
            custom_box1.grid(row=7,column=4)
            save_button = Button(tab4,width=10,height=1,text='Save',fg=fg,bg=bg,command=lambda: change_setting("GPUUsage", custom_box1.get('1.0', 'end-1c')))
            save_button.grid(row=8,column=4)
        opt = OptionMenu(tab4, variable, *repo_options)
        opt.config(width=8,font=('Ariel', '12'))
            
        opt.config(bg=bg)
        opt.config(fg=fg)
        opt.config(anchor="w")
        opt.grid(column=4,row=6)
        def callback(*args):
            if variable.get() != 'Custom':
                remove_custom()
                change_setting("GPUUsage", variable.get())
                read_settings()
            else:
                if GPUUsage == 'Default' or GPUUsage == 'Low' or GPUUsage == 'High' or GPUUsage == 'Very High':
                    change_setting("GPUUsage", "10")
                
                custom_box1 = Text(tab4,width=10,height=1)
                custom_box1.insert("end-1c", GPUUsage)
                custom_box1.grid(row=7,column=4)
                
                save_button = Button(tab4,width=10,height=1,text='Save',fg=fg,bg=bg,command=lambda: change_setting("GPUUsage", custom_box1.get('1.0', 'end-1c')))
                save_button.grid(row=8,column=4)
        variable.trace("w", callback)
    
        
        

    def remove_custom():
        try:
                    
                    custom_box1.destroy()
                    
                    save_button.destroy()
        except:
                    
                    pass
    def RenderDeviceDropDown():
        update_branch_label = Label(tab4,text="Render Device:",bg=bg,fg=fg)
        update_branch_label.grid(column=6,row=5)
        variable = StringVar(tab4)
        repo_options = ['CPU', 'GPU', 'Dual GPU', 'CPU + GPU']
        if RenderDevice != 'CPU + GPU':
            variable.set(RenderDevice)
        else:
            variable.set('CPU + GPU')
        opt = OptionMenu(tab4, variable, *repo_options)
        opt.config(width=9,font=('Ariel', '12'))
        
        opt.config(bg=bg)
        opt.config(fg=fg)
        opt.config(anchor="w")
        opt.grid(column=6,row=6)
        def callback(*args):
            if variable.get() != 'CPU + GPU':
                change_setting("RenderDevice", variable.get())
            else:
                change_setting("RenderDevice", 'CPU + GPU')

            
        variable.trace("w", callback)
    RenderDeviceDropDown()    
    gpu_usage_dropdown()
    video_image_dropdown()
    #show_dropdown()
    def video_quality_drop_down():
        vid_quality_label = Label(tab4,text="Video quality:", bg=bg,fg=fg).grid(column=1,row=2)
        vidQuality = videoQuality
        if vidQuality == "22":
            vidQuality1 = "Low"
        if vidQuality == "18":
            vidQuality1 = "Medium"
        if vidQuality == "14":
            vidQuality1 = "High"
        if vidQuality == "7":
            vidQuality1 = "Lossless"
        variable = StringVar(tab4)
        repo_options = ['Lossless','High', 'Medium', 'Low']
        variable.set(vidQuality1)
        opt = OptionMenu(tab4, variable, *repo_options)
        opt.config(width=9,font=('Ariel', '12'))
        opt.config(bg=bg)
        opt.config(fg=fg)
        
        opt.grid(column=1,row=3)
        def callback(*args):
                
                # Converts these to cfv format
                if variable.get() == "Low":
                    change_setting('videoQuality', '22')
                if variable.get() == "Medium":
                    change_setting('videoQuality', '18')
                if variable.get() == "High":
                    change_setting('videoQuality', '14')
                if variable.get() == "Lossless":
                    change_setting('videoQuality', '7')
                
        variable.trace("w", callback)
    video_quality_drop_down()
    class advancedOptions():
        def __init__(self):
            self.advanced_settings_window = Tk()
            try:
                        self.advanced_settings_window.iconphoto(False, PhotoImage(file=f'{onefile_dir}/icons/icon-256x256.png'))
            except:
                pass
            
            self.advanced_settings_window.config(bg=bg)
            self.layout()

            self.advanced_settings_window.geometry("600x400")
            self.advanced_settings_window.title('Advanced Settings')
            self.advanced_settings_window.resizable(False, False) 
            self.advanced_settings_window.mainloop()

        def layout(self):
            Label(self.advanced_settings_window, text='Extraction Image Type:',font=('Ariel', '12'),bg=bg,fg=fg).grid(column=1,row=0)
            Label(self.advanced_settings_window, text='                 Scene change detection sensitivity:',font=('Ariel', '12'),bg=bg,fg=fg).grid(column=2,row=0)

            def extraction_image_drop_down():
                extraction_image_variable = StringVar(self.advanced_settings_window)
                extraction_image_options = ['JPG','PNG']
                extraction_image_variable.set(ExtractionImageType.upper())
                extraction_imageDropDown = OptionMenu(self.advanced_settings_window, extraction_image_variable, *extraction_image_options)
                extraction_imageDropDown.config(width=4,font=('Ariel', '12'))
                extraction_imageDropDown.config(bg=bg)
                extraction_imageDropDown.config(fg=fg)
                extraction_imageDropDown.grid(column=1,row=1)
                
                def callback(*args):
                    change_setting('ExtractionImageType',(extraction_image_variable.get().lower()))
                    
                extraction_image_variable.trace("w", callback)
            extraction_image_drop_down()

            def transition_detection_drop_down():
                transition_detection_variable = StringVar(self.advanced_settings_window)
                extraction_image_options = ['Off','Low','Medium','High']
                if SceneChangeDetection == 'Off':
                    transition_detection_variable.set('Off')
                if SceneChangeDetection == '0.2':
                    transition_detection_variable.set('High')
                if SceneChangeDetection == '0.4':
                    transition_detection_variable.set('Medium')
                if SceneChangeDetection == '0.6':
                    transition_detection_variable.set('Low')
                transition_detection_drop_down = OptionMenu(self.advanced_settings_window, transition_detection_variable, *extraction_image_options)
                transition_detection_drop_down.config(width=6,font=('Ariel', '12'))
                transition_detection_drop_down.config(bg=bg)
                transition_detection_drop_down.config(fg=fg)
                transition_detection_drop_down.grid(column=2,row=1)
                
                def callback(*args):
                    if transition_detection_variable.get() == 'Off':
                        change_setting('SceneChangeDetection','Off')
                    if transition_detection_variable.get() == 'High':
                        change_setting('SceneChangeDetection','0.2')
                    if transition_detection_variable.get() == 'Medium':
                        change_setting('SceneChangeDetection','0.4')
                    if transition_detection_variable.get() == 'Low':
                        change_setting('SceneChangeDetection','0.6')
                    
                transition_detection_variable.trace("w", callback)
            transition_detection_drop_down()

    advanced_options_button = Button(tab4,width=15,height=1,text='Advanced Options',bg=bg,fg=fg,command=advancedOptions,font=('Ariel', '12'))
    



     # lays out the menu
    spacer_label2.grid(column=0,row=0)
    spacer_label2.config(padx=30)
    button_select_default_output.grid(column=1, row=0)
    default_output_label.grid(column=1, row=1)
    
    spacer_label.grid(column=2,row=0)
    theme_label.grid(column=4,row=0)
    theme_button.grid(column=4, row=1)
    spacer_label1.grid(column=5,row=0)
    #check_updates_button.grid(column=6,row=3)
    update_spacer_label.grid(column=6,row=2)
    #change_repo_dropdown.grid(column=5,row=2)
    Label(tab4,text='',bg=bg,fg=fg,font=('Ariel', '16')).grid(column=1,row=8)
    advanced_options_button.grid(column=1,row=9)


# this will show if updates exist
def start_update_check():
    global update_check_label
    if check_for_updates() == 1:
        update_check_label = Label(tab4,text="Updated, restart to apply.",bg=bg,fg=fg)
        check_updates_button = Button(tab4,text="Check For Updates", command=start_update_check_thread, bg=bg,fg=fg).grid(column=6,row=3)
        restart_window("Updated, re-launch the program to apply.")
    else:
        update_check_label = Label(tab4,text="No Updates",bg=bg,fg=fg)
        check_updates_button = Button(tab4,text="Check For Updates", command=start_update_check_thread, bg=bg,fg=fg).grid(column=6,row=3)
    update_check_label.grid(column=6,row=5)
# restarts the program


def restart():
    os.system("pkill -f GUI.py && python3 start.py")
def restart_thread():
    t1 = Thread(target=restart_window)
    t1.start()

def exit_thread():
    # Call work function
    t1 = Thread(target=exi11)
    t1.start()

# restart window, this allows the program to restart after a application settings changes. call this with a message to confirm restart of program.   
def restart_window(message):
    restart_window = Tk()
    centering_label = Label(restart_window, text="                                                                         ")
    restart_label = Label(restart_window, text=message, justify=CENTER)
    exit_button = Button(restart_window, text="Exit", command=exit_thread,justify=CENTER)
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


#This returns the settings for each gpu setting
def get_render_device(app):
    if app != 'realsr':
        if RenderDevice == 'GPU':
            return ""
        if RenderDevice == 'CPU':
            return "-g -1"
        if RenderDevice == 'Dual GPU':
            return "-g 0,0,1"
        if RenderDevice == 'CPU + GPU':
            return '-g -1,0,0'
    else:
        return ""
def gpu_setting(app):
    if GPUUsage == 'Default' or GPUUsage == 'Low' or GPUUsage == 'High' or GPUUsage == 'Very High':
         pass
    else:
        l = (f'-j {GPUUsage}:{GPUUsage}:{GPUUsage}')
        return l
    if GPUUsage == 'Default' and RenderDevice == 'GPU' or RenderDevice == 'CPU':
        
        return ""
        
    if GPUUsage == 'High' and RenderDevice == 'GPU' or RenderDevice == 'CPU':
        return "-j 3:7:3"
    if GPUUsage == 'Very High' and RenderDevice == 'GPU' or RenderDevice == 'CPU':
        return "-j 10:10:10"
    if GPUUsage == 'Low' and RenderDevice == 'GPU' or RenderDevice == 'CPU':
        return "-j 1:1:1"
    if app != 'realsr':
        if GPUUsage == 'Default' and RenderDevice == 'Dual GPU':
            return "-j 1:2,2,2:2"
        if GPUUsage == 'High' and RenderDevice != 'GPU' and RenderDevice == 'Dual GPU':
            return "-j 5:5,5,5:5"
        if GPUUsage == 'Very High' and RenderDevice != 'GPU' and RenderDevice == 'Dual GPU':
            return "-j 10:10,10,10:10"
        if GPUUsage == 'Low' and RenderDevice != 'GPU' and RenderDevice == 'Dual GPU':
            return "-j 1:1,1,1:1"
        if GPUUsage =='Default' and RenderDevice == 'CPU + GPU':
            return '-j 2:4,2,1:4'
        if GPUUsage =='Low' and RenderDevice == 'CPU + GPU':
            return '-j 1:2,1,1:2'
        if GPUUsage =='High' and RenderDevice == 'CPU + GPU':
            return '-j 8:8,8,8:8'
        if GPUUsage =='Very High' and RenderDevice == 'CPU + GPU':
            return '-j 10:10,12,12:10'
        
            
    else:
        if GPUUsage == 'Default':
           return "-j 1:2:2"
        if GPUUsage == 'High':
            return "-j 5:5:5"
        if GPUUsage == 'Very High':
            return "-j 10:10:10"
    
def latest_rife():
    # this code gets the latest versaion of rife vulkan
            

            latest = requests.get('https://github.com/nihui/rife-ncnn-vulkan/releases/latest/') 
            latest = latest.url
            latest = re.findall(r'[\d]*$', latest)
            latest = latest[0]
            current = rifeversion
            return(latest,current)
def get_all_models():
    if os.path.exists(f"{thisdir}/rife-vulkan-models/") == False:
        os.mkdir(f"{thisdir}/rife-vulkan-models/")
    if os.path.exists(f"{thisdir}/rife-vulkan-models/rife-HD/") != True:
        version = latest_rife() # calls latest function which gets the latest version release of rife and returns the latest and the current, if the version file doesnt exist, it updates and creates the file
        latest_ver = version[0]
        os.chdir(f"{thisdir}/files/")
        wget(f"https://github.com/nihui/rife-ncnn-vulkan/releases/download/{latest_ver}/rife-ncnn-vulkan-{latest_ver}-ubuntu.zip", f"rife-ncnn-vulkan-{latest_ver}-ubuntu.zip")
        with ZipFile(f'rife-ncnn-vulkan-{latest_ver}-ubuntu.zip','r') as f:
            f.extractall()
        os.chdir(f"{thisdir}")
        os.system(f'rm -rf "{thisdir}/rife-vulkan-models"')
        os.system(f'mkdir -p "{thisdir}/rife-vulkan-models"')
        os.system(f'mv "{thisdir}/rife-ncnn-vulkan-{latest_ver}-ubuntu" "{thisdir}/files/"')
        os.system(f'mv "{thisdir}/files/rife-ncnn-vulkan-{latest_ver}-ubuntu/"* "{thisdir}/rife-vulkan-models/"')
        change_setting('rifeversion', f'{latest_ver}')
        os.system(f'rm -rf "{thisdir}/files/rife-ncnn-vulkan-{latest_ver}-ubuntu.zip"')
        os.system(f'rm -rf "{thisdir}/files/rife-ncnn-vulkan-{latest_ver}-ubuntu"')
        os.system(f'chmod +x "{thisdir}/rife-vulkan-models/rife-ncnn-vulkan"')
    if os.path.exists(f"{thisdir}/Real-ESRGAN/") == False:
            os.mkdir(f"{thisdir}/Real-ESRGAN/")
    if os.path.isfile(f"{thisdir}/Real-ESRGAN/realesrgan-ncnn-vulkan") == False:
        ESRGAN_version = latest_ESRGAN()
        latest_ver_ESR = ESRGAN_version[0]
        os.chdir(f"{thisdir}/files/")
        os.system(f'rm -rf "{thisdir}/Real-ESRGAN"')
        os.system(f'mkdir -p "{thisdir}/Real-ESRGAN/"')
        wget('https://github.com/xinntao/Real-ESRGAN/releases/download/v0.2.5.0/realesrgan-ncnn-vulkan-20220424-ubuntu.zip','realesrgan-ncnn-vulkan-20220424-ubuntu.zip')
        os.system(f'mkdir -p "{thisdir}/files/realesrgan-ncnn-vulkan-20220424-ubuntu/"')
        os.chdir(f'{thisdir}/files/realesrgan-ncnn-vulkan-20220424-ubuntu/')
        with ZipFile(f'{thisdir}/files/realesrgan-ncnn-vulkan-20220424-ubuntu.zip','r') as f:
            f.extractall()
        os.system(f'mkdir -p "{thisdir}/Real-ESRGAN/models/"')
        os.system(f'mv "{thisdir}/files/realesrgan-ncnn-vulkan-20220424-ubuntu/models/"* "{thisdir}/Real-ESRGAN/models/"')
        os.chdir(f'{thisdir}/files')
        wget('https://github.com/xinntao/Real-ESRGAN-ncnn-vulkan/releases/download/v0.2.0/realesrgan-ncnn-vulkan-v0.2.0-ubuntu.zip', 'realesrgan-ncnn-vulkan-v0.2.0-ubuntu.zip')
        with ZipFile(f'{thisdir}/files/realesrgan-ncnn-vulkan-v0.2.0-ubuntu.zip','r') as f:
            f.extractall()
        os.chdir(f"{thisdir}")
        
        os.system(f'mv "{thisdir}/realesrgan-ncnn-vulkan-v0.2.0-ubuntu" "{thisdir}/files/"')
        os.system(f'mv "{thisdir}/files/realesrgan-ncnn-vulkan-v0.2.0-ubuntu/"* "{thisdir}/Real-ESRGAN"')
        change_setting('esrganversion', f'{latest_ver_ESR}')
        os.system(f'rm -rf "{thisdir}/files/realesrgan-ncnn-vulkan-v0.2.0-ubuntu.zip"')
        os.system(f'rm -rf "{thisdir}/files/realesrgan-ncnn-vulkan-v0.2.0-ubuntu"')
        os.system(f'chmod +x "{thisdir}/Real-ESRGAN/realesrgan-ncnn-vulkan"')
        os.system(f'rm -rf {thisdir}/files/realesrgan-ncnn-vulkan-20220424-ubuntu')
        os.system(f'rm -rf {thisdir}/files/realesrgan-ncnn-vulkan-20220424-ubuntu.zip')
    os.system(f'rm -rf "{thisdir}/temp/"')
get_all_models()


def preview_image():
        
        i=1
        g=1
        while i==1:
            if os.path.exists(f'{RenderDir}/{filename}/output_frames/') == False:
                 label.destroy()
                 break
                 
            dir_path = f'{RenderDir}/{filename}/output_frames/'
            files = os.listdir(dir_path)
            files.sort()
            sleep(1)
            try:
                
                img = PIL.Image.open(f"{RenderDir}/{filename}/output_frames/{files[-1]}")
                width, height = img.size
                desired_width = 820
                proportional_height = int((desired_width / float(width)) * height)
                img = img.resize((desired_width, proportional_height), PIL.Image.NEAREST)

                photo = ImageTk.PhotoImage(img)

                label = Label(tab3,image=photo,width=desired_width,height=proportional_height)
                
                label.grid(column=1,row=0)
                
                
            except:
                pass

  


#switches theme for tkinter

def darkTheme():
    change_setting('Theme', 'Dark')
    global bg
    global bg_button
    global fg
    bg="#4C4E52"
    fg="white"
    bg_button="#4C4E52"
    
    restart_window("Changing theme requires restart.")
    

def lightTheme():
    change_setting('Theme', 'Light')
    
    global bg
    global bg_button
    global fg
    bg="white"
    bg_button="white" 
    fg="black"
    
    restart_window("Changing theme requires restart.")
    
    
def sel_default_render_folder():
    
    select_default_render_folder = filedialog.askdirectory(initialdir = fr"/",
                                          title = "Select a Folder",)
    if isinstance(select_default_render_folder, str) == True and len(select_default_render_folder) > 0:
        change_setting('RenderDir', select_default_render_folder)
         #displays current default output folder
        default_render_label.destroy()
        default_render_label_1 = Label(tab4, text=select_default_render_folder,bg=bg,fg=fg, width=25, anchor="w")
        default_render_label_1.grid(column=6, row=1)
   

def sel_default_output_folder():
    global select_default_output_folder
    select_default_output_folder = filedialog.askdirectory(initialdir = fr"{homedir}",
                                          title = "Select a Folder",)
    if isinstance(select_default_output_folder, str) == True and len(select_default_output_folder) > 0:
        change_setting('OutputDir', select_default_output_folder)

        current_default_output_folder = OutputDir
        #displays current default output folder
        default_output_label.destroy()
        default_output_label_1 = Label(tab4, text=current_default_output_folder,bg=bg,fg=fg, width=25, anchor="w")
        default_output_label_1.grid(column=1, row=1)
        
'''def remove_processced_files():    #scraping this for now
    def start():
        i = 0
        while i == 0:
            frames_processced =len(list(Path(f'{RenderDir}/{filename}/output_frames/').glob('*')))
            frames_to_remove = int(frames_processced/2) - 20
            frame = str(frames_to_remove).zfill(8)
            os.system(f'rm -rf "{RenderDir}/{filename}/input_frames/frame_{frame}.png"')
            if os.path.exists(f'{RenderDir}/{filename}/input_frames/') == False:
                
                break
    Thread(target=start).start()'''




def show(program):
    # These 2 variables are the defaults, will need to remove when make default selector.
    if program == "rife":
        rifever = ""
    
        read_settings()
        interpolation_option = settings_dict['Interpolation_Option']
        rifever1 = Rife_Option
        
        isAnime = IsAnime
        
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
    if program == 'realsr':

        realESRGAN(realsr_model) 

# This code allows for the dropdown selector for the rife versions and interpolation option.  
# This was a very desprate debugging technique i used, apologize for the mess.
# The solution was me not being an idiot
def show_interp_opt():
    
    global iterp_opt_variable
    iterp_opt_variable = StringVar(tab1)
    interpolation_options = ['2X', '4X', '8X']
    iterp_opt_variable.set('2X')
    global interpOptDropDown
    interpOptDropDown = OptionMenu(tab1, iterp_opt_variable, *interpolation_options)
    interpOptDropDown.config(width=2,font=('Ariel', '12'))
    interpOptDropDown.config(bg=bg)
    interpOptDropDown.config(fg=fg)
    interpOptDropDown.grid(column=4,row=6)
    
    def callback(*args):
        change_setting('Interpolation_Option', iterp_opt_variable.get())
                
    iterp_opt_variable.trace("w", callback)
show_interp_opt()

def show_rife_ver():
    
    global rife_ver_variable
    rife_ver_variable = StringVar(tab1)
    interpolation_options = ['Rife', 'Rife-HD','Rife-UHD','Rife Anime','Rife 2.0','Rife 2.3', 'Rife 2.4','Rife 3.0', 'Rife 3.1','Rife 4.0', 'Rife 4.6']
    rife_ver_variable.set('Rife 2.3')
    global rifeVerDropDown
    rifeVerDropDown = OptionMenu(tab1, rife_ver_variable, *interpolation_options)
    rifeVerDropDown.config(width=10,font=('Ariel', '12'))
    rifeVerDropDown.config(bg=bg)
    rifeVerDropDown.config(fg=fg)
    rifeVerDropDown.grid(column=4,row=7)
    
    def callback(*args):
        
            if rife_ver_variable.get() == "Rife":
                change_setting("Rife_Option", 'Rife')
            if rife_ver_variable.get() == "Rife-HD":
                change_setting("Rife_Option", 'HD')
            if rife_ver_variable.get() == "Rife Anime":
                change_setting("Rife_Option", 'Anime')
            if rife_ver_variable.get() == "Rife-UHD":
                change_setting("Rife_Option", 'UHD')
            if rife_ver_variable.get() == "Rife 4.0":
                change_setting("Rife_Option", '4.0')
            if rife_ver_variable.get() == "Rife 3.0":
                change_setting("Rife_Option", '3.0')
            if rife_ver_variable.get() == "Rife 2.0":
                change_setting("Rife_Option", '2.0')
            if rife_ver_variable.get() == "Rife 2.3":
                change_setting("Rife_Option", '2.3')
            if rife_ver_variable.get() == "Rife 2.4":
                change_setting("Rife_Option", '2.4')
            if rife_ver_variable.get() == "Rife 3.1":
                change_setting("Rife_Option", '3.1')
            if rife_ver_variable.get() == "Rife 4.6":
                change_setting("Rife_Option", '4.6')
                
    rife_ver_variable.trace("w", callback)
show_rife_ver()

# The 8x and 4x progressbars are split into sections
# The 2x portion of the 4x takes up 1/3 of the progressbar, while the 4x takes up the rest 2/3s.
# the 8x portion is split into 7ths.
# the 2x portion is 0/7 - 1/7
# The 4x portion is 1/7-3/7
# the 8x protion is 3/7-7/7
def progressBar(starting_value,maximum,adding_value,ending_value):# This will help me not copy and paste
    i = 2
    p=0
    amount_of_input_files = (len([name for name in os.listdir(f'{RenderDir}/{filename}/input_frames/') if os.path.isfile(name)]))
    amount_of_output_files = amount_of_input_files * 2
    global progressbar
    progressbar = ttk.Progressbar(tab1,orient='horizontal', length=630, mode="determinate",maximum=maximum,value=starting_value)
    progressbar.grid(column=4, row=22)
    # Add progressbar updater
    progressbar["maximum"]=maximum
    while i == 2:
        frames_processed = len(list(Path(f'{RenderDir}/{filename}/output_frames/').glob('*')))
        
        amount_of_output_files = len(list(Path(f'{RenderDir}/{filename}/input_frames/').glob('*'))) * 2
            
        e = frames_processed/amount_of_output_files
        e*= 100
        e = int(e) + adding_value
        progressbar['value'] = e
        progressbar.update()
        p =2
        if progressbar['value'] == ending_value - 1: 
            progressbar1 = ttk.Progressbar(tab1,orient='horizontal', length=630, mode="determinate",maximum=maximum,value=ending_value)
            progressbar1.grid(column=4, row=22)
            progressbar.destroy()
            
            break


def progressBarThread(starting_value,maximum,adding_value,ending_value):
    t1 = Thread(target=lambda: progressBar(starting_value,maximum,adding_value,ending_value))
    t1.start()

def RealPB():
    i = 2
    amount_of_input_files = (len([name for name in os.listdir(f'{RenderDir}/{filename}/input_frames/') if os.path.isfile(name)]))
    amount_of_output_files = amount_of_input_files
    
    progressbar1 = ttk.Progressbar(tab2,orient='horizontal', length=630, mode="determinate")
    progressbar1.grid(column=4, row=22)
    # Add progressbar updater
    progressbar1["maximum"]=100
    while i == 2:
        frames_processed = len(list(Path(f'{RenderDir}/{filename}/output_frames/').glob('*')))
        amount_of_output_files = len(list(Path(f'{RenderDir}/{filename}/input_frames/').glob('*'))) 
        e = frames_processed/amount_of_output_files
        e*= 100
        e = int(e)
        progressbar1['value'] = e
        progressbar1.update()
#Calls respective function, creates new thread for progressbar and other things, will only execute if called.
def pbthreadreal():
    Thread(target=RealPB).start()
def threading(program):
    # Call work function
    t1 = Thread(target=lambda: show(program))
    t1.start()
def start_update_check_thread():
    t1 = Thread(target=start_update_check)
    t1.start()
    check_updates_button = Button(tab4,text="Check For Updates", command=start_update_check_thread, bg=bg,fg=fg, state=DISABLED).grid(column=6,row=3)
def anime_thread():
    t1 = Thread(target=AnimeInterpolation)
    t1.start()


#Button
settings_window()
def browseFiles():

    global videopath
    videopath = filedialog.askopenfilename(initialdir = fr"{homedir}",
                                          title = "Select a File",
                                          filetypes = (("Video Files",
                                                        ['*.mp4','*.mov','*.avi','*.mkv']),
                                                        
                                                       ("all files",
                                                        "*.*")))
    global filename 
    filename = os.path.split(videopath)[1]
    
    #change label contents
    global extension
    extension = (pathlib.Path(f'{videopath}/{filename}').suffix)


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
    return OutputDir
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
    cap=cv2.VideoCapture(fr'{videopath}')
    global fps
    fps = cap.get(cv2.CAP_PROP_FPS)
    global vidHeight
    vidHeight = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    global vidWidth
    vidWidth = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    # putting these here so it can get referenced every time an interpolation runs.
    



#create labels
def Anime():
    
    variable2 = StringVar(tab1)
    video_options = ['Default', 'Animation (Uneven Framerate)']
    variable2.set('Default')
    opt1 = OptionMenu(tab1, variable2, *video_options)
    opt1.config(width=29,font=('Ariel', '12'))
    opt1.config(bg=bg)
    opt1.config(fg=fg)
    opt1.grid(column=4,row=8)

    def callback(*args):
        if variable2.get() == 'Default':
            #start_button = Button(tab1, text="Start!", command=lambda: threading('rife'),bg=bg_button,fg=fg,width=7,height=3,font=('Ariel 13 bold')).grid(row = 22, column = 0)
            # UNGREY inter_opt and rive_ver buttons
            rifeVerDropDown.config(state="normal")
            global iterp_opt_variable2
            iterp_opt_variable2 = StringVar(tab1)
            interpolation_options = ['2X','4X', '8X']
            interpOptDropDown2 = OptionMenu(tab1, iterp_opt_variable2, *interpolation_options)
            interpOptDropDown2.config(width=2,font=('Ariel', '12'))
            iterp_opt_variable2.set('2X')
            interpOptDropDown2.config(bg=bg)
            interpOptDropDown2.config(fg=fg)
            change_setting('Interpolation_Option', '2X')
            change_setting('IsAnime', 'False')
            interpOptDropDown2.grid(column=4,row=6)
            
            def callback(*args):
                change_setting('Interpolation_Option', iterp_opt_variable2.get())

                
                
                change_setting('IsAnime', 'False')
            iterp_opt_variable2.trace("w", callback)
        else:
            #Button(tab1, text="Start!", command=anime_thread,bg=bg_button,fg=fg,width=7,height=3,font=('Ariel 13 bold')).grid(row = 22, column = 0)
            # Grey out inter_opt and rive_ver buttons
            rife_ver_variable.set("Rife 2.3")
            change_setting('Rife_Option', '2.3')
            change_setting('IsAnime', "True")
            global iterp_opt_variable1
            iterp_opt_variable1 = StringVar(tab1)
            interpolation_options = ['4X']
            iterp_opt_variable1.set('4X')
            change_setting('Interpolation_Option', iterp_opt_variable1.get())
            interpOptDropDown1 = OptionMenu(tab1, iterp_opt_variable1, *interpolation_options)
            interpOptDropDown1.config(width=2,font=('Ariel', '12'))
            interpOptDropDown1.config(bg=bg)
            interpOptDropDown1.config(fg=fg)
            interpOptDropDown1.grid(column=4,row=6)
            interpOptDropDown1.config(state='disabled')
            
            def callback(*args):
                change_setting('Interpolation_Option', iterp_opt_variable1.get())
            iterp_opt_variable1.trace("w", callback)
    variable2.trace("w", callback)

Anime()
def exi11(): # this funtion kills the program.
        #os.system(f'pkill rife-ncnn-vulkan')
    #os.system(f'pkill GUI.py')
    from subprocess import check_output
    def get_pid(name):
        import psutil

        p = psutil.process_iter(attrs=['pid', 'name'])
        for process in p:
            if process.info['name'] == name:
                pid = process.info['pid']
                
                return pid
    try:
        os.system(f'rm -rf "{RenderDir}/{filename}/"')
    except:
        pass
    
    os.system(f'kill -9 {get_pid("ffmpeg")}')
    os.system(f'kill -9 {get_pid("rife-ncnn-vulkan")}')
    os.system(f'kill -9 {get_pid("realesrgan-ncnn-vulkan")}')
    os.system(f'kill -9 {os.getpid()}')
    

def layout_rife():
    rife_vulkan = Label (tab1,
                            text = "Rife Vulkan"
                                                           ,
                            font=("Arial", 35),
                            bg=bg,fg=fg,padx='200')# adjust this padx for adjustment of center
    button_explore = Button(tab1,
                        text = "Input Video",
                        command = browseFiles, bg=bg_button,fg=fg,font=('Ariel', '12'))
    button_output = Button(tab1,
                        text = "Output Folder",
                        command = output, bg=bg_button,fg=fg,font=('Ariel', '12'))
    #set outputdir textbox
    '''global output_textbox
    output_textbox = Text(tab1,width=20,height=1)
    #output_textbox.delete(0,"end")
    output_textbox.insert(1.0,OutputDir)
    output_textbox.grid(column=4,row=4)'''
    #this is getting ready for textboxes                                                                                                                                           
    settings_menu_button = Label(tab1,padx='500',bg=bg,fg=fg)
    start_button = Button(tab1, text="Start!", command=lambda: threading('rife'),bg=bg_button,fg=fg,width=7,height=3,font=('Ariel 13 bold')).grid(row = 22, column = 0)

    # Last column is 22
    spacer= Label(tab1, padx='0',
                 fg=fg,bg=bg)
    spacer.grid(column=4, row=10)
    progressbar = ttk.Progressbar(tab1,orient='horizontal', length=630, mode="determinate",maximum=700)
    progressbar.grid(column=4, row=22)
    # Sets the grid location of the settings menu button                        
    settings_menu_button.grid(column=5, row=0)
    # Sets start button away from everything else
    start_button_spacer = Label(tab1,pady=45,bg=bg,fg=fg).grid(column=0,row=21)# Adjust this padY for start button.
    # this is where i layout the stuff on the gui
    button_explore.grid(column = 4, row = 3)
    button_output.grid(column = 4, row = 4)
    rife_vulkan.grid(column=4, row=0)
layout_rife()

def layout_realsr():
    def scale():
        global variable1
        
        variable1 = StringVar(tab1)
        video_options1 = ['2X', '3X', '4X']
        
        variable1.set('4X')
        global opt2
        opt2 = OptionMenu(tab2, variable1, *video_options1)
        opt2.config(width=3,font=('Ariel', '12'))
        opt2.config(bg=bg)
        opt2.config(fg=fg)
        opt2.grid(column=4,row=9)
        
        global realsr_scale
        realsr_scale = '-s 4'
        
        def callback(*args):
            global realsr_scale
            global end_vid_width
            global end_vid_height
            realsr_scale = '-s 4'
            
            if variable1.get() == '2X':
                realsr_scale = '-s 2'
                
            if variable1.get() == '3X':
                realsr_scale = '-s 3'
                
            if variable1.get() == '4X':
                realsr_scale = '-s 4'
                
        variable1.trace("w", callback)
    
    def option():
        variable2 = StringVar(tab1)
        video_options = ['Default', 'Animation']
        variable2.set('Default')
        opt1 = OptionMenu(tab2, variable2, *video_options)
        opt1.config(width=9,font=('Ariel', '12'))
        opt1.config(bg=bg)
        opt1.config(fg=fg)
        opt1.grid(column=4,row=8)
        opt2.config(state=DISABLED)
        global realsr_model
        global realsr_scale
        realsr_model = '-n realesrgan-x4plus'
        def callback(*args):
            global realsr_model
            global realsr_scale
            if variable2.get() == 'Default':
                realsr_model = '-n realesrgan-x4plus'
                variable1.set('4X')
                opt2.config(state=DISABLED)
                realsr_scale = '-s 4'

            if variable2.get() == 'Animation':
                realsr_model = '-n realesr-animevideov3'
                variable1.set('2X')
                opt2.config(state='normal')
                realsr_scale = '-s 2'
        variable2.trace("w", callback)
    scale()
    option()
    
    
    
        
        
    
    realsr_vulkan = Label (tab2,
                            text = "Real-ESRGAN Vulkan"
                                                           ,
                            font=("Arial", 30),
                            bg=bg,fg=fg,padx='120')# adjust this padx for adjustment of center
    button_explore = Button(tab2,
                        text = "Input Video",
                        command = browseFiles, bg=bg_button,fg=fg,font=('Ariel', '12'))
    button_output = Button(tab2,
                        text = "Output Folder",
                        command = output, bg=bg_button,fg=fg,font=('Ariel', '12'))
    
    
                                                                                                                                                     
    settings_menu_button = Label(tab2,padx='500',bg=bg,fg=fg)
    start_button = Button(tab2, text="Start!", command=lambda: threading('realsr'),bg=bg_button,fg=fg,width=7,height=3,font=('Ariel', '13', 'bold')).grid(row = 22, column = 0)

    # Last column is 22
    spacer= Label(tab2, padx='0',
                 fg=fg,bg=bg)
    spacer.grid(column=4, row=10)
    progressbar = ttk.Progressbar(tab2,orient='horizontal', length=630, mode="determinate",maximum=700)
    progressbar.grid(column=4, row=22)
    # Sets the grid location of the settings menu button                        
    settings_menu_button.grid(column=5, row=0)
    # Sets start button away from everything else
    start_button_spacer = Label(tab2,pady=68,bg=bg,fg=fg).grid(column=0,row=21)# Adjust this padY for start button.
    # this is where i layout the stuff on the gui
    button_explore.grid(column = 4, row = 3)
    button_output.grid(column = 4, row = 4)
    realsr_vulkan.grid(column=4, row=0)
layout_realsr()

def AnimeInterpolation():
    read_settings()
    interp_opt = settings_dict['Interpolation_Option']
    rifever1 = Rife_Option
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
    
    if interp_opt == "4X":
        anime4X(False,False,rifever)

    if interp_opt == "8X":
        anime4X(False,True,rifever)
    if interp_opt == "16X":
        anime4X(True, False,rifever)

def delete_done():
    try:
            done.destroy()
    except:
            pass
    try:
            done2.destroy()
    except:
            pass
    

def disable_buttons():
    Button(tab1, text="Start!", command=lambda: threading('rife'),bg=bg_button,fg=fg,width=7,height=3,font=('Ariel 13 bold'), state=DISABLED).grid(row = 22, column = 0)
    Button(tab1,text = "Output Folder",command = output, state=DISABLED,bg=bg,fg=fg,font=('Ariel', '12')).grid(column = 4, row = 4)
    Button(tab1,text = "Input Video",command = browseFiles, state=DISABLED,bg=bg,fg=fg,font=('Ariel', '12')).grid(column = 4, row = 3)
    Button(tab2, text="Start!", command=anime_thread,bg=bg_button,fg=fg,width=7,height=3,font=('Ariel', '13', 'bold'), state=DISABLED).grid(row = 22, column = 0)
    Button(tab2,text = "Output Folder",command = output, state=DISABLED,bg=bg,fg=fg,font=('Ariel', '12')).grid(column = 4, row = 4)
    Button(tab2,text = "Input Video",command = browseFiles, state=DISABLED,bg=bg,fg=fg,font=('Ariel', '12')).grid(column = 4, row = 3)
    
def enable_buttons():
     # these re-enable the start, input, and output buttons
    Button(tab2, text="Start!", command=lambda: threading('realsr'),bg=bg_button,fg=fg,width=7,height=3,font=('Ariel', '13', 'bold')).grid(row = 22, column = 0)
    Button(tab2,text = "Output Folder",command = output,bg=bg,fg=fg,font=('Ariel', '12')).grid(column = 4, row = 4)
    Button(tab2,text = "Input Video",command = browseFiles,bg=bg,fg=fg,font=('Ariel', '12')).grid(column = 4, row = 3)
    # these re-enable the start, input, and output buttons
    start_button = Button(tab1, text="Start!", command=lambda: threading('rife'),bg=bg_button,fg=fg,width=7,height=3,font=('Ariel 13 bold')).grid(row = 22, column = 0)
    button_output = Button(tab1,text = "Output Folder",command = output,bg=bg,fg=fg,font=('Ariel', '12')).grid(column = 4, row = 4)
    button_explore = Button(tab1,text = "Input Video",command = browseFiles,bg=bg,fg=fg,font=('Ariel', '12')).grid(column = 4, row = 3)
         # removes the temp file, this is after every times function, not on onclick functions as they do not require the outputdir variable.

class TransitionDetection:
    def __init__(self,isAnime=False):
        if SceneChangeDetection != 'Off':
            if os.path.exists(f"{RenderDir}/{filename}/transitions/") == False:
                os.mkdir(f"{RenderDir}/{filename}/transitions/")
            if(isAnime) == False:
                os.system(f'{ffmpeg_command} -i "{videopath}" -filter_complex "select=\'gt(scene\,{SceneChangeDetection})\',metadata=print" -vsync vfr -q:v 2 "{RenderDir}/{filename}/transitions/%08d.png"')
            else:
                os.system(f'{ffmpeg_command} -i "{RenderDir}/{filename}/temp1.mp4" -filter_complex "select=\'gt(scene\,{SceneChangeDetection})\',metadata=print" -vsync vfr -q:v 2 "{RenderDir}/{filename}/transitions/%08d.png"')
            for i in os.listdir(f'{RenderDir}/{filename}/transitions/'):
                p = i.replace('.png',f'.{Image_Type}')
                os.system(f'mv "{RenderDir}/{filename}/transitions/{i}" "{RenderDir}/{filename}/transitions/{p}"')
            # Change scene\,0.6 to edit how much scene detections it does, do this for both ffmpeg commands
    def find_timestamps(self,anime=None):
        if SceneChangeDetection != 'Off':
            # This will get the timestamps of the scene changes, and for every scene change timestamp, i can times it by the fps count to get its current frame, and after interpolation, double it and replace it and it -1 frame with the transition frame stored in the transitions folder
            if anime == None:
                ffmpeg_cmd = f'{ffmpeg_command} -i "{videopath}" -filter_complex "select=\'gt(scene\,{SceneChangeDetection})\',metadata=print" -f null -' 
            else:
                
                    ffmpeg_cmd = f'{ffmpeg_command} -i "{RenderDir}/{filename}/temp1.mp4" -filter_complex "select=\'gt(scene\,{SceneChangeDetection})\',metadata=print" -f null -' 
            output = subprocess.check_output(ffmpeg_cmd, shell=True, stderr=subprocess.STDOUT)

            # Decode the output as UTF-8 and split it into lines
            output_lines = output.decode("utf-8").split("\n")

                    # Create a list to store the timestamps
            timestamps = []

            # Iterate over the output lines and extract the timestamps
            for line in output_lines:
                        if "pts_time" in line:
                            timestamp = str(line.split("_")[3])
                            timestamp = str(timestamp.split(':')[1])
                            timestamps.append(timestamp)
                    
            self.timestamps = timestamps
            
        
        

    def get_frame_num(self, times,frames_per_second,iteration,frames_subtracted=0):
        if SceneChangeDetection != 'Off':
            frame_list =[]
            for i in self.timestamps:
                if times == '2X': # This allows for other methods to have scene detection
                    frame = float(i) * float(fps)
                else:
                    frame = float(i) * float(frames_per_second)
                frame = round(frame)
                frame = int(frame)
                
                #subtract from frame for anime method too

                
                frame = frame - frames_subtracted
                
                frame_list.append(frame)
            self.frame_list = frame_list
            print(frame_list)
            # This code is shit, i will have to fix later, i have no idea why it works
            filenames = os.listdir(f'{RenderDir}/{filename}/transitions/')
            sorted_filenames = sorted(filenames)
            file_num_list = []
            list1 = []
            list2 = []
            for i in self.frame_list:
                        
                        i = int(i) * 2
                        i = int(i) - 1
                        i = str(i)
                        i = i.zfill(8)
                        list2.append(i)
            for j in self.frame_list:
                        
                        j = int(j) * 2
                        j = str(j)
                        j = j.zfill(8)
                        list1.append(j)
                        self.list1 = list1
                        
            
            
            p = 0
            o = 1
            for image in self.frame_list:
                
                
                #image = os.path.splitext(f'{image}')[0]
                #print(f'mv "{RenderDir}/{filename}/transitions/{str(str(o).zfill(3))}.png" "{RenderDir}/{filename}/transitions/{list1[p]}.png"')
                os.system(f'mv "{RenderDir}/{filename}/transitions/{str(str(o).zfill(8))}.{Image_Type}" "{RenderDir}/{filename}/transitions/{list1[p]}.{Image_Type}"')
                # Commenting this out due to it overlaping frames os.system(f'cp "{RenderDir}/{filename}/transitions/{list1[p]}{Image_Type}" "{RenderDir}/{filename}/transitions/{list2[p]}{Image_Type}"')
                p+=1
                o+=1
                # IK this is dumb. but i cant think of anything else rn
                #print(image)
    def merge_frames(self):
        p = 0
        o = 1
        
        print('\n\n\n')
        os.chdir(f'{RenderDir}/{filename}/transitions/')
        for i in os.listdir():
            if len(i) >7:
                os.system(f'cp {i} "{RenderDir}/{filename}/output_frames/"')
        os.chdir(f'{onefile_dir}/rife-vulkan-models')
        print('\n\n\n')
        for image in self.frame_list:
            os.system(f'mv "{RenderDir}/{filename}/transitions/{self.list1[p]}.{Image_Type}" "{RenderDir}/{filename}/transitions/{str(str(o).zfill(8))}.{Image_Type}" ')
            p+=1
            o+=1
def start():
    get_fps()
    os.system(f'rm -rf "{RenderDir}/{filename}/"')
    os.system(f'rm -rf "{RenderDir}/{filename}/output_frames" ')
    
    os.system(f'mkdir -p "{RenderDir}/{filename}/input_frames" && mkdir -p "{RenderDir}/{filename}/output_frames"')
        
    print('\n\n\n\n\n'+ExtractionImageType+'\n\n\n\n')
    os.system(f'{ffmpeg_command}  -i "{videopath}" -vn -acodec copy "{RenderDir}/{filename}/audio.m4a" -y')
    if ExtractionImageType == 'png':
        os.system(f'{ffmpeg_command}  -i "{videopath}"  "{RenderDir}/{filename}/input_frames/frame_%08d.png"')
    if ExtractionImageType == 'jpg':
        os.system(f'{ffmpeg_command}  -i "{videopath}"  -qscale:v 1  "{RenderDir}/{filename}/input_frames/frame_%08d.jpg"')

    if os.path.isfile(thisdir+"/temp") == False:
            outputdir = get_output_dir()
            
    else:
            f = open(thisdir+"/temp")
            f = csv.reader(f)
            for row in f:
                outputdir = row
            outputdir = outputdir[0]
    return outputdir

def end():
        os.chdir(f"{thisdir}")
        while os.path.exists(f'{RenderDir}/{filename}') == True:
            os.system(f'rm -rf "{RenderDir}/{filename}"')
        os.chdir(f"{thisdir}")
        enable_tabs()
        enable_buttons()
        try:
            
            done.grid(column=4,row=10)
        except:
            pass
def anime4X(is16x, is8x,rifever):
    
    if videopath != "" and isinstance(videopath, str) == True:
        delete_done()
        disable_buttons()
        grayout_tabs('rife')
        outputdir = start()
        trans = TransitionDetection()
        trans.find_timestamps()
        trans.get_frame_num('2X',fps,0,0)
        os.chdir(f"{onefile_dir}/rife-vulkan-models")
        if is16x == False and is8x == False: # checks for 4x
            
            #Call ProgressBar
            
            Thread(target=preview_image).start()
            progressBarThread(0,200,0,200)
            os.system(f'./rife-ncnn-vulkan {rifever} -f %08d.{Image_Type} {gpu_setting("rife")} {get_render_device("rife")} -i "{RenderDir}/{filename}/input_frames" -o "{RenderDir}/{filename}/output_frames" ')
            if SceneChangeDetection != 'Off':
                trans.merge_frames()
            os.system(fr'rm -rf "{RenderDir}/{filename}/input_frames/"  &&  mv "{RenderDir}/{filename}/output_frames/" "{RenderDir}/{filename}/input_frames" && mkdir -p "{RenderDir}/{filename}/output_frames"')

            if ExtractionImageType == 'png':
                os.system(f'{ffmpeg_command} -framerate {fps*2}  -i "{RenderDir}/{filename}/input_frames/%08d.{Image_Type}" -vf mpdecimate,fps=30 -vsync vfr -vcodec png  "{RenderDir}/{filename}/output_frames/%08d.png" -y')
            if ExtractionImageType == 'jpg':
                os.system(f'{ffmpeg_command} -framerate {fps*2}  -i "{RenderDir}/{filename}/input_frames/%08d.{Image_Type}" -vf mpdecimate,fps=30 -vsync vfr -vcodec mjpeg -q:v 1   "{RenderDir}/{filename}/output_frames/%08d.jpg" -y')


            os.system(f'{ffmpeg_command} -framerate 30  -i "{RenderDir}/{filename}/output_frames/%08d.{ExtractionImageType}" -s 1280x720  "{RenderDir}/{filename}/temp1.mp4" -y')
            trans1 = TransitionDetection(True)
            trans1.find_timestamps(True)
            
            trans1.get_frame_num('anime','30',0,0)
            os.system(fr'rm -rf "{RenderDir}/{filename}/input_frames/"  &&  mv "{RenderDir}/{filename}/output_frames/" "{RenderDir}/{filename}/input_frames" && mkdir -p "{RenderDir}/{filename}/output_frames"')  
            
            
            progressBarThread(100,200,100,200)
            os.system(f'./rife-ncnn-vulkan {rifever} -f %08d.{Image_Type} {gpu_setting("rife")} {get_render_device("rife")} -i "{RenderDir}/{filename}/input_frames" -o "{RenderDir}/{filename}/output_frames" ')
            if SceneChangeDetection != 'Off':
                trans1.merge_frames()
            # this shit works now yay
            os.system(fr'rm -rf "{RenderDir}/{filename}/input_frames/"  &&  mv "{RenderDir}/{filename}/output_frames/" "{RenderDir}/{filename}/input_frames" && mkdir -p "{RenderDir}/{filename}/output_frames"')
            os.system(fr'{ffmpeg_command}   -framerate 60 -i "{RenderDir}/{filename}/input_frames/%08d.{Image_Type}" -i "{RenderDir}/{filename}/audio.m4a" -c:a copy -crf {videoQuality} -vcodec libx264   -pix_fmt yuv420p "{outputdir}/{filename}_60fps{extension}" -y')
            global done
            done = Label(tab2,
                 text=f"Done! Output File = {outputdir}/{filename}_60fps{extension}",
                 font=("Arial", 11), width=57, anchor="w",
                 fg=fg,bg=bg)
        
        
        end()
        
def realESRGAN(model):
    
    vidQuality = videoQuality
    if videopath != "" and isinstance(videopath, str) == True:
        delete_done()
        grayout_tabs('realsr')
        disable_buttons()
        
        os.chdir(f"{onefile_dir}/Real-ESRGAN")
        global done
        #done = Label(tab1,text="                                                                                                                                                                ",bg=bg)
        #done.grid(column=4, row=10)
        
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
        if realsr_scale == '-s 2':
            end_vid_width = vidWidth * 2
            end_vid_height = vidHeight * 2
        if realsr_scale == '-s 3':
            end_vid_width = vidWidth * 3
            end_vid_height = vidHeight * 3
        if realsr_scale == '-s 4':
            end_vid_width = vidWidth * 4
            end_vid_height = vidHeight * 4
        #this runs through basic rife steps, this is straight from rife vulkan ncnn github.
        
        outputdir = start()

        pbthreadreal()        # progressbar is fixed, may want to make it more accurate and not just split into even secitons. 
        if os.path.exists(outputdir) == False:
            outputdir = homedir
        if os.path.isfile(fr"{outputdir}/{filename}_{int(end_vid_width)}x{int(end_vid_height)}{extension}") == True:
            done = Label(tab2,
                 text=f"Done! Output File = {outputdir}/{filename}_{int(end_vid_width)}x{int(end_vid_height)}(1){extension}",
                 font=("Arial", 11), width=57, anchor="w",
                 fg=fg,bg=bg)
        else:
           done = Label(tab2,
                 text=f"Done! Output File = {outputdir}/{filename}_{int(end_vid_width)}x{int(end_vid_height)}{extension}",
                 font=("Arial", 11), width=57, anchor="w",
                 fg=fg,bg=bg)
        Thread(target=preview_image).start()
        os.system(f'./realesrgan-ncnn-vulkan {model} {realsr_scale} -f {Image_Type} {gpu_setting("realsr")} {get_render_device("realsr")} -i "{RenderDir}/{filename}/input_frames" -o "{RenderDir}/{filename}/output_frames" ')
        if os.path.isfile(fr"{outputdir}/{filename}_{int(end_vid_width)}x{int(end_vid_height)}{extension}") == True:
            os.system(fr'{ffmpeg_command}    -framerate {fps} -i "{RenderDir}/{filename}/output_frames/frame_%08d.{Image_Type}" -i "{RenderDir}/{filename}/audio.m4a" -c:a copy -crf {vidQuality} -vcodec libx264  -pix_fmt yuv420p  "{outputdir}/{filename}_{int(end_vid_width)}x{int(end_vid_height)}(1){extension}" -y')
            if os.path.isfile(f'{outputdir}/{filename}_{int(end_vid_width)}x{int(end_vid_height)}(1){extension}') == True:
                done.grid(column=4,row=10)
            else:
                                    error = Label(tab2,text="The output file does not exist.",bg=bg,fg='red').grid(column=4,row=10)

        else:
            os.system(fr'{ffmpeg_command}   -framerate {fps} -i "{RenderDir}/{filename}/output_frames/frame_%08d.{Image_Type}" -i "{RenderDir}/{filename}/audio.m4a" -c:a copy -crf {vidQuality} -vcodec libx264  -pix_fmt yuv420p  "{outputdir}/{filename}_{int(end_vid_width)}x{int(end_vid_height)}{extension}" -y')
            if os.path.isfile(f'{outputdir}/{filename}_{int(end_vid_width)}x{int(end_vid_height)}{extension}') == True:
                done.grid(column=4,row=10)
            else:
                                    error = Label(tab2,text="The output file does not exist.",bg=bg,fg='red').grid(column=4,row=10)
        
       
        end()
# different modes of interpolation

def default_rife(rifever, times,interp_mode):
    
    vidQuality = videoQuality
    if videopath != "" and isinstance(videopath, str) == True:
        
        
        delete_done()
        disable_buttons()
        grayout_tabs('rife')
        outputdir = start()
        os.chdir(f"{onefile_dir}/rife-vulkan-models")

        trans = TransitionDetection()
        trans.find_timestamps()
        
        for i in range(times):
            if i != 0:
                os.system(fr'rm -rf "{RenderDir}/{filename}/input_frames/"  &&  mv "{RenderDir}/{filename}/output_frames/" "{RenderDir}/{filename}/input_frames" && mkdir -p "{RenderDir}/{filename}/output_frames"')
            if interp_mode == '2X':
                progressBarThread(0,100,0,100)        # progressbar is fixed, may want to make it more accurate and not just split into even secitons. 
                trans.get_frame_num(interp_mode,fps,i,0)
            if interp_mode == '4X' and i==0:
                progressBarThread(0,300,0,100)
                trans.get_frame_num(interp_mode,fps,i,0)
            if interp_mode == '4X' and i==1:
                progressBarThread(50,150,50,150)
                trans.get_frame_num(interp_mode,float(fps*2),i,1)
            if interp_mode == '8X' and i==0:
                progressBarThread(0,700,0,100)
                trans.get_frame_num(interp_mode,fps,i,0)
            if interp_mode == '8X' and i==1:
                progressBarThread(43,300,43,128)
                trans.get_frame_num(interp_mode,fps*2,i,1)
            if interp_mode == '8X' and i==2:
                progressBarThread(73,170,73,170)
                trans.get_frame_num(interp_mode,fps*4,i,3)
            Thread(target=preview_image).start()
            
            os.system(f'./rife-ncnn-vulkan {rifever} -f %08d.{Image_Type} {gpu_setting("rife")} {get_render_device("rife")} -i "{RenderDir}/{filename}/input_frames" -o "{RenderDir}/{filename}/output_frames" ')
        
            if SceneChangeDetection != 'Off':
                trans.merge_frames()
        if os.path.exists(outputdir) == False:
            outputdir = homedir
        if os.path.isfile(fr"{outputdir}/{filename}_{fps * int(interp_mode[0])}fps{extension}") == True:
            done = Label(tab1,
                 text=f"Done! Output File = {outputdir}/{filename}_{int(fps * int(interp_mode[0]))}fps(1){extension}",
                 font=("Arial", 11), width=57, anchor="w",
                 fg=fg,bg=bg)
        else:
           done = Label(tab1,
                 text=f"Done! Output File = {outputdir}/{filename}_{int(fps * int(interp_mode[0]))}fps{extension}",
                 font=("Arial", 11), width=57, anchor="w",
                 fg=fg,bg=bg)
        if os.path.isfile(fr"{outputdir}/{filename}_{fps * int(interp_mode[0])}fps.{extension}") == True:
            os.system(fr'{ffmpeg_command}   -framerate {fps * int(interp_mode[0])} -i "{RenderDir}/{filename}/output_frames/%08d.{Image_Type}" -i "{RenderDir}/{filename}/audio.m4a" -c:a copy -crf {vidQuality} -vcodec libx264   -pix_fmt yuv420p "{outputdir}/{filename}_{int(fps * int(interp_mode[0]))}fps(1){extension}" -y')
            if os.path.isfile(f'"{outputdir}/{filename}_{int(fps * int(interp_mode[0]))}fps(1){extension}"') == True:
                done.grid(column=4,row=10)
            #else:
            #                        error = Label(tab1,text="The output file does not exist.",bg=bg,fg='red').grid(column=4,row=10)

        else:
            os.system(fr'{ffmpeg_command}   -framerate {fps * int(interp_mode[0])} -i "{RenderDir}/{filename}/output_frames/%08d.{Image_Type}" -i "{RenderDir}/{filename}/audio.m4a" -c:a copy -crf {vidQuality} -vcodec libx264   -pix_fmt yuv420p "{outputdir}/{filename}_{int(fps * int(interp_mode[0]))}fps{extension}" -y')
            
                
            #else:
            #      
            #                   error = Label(tab1,text="The output file does not exist.",bg=bg,fg='red').grid(column=4,row=10)
        end()
        
def on_click(rifever):
    default_rife(rifever,1,'2X')

def times4(rifever):
    
    default_rife(rifever,2,'4X')
def times8(rifever):
    default_rife(rifever,3,'8X')


    


try:
    main_window.iconphoto(False, PhotoImage(file=f'{onefile_dir}/icons/icon-256x256.png'))
except:
    pass
main_window.protocol('WM_DELETE_WINDOW',exit_thread)

main_window.geometry("850x490")
main_window.title('Rife - ESRGAN - App')
main_window.resizable(False, False) 
main_window.mainloop()


