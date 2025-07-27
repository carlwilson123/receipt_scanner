# Receipt Scanner

This project is a receipt scanning application that utilizes Optical Character Recognition (OCR) to extract text from receipt images. It provides a simple interface for users to scan their receipts and retrieve the relevant information.

## Project Structure

```
receipt-scanner
├── src
│   ├── main.py          # Entry point of the application
│   ├── scanner.py       # Contains the Scanner class for receipt scanning
│   └── utils.py         # Utility functions for image handling
├── requirements.txt     # Project dependencies
└── README.md            # Project documentation
```

## Installation

To set up the project, clone the repository and install the required dependencies:

```bash
git clone <repository-url>
cd receipt-scanner
pip install -r requirements.txt
```

## Usage

To start the receipt scanning process, run the following command:

```bash
python src/main.py
```

Follow the prompts to upload your receipt image, and the application will process it and display the extracted text.

## Dependencies

This project requires the following Python packages:

- `pytesseract`: For Optical Character Recognition.
- `opencv-python`: For image processing.

Make sure to have Tesseract OCR installed on your system for `pytesseract` to work properly. You can find installation instructions [here](https://github.com/tesseract-ocr/tesseract).

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.