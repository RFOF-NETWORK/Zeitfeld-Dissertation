# Zeitgradienten – Verarbeitete Daten

## Inhalt
Dieser Ordner enthält die aus den Rohdaten abgeleiteten Zeitgradienten.  
Die Gradienten repräsentieren die räumlichen und zeitlichen Veränderungen der Zeitmodulationen, die aus verschiedenen Quellen extrahiert wurden:

- Galaktische Gradienten  
- Solare Modulationsgradienten  
- Planetare Zeitgradienten  
- Kombinierte Interferenzgradienten  

## Herkunft der Daten
Die Daten in diesem Ordner entstehen aus der Verarbeitung folgender Rohdaten:

- `data/raw/gaia/`  
- `data/raw/nasa_solar/`  
- `data/raw/planetary_ephemerides/`  
- `data/raw/gps_time_dilation/`

## Typische Dateien
- `galaktische_gradientfelder.npy`  
- `solare_gradientprofile.csv`  
- `planetare_gradientmatrix.json`  
- `interferenzgradienten.parquet`

## Verwendung im Projekt
Diese verarbeiteten Gradienten werden genutzt in:

- `analysis/galaktische_zeitgradienten.ipynb`  
- `analysis/zeitfeld_interferenz.ipynb`  
- `analysis/relativistische_korrekturen.ipynb`

Sie bilden die Grundlage für:

- Tensorfelder  
- Interferenzmodelle  
- Zyklusüberlagerungen  
- Validierung des Zeitfeldmodells

## Format
Die Dateien liegen in folgenden Formaten vor:

- `.npy` (NumPy Arrays)  
- `.csv`  
- `.json`  
- `.parquet`

## Status
Alle Daten in diesem Ordner sind **bereits verarbeitet** und können direkt in den Analyse‑Notebooks geladen werden.
