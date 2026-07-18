from flask import Flask, request, jsonify
from predict import predict_img
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"

@app.route("/")
def home():
    return """
    <form action="/predict" method="post" enctype="multipart/form-data">
        <input type="file" name="file">
        <input type="submit">
    </form>
    """

@app.route("/predict", methods=["POST"])
def predict():
    file = request.files["file"]
    file.save("temp.jpg")

    result = predict_img("temp.jpg")

    return f"<h1>{result}</h1>"


@app.route("/test", methods=["POST"])
def test():

    print("FILES:", request.files)
    print("FORM:", request.form)

    file = request.files.get("file")

    if not file:
        return {"error": "No file received"}, 400

    file.save("test.jpg")

    return {"status": "received"}


if __name__ == "__main__":
    app.run(debug=True, host = "0.0.0.0", port=80)


