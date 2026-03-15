import os
import json
import re
from urllib.parse import quote

# 🔧 CHANGE ONLY THIS
BASE_CDN = "https://raw.githack.com/rathidhruv/some-new-s/main"

ROOT = os.path.dirname(os.path.abspath(__file__))

AUDIO_EXT = (".mp3", ".m4a", ".m4b", ".wav")


def extract_number(name):
    match = re.search(r'\d+', name)
    return int(match.group()) if match else 0


def num_word(n):
    words = [
        "", "One","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten",
        "Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen",
        "Seventeen","Eighteen","Nineteen","Twenty"
    ]
    if n < len(words):
        return words[n]
    return str(n)


def scan_book(folder):

    folder_path = os.path.join(ROOT, folder)

    files = [
        f for f in os.listdir(folder_path)
        if f.lower().endswith(AUDIO_EXT)
    ]

    files.sort(key=extract_number)

    chapters = []

    for i, file in enumerate(files, start=1):

        encoded = quote(file)

        url = f"{BASE_CDN}/{folder}/{encoded}"

        chapters.append({
            "name": f"Chapter {i}: Chapter {num_word(i)}",
            "url": url
        })

    return chapters


def main():

    folders = [
        f for f in os.listdir(ROOT)
        if os.path.isdir(os.path.join(ROOT, f))
    ]

    for folder in folders:

        chapters = scan_book(folder)

        if not chapters:
            continue

        out = f"{folder}.json"

        with open(out, "w", encoding="utf-8") as f:
            json.dump(chapters, f, ensure_ascii=False, indent=2)

        print(f"✅ {folder} → {len(chapters)} chapters")


if __name__ == "__main__":
    main()
