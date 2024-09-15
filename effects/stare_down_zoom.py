from moviepy.editor import VideoFileClip
from moviepy.video.fx.all import resize

def apply_stare_down_zoom(clip, zoom_factor=1.5, zoom_duration=5):
    def zoom_in(t):
        zoom = 1 + (zoom_factor - 1) * (t / zoom_duration)
        return resize(clip, zoom)

    return clip.fl_time(lambda t: zoom_in(t))

if __name__ == "__main__":
    clip = VideoFileClip('input_video.mp4')
    zoomed_clip = apply_stare_down_zoom(clip)
    zoomed_clip.write_videofile('stare_down_zoom_output.mp4')
