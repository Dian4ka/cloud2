from flask import Flask, request, jsonify

app = Flask(__name__)

data = []

@app.route("/", methods=["GET"])
def home():
    return "Hello from Flask Cloud App!"

@app.route("/items", methods=["GET"])
def get_items():
    return jsonify(data)

@app.route("/items", methods=["POST"])
def create_item():
    item = request.json
    data.append(item)
    return jsonify({"message": "Item added", "item": item}), 201

@app.route("/items/<int:index>", methods=["PUT"])
def update_item(index):
    if 0 <= index < len(data):
        data[index] = request.json
        return jsonify({"message": "Item updated", "item": data[index]})
    return jsonify({"error": "Index out of range"}), 404

@app.route("/items/<int:index>", methods=["DELETE"])
def delete_item(index):
    if 0 <= index < len(data):
        item = data.pop(index)
        return jsonify({"message": "Item deleted", "item": item})
    return jsonify({"error": "Index out of range"}), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
