from moviepy.editor import VideoFileClip, concatenate_videoclips
from moviepy.video.fx.all import resize, crop
import numpy as np

def apply_exaggerated_transitions(clip, num_transitions=10, transition_duration=1):
    subclips = []
    for _ in range(num_transitions):
        start_time = np.random.uniform(0, clip.duration - transition_duration)
        subclip = clip.subclip(start_time, start_time + transition_duration)
        subclip = subclip.fx(resize, height=np.random.randint(240, 480))
        subclip = subclip.fx(crop, x1=np.random.randint(0, 100), x2=np.random.randint(100, 200))
        subclips.append(subclip)
    
    return concatenate_videoclips(subclips)

if __name__ == "__main__":
    clip = VideoFileClip('input_video.mp4')
    exaggerated_transitions_clip = apply_exaggerated_transitions(clip)
    exaggerated_transitions_clip.write_videofile('exaggerated_transitions_output.mp4')
