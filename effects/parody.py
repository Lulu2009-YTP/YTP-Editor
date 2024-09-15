from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip, AudioFileClip

def apply_parody(clip, parody_texts=['LOL', 'Epic Fail'], audio_overlay='parody_audio.mp3'):
    # Add text overlay
    text_clips = [TextClip(text, fontsize=70, color='red', bg_color='black', size=clip.size)
                  .set_duration(clip.duration / len(parody_texts))
                  .set_pos(('center', 'bottom'))
                  for text in parody_texts]
    
    # Add parody audio overlay
    audio = AudioFileClip(audio_overlay).subclip(0, clip.duration)
    clip = clip.set_audio(audio)
    
    return CompositeVideoClip([clip] + text_clips)

if __name__ == "__main__":
    clip = VideoFileClip('input_video.mp4')
    parody_clip = apply_parody(clip)
    parody_clip.write_videofile('parody_output.mp4')
