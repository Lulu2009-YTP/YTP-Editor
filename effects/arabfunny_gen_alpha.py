from moviepy.editor import VideoFileClip, ImageClip, CompositeVideoClip, ColorClip
import numpy as np

def apply_arabfunny_gen_alpha(clip, overlay_image='arabfunny_overlay.png'):
    # Add a colorful background
    background = ColorClip(size=clip.size, color=(255, 255, 0), duration=clip.duration)
    
    # Overlay image
    overlay = ImageClip(overlay_image).set_duration(clip.duration).resize(height=clip.h // 2)
    
    # Composite video
    return CompositeVideoClip([background, clip, overlay.set_pos(('center', 'top'))])

if __name__ == "__main__":
    clip = VideoFileClip('input_video.mp4')
    arabfunny_gen_alpha_clip = apply_arabfunny_gen_alpha(clip)
    arabfunny_gen_alpha_clip.write_videofile('arabfunny_gen_alpha_output.mp4')
