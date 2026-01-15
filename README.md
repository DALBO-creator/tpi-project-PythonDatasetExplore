# Python Dataset Explore

Progetto per l'analisi e visualizzazione di un dataset contenente informazioni su videogiochi.

## Descrizione

Questo progetto carica un dataset JSON di videogiochi da un repository GitHub e fornisce:

- **Analisi statistica** dei dati (voti, piattaforme, generi, anni di rilascio)
- **Visualizzazioni grafiche** dei risultati (grafici a barre, grafici a torta)

## Struttura del Progetto

```
tpi-project-PythonDatasetExplore/
├── data/
│   └── m.json              # Dataset dei videogiochi
├── src/
│   ├── analisi.py          # Script di analisi dati
│   └── visualizzazione.py  # Script di visualizzazione
└── README.md
```

## Dataset

Il dataset contiene informazioni su videogiochi con i seguenti campi:
- Titolo del gioco
- Platform (piattaforma di gioco)
- Voto (meta_score)
- Generi
- Data di rilascio

## Utilizzo

Eseguire i file Python per ottenere analisi e visualizzazioni:

```bash
python src/analisi.py          # Mostra statistiche testuali
python src/visualizzazione.py  # Mostra grafici
```

## Requisiti

- `requests` - per scaricare il dataset
- `matplotlib` - per le visualizzazioni grafiche
