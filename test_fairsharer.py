from functions.py import fair_sharer 
import pytest
import numpy as np

def test_fair_sharer():
    # Test mit einer Iteration
    result = fair_sharer([0, 1000, 800, 0], 1)
    assert np.allclose(result, [100, 800, 900, 0])  # Überprüfe, ob das Ergebnis korrekt ist

    # Test mit zwei Iterationen
    result = fair_sharer([0, 1000, 800, 0], 2)
    assert np.allclose(result, [100, 890, 720, 90])  # Überprüfe, ob das Ergebnis korrekt ist

    # Test mit negativen Werten
    result = fair_sharer([-200, 500, -300, 100], 1)
    assert np.allclose(result, [0, 300, 400, -100])  # Überprüfe, ob das Ergebnis korrekt ist

    # Test mit einer großen Anzahl von Iterationen
    result = fair_sharer([10, 20, 30, 40, 50], 100)
    assert np.allclose(result, [25, 25, 25, 25, 25])

# Führe die Tests aus, wenn die Datei direkt ausgeführt wird
if __name__ == '__main__':
    pytest.main()
