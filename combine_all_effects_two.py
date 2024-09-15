from moviepy.editor import VideoFileClip
from effects.supercut import apply_supercut
from effects.video_remixed_meme import apply_video_remixed_meme
from effects.arabfunny_gen_alpha import apply_arabfunny_gen_alpha
from effects.parody import apply_parody
from effects.vidding import apply_vidding
from effects.dance import apply_dance

def apply_all_effects(clip):
    clip = apply_supercut(clip)
    clip = apply_video_remixed_meme(clip)
    clip = apply_arabfunny_gen_alpha(clip)
    clip = apply_parody(clip)
    clip = apply_vidding(clip)
    clip = apply_dance(clip)
    return clip

if __name__ == "__main__":
    clip = VideoFileClip('input_video.mp4')
    final_clip = apply_all_effects(clip)
    final_clip.write_videofile('final_output.mp4')
