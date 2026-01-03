import os
from openai import OpenAI
from moviepy import VideoFileClip
from dotenv import load_dotenv
from app.process.generateaudio import audio_gen
# from app.process.summarise import summarise_text
import assemblyai as aai
import json

from app.process.transcriptionWhisper import process_audio_file
load_dotenv()
API_KEY = os.getenv("OPENAIAPI_KEY")
aai.settings.api_key = os.getenv("ASSEMBLYAI_API_KEY")

def transcribe_video(video_path):
    client = OpenAI(api_key=API_KEY)

    # Extract audio from video -- MoviePy uses ffmpeg internally to do this task, so make sure ffmpeg is installed on your system. While deploying to production, You’ll need direct FFmpeg usage for reliability, speed, and control. It’s more efficient and stable for batch jobs.
    video = VideoFileClip(video_path)
    audio = video.audio
    audio_file_path = "output_audio.wav"
    audio.write_audiofile(audio_file_path)

    # Process audio file using Whisper-based transcription
    text = process_audio_file(audio_file_path)

    input_text = text
    speaker_wav = "output_audio.wav"
    audio_gen(input_text,speaker_wav, "af_heart")


    #direct FFMPEG usage to convert to wav if needed
    # def extract_audio(video_path, output_path="output.wav"):
    # """
    # Extract clean mono 16kHz PCM audio from a video file
    # """
    # try:
    #     (
    #         ffmpeg
    #         .input(video_path)
    #         .output(output_path, ac=1, ar=16000, vn=None, acodec='pcm_s16le')
    #         .run(quiet=True, overwrite_output=True)
    #     )
    #     return output_path
    # except ffmpeg.Error as e:
    #     print("FFmpeg error:", e)
    #     return None


    # Use OpenAI Whisper API for transcription with timestamping and assemblyAI as fallback
    # transcript_text = ""
    # timestamps = []

    # try:
    #     with open(audio_file_path, "rb") as audio_file:
    #         transcript = client.audio.transcriptions.create(
    #             model="whisper-1",
    #             file=audio_file,
    #             response_format="verbose_json"  
    #         )

    #     transcript_text = " ".join([seg["text"] for seg in transcript["segments"]])
    #     timestamps = [
    #         {"start": seg["start"], "end": seg["end"], "text": seg["text"]}
    #         for seg in transcript["segments"]
    #     ]

    # except Exception as e:
    #     print(f"Error during Whisper transcription: {e}")
    #     print("⚙️ Falling back to AssemblyAI...")

    #     config = aai.TranscriptionConfig(speech_model=aai.SpeechModel.universal, 
    #                                      speaker_labels=False,
    #                                      auto_highlights=False)
    #     transcriber = aai.Transcriber(config=config)
    #     transcript = transcriber.transcribe(audio_file_path)

    #     if transcript.status == "error":
    #         raise RuntimeError(f"Transcription failed: {transcript.error}")

    #     transcript_text = transcript.text
    #     timestamps = [
    #         {"start": w.start, "end": w.end, "text": w.text}
    #         for w in transcript.words
    #     ]

    # with open("transcript_with_timestamps.json", "w") as f:
    #     json.dump(timestamps, f, indent=2)

    # summarised_text = summarise_text(transcript_text, task="paraphrase")
    # print("📝 Summarised text:", summarised_text)

    # audio_gen(summarised_text)
    # return summarised_text, timestamps
