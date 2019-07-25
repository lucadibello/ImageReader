# ImageReader
This website is able to read all the text written in an image using OCR (Optical Character Recognition).
It uses Flask (back-end) and as front-end framework Material Design Bootstrap (jQuery edition).

# Setup
## Install requirements
### UNIX
'''bash
pip3 install -r requirements.txt
'''

### Windows
'''bash
pip install -r requirements.txt
'''


## Setup Tesseract path
Insert Tesseract file path in main.py (line 54):

"""python
if __name__ == '__main__':
    # Setup Tesseract executable path
    #Example: r'D:\TesseractOCR\tesseract'
    pytesseract.pytesseract.tesseract_cmd = r'<path_to_tesseract_exe>'

    app.run(debug=True)
"""

# Start website
## UNIX
'''bash
python3 main.py
'''

## Windows
'''bash
python main.py
'''

PS: The website will start on the port 5000
