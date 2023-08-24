import pytesseract
import os

def main():
    for root, dirs, files in os.walk('screenshots/'):
        for file in files:
            try:
                fpath = os.path.join(root, file)
                if fpath.endswith('.png'):
                    text = pytesseract.image_to_string(fpath)
                    with open(f"{fpath}_text.txt", "w") as f:
                        f.write(text)
            except Exception as e:
                print(e)

if __name__ == "__main__":
    main()