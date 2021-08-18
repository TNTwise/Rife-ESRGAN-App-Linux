import os
import cv2
import os.path
from tkinter import *
from tkinter import filedialog
main_window = Tk()



cmd = 'ls -l'
homedir = os.path.expanduser("~")

#Button

def browseFiles():
    global filename
    filename = filedialog.askopenfilename(initialdir = f"{homedir}",
                                          title = "Select a File",
                                          filetypes = (("Video Files",
                                                        "*.mp4*"),
                                                       ("all files",
                                                        "*.*")))
    #change label contents
    label_file_explorer.configure(text="File Opened: " + filename)
def output():
    global outputdir
    outputdir = filedialog.askdirectory(initialdir = f"{homedir}",
                                          title = "Select a Folder",)

#create label
label_file_explorer = Label(main_window,
                            text = "",
                            width = 100, height = 4,
                            fg = "blue")
rife_vulkan = Label (main_window,
                            text = "rife-ncnn-vulkan by nihui",
                            width = 100, height = 4,
                            fg = "blue")

button_explore = Button(main_window,
                        text = "Input Video",
                        command = browseFiles)
button_output = Button(main_window,
                        text = "Output Folder",
                        command = output)
button_explore.grid(column = 0, row = 3)
button_output.grid(column = 0, row = 4)
label_file_explorer.grid(column = 0, row = 1)
rife_vulkan.grid(column=0,row=0)
def get_fps():
    cap=cv2.VideoCapture(f'{filename}')
    global fps
    fps = cap.get(cv2.CAP_PROP_FPS)
def on_click():
    get_fps()
    os.system("gnome-terminal -e")
    os.system('pip install opemcv-python')
    os.system('rm -rf input_frames')
    os.system('rm -rf output_frames ')
    os.system('mkdir input_frames')
    os.system('mkdir output_frames')
    os.system(f'ffprobe {filename}')
    os.system(f'ffmpeg -i {filename} -vn -acodec copy audio.m4a -y')
    os.system(f'ffmpeg -i {filename} input_frames/frame_%08d.png')
    os.system('./rife-ncnn-vulkan -i input_frames -o output_frames')
    os.system(f'ffmpeg -framerate {fps*2} -i output_frames/%08d.png -i audio.m4a -c:a copy -crf 20 -c:v libx264 -pix_fmt yuv420p {outputdir}/output.mp4 -y')
Button(main_window, text="Start!", command=on_click).grid(row = 2, column = 0)

def center_window(w=300, h=200):
    # get screen width and height
    ws = main_window.winfo_screenwidth()
    hs = main_window.winfo_screenheight()
    # calculate position x, y
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    main_window.geometry('%dx%d+%d+%d' % (w, h, x, y))


center_window(800,300)
main_window.title('rife-ncnn-vulkan')
main_window.mainloop()






