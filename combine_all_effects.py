from moviepy.editor import VideoFileClip
from effects.stutter_loop import apply_stutter_loop
from effects.scrambling_random_chopping import apply_scrambling_random_chopping
from effects.stare_down_zoom import apply_stare_down_zoom
from effects.spadinner_effect import apply_spadinner_effect
from effects.ear_rape import apply_ear_rape
from effects.bleep_censors import apply_bleep_censors

def apply_all_effects(clip):
    clip = apply_stutter_loop(clip)
    clip = apply_scrambling_random_chopping(clip)
    clip = apply_stare_down_zoom(clip)
    clip = apply_spadinner_effect(clip)
    clip = apply_ear_rape(clip)
    clip = apply_bleep_censors(clip)
    return clip

if __name__ == "__main__":
    clip = VideoFileClip('input_video.mp4')
    final_clip = apply_all_effects(clip)
    final_clip.write_videofile('final_output.mp4')
