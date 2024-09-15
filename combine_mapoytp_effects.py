from moviepy.editor import VideoFileClip
from color_shift import apply_color_shift
from distorted_transitions import apply_distorted_transitions
from audio_glitches import apply_audio_glitches
from random_text_overlay import apply_random_text_overlay

def apply_mapoytp_effects(clip):
    clip = apply_color_shift(clip, color_factor=2.0, gamma=0.3)
    clip = apply_distorted_transitions(clip, num_transitions=15)
    clip = apply_audio_glitches(clip, volume_factor=1.5, stretch_factor=0.7)
    clip = apply_random_text_overlay(clip)
    return clip

if __name__ == "__main__":
    clip = VideoFileClip('input_video.mp4')
    final_clip = apply_mapoytp_effects(clip)
    final_clip.write_videofile('mapoytp_final_output.mp4')
