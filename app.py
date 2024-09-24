import os
from modelos.modelo_colorizacion import construir_modelo
from utilidades.utilidades_imagenes import cargar_imagen, guardar_imagen

# Ruta a la carpeta de datos
carpeta_entrada = 'datos/entrada/'
carpeta_salida = 'datos/salida/'

# Cargar el modelo entrenado
modelo = construir_modelo()
modelo.load_weights('modelos/pesos_del_modelo.weights.h5')  # Ajusta la ruta a tus pesos entrenados

def colorizar_imagen(ruta_entrada, ruta_salida):
    imagen, original_size = cargar_imagen(ruta_entrada)
    if imagen is not None:
        try:
            imagen_colorizada = modelo.predict(imagen)[0]
            guardar_imagen(imagen_colorizada, ruta_salida, original_size)
        except Exception as e:
            print(f"Error al procesar la imagen {ruta_entrada}: {e}")

# Procesar todas las imágenes en la carpeta de entrada
for archivo in os.listdir(carpeta_entrada):
    if archivo.endswith('.jpeg') or archivo.endswith('.jpg'):
        ruta_entrada = os.path.join(carpeta_entrada, archivo)
        ruta_salida = os.path.join(carpeta_salida, archivo)
        colorizar_imagen(ruta_entrada, ruta_salida)
        print(f"Imagen {archivo} colorizada y guardada en {ruta_salida}")
