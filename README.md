
<p align=center>
  <img src="https://github.com/TNTwise/Rife-Vulkan-GUI-Linux/blob/main/icons/Icon.svg" width = "25%">
</p>

# A simple GUI for Rife Vulkan on Linux
# Note: This program still requires testing on many different distros
 I am currently working on maintaining Arch and Ubuntu support. <br />
 It should work fine on all distros, but I would still like to do more testing. <br />
 Usually if an error occurs, it's with Rife itself, and not the GUI, <br />
 but I am working on a better implementation of showing errors to the user, instead of launching the GUI through Xterm. <br />
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
Add progressbar for update (Note: Will have to make update function run in a new thread to have progressbar update.) <br />
Fix pop up showing wrong password, even when password is right (only happens if window is re-launched from install button.) <br />
Fix check for updates still getting update even if you are on latest from main branch, maybe write time of update, and check with if statement? <br />
Make the listbox menu a dropdown menu <br />
Clean up GUI, Maybe switch to .pack instead of .grid? <br />
Make progressbar more accurate  <br />
Add a default rife version selector. <br />
Add a default interpolation option selector <br />
Add default folder selector. <br />
Fix Progress bar on different interpolation modes. <br />
Use default terminal instead of xterm. <br />
Add longer dependencies section. <br />
Add a limit of 2 selections in each times interpolation and rife version menu. <br />
Maybe package as appimage? <br />
Show errors on GUI itself, so i can remove the xterm dependency. <br />
