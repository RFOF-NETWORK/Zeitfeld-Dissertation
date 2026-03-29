"""
constants.py
------------

Zweck:
    Zentrale Sammlung aller physikalischen, astronomischen und
    projektspezifischen Konstanten, die im gesamten Zeitfeld‑Framework
    verwendet werden. Dieses Modul stellt sicher, dass alle Berechnungen
    konsistent, reproduzierbar und eindeutig definiert sind.

Physikalische Konstanten:
    - G: Gravitationskonstante
    - c: Lichtgeschwindigkeit
    - h: Plancksches Wirkungsquantum
    - k_B: Boltzmann-Konstante

Zeitkonstanten:
    - SECONDS_PER_DAY
    - JULIAN_DATE_OFFSET
    - GPS_EPOCH
    - TAI_OFFSET
    - UTC_LEAP_SECONDS (Liste)

Solare Parameter:
    - SOLAR_MASS
    - SOLAR_RADIUS
    - SOLAR_LUMINOSITY
    - SOLAR_CYCLE_MEAN_PERIOD

Planetare Parameter:
    - ORBITAL_PERIODS = {planet: period}
    - SEMI_MAJOR_AXES = {planet: axis}
    - ECCENTRICITIES = {planet: e}

Galaktische Parameter:
    - LOCAL_DENSITY
    - GALACTIC_ROTATION_SPEED
    - SUN_GALACTIC_RADIUS

Modellparameter:
    - TIMEFIELD_LAYER_WEIGHTS
    - INTERFERENCE_SCALING
    - TENSOR_NORMALIZATION

Verwendung:
    Wird genutzt von:
        - allen Skripten in tools/scripts/
        - allen Modulen in tools/utilities/
        - allen Notebooks in analysis/
        - Präsentations‑ und Visualisierungsmodulen

Hinweis:
    Dieses Modul enthält ausschließlich Konstanten und keine Logik.
"""
