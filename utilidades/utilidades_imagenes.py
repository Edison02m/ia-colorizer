from PIL import Image
import numpy as np

def cargar_imagen(ruta):
    try:
        imagen = Image.open(ruta).convert('L')
        original_size = imagen.size
        imagen = imagen.resize((256, 256))
        imagen = np.array(imagen) / 255.0
        imagen = imagen.reshape((1, 256, 256, 1))
        return imagen, original_size
    except Exception as e:
        print(f"Error al cargar la imagen {ruta}: {e}")
        return None, None

def guardar_imagen(array_imagen, ruta, original_size):
    try:
        array_imagen = array_imagen * 255.0
        array_imagen = array_imagen.astype(np.uint8)
        array_imagen = array_imagen.reshape((256, 256, 3))
        imagen = Image.fromarray(array_imagen)
        imagen = imagen.resize(original_size)  # Volver a cambiar al tamaño original
        imagen.save(ruta)
    except Exception as e:
        print(f"Error al guardar la imagen {ruta}: {e}")
