from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Diccionario para almacenar los datos del inventario
inventory_data = {
    '1': {
        'nombre': 'Manzanas',
        'precio': '$1.50',
        'peso': '0.2 kg',
        'descripcion': 'Frescas y jugosas'
    },
    '2': {
        'nombre': 'Plátanos',
        'precio': '$1.20',
        'peso': '0.15 kg',
        'descripcion': 'Maduros y dulces'
    },
    '3': {
        'nombre': 'Naranjas',
        'precio': '$1.00',
        'peso': '0.25 kg',
        'descripcion': 'Dulces y refrescantes'
    },
    '4': {
        'nombre': 'Uvas',
        'precio': '$2.00',
        'peso': '0.3 kg',
        'descripcion': 'Jugosas y deliciosas'
    },
    '5': {
        'nombre': 'Fresas',
        'precio': '$2.50',
        'peso': '0.1 kg',
        'descripcion': 'Dulces y aromáticas'
    },
    '6': {
        'nombre': 'Pera',
        'precio': '$1.80',
        'peso': '0.25 kg',
        'descripcion': 'Sabrosas y jugosas'
    },
    '7': {
        'nombre': 'Piña',
        'precio': '$2.20',
        'peso': '1.0 kg',
        'descripcion': 'Dulce y refrescante'
    },
    '8': {
        'nombre': 'Mangos',
        'precio': '$2.00',
        'peso': '0.3 kg',
        'descripcion': 'Dulces y jugosos'
    },
    '9': {
        'nombre': 'Kiwi',
        'precio': '$1.70',
        'peso': '0.1 kg',
        'descripcion': 'Ácido y refrescante'
    },
    '10': {
        'nombre': 'Cerezas',
        'precio': '$3.00',
        'peso': '0.15 kg',
        'descripcion': 'Dulces y jugosas'
    },
    '11': {
        'nombre': 'Sandías',
        'precio': '$4.00',
        'peso': '3.0 kg',
        'descripcion': 'Dulces y refrescantes'
    },
    '12': {
        'nombre': 'Melones',
        'precio': '$3.50',
        'peso': '2.5 kg',
        'descripcion': 'Dulces y jugosos'
    },
    '13': {
        'nombre': 'Mangostanes',
        'precio': '$5.00',
        'peso': '0.2 kg',
        'descripcion': 'Dulces y exóticos'
    },
    '14': {
        'nombre': 'Granadas',
        'precio': '$2.80',
        'peso': '0.3 kg',
        'descripcion': 'Dulces y jugosas'
    },
    '15': {
        'nombre': 'Ciruelas',
        'precio': '$2.50',
        'peso': '0.15 kg',
        'descripcion': 'Dulces y jugosas'
    }
}

@app.route('/api/inventory', methods=['GET'])
def get_inventory():
    """Obtiene todos los datos del inventario."""
    return jsonify(inventory_data)

@app.route('/api/inventory/<product_id>', methods=['GET'])
def get_product_by_id(product_id):
    """Obtiene los datos de un producto específico por su ID."""
    product = inventory_data.get(product_id)
    if product:
        return jsonify(product)
    else:
        return jsonify({'error': 'Product not found'}), 404

@app.route('/api/inventory', methods=['POST'])
def add_product():
    """Añade un nuevo producto al inventario."""
    if not request.json or 'nombre' not in request.json or 'precio' not in request.json \
            or 'peso' not in request.json or 'descripcion' not in request.json:
        return jsonify({'error': 'Invalid input'}), 400
    product_id = str(len(inventory_data) + 1)
    product = {
        'nombre': request.json['nombre'],
        'precio': request.json['precio'],
        'peso': request.json['peso'],
        'descripcion': request.json['descripcion']
    }
    inventory_data[product_id] = product
    return jsonify({'message': 'Product added'}), 201

@app.route('/api/inventory/<product_id>', methods=['PUT'])
def update_product(product_id):
    """Actualiza los datos de un producto específico por su ID."""
    if not request.json or 'nombre' not in request.json or 'precio' not in request.json \
            or 'peso' not in request.json or 'descripcion' not in request.json:
        return jsonify({'error': 'Invalid input'}), 400
    if product_id in inventory_data:
        inventory_data[product_id] = {
            'nombre': request.json['nombre'],
            'precio': request.json['precio'],
            'peso': request.json['peso'],
            'descripcion': request.json['descripcion']
        }
        return jsonify({'message': 'Product updated'})
    else:
        return jsonify({'error': 'Product not found'}), 404

@app.route('/api/inventory/<product_id>', methods=['DELETE'])
def delete_product(product_id):
    """Elimina un producto del inventario por su ID."""
    if product_id in inventory_data:
        del inventory_data[product_id]
        return jsonify({'message': 'Product deleted'})
    else:
        return jsonify({'error': 'Product not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
