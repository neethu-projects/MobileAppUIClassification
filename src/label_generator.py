import os
import json
import shutil

root = r"C:\Users\neeth\OneDrive\Desktop\Masters in AI\SEM-2\Deep Learning\DL-CA1-MobileAppUI\unique_uis\combined"

output = r"C:\Users\neeth\OneDrive\Desktop\dataset_rico"

os.makedirs(output, exist_ok=True)

def get_label(activity_name):
    activity_name = activity_name.lower()

    if "login" in activity_name:
        return "login"
    elif "home" in activity_name:
        return "home"
    elif "setting" in activity_name:
        return "settings"
    elif "profile" in activity_name:
        return "profile"
    else:
        return "other"

count = 0

for file in os.listdir(root):
    if file.endswith(".json"):
        json_path = os.path.join(root, file)
        img_path = json_path.replace(".json", ".jpg")

        if not os.path.exists(img_path):
            continue

        with open(json_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        activity = data.get("activity_name", "")
        label = get_label(activity)

        label_folder = os.path.join(output, label)
        os.makedirs(label_folder, exist_ok=True)

        shutil.copy(img_path, os.path.join(label_folder, file.replace(".json", ".jpg")))

        count += 1

        if count % 1000 == 0:
            print("Processed:", count)

print("Done. Total images:", count)