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
    
    conteggio = {}
    for gioco in lista_giochi:
        if isinstance(gioco, dict):
            p = gioco.get('platform', 'Sconosciuta')
            conteggio[p] = conteggio.get(p, 0) + 1
    
    print("\nDistribuzione per piattaforma:")
    for p, n in conteggio.items():
        print(f"- {p}: {n}")

if data:
    analizza_voti(data)
    conta_piattaforme(data)