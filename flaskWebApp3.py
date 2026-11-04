from flask import Flask, jsonify, request
import pandas as pd

app = Flask(__name__)

df = pd.read_csv('cars.csv')

@app.route('/')
def index():
    return jsonify({"message": "Welcome to my First API"})

@app.route('/hello', methods=['GET'])
def hello():
    return jsonify({"message": "Welcome to my first API"})

@app.route('/cars')
def get_cars():
    return jsonify(df.head(10).to_dict(orient='records'))

@app.route('/manufacturers')
def manufacturers():
    return jsonify(df['CarName'].str.split().str[0].unique().tolist())

@app.route("/cars/prices")
def cars_prices():
    return jsonify(df[['CarName', 'price']].to_dict(orient='records'))

sample_data = [
    {"id": 1, "name": "Toyota Corolla", "price": 20000},
    {"id": 2, "name": "Honda Civic", "price": 22000},
]
@app.route('/data', methods=['GET'])
def get_data():
    return jsonify(sample_data)

@app.route('/data', methods=['POST'])
def add_data():
    new_item = request.get_json()
    if not new_item:
        return jsonify({"error": "No JSON body provided"}), 400
    new_item["id"] = len(sample_data) + 1
    sample_data.append(new_item)
    return jsonify(new_item), 201

if __name__ == '__main__':
    app.run(debug=True, port=5030)
