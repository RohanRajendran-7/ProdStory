from moviepy import VideoFileClip, AudioFileClip

video_path = "/Users/rohanrajendran/Test/media/sample.mov"
audio_path = "/Users/rohanrajendran/Test/output_audio.wav"
output_path = "/Users/rohanrajendran/Test/media/output_video1.mp4"

video = VideoFileClip(video_path)
new_audio = AudioFileClip(audio_path)

print("Video duration:", video.duration)
print("Audio duration:", new_audio.duration)

# 1. Explicitly remove existing audio
video_no_audio = video.without_audio()

# 2. Attach new audio (shorter audio is OK)
final = video_no_audio.with_audio(new_audio)

# 3. Write output
final.write_videofile(
    output_path,
    codec="libx264",
    audio_codec="aac"
)
