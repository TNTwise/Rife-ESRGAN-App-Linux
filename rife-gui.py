import os
import sys
homedir = os.path.expanduser(r"~")
os.chdir(f"{homedir}/Rife-Vulkan-GUI/")
os.system(fr'xterm -e bash -c "python3 GUI.py"')
os.system("pkill rife-gui")
