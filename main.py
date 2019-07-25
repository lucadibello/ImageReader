import pytesseract
from flask import Flask, request, render_template
app = Flask(__name__)


@app.route('/')
def hello():
    return render_template("index.html", title="Image Reader")


@app.route('/uploader', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        print(f)
        return 'file uploaded successfully'


if __name__ == '__main__':
    app.run()
