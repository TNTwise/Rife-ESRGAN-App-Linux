# Rife-Vulkan-GUI
# Installation: (linux)
Download the Latest Release of Rife-Vulkan-GUI. <br />
Extract the files. <br />
Run GUI. <br />
If it does not run, right click and go to properties -> permissions and check Allow executing file as program.<br />

# Debugging:
If you have any issues, use python GUI.py to open up a terminal window to see what the problem is.<br />

# Known issues: <br />
error: ../mesa-21.1.6/src/intel/vulkan/anv_device.c:3543: GPU hung on one of our command buffers (VK_ERROR_DEVICE_LOST) <br />
vkQueueSubmit failed -4 <br />
This means you are most likely using integrated graphics, using your RAM as VRAM and you do not have enough.<br />
If thats not the case, your gpu might not support vulkan. <br />
If your gpu doesn't support vulkan, I'd recommend using https://github.com/hzwer/arXiv2020-RIFE instead. <br />
If It says its done, but the video file is corrupt. most likely an error happened. 
