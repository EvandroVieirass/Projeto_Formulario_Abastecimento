# importando sqllite

import sqlite3 as lite

#criando conexão

con = lite.connect('dados.db')

#inserir informações


def inserir_informacao(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO formulario (nome,email,telefone,dtabastecimento,combustivel,observacao)VALUES (?,?,?,?,?,?)"
        cur.execute(query,i)


#acessando informações
def mostrar_informacao():
    lista = []
    with con:
        cur = con.cursor()
        query = "SELECT * FROM formulario"
        cur.execute(query)
        informacao = cur.fetchall()
        for i in informacao:
            lista.append(i)
    return lista


#atualizar informações
def atualizar_info(i):
    
    with con:
        cur = con.cursor()
        query = "UPDATE formulario SET nome=?,email=?,telefone=?,dtabastecimento=?,combustivel=?,observacao=? WHERE id=?"
        cur.execute(query,i)


#deletar informações
def deletar_info(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM formulario WHERE id=?"
        cur.execute(query,i)

