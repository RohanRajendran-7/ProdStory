import torch
import soundfile as sf
from typing import List, Dict
from transformers import AutoModelForSpeechSeq2Seq, AutoProcessor, pipeline
from app.process.summarise import paraphrase_text
import librosa

def load_model_and_processor(model_id: str, device: str, torch_dtype: torch.dtype):
    model = AutoModelForSpeechSeq2Seq.from_pretrained(
        model_id,
        torch_dtype=torch_dtype,
        low_cpu_mem_usage=True,
    )
    model.to(device)

    processor = AutoProcessor.from_pretrained(model_id)

    pipe = pipeline(
        "automatic-speech-recognition",
        model=model,
        tokenizer=processor.tokenizer,
        feature_extractor=processor.feature_extractor,
        chunk_length_s=30,
        batch_size=16,
        torch_dtype=torch_dtype,
        device=device,
    )
    return model, processor, pipe

def preprocess_audio(audio_file: str, target_sr: int = 16000) -> Dict:
    audio_array, sr = sf.read(audio_file)

    if audio_array.ndim > 1:  # Convert stereo to mono
        audio_array = audio_array.mean(axis=1)

    if sr != target_sr:  # Resample if necessary
        audio_array = librosa.resample(audio_array, orig_sr=sr, target_sr=target_sr)
        sr = target_sr

    return {"array": audio_array, "sampling_rate": sr}

def chunks_to_segments(chunks: List[Dict], pause_threshold: float = 0.6) -> List[Dict]:
    segments = []
    current_words = []
    seg_start = chunks[0]['timestamp'][0]

    for i, ch in enumerate(chunks):
        word = ch['text']
        start, end = ch['timestamp']

        if not current_words:
            seg_start = start

        current_words.append(word)

        # Compute gap to next word
        if i < len(chunks) - 1:
            next_start = chunks[i+1]['timestamp'][0]
            gap = next_start - end
            if gap > pause_threshold:
                segments.append({
                    "text": "".join(current_words).strip(),
                    "start": seg_start,
                    "end": end,
                })
                current_words = []

    # Flush last segment
    if current_words:
        segments.append({
            "text": "".join(current_words).strip(),
            "start": seg_start,
            "end": chunks[-1]['timestamp'][1],
        })

    return segments

def add_speaking_stats(segments: List[Dict]) -> List[Dict]:
    for seg in segments:
        words = seg["text"].split()
        seg["word_count"] = len(words)
        seg["duration"] = seg["end"] - seg["start"]
        seg["wps"] = seg["word_count"] / seg["duration"] if seg["duration"] > 0 else 0
    return segments

def process_audio_file(audio_file: str, model_id: str = "openai/whisper-large-v3", pause_threshold: float = 0.6) -> List[Dict]:
    device = "cuda:0" if torch.cuda.is_available() else "cpu"
    torch_dtype = torch.float16 if torch.cuda.is_available() else torch.float32

    # Load model and processor
    model, processor, pipe = load_model_and_processor(model_id, device, torch_dtype)

    # Preprocess audio
    audio_input = preprocess_audio(audio_file)

    # Get speech recognition results
    result = pipe(audio_input, return_timestamps="word")
    chunks = result['chunks']

    # Convert chunks to segments
    segments = chunks_to_segments(chunks, pause_threshold)

    # Add speaking stats to segments
    final_segments = add_speaking_stats(segments)

    # Paraphrase the first segment (optional)
    first_seg = final_segments[0]
    rewritten = paraphrase_text(first_seg["text"], first_seg["word_count"])

    print("Rewritten (formal):", rewritten)

    return rewritten

# # Example usage
# audio_file = "/path/to/your/audio.wav"
# final_segments = 

# # Optionally, inspect the first segment
# print("First segment (raw):", final_segments[0])
