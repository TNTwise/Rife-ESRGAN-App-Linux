sudo cp rife-gui /usr/bin/rife-gui
sudo cp ../icons/Icon.svg /usr/share/icons/hicolor/scalable/apps/Rife.svg
sudo apt install ffmpeg python3-opencv python3-tk tk python3-pip xterm 
sudo pacman -S tk opencv xterm ffmpeg python-pip
cp Rife-Vulkan-GUI.desktop /home/$USER/.local/share/applications/
mkdir /home/$USER/Rife-Vulkan-GUI
cp -r ../* /home/$USER/Rife-Vulkan-GUI
