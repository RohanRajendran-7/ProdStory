
# import os
# import numpy as np
# from PIL import Image
# from moviepy.editor import ImageClip, CompositeVideoClip, TextClip
# from moviepy.video.fx import all as vfx

# # -------- CONFIG --------
# LAYERS_DIR = "layers/"
# OUTPUT_FILE = "product_video.mp4"
# TAGLINE = "Step Into the Storm"

# # -------- LOAD LAYERS --------
# def load_layer(name, duration=5, opacity=1.0):
#     path = os.path.join(LAYERS_DIR, name)
#     if not os.path.exists(path):
#         return None
#     img = np.array(Image.open(path).convert("RGBA"))
#     clip = ImageClip(img, duration=duration).set_opacity(opacity)
#     return clip

# background = load_layer("background.png", duration=6)
# subject = load_layer("subject.png", duration=6)

# # Optional layers
# rain = load_layer("rain.png", duration=6, opacity=0.5)
# neon = load_layer("neon_signs.png", duration=6)
# crowd = load_layer("crowd.png", duration=6)

# clips = []

# # Background fades in
# if background:
#     clips.append(background.fx(vfx.fadein, 1))

# # Rain overlay (scroll effect)
# if rain:
#     clips.append(rain.set_position("center").fx(vfx.scroll, 0, -50))

# # Neon signs (slight zoom-in)
# if neon:
#     clips.append(neon.fx(vfx.fadein, 2).fx(vfx.resize, 1.1))

# # Crowd (slide from bottom)
# if crowd:
#     clips.append(crowd.set_position("center").fx(vfx.slide_in, 2, "bottom"))

# # Subject zooms in last
# if subject:
#     clips.append(subject.fx(vfx.fadein, 2).fx(vfx.resize, 1.1))

# # Add tagline
# txt = (TextClip(TAGLINE, fontsize=60, color="white", font="Arial-Bold")
#        .set_duration(3)
#        .set_position(("center", "bottom"))
#        .fx(vfx.fadein, 1).fx(vfx.fadeout, 1))
# clips.append(txt)

# # -------- COMBINE --------
# final = CompositeVideoClip(clips, size=background.size if background else (1280, 720))
# final = final.fx(vfx.resize, width=1280)  # ensure standard size
# final.write_videofile(OUTPUT_FILE, fps=24)

# print(f"[✔] Video saved as {OUTPUT_FILE}")

