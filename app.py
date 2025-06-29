from flask import Flask, request, jsonify
from PIL import Image
import io

app = Flask(__name__)

@app.route('/analyze', methods=['POST'])
def analyze():
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'}), 400
    file = request.files['image']
    img_bytes = file.read()
    image = Image.open(io.BytesIO(img_bytes))

    # ตัวอย่างผลวิเคราะห์ (แทนที่ด้วยโมเดล AI จริง ๆ ได้)
    result = {
        "buy_signal": True,
        "sell_signal": False,
        "winrate_estimate": 0.82,
        "note": "ตัวอย่างผลวิเคราะห์"
    }
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
