from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip
import numpy as np

def apply_quirky_text_overlays(clip):
    text_clips = []
    for _ in range(10):  # Adding 10 random text clips
        txt_clip = TextClip("Kneesocks", fontsize=np.random.randint(30, 100), color='white', bg_color='black', size=clip.size)
        txt_clip = txt_clip.set_duration(np.random.uniform(1, 3)).set_pos((np.random.randint(0, clip.w), np.random.randint(0, clip.h)))
        text_clips.append(txt_clip)
    
    return CompositeVideoClip([clip] + text_clips)

if __name__ == "__main__":
    clip = VideoFileClip('input_video.mp4')
    quirky_text_overlay_clip = apply_quirky_text_overlays(clip)
    quirky_text_overlay_clip.write_videofile('quirky_text_overlay_output.mp4')
