from functions import fair_sharer 
import pytest
import numpy as np

def test_fair_sharer():
    # Test with one iteration
    result = fair_sharer([0, 1000, 800, 0], 1)
    assert np.allclose(result, np.array([100, 800, 900, 0]), atol=1e-5, rtol=1e-5)

    # Test with two iterations
    result = fair_sharer([0, 1000, 800, 0], 2)
    assert np.allclose(result, np.array([100, 890, 720, 90]), atol=1e-5, rtol=1e-5)

    # Test with negative values
    result = fair_sharer([-200, 500, -300, 100], 1)
    assert np.allclose(result, np.array([0, 300, 400, -100]), atol=1e-5, rtol=1e-5)


# Führe die Tests aus, wenn die Datei direkt ausgeführt wird
if __name__ == '__main__':
    pytest.main()
