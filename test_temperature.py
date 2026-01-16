from temperature import celsius_to_fahrenheit

def test_positive_value():
    assert celsius_to_fahrenheit(25) == 77.0

def test_zero_celsius():
    assert celsius_to_fahrenheit(0) == 32.0

def test_negative_value():
    assert celsius_to_fahrenheit(-40) == -40.0
