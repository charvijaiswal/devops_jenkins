from flask import Flask, request, jsonify

app = Flask(__name__)

# Temporary product data
products = [
    {
        'id': 1,
        'name': 'Mac Book Pro',
        'price': 45.55,
        'description': 'Amazing laptop with awesome security'
    },
    # Other products...
]

# Temporary cart data stored in a Python dictionary for each user
carts = {}

# Routes for handling different API endpoints
@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(products)

@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = next((p for p in products if p['id'] == product_id), None)
    if not product:
        return jsonify({'error': f'Product with ID {product_id} not found'}), 404
    return jsonify(product)

@app.route('/products', methods=['POST'])
def add_product():
    data = request.get_json()
    if not all(key in data for key in ('name', 'price', 'description')):
        return jsonify({'error': 'Missing required fields'}), 400
    
    new_product = {
        'id': len(products) + 1,
        'name': data['name'],
        'price': data['price'],
        'description': data['description']
    }
    products.append(new_product)
    return jsonify(new_product), 201

@app.route('/cart', methods=['GET'])
def view_cart():
    user_id = request.args.get('user_id')
    if not user_id:
        return jsonify({'error': 'User ID is required'}), 400
    
    cart = carts.get(user_id, {})
    # Rest of the function remains unchanged...

@app.route('/cart/add', methods=['POST'])
def add_to_cart():
    data = request.get_json()
    if not all(key in data for key in ('user_id', 'product_id')):
        return jsonify({'error': 'Missing required fields'}), 400

    user_id = data['user_id']
    product_id = data['product_id']
    quantity = data.get('quantity', 1)

    # Rest of the function remains unchanged...

@app.route('/cart/delete', methods=['POST'])
def delete_from_cart():
    data = request.get_json()
    if not all(key in data for key in ('user_id', 'product_id')):
        return jsonify({'error': 'Missing required fields'}), 400

    user_id = data['user_id']
    product_id = data['product_id']

    # Rest of the function remains unchanged...

if __name__ == '__main__':
    app.run(debug=True)
