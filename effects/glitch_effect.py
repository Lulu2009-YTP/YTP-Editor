import numpy as np
from moviepy.video.fx.all import colorx, resize
from moviepy.editor import VideoFileClip

def apply_glitch_effect(clip):
    def glitch_frame(frame):
        # Randomly shift horizontal stripes
        h, w, _ = frame.shape
        stripe_height = np.random.randint(1, 10)
        num_stripes = h // stripe_height
        for i in range(num_stripes):
            if np.random.random() > 0.5:  # Randomly apply glitch
                y_start = i * stripe_height
                y_end = y_start + stripe_height
                x_offset = np.random.randint(0, 20)
                frame[y_start:y_end] = np.roll(frame[y_start:y_end], x_offset, axis=1)
        return frame
    
    return clip.fl_image(glitch_frame)

if __name__ == "__main__":
    clip = VideoFileClip('input_video.mp4')
    glitched_clip = apply_glitch_effect(clip)
    glitched_clip.write_videofile('glitched_output.mp4')
