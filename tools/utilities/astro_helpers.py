"""
astro_helpers.py
----------------

Zweck:
    Sammlung astronomischer Hilfsfunktionen, die für Koordinatentransformationen,
    Zeitumrechnungen und Ephemeriden‑Berechnungen im gesamten Zeitfeld‑Projekt
    benötigt werden. Dieses Modul stellt die astronomische Grundlage für alle
    Modelle, Tensorfelder und Frequenzanalysen bereit.

Hauptfunktionen:
    - to_julian_date(datetime_obj)
    - from_julian_date(jd)
    - convert_time_scale(value, source_scale, target_scale)
    - interpolate_ephemerides(ephemeris_data, target_times)
    - galactic_to_equatorial(l, b)
    - equatorial_to_galactic(ra, dec)

Eingaben:
    - Zeitangaben (UTC, TAI, GPS, JD)
    - Ephemeriden‑Datensätze
    - astronomische Koordinaten (RA/Dec, galaktisch)
    - optionale Interpolationsparameter

Ausgaben:
    - konvertierte Zeitwerte
    - interpolierte Ephemeriden
    - transformierte Koordinaten
    - Hilfsdaten für Tensor‑ und Frequenzmodelle

Abhängigkeiten:
    - numpy
    - datetime
    - constants (Zeitkonstanten, astronomische Parameter)

Verwendung:
    Wird genutzt von:
        - tools/scripts/zeitfeld_tensor_generator.py
        - tools/scripts/fourier_zyklen.py
        - analysis/galaktische_zeitgradienten.ipynb
        - analysis/zyklusanalyse.ipynb
        - allen Modulen, die Zeit‑ oder Koordinatentransformationen benötigen
"""
