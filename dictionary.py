class Dictionary:
    def __init__(self):
        self.parole={}

    def addWord(self, parola):
        parola=parola.strip().split(" ")
        self.parole[parola[0]]=[]
        self.parole[parola[0]].append(parola[1])

    def translate(self, ricercata):
        return self.parole[ricercata]

    def translateWordWildCard(self,query: str):
        flag = False
        for parola in self.parole:
            if len(parola) == len(query):
                corrisponde = True
                for i in range(len(query)):
                    if query[i] != "?" and query[i] != parola[i]:
                        corrisponde = False
                        break

                if corrisponde:
                    flag = True
                    traduzioni = self.parole[parola]
                    traduzioni_unite = ", ".join(traduzioni)
                    print(f"Match trovato per '{parola}': {traduzioni_unite}")
        if not flag:
            print("Nessun match trovato")