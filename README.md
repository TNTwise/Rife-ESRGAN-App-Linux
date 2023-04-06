<p align=center>
  <img src="https://github.com/TNTwise/Rife-Vulkan-GUI-Linux/blob/main/icons/icon-256x256.png" width = "25%">
</p>

## A simple GUI for Frame Interpolation and Upscaling on Linux
rife-ncnn-vulkan: https://github.com/nihui/rife-ncnn-vulkan<br/>
Real-ESRGAN-ncnn-vulkan: https://github.com/xinntao/Real-ESRGAN-ncnn-vulkan<br />
[Dependencies](https://github.com/TNTwise/Rife-ESRGAN-App-Linux#dependencies)<br />
[Building](https://github.com/TNTwise/Rife-ESRGAN-App-Linux/#building)<br/>
[Errors](https://github.com/TNTwise/Rife-ESRGAN-App-Linux/#errors)<br/>
[TODO](https://github.com/TNTwise/Rife-ESRGAN-App-Linux/#todo)<br/>

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

## Installing Dependencies <br />

On Ubuntu <br />
```
sudo apt install python3-opencv ffmpeg python3-tk konsole libavfilter-dev libavfilter8 libswscale-dev python3-pil.imagetk 
```
On Arch/Arch based Distros <br />
```
sudo pacman -S tk opencv konsole ffmpeg python-pip
```
On SteamOS/Steam Deck <br />
```
Run "Start"
```
As of latest SteamOs 3.4, it does not error out when launching it from "Start". <br />

## Building
Install needed dependencies
```
yay -S pyinstaller
```
run GUI.py at least once to install PIP dependencies
```
make
```
# Compile Appimage
```
git clone https://github.com/TNTwise/Rife-ESRGAN-App-AppImage.git
```
replace GUIPortable.temp with the compiled GUIPortable<br/>
```
chmod +x Rife-ESRGAN-App.AppDir/AppRun
appimagetool Rife-ESRGAN-App.AppDir 
```

## Errors
vkQueueSubmit failed and vkAllocateMemory failed happens when there isn't enough VRAM for the current frame. 
```
Lower the system load if you see these errors or if the output video is corrupted.
```
If RealESRGAN does not seem to be working, or Rife is slow, make sure you have the vulkan package installed based on your hardware.<br/>
For example:<br />
Intel:
```
sudo pacman -S vulkan-intel
```
AMD:
```
sudo pacman -S vulkan-radeon
```
NVIDIA:
```
sudo pacman -S nvidia-utils
```

## TODO
### Before all this, The next release will use QT instead of Tkinter. I will also split GUI.py into multiple, easier to manage scripts. The code which this app is based on is bad, so I will attempt to re-write most of it.
add fullscreen button for preview<br />
automatic detection of max usage per system, do this by having a test video render at 1080p, 4k, and 8k and detect the max settings the system can run without erroring out with a not enough vram error.
make anime progress bar dynamic, have the first section be the fps out of the fps + 30.
fix missing riff tag when using anything other than png, try converting the frames to webp using ffmpeg <br />
Have animeintterpolation interpolate regularly until the last iteration and then lower to 30 and interpolate.
make an option that allows for changing of extracted image type.<br />
Fix issue where output video errors out if codec is not right, even if filename is .mp4<br/>
Add CLI support for basic interpolation. <br/>
For next release, add advanced settings tab. <br />
Add support for changing between yuv420p yuv422p yuv244p rgb24 pix_fmt <br />
Add automatic conversion to supported format<br/>
Maybe add a message to ask if user wants to save last output files if greater than 2x interpolation.
Add a try except function for reading settings <br />
Add a function that deletes already processced files (check if file num x 2 exists in output_folder)
Fix CPU + GPU combo not working with realsrgan <br />
Add shutdown when done<br />
Disable tabs when on a certain upscale mode<br />
Add realesrgan support to upscale video resolution, make app more general purpose<br />
Set up queue system <br />
Add scalability to GUI<br />
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
