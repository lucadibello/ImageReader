import datetime
import io

import pytesseract
from PIL import Image
from flask import Flask, request, render_template, redirect, url_for, session

app = Flask(__name__)

# Secret key for sessions encryption
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.route('/')
def home():
    return render_template("index.html", title="Image Reader")


@app.route('/scanner', methods=['GET', 'POST'])
def scan_file():
    if request.method == 'POST':
        start_time = datetime.datetime.now()
        image_data = request.files['file'].read()

        scanned_text = pytesseract.image_to_string(Image.open(io.BytesIO(image_data)))

        print("Found data:", scanned_text)

        session['data'] = {
            "text": scanned_text,
            "time": str((datetime.datetime.now() - start_time).total_seconds())
        }

        return redirect(url_for('result'))


@app.route('/result')
def result():
    if "data" in session:
        data = session['data']
        return render_template(
            "result.html",
            title="Result",
            time=data["time"],
            text=data["text"],
            words=len(data["text"].split(" "))
        )
    else:
        return "Wrong request method."


if __name__ == '__main__':
    # Setup Tesseract executable path
    pytesseract.pytesseract.tesseract_cmd = r'D:\TesseractOCR\tesseract'
    app.run(debug=True)
