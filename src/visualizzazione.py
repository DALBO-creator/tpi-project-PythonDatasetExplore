import requests
import matplotlib.pyplot as plt

url = "https://raw.githubusercontent.com/DALBO-creator/tpi-project-PythonDatasetExplore/main/data/m.json"
response = requests.get(url)
data = response.json()

#Distribuzione per piattaforma
conteggio_piattaforme = {}
for gioco in data:
    platform = gioco.get('platform', 'Sconosciuta')
    conteggio_piattaforme[platform] = conteggio_piattaforme.get(platform, 0) + 1

piattaforme = list(conteggio_piattaforme.keys())
numeri = list(conteggio_piattaforme.values())

plt.figure(figsize=(12, 6)) #larghezza e altezza in pollici
plt.barh(piattaforme, numeri, color='skyblue', edgecolor='black')
plt.title('Distribuzione dei Giochi per Piattaforma', fontsize=14, fontweight='bold')
plt.ylabel('Piattaforma', fontsize=12)
plt.xlabel('Numero di Giochi', fontsize=12)
plt.tight_layout() #tight layout serve per evitare sovrapposizioni andando a sistemare automaticamente gli spazi tra gli elementi del grafico
plt.show()

#Top 5 generi
generi_count = {}
for gioco in data:
    generi = gioco.get('genres', [])
    for genere in generi:
        generi_count[genere] = generi_count.get(genere, 0) + 1

generi_ordinati = sorted(generi_count.items(), key=lambda x: x[1], reverse=True)
top5_generi = generi_ordinati[:5]

generi_nomi = [g[0] for g in top5_generi] #estrae i nomi dei generi (primo elemento della tupla)
generi_conteggi = [g[1] for g in top5_generi] #estrae i conteggi dei generi (secondo elemento della tupla)

plt.figure(figsize=(10, 8))
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#ff99cc']
plt.pie(generi_conteggi, labels=generi_nomi, autopct='%1.1f%%', colors=colors) #autopct='%1.1f%%' mostra percentuali (calolate automaticamente in base ai dati forniti) con una cifra decimale
plt.title('Top 5 Generi più Popolari', fontsize=14, fontweight='bold')
plt.tight_layout() 
plt.show()

#Distribuzione per fascia di voto 

fasce = {'Basso\n(<60)': 0, 'Medio\n(60-69)': 0, 'Buono\n(70-79)': 0, 'Eccellente\n(80+)': 0}

for gioco in data:
    voto = gioco.get('meta_score')
    if voto is not None:
        if voto >= 80:
            fasce['Eccellente\n(80+)'] += 1
        elif voto >= 70:
            fasce['Buono\n(70-79)'] += 1
        elif voto >= 60:
            fasce['Medio\n(60-69)'] += 1
        else:
            fasce['Basso\n(<60)'] += 1

fasce_nomi = list(fasce.keys())
fasce_conteggi = list(fasce.values())

plt.figure(figsize=(10, 6))
colori = ['#ff6b6b', '#ffd93d', '#6bcf7f', '#4d96ff']
plt.bar(fasce_nomi, fasce_conteggi, color=colori, edgecolor='black')
plt.title('Distribuzione dei Giochi per Fascia di Voto', fontsize=14, fontweight='bold')
plt.ylabel('Numero di Giochi', fontsize=12)
plt.xlabel('Fascia di Voto', fontsize=12)
plt.tight_layout()
plt.show()

