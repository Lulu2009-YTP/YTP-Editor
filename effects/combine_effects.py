from moviepy.editor import VideoFileClip
from glitch_effect import apply_glitch_effect
from stutter_effect import apply_stutter_effect
from color_manipulation import apply_color_manipulation
from audio_distortion import apply_audio_distortion

def apply_all_effects(clip):
    clip = apply_glitch_effect(clip)
    clip = apply_stutter_effect(clip)
    clip = apply_color_manipulation(clip)
    clip = apply_audio_distortion(clip)
    return clip

if __name__ == "__main__":
    clip = VideoFileClip('input_video.mp4')
    final_clip = apply_all_effects(clip)
    final_clip.write_videofile('final_output.mp4')
