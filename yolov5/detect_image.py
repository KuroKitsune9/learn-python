import cv2
import torch
import os
from pathlib import Path

# Load model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', trust_repo=True)

# Folder gambar
image_folder = 'data/images/'
image_paths = list(Path(image_folder).glob('*.*'))

if not image_paths:
    print("Tidak ada gambar di folder:", image_folder)
    exit()

# Loop gambar
for img_path in image_paths:
    print(f"\n[INFO] Mendeteksi objek pada: {img_path.name}")
    
    # Deteksi
    results = model(str(img_path))
    
    # Dapatkan gambar dengan kotak deteksi
    result_img = results.render()[0]  # np array

    # Resize untuk ditampilkan lebih nyaman
    scale_percent = 120  # ubah sesuai kebutuhan (misal 100, 150)
    width = int(result_img.shape[1] * scale_percent / 100)
    height = int(result_img.shape[0] * scale_percent / 100)
    dim = (width, height)
    resized = cv2.resize(result_img, dim, interpolation=cv2.INTER_AREA)

    # Tampilkan
    cv2.imshow(f"Deteksi: {img_path.name}", resized)
    print("Tekan [q] untuk lanjut ke gambar berikutnya")
    
    while True:
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break

cv2.destroyAllWindows()
