# API - é um lugar para disponibilizar recursos e/ou funcionalidades
# 1 objetivo - criar um api que disponibiliza a consulta, criação, edição e exclusão de livros
# 2 URL BASE - LOCALHOST
# 3 END POINTS-
"""
-localhost/livros (GET) - onde posso consultar
-localhost/livros/id (GET)(GET com id) - quero obter um livro específico 
-localhost/livro/id(PUT) - quero ter a possibilidade de modificar o livro
-localhost/livro/id (DELETE) - excluir um livro por id
"""
# 4 - Quais recursos ? Livros (posso disponibilizar tanto uma funcionalidade como um recurso)

# Flask
#pip install flask

#---------------------------------------------------------------------------------------------
from flask import Flask, jsonify, request
# flask para criar api/ servidor
# jsonify, que nos permite retornar no formato json
# request para acessar os dados que estão vindo e indo dentro das requisições

# para criar o api flask, o servidor que estará rodando esta api
app = Flask(__name__)

# fonte de dados
# neste exemplo vamos utilizar um dicionário bem simples;
# poderia ser feito por um arquivo

livros = [
    {
        'id' : 1,
        'titulo': 'O Senhor dos Anéis',
        'autor' : 'J.R.R Tolkien'
    },
    {
        'id' : 2,
        'titulo': 'Harry Potter e a Pedra Filosofal',
        'autor' : 'J.K Howling'
    },
    {
        'id' : 3,
        'titulo': 'James Clear',
        'autor' : 'Hábitos Atômicos'
    }
]

# consultar todos
# criar uma função que irá retornar algo

# para isso ser considerado um api tenho que decorar ela
# passo um app route , e digitar qual a url que tenho que digitar para chegar nela
# para ser mais específico, eu utilizo o methods =['GET'] para demonstrar que eu quero só o get
@app.route('/livros', methods =['GET'])
def obter_livro():
    # pegar algo e retornar algo em formato json que é esperado em uma api
    return jsonify(livros)


# consultar por id
# especificando que eu espero numero inteiro e será identificado por id
# escrevo o link http://localhost:8000/livros/1  , 1 é o id que eu quero ver
@app.route('/livros/<int:id>', methods=['GET'])
def obter_livro_por_id(id):
    # iterar por todos os livros e verificar se o id é igual ao que foi passado
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)

# editar
# put é um método que nos permite alterar informação
@app.route('/livros/<int:id>',methods=['PUT'])
def editar_livro_por_id(id):
    # para obter informação que foi enviado do usuário para o api, utilizamos o request.get_json()
    livro_alterado = request.get_json()
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])

#Criar
@app.route('/livros', methods=['POST'])
def incluir_novo_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)

    return jsonify(livros)

# excluir
@app.route('/livros/<int:id>', methods=['DELETE'])
def excluir_livros(id):
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]
    return jsonify(livros)

app.run(port=8000, host='localhost', debug=True)
# "http://localhost:8000/livros".

# utilizar o postman
# + , get, http://localhost:8000/livros, send


# para utilizar o PUT, tem que selecionar o PUT , ir no Body, raw, alterar o tipo para JSON;

# para utilizar o POST, vou criar uma nova aba no postman, selecionar POST, colar a url http://localhost:8000/livros

"""
{
    "id" : 4,
    "titulo" : "Um grande livro",
    "Autor" : "Lucas"
}
"""

# para utilizar o DELETE, vamos mudar o método para DELETE NO POSTMAN
# e colocar a url livros/id que eu quero deletar