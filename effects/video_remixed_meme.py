from moviepy.editor import VideoFileClip, concatenate_videoclips, TextClip, CompositeVideoClip
import numpy as np

def apply_video_remixed_meme(clip, meme_texts=['Meme1', 'Meme2', 'Meme3']):
    clips = []
    duration = clip.duration
    for i in range(len(meme_texts)):
        start_time = np.random.uniform(0, duration - 2)
        end_time = start_time + 2
        subclip = clip.subclip(start_time, end_time)
        
        # Add meme text overlay
        text = TextClip(meme_texts[i % len(meme_texts)], fontsize=50, color='white', bg_color='black')
        text = text.set_duration(2).set_pos(('center', 'center'))
        
        composite = CompositeVideoClip([subclip, text])
        clips.append(composite)
    
    return concatenate_videoclips(clips)

if __name__ == "__main__":
    clip = VideoFileClip('input_video.mp4')
    remixed_meme_clip = apply_video_remixed_meme(clip)
    remixed_meme_clip.write_videofile('video_remixed_meme_output.mp4')
