from app.converters import convert_temperature, convert_length

def test_convert_temperature():
    assert convert_temperature("celsius", "fahrenheit", 0) == 32
    assert convert_temperature("fahrenheit", "celsius", 32) == 0

def test_convert_length():
    assert convert_length("meters", "kilometers", 1000) == 1
    assert convert_length("kilometers", "meters", 1) == 1000
