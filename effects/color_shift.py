from moviepy.editor import VideoFileClip
from moviepy.video.fx.all import colorx, gamma_corr

def apply_color_shift(clip, color_factor=1.5, gamma=0.5):
    # Apply extreme color shift
    clip = clip.fx(colorx, color_factor)
    # Apply gamma correction for additional distortion
    clip = clip.fx(gamma_corr, gamma)
    return clip

if __name__ == "__main__":
    clip = VideoFileClip('input_video.mp4')
    color_shifted_clip = apply_color_shift(clip)
    color_shifted_clip.write_videofile('color_shifted_output.mp4')
