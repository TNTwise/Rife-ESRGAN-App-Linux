all: BuildApp
BuildApp:
        #curl -O "https://bootstrap.pypa.io/get-pip.py" > get-pip.py
		python3 GUI.py --compile-appimage
		curl https://johnvansickle.com/ffmpeg/releases/ffmpeg-release-amd64-static.tar.xz > ffmpeg-release-amd64-static.tar.xz
		tar xf ffmpeg-release-amd64-static.tar.xz
		python3 -m PyInstaller --icon=icons/icon-256x256.png -F --noconfirm --add-data="icons/icon-256x256.png":"./icons/"   --add-binary="ffmpeg-6.0-amd64-static/ffmpeg:." --add-binary="/usr/bin/python3:." --add-binary="/usr/bin/curl:." --add-binary="/usr/bin/python3:."   GUIPortable.py
		rm -rf ffmpeg-git-amd64-static.tar.xz
		rm -rf ffmpeg-6.0-amd64-static
