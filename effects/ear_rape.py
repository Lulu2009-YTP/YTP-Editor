from moviepy.editor import VideoFileClip
from moviepy.audio.fx.all import volumex

def apply_ear_rape(clip, volume_factor=10.0):
    audio = clip.audio.fx(volumex, volume_factor)
    return clip.set_audio(audio)

if __name__ == "__main__":
    clip = VideoFileClip('input_video.mp4')
    ear_rape_clip = apply_ear_rape(clip)
    ear_rape_clip.write_videofile('ear_rape_output.mp4')
