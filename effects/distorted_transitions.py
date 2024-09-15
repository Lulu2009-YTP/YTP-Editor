from moviepy.editor import VideoFileClip, concatenate_videoclips
from moviepy.video.fx.all import crop

def apply_distorted_transitions(clip, num_transitions=10, transition_duration=0.5):
    subclips = []
    for _ in range(num_transitions):
        start_time = np.random.uniform(0, clip.duration - transition_duration)
        subclip = clip.subclip(start_time, start_time + transition_duration)
        subclip = subclip.fx(crop, x1=np.random.randint(0, 100), x2=np.random.randint(100, 200), y1=0, y2=clip.h)
        subclips.append(subclip)
    
    return concatenate_videoclips(subclips)

if __name__ == "__main__":
    clip = VideoFileClip('input_video.mp4')
    distorted_transitions_clip = apply_distorted_transitions(clip)
    distorted_transitions_clip.write_videofile('distorted_transitions_output.mp4')
