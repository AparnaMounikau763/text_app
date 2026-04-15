import pytest
from app.validator import validate_text

def test_exact_boundary_length():
    assert validate_text("hey") == True   # length = 3 (boundary)

def test_below_boundary_length():
    with pytest.raises(ValueError):
        validate_text("hi")  # length = 2