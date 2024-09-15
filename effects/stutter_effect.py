from moviepy.editor import VideoFileClip, concatenate_videoclips

def apply_stutter_effect(clip, num_repeats=5):
    def stutter_frame(frame):
        return np.repeat(frame, num_repeats, axis=0)
    
    stuttered_clips = []
    for t in range(0, int(clip.duration), 1):
        subclip = clip.subclip(t, t+1)
        stuttered_clips.append(subclip.fl_image(stutter_frame))
    
    return concatenate_videoclips(stuttered_clips)

if __name__ == "__main__":
    clip = VideoFileClip('input_video.mp4')
    stuttered_clip = apply_stutter_effect(clip)
    stuttered_clip.write_videofile('stuttered_output.mp4')
