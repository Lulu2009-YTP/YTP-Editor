from moviepy.editor import VideoFileClip
from exaggerated_transitions import apply_exaggerated_transitions
from vibrant_color_shifts import apply_vibrant_color_shifts
from quirky_text_overlays import apply_quirky_text_overlays
from audio_pitch_echo import apply_audio_pitch_echo

def apply_krisame_effects(clip):
    clip = apply_exaggerated_transitions(clip, num_transitions=12)
    clip = apply_vibrant_color_shifts(clip, color_factor=3.0, tint_color_value=(255, 0, 0))
    clip = apply_quirky_text_overlays(clip)
    clip = apply_audio_pitch_echo(clip, volume_factor=2.0, pitch_factor=0.5)
    return clip

if __name__ == "__main__":
    clip = VideoFileClip('input_video.mp4')
    final_clip = apply_krisame_effects(clip)
    final_clip.write_videofile('krisame_final_output.mp4')
