from moviepy.editor import VideoFileClip
from moviepy.audio.fx.all import volumex, audio_fadein, audio_fadeout

def apply_audio_distortion(clip, volume_factor=1.5, fadein_duration=1, fadeout_duration=1):
    audio = clip.audio
    distorted_audio = audio.fx(volumex, volume_factor).fx(audio_fadein, fadein_duration).fx(audio_fadeout, fadeout_duration)
    return clip.set_audio(distorted_audio)

if __name__ == "__main__":
    clip = VideoFileClip('input_video.mp4')
    audio_distorted_clip = apply_audio_distortion(clip)
    audio_distorted_clip.write_videofile('audio_distorted_output.mp4')
