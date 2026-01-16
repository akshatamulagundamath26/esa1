from temperature import celsius_to_fahrenheit

def test_positive_value():
    assert celsius_to_fahrenheit(25) == 77.0
