import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def fillDDAnno(self):
        anni = ["2015", "2016", "2017", "2018"]
        for a in anni:
            self._view._ddAnno.options.append(ft.dropdown.Option(data=a, text=a, on_click=self.selectAnno))
        self._view.update_page()

    def fillDDColore(self):
        colori = self._model._colori
        for c in colori:
            self._view._ddColore.options.append(ft.dropdown.Option(data=c, text=c, on_click=self.selectColore))
        self._view.update_page()

    def fillDDProdotto(self):
        prodotti = self._model._nodes
        for p in prodotti:
            self._view._ddProdotto.options.append(ft.dropdown.Option(data=p, text=p, on_click=self.selectProdotto))
        self._view.update_page()
    def selectAnno(self, e):
        if e.control.data is None:
            self._choiceAnno = None
        else:
            self._choiceAnno = e.control.data

    def selectColore(self, e):
        if e.control.data is None:
            self._choiceColore = None
        else:
            self._choiceColore = e.control.data

    def selectProdotto(self, e):
        if e.control.data is None:
            self._choiceProdotto = None
        else:
            self._choiceProdotto = e.control.data

    def handle_graph(self, e):
        self._model._creaGrafo(self._choiceColore, self._choiceAnno)
        nNodi, nArchi = self._model.getGraphDetails()
        self._view.txt_result1.controls.clear()
        self._view.txt_result1.controls.append(ft.Text(f"Grafo correttamente creato.\n"
                                                       f"Il grafo ha {nNodi} nodi e {nArchi} archi"))

        self.fillDDProdotto()
        self._view._btnCammino.disabled = False
        self._view.update_page()


    def handle_percorso(self, e):
        percorso = self._model.percorso(self._choiceProdotto)
        self._view.txt_result2.controls.clear()
        self._view.txt_result2.controls.append(ft.Text(f"Il percorso trovato ha lunghezza {len(percorso)}"))
        for a in percorso:
            self._view.txt_result2.controls.append(ft.Text(f"{a[0]} --> {a[1]}: {a[2]}"))
        self._view.update_page()

