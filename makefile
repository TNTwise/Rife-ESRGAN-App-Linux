all: BuildApp
BuildApp:
        #curl -O "https://bootstrap.pypa.io/get-pip.py" > get-pip.py
		python3 GUI.py --compile-appimage
		curl https://johnvansickle.com/ffmpeg/releases/ffmpeg-release-amd64-static.tar.xz > ffmpeg-release-amd64-static.tar.xz
		tar xf ffmpeg-release-amd64-static.tar.xz
		python3 -m PyInstaller --icon=icons/icon-256x256.png -F --noconfirm --hidden-import='PIL._tkinter_finder' --add-data="icons/icon-256x256.png":"./icons/"   --add-binary="ffmpeg-6.0-amd64-static/ffmpeg:." --add-binary="/usr/bin/curl:."    GUIPortable.py
		rm -rf ffmpeg-release-amd64-static.tar.xz
		rm -rf ffmpeg-6.0-amd64-static
