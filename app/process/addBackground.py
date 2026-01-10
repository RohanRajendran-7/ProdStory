from moviepy import VideoFileClip, ImageClip, CompositeVideoClip


video_path = "media/output_video1.mp4"
bg_img_path = "media/minimalist-background-gradient-colorful-style_698780-836.avif"
output_path = "output_bg.mp4"

video = VideoFileClip(video_path)
W, H = 1920, 1080
# Make background same duration as video
bg = (
    ImageClip(bg_img_path)
    .resized((W, H))
    .with_duration(video.duration)
)

# Resize video to fit inside background (keeping aspect ratio)
video_layer = (
    video
    .resized(height=900)  # resize video to fit inside background
    .with_position(("center", "center"))
)
final = CompositeVideoClip([bg, video_layer], size=(W, H))

final.write_videofile(output_path, codec="libx264", audio_codec="aac", fps=video.fps)
