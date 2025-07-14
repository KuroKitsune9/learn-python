import os
import shutil
import random

# Path folder gambar awal (yang berisi folder A-Z)
source_dir = r"C:\Users\Muharafi Dalilah\Downloads\Citra BISINDO"

# Folder tujuan
train_dir = r"datasets/bisindo/images/train"
val_dir = r"datasets/bisindo/images/val"

# Rasio validasi
val_ratio = 0.2

# Loop semua kelas
for class_name in os.listdir(source_dir):
    class_path = os.path.join(source_dir, class_name)
    if not os.path.isdir(class_path):
        continue

    images = [img for img in os.listdir(class_path) if img.endswith(('.jpg', '.png', '.jpeg'))]
    random.shuffle(images)

    val_count = int(len(images) * val_ratio)

    for i, img_name in enumerate(images):
        src = os.path.join(class_path, img_name)
        dst_dir = val_dir if i < val_count else train_dir
        dst_class_dir = os.path.join(dst_dir, class_name)
        os.makedirs(dst_class_dir, exist_ok=True)
        shutil.copy2(src, os.path.join(dst_class_dir, img_name))

print("Pemecahan train/val selesai.")
