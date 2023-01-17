all: BuildApp
BuildApp:
	pyinstaller -F --add-binary="/usr/lib64/ffmpeg4.4/pkgconfig/*:./usr/lib64/ffmpeg4.4/pkgconfig/"  --add-binary="/usr/lib64/ffmpeg4.4/*.so:./usr/lib64/ffmpeg4.4/" --add-binary="/usr/bin/ffmpeg:."  GUIAppimage.py 
