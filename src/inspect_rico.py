import os

root = r"C:\Users\neeth\OneDrive\Desktop\Masters in AI\SEM-2\Deep Learning\DL-CA1-MobileAppUI\unique_uis\combined"

print("Checking combined folder...\n")

print("Total items in combined:", len(os.listdir(root)))

print("\nFirst-level contents:")
for item in os.listdir(root)[:30]:
    print(item)