import requests
url = "https://raw.githubusercontent.com/DALBO-creator/tpi-project-PythonDatasetExplore/main/data/m.json"

response = requests.get(url)
data = response.json()
print(f"Totale record: {len(data)}")


def analizza_voti(lista_giochi):
    
    voti = []
    for gioco in lista_giochi:
        if gioco.get('meta_score') is not None:
            voti.append(gioco['meta_score'])
    
    if voti:
        print(f"Voto Massimo: {max(voti)}")
        print(f"Voto Minimo: {min(voti)}")
        print(f"Voto Medio: {sum(voti) / len(voti):.2f}")
    else:
        print("Nessun voto numerico trovato")

def conta_piattaforme(lista_giochi):
    conteggio = {} # nuovo dizionario vuoto
    for gioco in lista_giochi:
        platform = gioco.get('platform', 'Sconosciuta') #per ogni gioco recupersa il valore della chiave platform (sconosciuta se non esiste)
        conteggio[platform] = conteggio.get(platform, 0) + 1 #se la piattaforma esiste nel dizionario conteggio incrementa il suo valore di 1, altrimenti inizializza a 0 e poi incrementa di 1
    
    print("\nDistribuzione per piattaforma:")
    for platform, count in conteggio.items(): #.items estrare coppie chiave-valore dal dizionario --> per ogni coppia all'interno dell'insieme delle coppie..
        print(f"- {platform}: {count}")

def conta_generi(lista_giochi): 
    generi_count = {}
    for gioco in lista_giochi:
        generi = gioco.get('genres', []) #genres è una lista (più generi per gioco), quindi o lista dei generi o lista vuota
        for genere in generi:
            generi_count[genere] = generi_count.get(genere, 0) + 1
    
    print("\nDistribuzione per genere (top 10):")
    generi_ordinati = sorted(generi_count.items(), key=lambda x: x[1], reverse=True) #key=lambda x: x[1] ordina in base al secondo elemento (quello a indice 1) della tupla (il conteggio) 
    for genere, count in generi_ordinati[:10]:
        print(f"- {genere}: {count}")


def gioco_con_voto_massimo(lista_giochi):
    gioco_migliore = None
    voto_max = -1
    
    for gioco in lista_giochi:
        voto = gioco.get('meta_score')
        if voto is not None and voto > voto_max:
            voto_max = voto
            gioco_migliore = gioco
    
    if gioco_migliore:
        print(f"\nGioco con voto massimo: {gioco_migliore.get('title', 'Sconosciuto')} ({voto_max})")
        #The Legend of Zelda: Ocarina of Time (99) (il mio gioco preferito!)


def conta_giochi_per_anno(lista_giochi):
    anni_count = {}
    for gioco in lista_giochi:
        date_str = gioco.get('date', '') #recupera la data di rilascio del gioco (il secondo parametro '' serve per evitare errori se la chiave non esiste)
        if ',' in date_str: #verifica che ci sia una virgola nella data
            anno = date_str.split(',')[1].strip() #estrae l'anno dalla data .strim = .trim di java o js
            #vi sono delle date vuote o senza ',', quindi metto un controllo per evitaere errori --> se non c'è la ',' nel record, questo viene saltato
            if anno:
                anni_count[anno] = anni_count.get(anno, 0) + 1 #aggiorna conteggio o inizializza..
    
    print("\nGiochi per anno:")
    for anno in sorted(anni_count.keys()):
        print(f"- {anno}: {anni_count[anno]}")


def giochi_per_voto_range(lista_giochi):
    
    fasce = {'Eccellente (80+)': 0, 'Buono (70-79)': 0, 'Medio (60-69)': 0, 'Basso (<60)': 0}
    
    for gioco in lista_giochi:
        voto = gioco.get('meta_score')
        if voto is not None:
            if voto >= 80:
                fasce['Eccellente (80+)'] += 1
            elif voto >= 70:
                fasce['Buono (70-79)'] += 1
            elif voto >= 60:
                fasce['Medio (60-69)'] += 1
            else:
                fasce['Basso (<60)'] += 1
    
    print("\nGiochi per fascia di voto:")
    for fascia, count in fasce.items():
        print(f"- {fascia}: {count}")        

if data:
    analizza_voti(data)
    conta_piattaforme(data)
    conta_generi(data)
    gioco_con_voto_massimo(data)
    conta_giochi_per_anno(data)
    giochi_per_voto_range(data)

"""
Python Dataset Explore - Data Analysis Module

Official documentation:
https://github.com/DALBO-creator/tpi-project-PythonDatasetExplore/wiki

This module provides statistical analysis functions for the Nintendo videogame dataset.
"""
