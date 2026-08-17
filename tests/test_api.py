import httpx

BASE_URL = "http://localhost:8000"

def test_health():
    """Verifica que el endpoint de salud responda 200 OK."""
    respuesta = httpx.get(f"{BASE_URL}/health")
    assert respuesta.status_code == 200
    assert respuesta.json()["estado"] == "ok"

def test_clasificar_eco():
    """Verifica que el motor por reglas clasifique correctamente un fix."""
    payload = {"texto": "arregla el bug de inicio de sesion", "motor": "eco"}
    respuesta = httpx.post(f"{BASE_URL}/clasificar", json=payload)
    assert respuesta.status_code == 200
    datos = respuesta.json()
    assert datos["tipo"] == "fix"
    assert datos["motor"] == "eco"
