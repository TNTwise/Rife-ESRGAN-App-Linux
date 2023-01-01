import os
import re
thisdir = os.getcwd()
os.chdir("output_frames/")
def convert_i(i):
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
    return i
frames = len([name for name in os.listdir('.') if os.path.isfile(name)])
for i in range(frames):
    i+=1
    p = int(i) + 1000
    i = convert_i(i)
    p = convert_i(p)
    
    os.system(f'mv "{thisdir}/output_frames/frame_{str(p)}.png" "{thisdir}/output_frames/frame_{str(i)}.png"' )
    
        