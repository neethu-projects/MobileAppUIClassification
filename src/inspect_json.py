import json

path = r"C:\Users\neeth\OneDrive\Desktop\Masters in AI\SEM-2\Deep Learning\MobileAppUIClassification\unique_uis\combined\1001.json"

with open(path, "r") as f:
    data = json.load(f)

print(data)