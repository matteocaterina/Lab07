from database.DB_connect import ConnessioneDB
from model.artefattoDTO import Artefatto

"""
    ARTEFATTO DAO
    Gestisce le operazioni di accesso al database relative agli artefatti (Effettua le Query).
"""

class ArtefattoDAO:
    def __init__(self):
        pass

    # TODO
    @staticmethod
    def leggi_epoche_artefatti():
        lista_epoche = []
        cnx = ConnessioneDB.get_connection()
        if cnx is None:
            print('Connection Failed')
            return None
        else:
            cursor = cnx.cursor(dictionary=True)
            query = f'SELECT * FROM artefatto'
            cursor.execute(query)
            for a in cursor:
                artefatto = Artefatto(a['id'],a['nome'], a['tipologia'], a['epoca'], a['id_museo'])
                lista_epoche.append(artefatto.epoca)

        cnx.close()
        cursor.close()
        return lista_epoche

    @staticmethod
    def leggi_filtro_artefatto(epoca):
        lista_artefatti_filtro = []
        cnx = ConnessioneDB.get_connection()
        if cnx is None:
            print('Connection Failed')
            return None
        else:
            cursor = cnx.cursor(dictionary=True)
            if epoca is None:
                query = f'SELECT * FROM artefatto'
                cursor.execute(query)
                for a in cursor:
                    artefatto = Artefatto(a['id'], a['nome'], a['tipologia'], a['epoca'], a['id_museo'])
                    lista_artefatti_filtro.append(artefatto)
            else:
                query = 'SELECT * FROM artefatto WHERE epoca = %s'
                cursor.execute(query, (epoca,))
                for a in cursor:
                    artefatto = Artefatto(a['id'], a['nome'], a['tipologia'], a['epoca'], a['id_museo'])
                    lista_artefatti_filtro.append(artefatto)

        cnx.close()
        cursor.close()
        return lista_artefatti_filtro