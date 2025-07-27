import cv2
import pytesseract
from scanner import Scanner

def main():
    print("Welcome to the Receipt Scanner!")
    image_path = input("Please enter the path to the receipt image: ")
    
    scanner = Scanner()
    scanned_text = scanner.scan_receipt(image_path)
    
    print("Scanned Text:")
    print(scanned_text)

if __name__ == "__main__":
    main()