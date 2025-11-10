from database.museo_DAO import MuseoDAO
from database.artefatto_DAO import ArtefattoDAO

'''
    MODELLO: 
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Si occupa di interrogare il DAO (chiama i metodi di MuseoDAO e ArtefattoDAO)
'''

class Model:
    def __init__(self):
        self._museo_dao = MuseoDAO()
        self._artefatto_dao = ArtefattoDAO()

    # --- ARTEFATTI ---
    def get_artefatti_filtrati(self, museo:str, epoca:str):
        """Restituisce la lista di tutti gli artefatti filtrati per museo e/o epoca (filtri opzionali)."""
        # TODO

        museo = None if museo == 'Nessun Filtro' else museo
        epoca = None if epoca == 'Nessun Filtro' else epoca

        lista_artefatti = self._artefatto_dao.leggi_filtro_artefatto(epoca)

        if museo is None:
            return lista_artefatti

        lista_musei = self._museo_dao.leggi_filtro_museo(museo)
        lista_filtrata = []

        for museo in lista_musei:
            for artefatto in lista_artefatti:
                if museo.id == artefatto.id_museo:
                    lista_filtrata.append(artefatto)
        return lista_filtrata


    def get_epoche(self):
        """Restituisce la lista di tutte le epoche."""
        # TODO
        lista_epoche = self._artefatto_dao.leggi_epoche_artefatti()
        return lista_epoche


    # --- MUSEI ---
    def get_musei(self):
        """ Restituisce la lista di tutti i musei."""
        # TODO
        lista_musei = self._museo_dao.leggi_dati_museo()
        return lista_musei

