import os
import subprocess
class TransitionDetection:
    def __init__(self,vidpath,RenderDir,filename):
        self.get_transitions_amout(vidpath,RenderDir,filename)
    
    def get_transitions_amout(self,vidpath,RenderDir,filename):
        

        # FFmpeg command to detect scene changes and output timestamps
        ffmpeg_cmd = f'ffmpeg -i {vidpath} -filter_complex "select=\'gt(scene\,0.4)\',metadata=print" -f null -'
        os.mkdir(f'{RenderDir}/{filename}/transitions/')
        os.system(f'ffmpeg -i {vidpath} -filter_complex "select=\'gt(scene\,0.4)\',metadata=print" -vsync vfr -q:v 2 {RenderDir}/{filename}/transitions/output_%03d.png')

        # Execute the command and capture the output
        output = subprocess.check_output(ffmpeg_cmd, shell=True, stderr=subprocess.STDOUT)

        # Decode the output as UTF-8 and split it into lines
        output_lines = output.decode("utf-8").split("\n")

        # Create a list to store the timestamps
        timestamps = []

        # Iterate over the output lines and extract the timestamps
        for line in output_lines:
            if "pts_time" in line:
                timestamp = str(line.split("_")[3])
                timestamps.append(timestamp)

                # Print the list of timestamps
        self.timestamps = timestamps
    def return_timestamps(self):
        return self.timestamps
TransitionDetection()
