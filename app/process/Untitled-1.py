# INPUT_FILE = "/Users/rohanrajendran/Test/sample.jpeg"
# OUTPUT_DIR = "layers/"

# os.makedirs(OUTPUT_DIR, exist_ok=True)

# def save(img, name):
#     path = os.path.join(OUTPUT_DIR, name)
#     img.save(path)
#     print(f"[+] Saved {path}")
#     return path

# # 1. Open original
# original = Image.open(INPUT_FILE).convert("RGBA")

# # 2. Subject (main character)
# subject_mask = remove(original, only_mask=True)
# subject = Image.composite(original, Image.new("RGBA", original.size, (0,0,0,0)), subject_mask)
# save(subject, "subject.png")

# # 3. Background (without subject)
# background = remove(original)
# save(background, "background.png")

# # 4. Rain overlay (synthetic transparent layer)
# rain = Image.new("RGBA", original.size, (0,0,0,0))
# draw = rain.load()
# for x in range(0, original.size[0], 5):
#     for y in range(0, original.size[1], 40):
#         draw[x, y] = (255, 255, 255, 60)  # white drops
# save(rain, "rain.png")

# # 5. Neon signs extraction (color threshold trick)
# cv_img = cv2.cvtColor(np.array(original), cv2.COLOR_RGBA2BGR)
# hsv = cv2.cvtColor(cv_img, cv2.COLOR_BGR2HSV)
# mask = cv2.inRange(hsv, (120, 50, 50), (160, 255, 255))  # purples/pinks
# neon = cv2.bitwise_and(cv_img, cv_img, mask=mask)
# neon = Image.fromarray(cv2.cvtColor(neon, cv2.COLOR_BGR2RGBA))
# save(neon, "neon_signs.png")

# # 6. Crowd silhouettes (approx by dark area threshold)
# gray = cv2.cvtColor(cv_img, cv2.COLOR_BGR2GRAY)
# _, mask_crowd = cv2.threshold(gray, 50, 255, cv2.THRESH_BINARY_INV)
# crowd = cv2.bitwise_and(cv_img, cv_img, mask=mask_crowd)
# crowd = Image.fromarray(cv2.cvtColor(crowd, cv2.COLOR_BGR2RGBA))
# save(crowd, "crowd.png")

# print("[✔] All layers exported!")