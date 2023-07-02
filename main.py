#!/usr/bin/env python3

# Required Libraries
from pathlib import Path
import face_recognition

default_encodings_path = Path("output/econdings.pkl")

Path("training").mkdir(exists_ok=True)
Path("output").mkdir(exists_ok=True)
Path("validation").mkdir(exists_ok=True)

def encode_known_faces(
        model: str = "hog", encodings_location: Path = default_encodings_path
) -> None:
    names = []
    encodings = []
    for filepath in Path("training").glob("*/*"):
        name = filepath.parent.name
        image = face_recognition.load_image_file(filepath)
