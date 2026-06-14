import os

dataset_path = r"C:\DL-CA1\MobileAppUIClassification\dataset\dataset_rico_small"

print("Exists:", os.path.exists(dataset_path))
print("Classes:", os.listdir(dataset_path))