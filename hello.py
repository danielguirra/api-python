from flask import Flask, jsonify, request

lista_nomes = ["João", "Maria", "José"]
app = Flask(__name__)
@app.get('/')
def test():
    return 'ekwk'

# @app.route('/')
# def index():
#     return "Olá, mundo!"

@app.route('/names')
def nomes():
   
    return jsonify(lista_nomes)

@app.route('/add-new-name', methods=['POST'])
def novo_nome():
    novo_nome = request.args.get('name')
    if not novo_nome:
        return jsonify({'error': 'O parâmetro name é obrigatório'}), 400
    lista_nomes.append(novo_nome)
    return jsonify({'message': 'Nome adicionado com sucesso'})

@app.route('/edit-name/<int:id>', methods=['PUT'])
def atualizar_nome(id):
    nome = request.args.get('name')
    if not nome:
        return jsonify({'error': 'O parâmetro name é obrigatório'}), 400
    if id >= len(lista_nomes) or id < 0:
        return jsonify({'error': 'O ID do nome não é válido'}), 400
    lista_nomes[id] = nome
    return jsonify({'message': 'Nome atualizado com sucesso'})



if __name__ == '__main__':
    app.run(debug=True,port=3000)
