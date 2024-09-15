from moviepy.editor import VideoFileClip, AudioFileClip, CompositeAudioClip
from moviepy.audio.fx.all import audio_fadein, audio_fadeout

def apply_bleep_censors(clip, bleep_sound_path='bleep_sound.mp3', censor_times=[(5, 10)]):
    audio = clip.audio
    bleep_sound = AudioFileClip(bleep_sound_path).subclip(0, 1)
    
    def apply_censor(t):
        for start, end in censor_times:
            if start <= t < end:
                return bleep_sound
        return audio
    
    censored_audio = CompositeAudioClip([apply_censor(t) for t in range(int(clip.duration))])
    return clip.set_audio(censored_audio)

if __name__ == "__main__":
    clip = VideoFileClip('input_video.mp4')
    censored_clip = apply_bleep_censors(clip)
    censored_clip.write_videofile('bleep_censors_output.mp4')
