from fastapi import APIRouter
from app.converters import convert_temperature, convert_length

router = APIRouter(
    prefix="/convert",
    tags=["Conversor de Unidades"],
)

@router.get("/temperature")
def temperature(from_unit: str, to_unit: str, value: float):
    """
    Converte temperatura de uma unidade para outra.
    """
    result = convert_temperature(from_unit, to_unit, value)
    return {"from": from_unit, "to": to_unit, "value": value, "result": result}

@router.get("/length")
def length(from_unit: str, to_unit: str, value: float):
    """
    Converte comprimento de uma unidade para outra.
    """
    result = convert_length(from_unit, to_unit, value)
    return {"from": from_unit, "to": to_unit, "value": value, "result": result}
