from flask import Flask, jsonify, request
app = Flask(__name__)

menus = [
    {"id": 1, "name": "Espresso", "price": 3800},
    {"id": 2, "name": "Americano", "price": 4100},
    {"id": 3, "name": "CafeLatte", "price": 4600},
]


@app.route('/')
def hello_flask():
    return "Hello World!!"

@app.route('/menus', methods=['GET'])
def get_menus():
    return jsonify(menus)

@app.route('/menus', methods = ['POST'])
def create_menu():
    request_data = request.get_json()  
    new_menu = {
        "id" : 4,
        "name" : request_data['name'],
        "price" : request_data['price'],
    }
    menus.append(new_menu)
    return jsonify(new_menu)


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
