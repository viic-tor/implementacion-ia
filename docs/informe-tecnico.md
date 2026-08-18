### Simulacro de Respaldo
Se implementó y verificó una estrategia de copias de seguridad para el volumen de PostgreSQL utilizando `pg_dump` mediante el comando:
`docker exec -t db-ia pg_dump -U postgres -d iadb -c > backups/respaldo.sql`

### Diagrama Arquitectónico (Flujo de Datos)
1. **Cliente** -> (HTTP/REST) -> **API FastAPI (Puerto 8000)**
2. **API FastAPI** -> (Reglas/Regex) -> **Motor Eco** (Respaldo)
3. **API FastAPI** -> (HTTP/JSON) -> **Motor Ollama Local (Puerto 11434)**
4. **API FastAPI** -> (TCP/SQL) -> **PostgreSQL (Puerto 5432)** -> **Volumen pgdata**
