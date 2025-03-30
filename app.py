from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/puan-hesapla', methods=['POST'])
def puan_hesapla():
    data = request.get_json()
    dogru = int(data.get('dogru', 0))
    yanlis = int(data.get('yanlis', 0))

    net = dogru - (yanlis / 4)
    
    # Gerçek YKS puan formülüne göre hesaplama
    puan = 100 + (net * 4)  # Basit örnek bir hesaplama (gerçek formül daha karmaşıktır!)

    return jsonify({"sonuc": round(puan, 2)})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
