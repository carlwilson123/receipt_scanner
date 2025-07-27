#region imports
from PIL import Image#type: ignore
import pytesseract #type: ignore

#endregion

class ImageProcessor():
    #region class initialization
    def __init__(self,tess_path: str):
        
        #pytesseract setup
        
        self.tess_path = tess_path

        pytesseract.pytesseract.tesseract_cmd = self.tess_path
    #endregion
    
    
if __name__ == "__main__":
    #debugging code to test the ImageProcessor class
    temp = ImageProcessor(r'C:\Program Files\Tesseract-OCR\tesseract.exe')
    
    
    pass