import dictionary
class Translator:

    def __init__(self):
        self.dizionario = dictionary.Dictionary()

    def printMenu(self):
        # 1. Aggiungi nuova parola
        # 2. Cerca una traduzione
        # 3. Cerca con wildcard
        # 4. Exit
        print("--------------------")
        print("--------------------")
        print("    Traduttore      ")
        print("1. New Word         ")
        print("2. Search Word      ")
        print("3. Search char      ")
        print("4. Print All        ")
        print("5. Exit             ")
        print("--------------------")
        print("--------------------")
        print()
        return int(input("inserisci valore: "))


    def loadDictionary(self, dict):
        #dizionario = dictionary.Dictionary()
        # dict is a string with the filename of the dictionary
        with open(dict, "r", encoding="utf-8") as file:
            riga = file.readline()
            while riga:
                self.dizionario.addWord(riga)
                riga = file.readline()
            file.close()
        return self.dizionario

    def handleAdd(self, entry):
        # entry is a tuple <parola_aliena> <traduzione1 traduzione2 ...>

        pass

    def handleTranslate(self, query):
        # query is a string <parola_aliena>
        return self.dizionario.translate(query)

    def handleWildCard(self,query):
        # query is a string with a ? --> <par?la_aliena>
        if query.count("?") != 1:
            print("Errore: la ricerca con wildcard deve contenere esattamente un carattere '?'.")
            return

            # 2. CONTROLLO ALFABETICO: Rimuovo temporaneamente il "?" per assicurarmi
            # che tutto il resto sia composto solo da lettere
        if not query.replace("?", "").isalpha():
            print("Errore: la parola può contenere solo lettere e un singolo '?'.")
            return

        return self.dizionario.translateWordWildCard(query)

    def printAll(self):
        # query is a string with a ? --> <par?la_aliena>
        print()
        for parola in self.dizionario.parole:
            print(parola, end=": ")
            for p in self.dizionario.parole[parola]:
                print(p, end=" ")
            print()