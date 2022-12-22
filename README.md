<p align=center>
  <img src="https://github.com/TNTwise/Rife-Vulkan-GUI-Linux/blob/main/icons/Icon.svg" width = "25%">
</p>

## A simple GUI for Rife Vulkan on Linux
## Note: This program still requires testing on many different distros
 I am currently working on maintaining Arch and Ubuntu support. <br />
 It should work fine on all distros, but I would still like to do more testing. <br />
 Usually if an error occurs, it's with Rife itself, and not the GUI, <br />
 but I am working on a better implementation of showing errors to the user, instead of launching the GUI through Xterm. <br />
## Dependencies: 
OpenCV <br />
Tkinter<br />
Xterm <br />
```
To run this program, you can just click on "Start".
```
There is a new install.sh script in the install directory that you can run that will install it to your system. <br />
You can either search for Rife in your destop enfironment, or can run rife-gui from your terminal. <br />
This install method will copy everything to the home folder, and execute from there. <br />
## Installing Dependencies
On Ubuntu <br />
```
sudo apt install python3-opencv ffmpeg python3-tk konsole wget
```
On Arch/Arch based Distros <br />
```
sudo pacman -S tk opencv konsole ffmpeg python-pip wget
```
On SteamOS/Steam Deck <br />
```
python GUI.py
```
Run this in your terminal in the directory where Rife GUI is installed, may add konsole support later <br />

## Errors
vkQueueSubmit failed and vkAllocateMemory failed happens when there isn't enough VRAM for the current frame. Downscale the video or get a better PC if this happens.

## TODO
fix 16x progressbar on anime, because it is actually 32x <br />
make anime 8x smoother? <br />
fix brogressbar not showing somtimes when animation profile is selected. <br />
Use less temp files <br />
Check if done file exists, and if not, throw error <br />
Add in built terminal <br />
Add stop button for interpolation <br />
Make portable installer, that is just one file to install the program <br />
Remodel the entire GUI <br />
Fix start executable not working on SteamOS<br />
Add more models, add drop downs for selecting different rife variations (cuda, vulkan, standard) add DAIN and CAIN too. <br />
Add selector for default directory to process frames, this could help people with low disk space. <br />
Make rife version and interpolation multiplier dropdown menus <br />
Make settings menu a tab instead of a window <br />
Add ETA for video interpolation <br />
Toggle between stable and testing branch (Dropdown Menu) <br />
Add suspend/resume feature <br />
Add uninstall button <br />
Support Dain Vulkan <br />
Clean up files <br />
Add progressbar for update (Note: Will have to make update function run in a new thread to have progressbar update.) <br />
Fix pop up showing wrong password, even when password is right (only happens if window is re-launched from install button.) <br />
Clean up GUI, Maybe switch to .pack instead of .grid? <br />
Add a default rife version selector. <br />
Add a default interpolation option selector <br />
Add longer dependencies section. <br />
Show errors on GUI itself, so i can remove the xterm dependency. <br />
