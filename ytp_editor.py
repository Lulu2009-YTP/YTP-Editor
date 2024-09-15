import moviepy.editor as mp
import numpy as np
import os
from moviepy.video.fx.all import *
from moviepy.audio.fx.all import *

# Set your project paths
ASSETS_DIR = 'assets/'
OUTPUT_DIR = 'output/'

# 3D Cube Transition (Simple Example using Rotation)
def create_3d_cube_clip(clip, duration=5):
    # Rotate and zoom to simulate 3D cube effect
    return clip.fx(mirror_x).fx(rotate, angle=360*duration).set_duration(duration)

# Random Poopism Effects (Glitches, Pitch Shift, Speed up, Reverse, etc.)
def apply_poopy_effects(clip):
    effects = [
        lambda c: c.fx(speedx, 1.5),  # Speed up
        lambda c: c.fx(vfx.time_mirror),  # Reverse
        lambda c: c.fx(rotate, angle=30),  # Rotation
        lambda c: c.volumex(1.5),  # Volume boost
        lambda c: c.fx(vfx.colorx, 0.5)  # Color reduction for Poopism
    ]
    np.random.shuffle(effects)
    return effects[0](clip)

# Generate Random YTP Cuts
def create_random_cuts(clip, num_cuts=10, min_duration=0.5, max_duration=2):
    subclips = []
    for _ in range(num_cuts):
        start_time = np.random.uniform(0, clip.duration - max_duration)
        duration = np.random.uniform(min_duration, max_duration)
        subclip = clip.subclip(start_time, start_time + duration)
        subclips.append(apply_poopy_effects(subclip))
    return mp.concatenate_videoclips(subclips)

# Kneesocks Krisame 3D Effect (Zoom + Color Tint)
def kneesocks_effect(clip, color=(255, 0, 0), zoom_factor=1.5, duration=3):
    return clip.fx(vfx.colorx, 0.7).fx(vfx.fadein, duration/3).fx(vfx.fadeout, duration/3).resize(zoom_factor)

# Apply YTP Style Layers (Sound Distortion, Random Text)
def ytp_overlay_effects(clip):
    random_text = mp.TextClip("Random YTP Text", fontsize=70, color='white', bg_color='red', size=clip.size)
    text_clip = random_text.set_pos(('center', 'bottom')).set_duration(clip.duration)
    
    distorted_audio = clip.audio.fx(vfx.audio_fadein, 0.5).fx(vfx.audio_fadeout, 0.5).volumex(2)
    return mp.CompositeVideoClip([clip, text_clip]).set_audio(distorted_audio)

# Main Function to Combine Clips and Apply YTP Effects
def create_ytp_video(input_file, output_file):
    original_clip = mp.VideoFileClip(input_file)

    # Create a YTP video with random cuts and 3D effects
    yt_cuts = create_random_cuts(original_clip)
    yt_cuts = yt_cuts.fx(vfx.lum_contrast, lum=70, contrast=60)  # Lum/Contrast for YTP
    yt_3d = create_3d_cube_clip(yt_cuts, duration=5)
    
    # Apply Kneesocks Krisame effect on a specific section
    krisame_clip = kneesocks_effect(original_clip.subclip(5, 10))

    # Overlay random YTP elements like text and audio distortion
    final_clip = ytp_overlay_effects(yt_3d)
    
    # Export the final video
    final_clip.write_videofile(os.path.join(OUTPUT_DIR, output_file), codec="libx264")

if __name__ == "__main__":
    # Example Usage: Process an input video with YTP effects
    input_video = os.path.join(ASSETS_DIR, 'input_video.mp4')
    output_video = 'ytp_output.mp4'
    
    create_ytp_video(input_video, output_video)
