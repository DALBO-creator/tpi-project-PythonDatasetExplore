# Documentazione dei Moduli

## analisi.py

Script che esegue analisi statistiche sul dataset di videogiochi.

### Funzionalità

**`analizza_voti(lista_giochi)`**
- Calcola e stampa il voto massimo, minimo e medio dei giochi nel dataset

**`conta_piattaforme(lista_giochi)`**
- Conta il numero di giochi per ogni piattaforma
- Stampa la distribuzione in formato tabulare

**`conta_generi(lista_giochi)`**
- Conta gli occorrenze di ogni genere nei giochi
- Stampa i top 10 generi più popolari

**`gioco_con_voto_massimo(lista_giochi)`**
- Trova e stampa il titolo del gioco con il voto più alto

**`conta_giochi_per_anno(lista_giochi)`**
- Estrae l'anno di rilascio da ogni gioco
- Conta i giochi per anno
- Stampa il conteggio in ordine cronologico

**`giochi_per_voto_range(lista_giochi)`**
- Categorizza i giochi in 4 fasce di voto:
  - Eccellente (80+)
  - Buono (70-79)
  - Medio (60-69)
  - Basso (<60)

### Output

Lo script stampa a console:
- Statistiche sui voti
- Distribuzione per piattaforma
- Top 10 generi
- Gioco con voto massimo
- Distribuzione per anno
- Distribuzione per fascia di voto

---

## visualizzazione.py

Script che crea visualizzazioni grafiche dei dati del dataset.

### Grafici Generati

**1. Distribuzione dei Giochi per Piattaforma**
- Grafico a barre orizzontale
- Mostra il numero di giochi per ogni piattaforma

**2. Top 5 Generi Più Popolari**
- Grafico a torta (pie chart)
- Mostra le percentuali dei 5 generi principali

**3. Distribuzione dei Giochi per Fascia di Voto**
- Grafico a barre verticale
- Visualizza il numero di giochi in ogni fascia di voto

### Caratteristiche

- Utilizzo di colori distinti per ogni elemento
- Etichette chiare e titoli descrittivi
- Layout automatico per evitare sovrapposizioni (`tight_layout()`)
- Percentuali automatiche nei grafici a torta
