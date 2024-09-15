from moviepy.editor import VideoFileClip
from moviepy.video.fx.all import colorx

def apply_color_manipulation(clip, factor=0.5):
    return clip.fx(colorx, factor)

if __name__ == "__main__":
    clip = VideoFileClip('input_video.mp4')
    color_manipulated_clip = apply_color_manipulation(clip)
    color_manipulated_clip.write_videofile('color_manipulated_output.mp4')
