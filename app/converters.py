def convert_temperature(from_unit: str, to_unit: str, value: float) -> float:
    if from_unit == "celsius" and to_unit == "fahrenheit":
        return (value * 9/5) + 32
    elif from_unit == "fahrenheit" and to_unit == "celsius":
        return (value - 32) * 5/9
    else:
        raise ValueError("Conversão não suportada.")

def convert_length(from_unit: str, to_unit: str, value: float) -> float:
    if from_unit == "meters" and to_unit == "kilometers":
        return value / 1000
    elif from_unit == "kilometers" and to_unit == "meters":
        return value * 1000
    else:
        raise ValueError("Conversão não suportada.")
