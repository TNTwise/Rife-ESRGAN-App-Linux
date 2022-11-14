#!/usr/bin/python3
import os
import sys
os.system("xterm -e 'bash -c \"python3 GUI.py\" '")
os.system("konsole -e 'bash -c \"python3 GUI.py\" '")
os.system("gnome-terminal -e 'bash -c \"python3 GUI.py\" '")
os.system("alacritty -e 'bash -c \"python3 GUI.py\" '")
os.system("terminator -e 'bash -c \"python3 GUI.py\" '")

exit()
