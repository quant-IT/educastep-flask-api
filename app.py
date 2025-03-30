from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)

# TÜM domainlerden isteğe izin ver
CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.route('/api/puan-hesapla', methods=['POST'])
def puan_hesapla():
    data = request.get_json()
    dogru = int(data.get('dogru', 0))
    yanlis = int(data.get('yanlis', 0))

    net = dogru - (yanlis / 4)
    
    puan = 100 + (net * 4)

    return jsonify({"sonuc": round(puan, 2)})

if __name__ == '__main__':
    app.run(debug=True)
