from moviepy.editor import VideoFileClip, vfx
from moviepy.video.fx.all import speedx, colorx

def apply_vidding(clip):
    # Apply speed adjustment
    clip = clip.fx(speedx, 1.5)
    
    # Apply color enhancement
    clip = clip.fx(colorx, 1.2)
    
    return clip

if __name__ == "__main__":
    clip = VideoFileClip('input_video.mp4')
    vidding_clip = apply_vidding(clip)
    vidding_clip.write_videofile('vidding_output.mp4')
