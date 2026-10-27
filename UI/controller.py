import flet as ft
from UI.view import View
from model.model import DepositoStrumenti

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: DepositoStrumenti):
        self._model = model
        self._view = view

    def get_nome(self):
        return self._model.nome      #ritorna il nome dell oggetto modello

    def get_responsabile(self):
        return self._model.responsabile         #ritorna il nome dell oggetto modello

    def set_responsabile(self, responsabile):
        self._model.responsabile = responsabile      #cambia responsabile dell attributo del oggetto modello

    def conferma_responsabile(self, e):
        self._model.responsabile = self._view.input_responsabile.value
        self._view.txt_responsabile.value = f"Responsabile: {self._model.responsabile}"
        self._view.update()

    # Altre Funzioni Event Handler
    # TODO ci provo

    def mostra_strumenti(self):  #per il tasto mostra strumenti dell listview della view
        strumenti = self._model.get_strumenti()
        self._view.lista_strumenti.controls.clear()
        for strumento in strumenti:
            self._view.lista_strumenti.controls.append(ft.Text(str(strumento)))

        self._view.update()

    def get_strumenti_tipo(self,):  #come prima ma per la ricerca
        strumenti = self._model.cerca_strumenti_per_tipo(tipo)
        self._view.lista_strumenti_ricerca.controls.clear() #pulire lista per non avere duplicati
        for strumento in strumenti:
            self._view.lista_strumenti_ricerca.controls.append(ft.Text(str(strumento)))

        self._view.update()


