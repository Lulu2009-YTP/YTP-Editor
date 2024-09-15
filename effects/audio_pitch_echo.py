from moviepy.editor import VideoFileClip
from moviepy.audio.fx.all import volumex, time_stretch, audio_fadein, audio_fadeout

def apply_audio_pitch_echo(clip, volume_factor=1.5, pitch_factor=0.8):
    audio = clip.audio
    # Apply pitch shift and echo
    audio = audio.fx(volumex, volume_factor)
    audio = audio.fx(time_stretch, pitch_factor)
    audio = audio.fx(audio_fadein, 1).fx(audio_fadeout, 1)
    return clip.set_audio(audio)

if __name__ == "__main__":
    clip = VideoFileClip('input_video.mp4')
    audio_pitch_echo_clip = apply_audio_pitch_echo(clip)
    audio_pitch_echo_clip.write_videofile('audio_pitch_echo_output.mp4')
