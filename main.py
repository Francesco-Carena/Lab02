import translator as tr

t = tr.Translator()
flag=True
t.loadDictionary("dictionary.txt")
while(flag):
    txtIn=t.printMenu()
    if txtIn == 1:
        print()
        txtIn = input("Inserisci la traduzione da agigungere: ").lower()
        copia=txtIn.split(" ")
        if copia[0].isalpha() and copia[1].isalpha():
            if copia[0] in t.dizionario.parole:
                t.dizionario.parole[copia[0]].append(copia[1])
                print("altra traduziona aggiunta")
            if copia[0] not in t.dizionario.parole:
                t.dizionario.addWord(txtIn)
                print("parola agigunta correttamente")

    if txtIn == 2:
        txtIn = input().lower()
        if txtIn.isalpha() and txtIn in t.dizionario.parole:
            trovata=t.handleTranslate(txtIn)
            print(f"La traduzione della parola cercata è: {trovata}")

    if txtIn == 3:
        txtIn = input().lower()
        t.handleWildCard(txtIn)

    if txtIn == 4:
        t.printAll()

    if txtIn == 5:
        flag=False