from PIL import Image
import os

def convertir_a_webp(ruta_entrada, ruta_salida, calidad=85):
    # Verificar si la carpeta de salida existe, si no, crearla
    if not os.path.exists(ruta_salida):
        os.makedirs(ruta_salida)

    # Recorrer recursivamente la carpeta de entrada
    for ruta_actual, carpetas, archivos in os.walk(ruta_entrada):
        for archivo in archivos:
            # Comprobar si el archivo es una imagen JPEG o PNG
            if archivo.lower().endswith((".jpg", ".jpeg", ".png")):
                ruta_completa_entrada = os.path.join(ruta_actual, archivo)
                nombre_archivo, _ = os.path.splitext(archivo)
                ruta_completa_salida = os.path.join(ruta_salida, f"{nombre_archivo}.webp")

                # Abrir la imagen y guardarla en formato WebP con compresión
                imagen = Image.open(ruta_completa_entrada)
                imagen.save(ruta_completa_salida, "webp", quality=calidad)

if __name__ == "__main__":
    # Rutas de entrada y salida
    carpeta_entrada = "."
    carpeta_salida = "."

    # Llamar a la función para convertir imágenes a WebP con compresión
    convertir_a_webp(carpeta_entrada, carpeta_salida)
