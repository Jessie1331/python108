import json
from flask import Flask, request
from config import Me
from mock_data import Catalog

app = Flask(__name__)
@app.get("/api")
def index():
    return "WELCOM TO THE FINAL"

@app.post("/api/version")
def version():
    v = {
        "version": "1.0.0"
        "name"  "Jesenia"
    }
    return json.dumps(v)


@app.get("/api/about")
def about():
    return json.dumps(Me)

@app.get("/api/Catalog")
def get_catalog():
    return json.dumps(Catalog)
@app.post('/api/Catalog')
def save_product():
    product = request.get_json()
    product["_id"] = [len(Catalog) + 1]
    Catalog.append(product)

    return json.dumps(product)
@app.Get('api/reports')
def get_reports():
    return json.dumps(Catalog)


@app.put('/api/Catalog/<id>')
def update_product(id):
    product = request.get_json()
    Catalog[id] = product
    return json.dumps(product)

app.run(debug=True)