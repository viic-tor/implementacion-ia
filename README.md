# implementacion-ia
Implementando ia hasta en la SOPA
# Clasificador de Commits IA - Proyecto SENA

Servicio de inferencia de IA local optimizado para entornos Linux nativos, utilizando Ollama (qwen2.5:0.5b / gemma3:270m) y FastAPI.

## Tecnologías
- **Backend:** FastAPI (Python 3.12)
- **Base de Datos:** PostgreSQL 16 (Alpine)
- **Motor IA:** Ollama Local (CPU-only para hardware limitado)
- **Orquestación:** Docker y Docker Compose
- **Calidad:** GitHub Actions (CI), Pytest y k6.

## Despliegue Rápido
1. Clonar el repositorio.
2. Copiar `.env.example` a `.env` y configurar credenciales.
3. Ejecutar `docker compose up -d --build`.
4. Acceder a `http://localhost:8000/docs`.
