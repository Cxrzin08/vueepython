from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app) 

usuarios_db = []

@app.route('/novo-usuario', methods=['POST'])
def novo_usuario():
    data = request.get_json()
    
    if not data or 'nome' not in data:
        return jsonify({'message': 'Dados inválidos'}), 400
    
    nome = data['nome'].strip()
    
    if not nome:
        return jsonify({'message': 'Nome não pode estar vazio'}), 400
    
    if nome in usuarios_db:
        return jsonify({'message': 'Usuário já existe'}), 409
    
    usuarios_db.append(nome)
    return jsonify({
        'message': f'Usuário {nome} cadastrado com sucesso!',
        'usuario': nome
    }), 201

@app.route('/pegar-usuarios', methods=['GET'])
def pegar_usuarios():
    return jsonify({'usuarios': usuarios_db})

if __name__ == '__main__':
    app.run(debug=True, port=5000)