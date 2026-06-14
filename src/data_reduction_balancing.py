import os
import shutil
import random

input_dir = r"C:\Users\neeth\OneDrive\Desktop\dataset_rico"
output_dir = r"C:\Users\neeth\OneDrive\Desktop\dataset_rico_small"

os.makedirs(output_dir, exist_ok=True)

target_size = 2000  # per class max

for class_name in os.listdir(input_dir):
    class_path = os.path.join(input_dir, class_name)

    if not os.path.isdir(class_path):
        continue

    images = os.listdir(class_path)
    random.shuffle(images)

    selected = images[:target_size]

    new_class_path = os.path.join(output_dir, class_name)
    os.makedirs(new_class_path, exist_ok=True)

    for img in selected:
        shutil.copy(
            os.path.join(class_path, img),
            os.path.join(new_class_path, img)
        )

    print(f"{class_name}: {len(selected)} images copied")

print("Done.")