from googlesearch import search
from statistics import mode


# Regras de negocio
class Services:
    def __init__(self, name, num_results=10):
        self.name = name
        self.listAll = []
        self.num_results = num_results

    def search_name(self):
        self.listAll = search(self.name,self.num_results+1,lang="pt-BR")
        if(len(self.listAll) > 10):
            return [self.listAll[i] for i in range(10) ]
        return self.listAll

    def __str__(self):
        return "<Lista resultado %r>" % self.listAll


class Popular:
    def __init__(self, lista):
        self.lista = lista

    def find_popular(self):
        self.new_list = [element.lower() for element in self.lista]
        return mode(self.new_list)
