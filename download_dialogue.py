import kagglehub
import shutil
import os

# Download
path = kagglehub.dataset_download("liury123/my-little-pony-transcript")
print("Cached dataset at:", path)

# Move to Repository
target = "data"
os.makedirs(target, exist_ok=True)

for fname in os.listdir(path):
    shutil.copy(os.path.join(path, fname), target)
print("Copied into:", target)