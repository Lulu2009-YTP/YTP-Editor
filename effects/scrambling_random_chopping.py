from moviepy.editor import VideoFileClip
import numpy as np

def apply_scrambling_random_chopping(clip, num_chunks=20):
    duration = clip.duration
    chunk_size = duration / num_chunks
    chunks = []
    for _ in range(num_chunks):
        start_time = np.random.uniform(0, duration - chunk_size)
        end_time = start_time + chunk_size
        chunk = clip.subclip(start_time, end_time)
        chunks.append(chunk)
    
    np.random.shuffle(chunks)
    return concatenate_videoclips(chunks)

if __name__ == "__main__":
    clip = VideoFileClip('input_video.mp4')
    scrambled_clip = apply_scrambling_random_chopping(clip)
    scrambled_clip.write_videofile('scrambled_output.mp4')
