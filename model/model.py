import copy

import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._grafo = nx.Graph()
        self._idMap = {}
        self._colori = DAO.getAllColors()

    def _creaGrafo(self, colore, anno):
        self._grafo.clear()
        self._nodes = DAO.getAllNodes(colore)
        self._grafo.add_nodes_from(self._nodes)
        nodi = self._nodes
        for u in nodi:
            for v in nodi:
                if u != v:
                    arco = DAO.getEdge(u, v, int(anno))
                    if arco[0][0] != None:
                        self._grafo.add_edge(arco[0][0], arco[0][1], weight=arco[0][2])

    def getGraphDetails(self):
        return len(self._grafo.nodes), len(self._grafo.edges)

    def percorso(self, partenza):
        self._bestPath = []
        self._ricorsione(partenza, [])
        return self._bestPath

    def _ricorsione(self, nodo, parziale):
        if len(parziale) > 0:
            if len(parziale) >= len(self._bestPath):
                self._bestPath = copy.deepcopy(parziale)
        vicini = self._grafo.neighbors(nodo)
        for v in vicini:
            peso = self._grafo[nodo][v]["weight"]
            peso_precedente = 0
            if len(parziale) > 0:
                peso_precedente = parziale[-1][2]
            if peso >= peso_precedente and self.filtroArchi(nodo, v, parziale):
                parziale.append((nodo, v, peso))
                self._ricorsione(v, parziale)
                parziale.pop()

    def filtroNodi(self, v, parziale):  # non dice percorso semplice quindi non devo filtrare i nodi
        pass

    def filtroArchi(self, n, v, parziale):
        for a in parziale:
            if a[:2] == (n, v) or a[:2] == (v, n):
                return False
        return True
