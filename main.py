"""One Line, One Laugh entry: writes a single funny line (124 chars) to /output/entry.txt."""
import os

LINE = "My barber asked if I wanted it shorter on the sides. I said yes, and now my ID photo looks like a witness-protection update."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
