"""
fourier_zyklen.py
-----------------

Zweck:
    Führt Fourier-Analysen auf Zeitreihen durch, insbesondere für:
    - solare Zyklen
    - planetare Perioden
    - galaktische Modulationen

Hauptfunktionen:
    - compute_fft(time_series, sampling_rate)
    - identify_peaks(frequency_spectrum, threshold)
    - export_spectrum(output_path)

Eingaben:
    - Zeitreihen (Listen, NumPy-Arrays)
    - Sampling-Rate
    - optionale Filterparameter

Ausgaben:
    - Frequenzspektren (NumPy-Arrays)
    - Peak-Listen
    - exportierte Spektren (.csv, .npy)

Abhängigkeiten:
    - numpy
    - scipy.signal
    - pandas (optional)
    - plotting.py (für Visualisierung)

Verwendung:
    Wird genutzt von:
        - analysis/zyklusanalyse.ipynb
        - analysis/zeitfeld_interferenz.ipynb
        - presentation/figures/
"""
