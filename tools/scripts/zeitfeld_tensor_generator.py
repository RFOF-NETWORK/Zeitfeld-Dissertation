"""
zeitfeld_tensor_generator.py
----------------------------

Zweck:
    Generiert Tensorfelder für das vollständige Zeitfeldmodell.
    Das Skript koppelt galaktische, solare, planetare und relativistische
    Komponenten zu einem konsistenten Tensorfeld.

Hauptfunktionen:
    - build_gradient_tensor(gradient_data)
    - combine_timefield_layers(galactic, solar, planetary, relativistic)
    - export_tensorfield(output_path)
    - generate_interference_tensor(tensor_a, tensor_b)

Eingaben:
    - verarbeitete Gradienten aus data/processed/zeitgradienten/
    - Gravitationsprofile aus data/processed/gravitationsprofile/
    - Frequenzdaten aus data/processed/zyklusfrequenzen/
    - Modellparameter aus tools/utilities/constants.py

Ausgaben:
    - Tensorfelder (.npy, .json)
    - Interferenz‑Tensoren
    - Exportierte Modelle für analysis/zeitfeld_interferenz.ipynb

Abhängigkeiten:
    - numpy
    - scipy
    - astro_helpers (Koordinatentransformationen)
    - constants (physikalische Parameter)
    - plotting (optionale Visualisierung)

Verwendung:
    Wird genutzt von:
        - analysis/galaktische_zeitgradienten.ipynb
        - analysis/zeitfeld_interferenz.ipynb
        - presentation/figures/
"""
