
import os
import sys
from PIL import Image
from rembg import remove


INPUT_FILE = "/Users/rohanrajendran/Test/headphones.jpeg"
OUTPUT_DIR = "layers/"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def save(img, name):
    path = os.path.join(OUTPUT_DIR, name)
    img.save(path)
    print(f"[+] Saved {path}")
    return path

# -------- MAIN --------
original = Image.open(INPUT_FILE).convert("RGBA")

# 1. Subject (main object/foreground)
subject_mask = remove(original, only_mask=True)
subject = Image.composite(original, Image.new("RGBA", original.size, (0,0,0,0)), subject_mask)
save(subject, "subject.png")

# 2. Background (scene without subject)
background = remove(original)
save(background, "background.png")

print("[✔] Done. Layers exported to 'layers/'")
