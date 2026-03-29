# Zyklusfrequenzen – Verarbeitete Daten

## Inhalt
Dieser Ordner enthält die aus den Rohdaten extrahierten Frequenzen, Perioden und Resonanzmuster verschiedener astronomischer und physikalischer Zyklen.

Enthaltene Frequenztypen:

- Solare Zyklen  
  - Schwabe‑Zyklus (~11 Jahre)  
  - Hale‑Zyklus (~22 Jahre)  
  - Gleissberg‑Zyklus (~80–100 Jahre)

- Planetare Zyklen  
  - Synodische Perioden  
  - Bahnfunktionen  
  - Resonanzverhältnisse (z. B. Jupiter–Saturn)

- Galaktische Modulationen  
  - Langperiodische Gradienten  
  - Lokale Dichtewellen

- Kombinierte Interferenzfrequenzen  
  - Überlagerungen  
  - Beat‑Frequenzen  
  - Resonanzcluster

## Herkunft der Daten
Die Daten in diesem Ordner entstehen aus der Verarbeitung folgender Rohdaten:

- `data/raw/nasa_solar/`  
- `data/raw/planetary_ephemerides/`  
- `data/raw/gaia/`

## Typische Dateien
- `solare_frequenzen.csv`  
- `planetare_perioden.json`  
- `resonanzspektrum.npy`  
- `interferenzcluster.parquet`  
- `fourier_spektren/` (Unterordner)

## Verwendung im Projekt
Diese verarbeiteten Frequenzen werden genutzt in:

- `analysis/zyklusanalyse.ipynb`  
- `analysis/zeitfeld_interferenz.ipynb`  
- `analysis/galaktische_zeitgradienten.ipynb`

Sie bilden die Grundlage für:

- Fourier‑Analysen  
- Wavelet‑Analysen  
- Resonanzmodelle  
- Interferenzsimulationen  
- Kopplung der Zeitfeldschichten

## Format
Die Dateien liegen in folgenden Formaten vor:

- `.csv`  
- `.json`  
- `.npy`  
- `.parquet`

## Status
Alle Daten in diesem Ordner sind **bereits verarbeitet** und können direkt in den Analyse‑Notebooks geladen werden.
