# Tarea 2: Procesador de Datos Dockerizado

## Cómo construir y ejecutar
1. **Construir la imagen:**
   `docker build -t procesador:1.0 .`
2. **Ejecutar el contenedor:**
   `docker run --rm -v "${PWD}/datos:/data/input:ro" -v "${PWD}/salida:/data/output" procesador:1.0`

## Variables de entorno
| Variable | Descripción | Valor por defecto |
| -------- | ----------- | ----------------- |
| `INPUT_FILE` | Ruta interna de lectura del archivo CSV. | `/data/input/datos.csv` |
| `OUTPUT_FILE`| Ruta interna donde se guardará el resumen CSV. | `/data/output/resultado.csv` |

*(Nota: No se exponen puertos ya que el script ejecuta una tarea y finaliza, no es un servidor).*

## Volúmenes de entrada y salida
* **Entrada:** La carpeta local `datos` se monta en `/data/input` como solo lectura (`:ro`).
* **Salida:** La carpeta local `salida` se monta en `/data/output` para persistir los resultados.

## Ejemplo con salida esperada
Al ejecutar el contenedor con el archivo `datos.csv` provisto, la terminal debe mostrar:
> Iniciando procesamiento...
> Ruta de entrada configurada: /data/input/datos.csv
> Ruta de salida configurada: /data/output/resultado.csv
> Procesamiento exitoso. Archivo guardado en /data/output/resultado.csv

La carpeta `salida` contendrá el archivo `resultado.csv` con las estadísticas descriptivas del procesamiento de Pandas.

## Evidencia de Publicación
La imagen se encuentra publicada en Docker Hub con la etiqueta de versión 1.0 (no solo latest).
Enlace: https://hub.docker.com/layers/jusstyyn/procesador/1.0/images/sha256%3Af694defb9c7b157f8554e9fcf637d1993654f85fc04b99958c5c49f302e4dcdf?uuid=C90DBCF3-AAE3-4FC0-94C5-7A04F617A83F

![alt text](image-1.png)