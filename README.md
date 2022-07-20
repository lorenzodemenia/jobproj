# Jobproj

Ho voluto in questo progetto creare io una mia funzione che va a fare il parsing dell'indirizzo, per farla ho usato VSCode.
# Il mio ragionamento : 
  1. Ho cercato un punto in comune fra tutte le possibili combinazioni di indirizzi proposti e che potrebbero propormi 
  2. Ho notato che la dimensione e il tipo del cap sono fisse e quindi riconoscibili, in particolare ho visto che il cap è composto da 5 numeri 
  3. Sapendo questo, per prima cosa, ho tolto tutte le virgole e ho diviso la stringa in sotto stringhe, dividendole ogni volta che trovava uno spazio
  4. Ho contato la posizione esatta del cap all'interno della lista di liste 
  5. Sapendo la posizione esatta mi è bastata usare questa informazione per raccogliere le altre informazioni 

# Come ho gestito il tutto con Django: 

Per farlo interfacciare con Django ho fatto tutti i settaggi iniziali, quindi:
  1. Scaricare e installare Django 
  2. Creare l'app e inserirla nel file settings.py
  3. Impostare le views ( io in Flask le ho viste come route ) 
  4. Ho passato i dati attraverso delle liste che venivano inserite dentro ad un dizionario, così da poterlo poi scorrere nel file che andava a                      
      renderizzare 
  5. Per gestire l'errore mi sono basato sugli elementi elencati sopra per controllare se rispettava la forma richiesta 

Per visualizzare l'output, l'ho inserito dentro un dizionario e poi visualizzato nel file parser.html 

Volevo utilizzare anche deepparse ma non mi permetteva di installarlo, con essa avrei utilizzato delle chiamate a funzione per fare il parsing degli indirizzi 
