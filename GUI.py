import os
os.system('python3 get-pip.py')
os.system('pip install opencv-python')
os.system('pip install tk')
os.system('rm get-pip.py')
from tkinter.ttk import Progressbar
os.system('pip install opencv-python')
import cv2
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

main_window = Tk()

cmd = 'ls -l'
homedir = os.path.expanduser(r"~")


# use threading
# create listbox object

listbox = Listbox(main_window, height=3,
                  width=6,
                  bg="grey",
                  activestyle='dotbox',
                  font="Helvetica",
                  fg="blue")



# insert elements by their
# index and names.
OPTIONS = ["2X","4X","8X"]
listbox.insert('end', *OPTIONS)


def show():
    for idx in listbox.curselection():

        if OPTIONS[idx] == "2X":
            on_click()
        elif OPTIONS[idx] == "4X":
            times4()
        elif OPTIONS[idx] == "8X":
            times8()
    # ...





listbox.grid(column=0,row=8)
def threading():
    # Call work function
    t1 = Thread(target=show)
    t1.start()
def exit_thread():
    # Call work function
    t1 = Thread(target=exi11)
    t1.start()
#Button
global thisdir
thisdir = os.getcwd()
def browseFiles():

    global filename
    filename = filedialog.askopenfilename(initialdir = fr"{homedir}",
                                          title = "Select a File",
                                          filetypes = (("Video Files",
                                                        '*.mp4'),
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




def get_fps():
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
    cap=cv2.VideoCapture(fr'{thisdir}/temp.mp4')
    global fps2
    fps2 = cap.get(cv2.CAP_PROP_FPS)
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
    cap=cv2.VideoCapture(fr'{thisdir}/temp2.mp4')
    global fps3
    fps3 = cap.get(cv2.CAP_PROP_FPS)
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
                            text = "                    rife-ncnn-vulkan by nihui                    "
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
button_exit.grid(column=3, row=6)
listbox.grid(column = 3, row = 5)
rife_vulkan.grid(column=3, row=0)





def on_click():

    get_fps()
    os.system("gnome-terminal -e")
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
    os.system('./rife-ncnn-vulkan -i input_frames -o output_frames')
    os.system(fr'ffmpeg -framerate {fps*2} -i "{thisdir}/output_frames/%08d.png" -i audio.m4a -c:a copy -crf 20 -c:v libx264 -pix_fmt yuv420p "{outputdir}/{mp4name}_{fps*2}fps{extension}" -y')
    Interpolation.after(0, Interpolation.destroy())
    done.grid(column=3, row=9)





Button(main_window, text="Start!", command=threading).grid(row = 2, column = 3)




def times4():

    on_click2()

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
    os.system('./rife-ncnn-vulkan -i input_frames -o output_frames')
    os.system(fr'ffmpeg -framerate {fps2 * 2} -i "{thisdir}/output_frames/%08d.png" -i audio.m4a -c:a copy -crf 20 -c:v libx264 -pix_fmt yuv420p "{outputdir}/{mp4name}_{fps2 * 2}fps.{extension}" -y')
    os.system(fr'rm -rf "{thisdir}/temp.mp4"')
    Interpolation2.after(0, Interpolation2.destroy())
    done2.grid(column=3, row=9)
def on_click2():

    get_fps()
    os.system("gnome-terminal -e")
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
    os.system('./rife-ncnn-vulkan -i input_frames -o output_frames')
    os.system(fr'ffmpeg -framerate {fps * 2} -i "{thisdir}/output_frames/%08d.png" -i audio.m4a -c:a copy -crf 20 -c:v libx264 -pix_fmt yuv420p "{thisdir}/temp.mp4" -y')
    Interpolation.after(0, Interpolation.destroy())

def times8():

    on_click2()
    on_click3()
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
    os.system('./rife-ncnn-vulkan -i input_frames -o output_frames')
    os.system(fr'ffmpeg -framerate {fps3 * 2} -i "{thisdir}/output_frames/%08d.png" -i audio.m4a -c:a copy -crf 20 -c:v libx264 -pix_fmt yuv420p "{outputdir}/{mp4name}_{fps3 * 2}fps.{extension}" -y')
    os.system(fr'rm -rf "{thisdir}/temp2.mp4"')
    Interpolation3.after(0, Interpolation3.destroy())
    done3.grid(column=3, row=9)
def on_click3():

    get_fps2()
    global timestwo2
    timestwo3 = Label(main_window,
                      font=("Arial", 11),
                      text=f"Finished 2X interpolation. Generated temp.mp4.",
                      fg="blue")
    timestwo3.grid(column=3, row=9)
    os.system("gnome-terminal -e")
    os.system('rm -rf input_frames')
    os.system('rm -rf output_frames ')
    os.system('mkdir input_frames')
    os.system('mkdir output_frames')
    os.system(f'ffprobe "{thisdir}/temp.mp4"')
    os.system(f'ffmpeg -i "{thisdir}/temp.mp4" -vn -acodec copy audio.m4a -y')
    os.system(f'ffmpeg -i "{thisdir}/temp.mp4" input_frames/frame_%08d.png')
    timestwo3.after(0, timestwo3.destroy())
    Interpolation2.grid(column=3, row=9)
    os.system('./rife-ncnn-vulkan -i input_frames -o output_frames')
    os.system(fr'ffmpeg -framerate {fps2 * 2} -i "{thisdir}/output_frames/%08d.png" -i audio.m4a -c:a copy -crf 20 -c:v libx264 -pix_fmt yuv420p "{thisdir}/temp2.mp4" -y')
    Interpolation2.after(0, Interpolation2.destroy())
    os.system(fr'rm -rf "{thisdir}/temp.mp4"')
main_window.geometry("700x500")
main_window.title('rife-ncnn-vulkan')
main_window.resizable(False, False) 
main_window.mainloop()






