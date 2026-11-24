import os
import zipfile

print("Merging parts...")
with open("human_maintenance.zip", "wb") as out:
    for i in range(8):
        part_name = f"parts/human_maintenance.part{i:02d}"
        print(f"Reading {part_name}...")
        # In codespace, parts are already locally available if git pulled, or we can read them
        # Since we are running inside Codespace, we can just read local files in parts/ directory
        with open(part_name, "rb") as f:
            out.write(f.read())

print("Extracting zip...")
with zipfile.ZipFile("human_maintenance.zip", "r") as zip_ref:
    zip_ref.extractall("extracted_files")

print("SUCCESS: Files extracted to extracted_files/")
