"""One Line, One Laugh entry: writes a single funny line (87 chars) to /output/entry.txt."""
import os

LINE = "I finally organized my photos by date, and now I know exactly when I stopped being fun."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
