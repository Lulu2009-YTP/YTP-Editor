from moviepy.editor import VideoFileClip
from moviepy.video.fx.all import colorx, tint_color

def apply_vibrant_color_shifts(clip, color_factor=2.0, tint_color_value=(0, 255, 0)):
    # Apply color scaling
    clip = clip.fx(colorx, color_factor)
    # Apply tint effect
    clip = clip.fx(tint_color, color=tint_color_value)
    return clip

if __name__ == "__main__":
    clip = VideoFileClip('input_video.mp4')
    vibrant_color_shifts_clip = apply_vibrant_color_shifts(clip)
    vibrant_color_shifts_clip.write_videofile('vibrant_color_shifts_output.mp4')
