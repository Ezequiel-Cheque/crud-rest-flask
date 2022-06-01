from flask import Flask, jsonify, request

app = Flask(__name__)

from products import products

@app.route('/')
def hello():
    return "Hello world from flask"

@app.route('/products')
def getProducts():
    return jsonify({"products": products, "message": "Product's list" })

@app.route('/products/<string:product_name>')
def getProduct(product_name):
    productsFound = [product for product in products if product['name'] == product_name]
    if (len(productsFound) > 0):
        return jsonify({"product": productsFound[0]})
    return jsonify({"message": "Product not fund"})

@app.route('/products', methods=["POST"])
def addProduct():
    new_product = {
        "name": request.json['name'],
        "price": request.json['price'],
        "quantity": request.json['name']
    }
    products.append(new_product)
    return jsonify({ "message": "Product Add Successfully", "products": products })


if __name__ == '__main__':
    app.run(debug=True, port=4000)