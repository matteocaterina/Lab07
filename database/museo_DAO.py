from database.DB_connect import ConnessioneDB
from model.museoDTO import Museo

"""
    Museo DAO
    Gestisce le operazioni di accesso al database relative ai musei (Effettua le Query).
"""

class MuseoDAO:
    def __init__(self):
        pass

    # TODO
    @staticmethod
    def leggi_dati_museo():
        lista_musei = []
        cnx = ConnessioneDB.get_connection()
        if cnx is None:
            print('Connection Failed')
            return None
        else:
            cursor = cnx.cursor(dictionary=True)
            query = 'SELECT * FROM museo'
            cursor.execute(query)
            for m in cursor:
                museo = Museo(int(m['id']),m['nome'],m['tipologia'])
                lista_musei.append(museo.nome)

        cursor.close()
        cnx.close()
        return lista_musei

    @staticmethod
    def leggi_filtro_museo(nome):
        lista_musei_filtro = []
        cnx = ConnessioneDB.get_connection()
        if cnx is None:
            print('Connection Failed')
            return None
        else:
            cursor = cnx.cursor(dictionary = True)
            query = f'SELECT * FROM museo WHERE nome = %s'
            cursor.execute(query, (nome,))
            for m in cursor:
                museo = Museo(m['id'],m['nome'],m['tipologia'])
                lista_musei_filtro.append(museo)

        cursor.close()
        cnx.close()
        return lista_musei_filtro
