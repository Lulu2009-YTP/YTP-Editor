from moviepy.editor import VideoFileClip, concatenate_videoclips

def apply_stutter_loop(clip, num_repeats=10, loop_duration=1):
    stutter_clips = []
    for t in range(0, int(clip.duration), loop_duration):
        subclip = clip.subclip(t, min(t + loop_duration, clip.duration))
        stuttered = concatenate_videoclips([subclip] * num_repeats)
        stutter_clips.append(stuttered)
    
    return concatenate_videoclips(stutter_clips)

if __name__ == "__main__":
    clip = VideoFileClip('input_video.mp4')
    stuttered_clip = apply_stutter_loop(clip)
    stuttered_clip.write_videofile('stutter_loop_output.mp4')
