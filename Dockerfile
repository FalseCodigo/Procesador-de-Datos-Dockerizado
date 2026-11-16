# Base slim con versión fija
FROM python:3.12.1-slim

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar requirements primero e instalar dependencias (optimización de caché)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Crear un usuario sin privilegios
RUN useradd -m appuser

# Copiar el script de Python
COPY app.py .

# Crear las carpetas para las rutas configurables y ajustar permisos
RUN mkdir -p /data/input /data/output && \
    chown -R appuser:appuser /app /data

# Cambiar al usuario sin privilegios por seguridad
USER appuser

# Comando de ejecución en forma exec
CMD ["python", "app.py"]