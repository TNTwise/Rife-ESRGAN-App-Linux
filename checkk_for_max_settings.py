import os
import subprocess
p = subprocess.Popen((f'./rife-vulkan-models/rife-ncnn-vulkan -i input_frames -o output_frames'),shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
out, error = p.communicate()

def count_indents(s):
    """
    Returns the number of leading spaces on the first line of a string.
    """
    first_line = s.split('\n')[0]  # get the first line
    return len(first_line) - len(first_line.lstrip())

if count_indents(str(error)) > 10:
    print('failed')
    print(error)