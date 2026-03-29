"""
datenbereinigung.py
-------------------

Zweck:
    Bereinigt, harmonisiert und synchronisiert alle Rohdatenquellen des
    Zeitfeld-Projekts. Dieses Skript stellt sicher, dass alle Daten
    konsistent, vollständig und analysierbar sind, bevor sie in die
    verarbeiteten Datensätze überführt werden.

Hauptfunktionen:
    - remove_outliers(data, method="iqr")
    - interpolate_missing(data, method="linear")
    - normalize_timeseries(data)
    - sync_time_axes(datasets, target_scale="UTC")
    - export_cleaned(output_path)

Eingaben:
    - Rohdaten aus:
        * data/raw/gaia/
        * data/raw/nasa_solar/
        * data/raw/planetary_ephemerides/
        * data/raw/gps_time_dilation/
    - optionale Parameter für Filter, Interpolation und Normalisierung

Ausgaben:
    - bereinigte Datensätze (.csv, .json, .npy)
    - synchronisierte Zeitachsen
    - normalisierte Messreihen
    - Export nach data/processed/

Abhängigkeiten:
    - numpy
    - pandas
    - scipy.interpolate
    - constants (für Zeitkonstanten)
    - astro_helpers (für Zeitumrechnungen)

Verwendung:
    Wird genutzt von:
        - allen Skripten in tools/scripts/
        - allen Notebooks in analysis/
        - preprocessing-Pipelines für data/processed/
"""
