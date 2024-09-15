from moviepy.editor import VideoFileClip, ImageClip, CompositeVideoClip

def apply_spadinner_effect(clip, image_path='spadinner_image.png'):
    image = ImageClip(image_path).set_duration(clip.duration).resize(clip.size)
    return CompositeVideoClip([clip, image.set_opacity(0.5)])

if __name__ == "__main__":
    clip = VideoFileClip('input_video.mp4')
    spadinner_clip = apply_spadinner_effect(clip)
    spadinner_clip.write_videofile('spadinner_output.mp4')
