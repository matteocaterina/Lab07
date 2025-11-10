import flet as ft
from UI.view import View
from model.model import Model

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: Model):
        self._model = model
        self._view = view

        # Variabili per memorizzare le selezioni correnti
        self.museo_selezionato = None
        self.epoca_selezionata = None

    # POPOLA DROPDOWN
    # TODO
    def popola_dropdown(self):

        lista_nomi_musei = self._model.get_musei()
        set_epoche = set(self._model.get_epoche())

        self._view.btn_museo.options.clear()
        self._view.btn_museo.options.append(ft.dropdown.Option('Nessun Filtro'))
        for nome_museo in lista_nomi_musei:
            self._view.btn_museo.options.append(ft.dropdown.Option(nome_museo))

        self._view.btn_epoca.options.clear()
        self._view.btn_epoca.options.append(ft.dropdown.Option('Nessun Filtro'))
        for epoca in set_epoche:
            self._view.btn_epoca.options.append(ft.dropdown.Option(epoca))

        self._view.update()



    # CALLBACKS DROPDOWN
    # TODO
    def handler_dropdown_museo(self,e):
        self.museo_selezionato = self._view.btn_museo.value

    def  handler_dropdown_epoca(self,e):
        self.epoca_selezionata = self._view.btn_epoca.value


    # AZIONE: MOSTRA ARTEFATTI
    # TODO
    def mostra_artefatti(self,e):

        try:
            self.museo_selezionato = self._view.btn_museo.value.strip()
            self.epoca_selezionata = self._view.btn_epoca.value.strip()

        except AttributeError:
            self._view.show_alert(' ❌ Selezionare un fitro per museo ed epoca')
            return

        artefatti = self._model.get_artefatti_filtrati(self.museo_selezionato, self.epoca_selezionata)

        self._view.list_view.controls.clear()

        if not artefatti:
            self._view.show_alert('nessun artefatto trovato')
        else:
            for artefatto in artefatti:
                self._view.list_view.controls.append(ft.Text(str(artefatto)))


        self._view.update()




