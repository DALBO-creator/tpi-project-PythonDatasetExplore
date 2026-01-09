import requests
import matplotlib.pyplot as plt

# --- 1. CARICAMENTO DATI ---
# Utilizzo l'URL raw come richiesto dalle specifiche del progetto
url = "https://raw.githubusercontent.com/DALBO-creator/tpi-project-PythonDatasetExplore/main/data/m.json"
response = requests.get(url)
data = response.json()

# --- 1. CARICAMENTO E DEBUG ---
url = "https://raw.githubusercontent.com/DALBO-creator/tpi-project-PythonDatasetExplore/main/data/m.json"
response = requests.get(url)
data = response.json()

# Stampa il tipo di dato e il contenuto per capire la struttura
print(f"Tipo di data: {type(data)}") 

# Se 'data' è un dizionario, dobbiamo trovare la chiave che contiene la lista dei giochi
if isinstance(data, dict):
    print("Chiavi trovate nel JSON:", data.keys())
    # Sostituisci 'lista_giochi' con la chiave corretta che vedi nei print sopra
    # Spesso i dataset hanno una struttura come data['games'] o data['results']
    # Se il file m.json è quello che hai postato prima, dovrebbe essere una lista.
    

print(f"Dataset caricato. Totale record: {len(data)}")

# --- 2. ELABORAZIONE DATI (LOGICA BASILARE) ---
# Creiamo liste pulite per le analisi, saltando i valori 'null' (None)
voti_critica = []
voti_utenti = []
piattaforme = []

for gioco in data:
    # Filtro per statistiche sui voti
    if gioco['meta_score'] is not None and gioco['user_score'] is not None:
        voti_critica.append(gioco['meta_score'])
        voti_utenti.append(gioco['user_score'])
    
    # Raccolta piattaforme per conteggio frequenze
    if gioco['platform']:
        piattaforme.append(gioco['platform'])

# --- 3. CALCOLO VALORI STATISTICI ---
if voti_critica:
    print(f"Voto massimo (Critica): {max(voti_critica)}")
    print(f"Voto medio (Critica): {sum(voti_critica)/len(voti_critica):.2f}")

# --- 4. VISUALIZZAZIONI GRAFICHE (MATPLOTLIB) ---

# GRAFICO 1: Confronto tra categorie (Bar Chart)
# Rappresenta quanti giochi ci sono per ogni console
conteggio_piattaforme = {}
for p in piattaforme:
    conteggio_piattaforme[p] = conteggio_piattaforme.get(p, 0) + 1

plt.figure(figsize=(10, 6))
plt.bar(conteggio_piattaforme.keys(), conteggio_piattaforme.values(), color='tomato')
plt.title('Numero di giochi per Piattaforma')
plt.xlabel('Console')
plt.ylabel('Quantità')

# GRAFICO 2: Distribuzione dei dati (Histogram)
# Rappresenta come sono distribuiti i punteggi della critica
plt.figure(figsize=(10, 6))
plt.hist(voti_critica, bins=20, color='skyblue', edgecolor='black')
plt.title('Distribuzione dei Meta Score')
plt.xlabel('Punteggio (0-100)')
plt.ylabel('Numero di giochi')

# GRAFICO 3: Relazione tra due variabili (Scatter Plot)
# Rappresenta la correlazione tra voto critica e voto utenti
plt.figure(figsize=(10, 6))
plt.scatter(voti_critica, voti_utenti, alpha=0.5, c='green')
plt.title('Relazione tra Meta Score e User Score')
plt.xlabel('Voto Critica')
plt.ylabel('Voto Utenti')

# Mostra tutti i grafici
plt.show()