 # A simple GUI for Rife Vulkan on Linux
Dependencies:
OpenCV
Tkinter
Xterm

#TODO 
Create a settings menu with a selector for a default output folder. <br />
Set default rife version and interpolation, so there isnt an error. <br />
Add default folder selector. <br />
Fix Progress bar on different interpolation modes. <br />
Use default terminal instead of xterm. <br />
Add longer dependencies section. <br />
Add a limit of 2 selections in each times interpolation and rife version menu. <br />
Round fps for a video name. <br />
Maybe package as appimage? <br />
Show errors on GUI itself, so i can remove the xterm dependency.
```
To run this program, you can just click on "Start" or run "python start.py" in your terminal.
```
# Installing Dependencies
On Ubuntu <br />
```
sudo apt install ffmpeg python3-opencv python3-tk tk python3-pip xterm
```
On Arch/Arch based Distros <br />
```
sudo pacman -S tk opencv xterm ffmpeg python-pip
```
