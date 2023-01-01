import os
import cv2
thisdir = os.getcwd()
def with_opencv(filename):
    
    video = cv2.VideoCapture(filename)

    frames = video.get(cv2.CAP_PROP_FRAME_COUNT)
    fps = video.get(cv2.CAP_PROP_FPS)
    seconds = round(frames / fps)
    return seconds,frames
seconds,frames = with_opencv("input.mp4")
if os.path.exists(f"{thisdir}/render_frames/") == False:
    os.mkdir(f"{thisdir}/render_frames/")
for i in range(1000):
    if len(f"{i}") == 1:
        i = f"0000000{i}"
    if len(f"{i}") == 2:
        i = f"000000{i}"
    if len(f"{i}") == 3:
        i = f"00000{i}"
    if len(f"{i}") == 4:
        i = f"0000{i}"
    if len(f"{i}") == 5:
        i = f"000{i}"
    if len(f"{i}") == 6:
        i = f"00{i}"
    if len(f"{i}") == 7:
        i = f"0{i}"
    os.system(f'mv "{thisdir}/output_frames/frame_{i}.png" "{thisdir}/render_frames/"')


def get_fps(filename):
    return cv2.VideoCapture(fr'{filename}').get(cv2.CAP_PROP_FPS)
os.system(fr'ffmpeg -framerate {get_fps("input.mp4")} -i "{thisdir}/render_frames/frame_%08d.png"  -c:a copy -crf 18 -vcodec libx264  "{thisdir}/1.mp4"')
print(len([name for name in os.listdir('.') if os.path.isfile(name)]))