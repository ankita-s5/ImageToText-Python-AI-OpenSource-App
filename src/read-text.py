import easyocr
import os


def main():
    reader = easyocr.Reader(['en'],gpu=False)  # Initialize EasyOCR reader for English without GPU
    current_dir = os.path.dirname(os.path.abspath(__file__)) 
   # image_path = os.path.join(current_dir, '/images/1.png')
    image_path= "../images/1.png"
    if not os.path.exists(image_path):
        print(f"Image file not found at {image_path}")
        return

    result = reader.readtext(image_path)
    print("Detected text:")
    for detection in result:
        print(detection[1])  # Print the detected text


if __name__ == "__main__":
    main()
