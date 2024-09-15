from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip
import numpy as np

def apply_random_text_overlay(clip):
    text_clips = []
    for _ in range(5):  # Adding 5 random text clips
        txt_clip = TextClip("Random Text", fontsize=70, color='white', bg_color='black', size=clip.size)
        txt_clip = txt_clip.set_duration(np.random.uniform(0.5, 2.0)).set_pos((np.random.randint(0, clip.w), np.random.randint(0, clip.h)))
        text_clips.append(txt_clip)
    
    return CompositeVideoClip([clip] + text_clips)

if __name__ == "__main__":
    clip = VideoFileClip('input_video.mp4')
    text_overlay_clip = apply_random_text_overlay(clip)
    text_overlay_clip.write_videofile('text_overlay_output.mp4')
