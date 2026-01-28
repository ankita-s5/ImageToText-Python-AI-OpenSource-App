# 🖼️ ImageToText – Python AI Open Source App

## 📌 Project Overview
**ImageToText** is an open-source Python application that extracts text from images using **AI-powered Optical Character Recognition (OCR)**.
The app converts images containing printed or handwritten text into machine-readable text with high accuracy.

This project demonstrates practical use of **Computer Vision, OCR, and Python AI libraries** in a clean and extensible way.

---

## 🎯 Key Features
- 📸 Extract text from images (JPG, PNG, JPEG)
- 🧠 AI-powered OCR using Python
- 🔍 Supports printed and basic handwritten text
- ⚡ Fast and lightweight processing
- 📄 Export extracted text
- 🧩 Easy integration with other Python projects

---

## 🧠 Skills Demonstrated
- Optical Character Recognition (OCR)
- Image preprocessing
- Python AI libraries
- File handling
- Open-source project structuring

---

## 🛠 Tech Stack
- **Language:** Python
- **OCR Engine:** EasyOCR
- **Libraries:** OpenCV, Pillow, NumPy

---

## 📂 Project Structure
```text
ImageToText-Python-AI-OpenSource-App/
│
├── images/
│   └── sample_image.png
│
├── src/
│   ├── image_to_text.py
│   └── preprocessing.py
│
├── output/
│   └── extracted_text.txt
│
├── requirements.txt
└── README.md
```

---

## ▶️ How to Run the Application

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/ankita-s5/ImageToText-Python-AI-OpenSource-App.git
cd ImageToText-Python-AI-OpenSource-App
```

### 2️⃣ Create Virtual Environment (Recommended)
```bash
python -m venv venv
source venv/binactivate   # Linux / Mac
venv\Scripts\activate    # Windows
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 5️⃣ Run the App
```bash
python src/image_to_text.py
```

---

## 📸 Example Usage
```python
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

```

---

## 📊 Output
- Extracted text printed to console
- Saved to `output/extracted_text.txt`
- Ready for NLP or analytics pipelines

---

## 🚀 Future Enhancements
- Multi-language OCR
- Handwritten text accuracy improvement
- GUI / Web App
- PDF to Text support
- REST API deployment

---

## 👩‍💻 Author
**Ankita Singh**  
Data Scientist | Python | AI | Computer Vision

🔗 GitHub: https://github.com/ankita-s5  
🔗 LinkedIn: https://www.linkedin.com/in/ankita-singh-50247b3a6/

---

## 🤝 Contributing
Contributions are welcome!
Fork the repo, raise issues, or submit pull requests.

---


> 💡 *Turning images into actionable text using AI.*
