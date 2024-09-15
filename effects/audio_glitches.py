from moviepy.editor import VideoFileClip
from moviepy.audio.fx.all import audio_fadein, audio_fadeout, volumex, time_stretch

def apply_audio_glitches(clip, volume_factor=1.2, stretch_factor=0.8):
    audio = clip.audio
    # Apply volume boost and time stretch for glitches
    audio = audio.fx(volumex, volume_factor)
    audio = audio.fx(time_stretch, stretch_factor)
    audio = audio.fx(audio_fadein, 1).fx(audio_fadeout, 1)
    return clip.set_audio(audio)

if __name__ == "__main__":
    clip = VideoFileClip('input_video.mp4')
    audio_glitched_clip = apply_audio_glitches(clip)
    audio_glitched_clip.write_videofile('audio_glitched_output.mp4')
