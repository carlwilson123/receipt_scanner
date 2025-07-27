class Scanner:
    def __init__(self):
        pass

    def scan_receipt(self, image_path):
        # Load the image
        image = self.load_image(image_path)
        # Extract text from the image
        text = self.extract_text(image)
        return text

    def extract_text(self, image):
        import pytesseract
        # Use pytesseract to do OCR on the image
        text = pytesseract.image_to_string(image)
        return text

    def load_image(self, image_path):
        import cv2
        # Load the image using OpenCV
        image = cv2.imread(image_path)
        return image