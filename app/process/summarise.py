import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from app.process.generateaudio import audio_gen
# Load model and tokenizer
model_name = "Qwen/Qwen3-0.6B"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype="auto",
    device_map="auto"
)

def paraphrase_text(text, target_wc):
    """
    Paraphrases text in a formal tone while roughly preserving word count.
    """
    # Prepare instruction
    prompt = (
        f"Rewrite the following text in a clear and professional tone. "
        f"Remove filler words like 'so', 'you know', 'um'. "
        f"Keep the meaning as is\n\n"
        f"Text:\n{text}\n\n"
        f"Rewritten:"
    )

    # Apply chat template with thinking disabled
    chat_text = tokenizer.apply_chat_template(
        [{"role": "user", "content": prompt}],
        tokenize=False,
        add_generation_prompt=True,
        enable_thinking=False  # disables step-by-step reasoning
    )

    # Encode input
    model_inputs = tokenizer([chat_text], return_tensors="pt").to(model.device)

    # Generate output
    max_tokens = target_wc * 3  # allow some flexibility
    generated_ids = model.generate(
        **model_inputs,
        max_new_tokens=max_tokens,
        do_sample=True,
        temperature=0.7,
        top_p=0.9,
        repetition_penalty=1.2
    )

    # Extract output
    output_ids = generated_ids[0][len(model_inputs.input_ids[0]):]
    content = tokenizer.decode(output_ids, skip_special_tokens=True).strip()

    return content

# Example usage
first_seg = {
    "text": "so this is by default our close-up so by here you can see the difference in videos so this is some user world video this is some manual video or the agent video and these are the you know testimonials from the various users",
    "word_count": 45
}

rewritten = paraphrase_text(first_seg["text"], first_seg["word_count"])
print("Rewritten:", rewritten)
speaker_wav = "output_audio.wav"

audio_gen(rewritten,speaker_wav, "af_heart")
