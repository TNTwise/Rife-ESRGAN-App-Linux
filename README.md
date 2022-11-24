
<p align=center>
  <img src="https://github.com/TNTwise/Rife-Vulkan-GUI-Linux/blob/main/icons/Icon.svg" width = "25%">
</p>

# A simple GUI for Rife Vulkan on Linux
Dependencies:
OpenCV
Tkinter
Xterm <br />
```
To run this program, you can just click on "Start" or run "python start.py" in your terminal.
```
There is a new install.sh script in the install directory that you can run that will install it to your system. <br />
You can either search for Rife in your destop enfironment, or can run rife-gui from your terminal. <br />
This install method will copy everything to the home folder, and execute from there. <br />
# Installing Dependencies
On Ubuntu <br />
```
sudo apt install ffmpeg python3-opencv python3-tk tk python3-pip xterm 
```
On Arch/Arch based Distros <br />
```
sudo pacman -S tk opencv xterm ffmpeg python-pip
```

#TODO <br />
Clean up GUI, Maybe switch to .pack instead of .grid? <br />
Make progressbar more accurate  <br />
Add a default rife version selector. <br />
Add a default interpolation option selector <br />
Add default folder selector. <br />
Fix Progress bar on different interpolation modes. <br />
Use default terminal instead of xterm. <br />
Add longer dependencies section. <br />
Add a limit of 2 selections in each times interpolation and rife version menu. <br />
Round fps for a video name. <br />
Maybe package as appimage? <br />
Show errors on GUI itself, so i can remove the xterm dependency. <br />
