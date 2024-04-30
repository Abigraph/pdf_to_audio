import PyPDF2
from gtts import gTTS
import os

def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for page_number in range(len(reader.pages)):
            text += reader.pages[page_number].extract_text()
    return text

def convert_text_to_audio(text, output_path):
    tts = gTTS(text)
    tts.save(output_path)

def main(pdf_path, output_path):
    text = extract_text_from_pdf(pdf_path)
    convert_text_to_audio(text, output_path)

if __name__ == "__main__":
    pdf_path = "C:\\FILE\\pdf\\application.pdf"
    output_path = "C:\\FILE\\pdf.mp3"
    main(pdf_path, output_path)
    print("Done")
