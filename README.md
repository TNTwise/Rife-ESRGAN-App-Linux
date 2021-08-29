# Rife-Vulkan-GUI, Based on rife-ncnn-vulkan
DO NOT CLONE REPO. CLONING RESULTS IN A BUG. DOWNLOAD FROM RELEASE TAB <br />
I do not update the source code regularly. The source code is already in the releases I push out.
# Installation: (linux)
Download the Latest Release of Rife-Vulkan-GUI. <br />
Extract the files. <br />
Install opencv-python, tk, and xterm (according to your distrobution)<br /> 
Run start. <br />
If it does not run, right click and go to properties -> permissions and check Allow executing file as program.<br />

# Usage:
Select a video with Input Video<br />
Select a Output Directory with Output Folder.<br />
Select 2X or 4X depending on how many times you want your video to be interpolated.<br />
Start!.<br />
# Known issues: <br />
error: ../mesa-21.1.6/src/intel/vulkan/anv_device.c:3543: GPU hung on one of our command buffers (VK_ERROR_DEVICE_LOST) <br />
vkQueueSubmit failed -4 <br />
This means you are most likely using integrated graphics, using your RAM as VRAM and you do not have enough. Downscale your video<br />
If thats not the case, your gpu might not support vulkan. <br />
If your gpu doesn't support vulkan, I'd recommend using https://github.com/hzwer/arXiv2020-RIFE instead. <br />
If It says its done, but the video file is corrupt. most likely an error happened. <br />

THESE ISSUES ARE NOT FROM MY PROGRAM. DO NOT ASK FOR SUPPORT ON THIS PAGE.
# DON'T HAVE spaces or any punctuation in file name

