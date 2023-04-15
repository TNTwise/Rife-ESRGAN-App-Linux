all: BuildApp
BuildApp:
        #curl -O "https://bootstrap.pypa.io/get-pip.py" > get-pip.py
		python3 GUI.py --compile-appimage
		wget https://johnvansickle.com/ffmpeg/builds/ffmpeg-git-amd64-static.tar.xz
		tar xf ffmpeg-git-amd64-static.tar.xz
		pyinstaller --icon=icons/icon-256x256.png -F --noconfirm --add-data="icons/icon-256x256.png":"./icons/"   --add-binary="ffmpeg-git-20230313-amd64-static/ffmpeg:." --add-binary="/usr/bin/python3:." --add-binary="/usr/bin/curl:." --add-binary="/usr/bin/python3:."   GUIPortable.py
		rm -rf ffmpeg-git-amd64-static.tar.xz
		rm -rf ffmpeg-git-amd64-static
