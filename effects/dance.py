from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip, vfx
import numpy as np

def apply_dance(clip):
    # Add dancing text overlay
    def make_dance_text(t):
        size = 50 + 50 * np.sin(t * np.pi)
        return TextClip("Dance Time!", fontsize=size, color='cyan', bg_color='black', size=clip.size).set_duration(1).set_pos(('center', 'center'))

    # Apply effect to make text "dance"
    dance_clips = [make_dance_text(t) for t in np.arange(0, clip.duration, 1)]
    
    return CompositeVideoClip([clip] + dance_clips)

if __name__ == "__main__":
    clip = VideoFileClip('input_video.mp4')
    dance_clip = apply_dance(clip)
    dance_clip.write_videofile('dance_output.mp4')
