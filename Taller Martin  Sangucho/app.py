from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return jsonify({"mensaje": "Hola, soy Martin Sangucho - Taller individual"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
