# Proyecto de Colorización de Imágenes

Este proyecto utiliza un modelo de aprendizaje profundo para colorizar imágenes en blanco y negro. El modelo está basado en una arquitectura de red neuronal convolucional (CNN) implementada con TensorFlow y Keras.

## Estructura del Proyecto

```
.
├── datos/
│   ├── entrada/
│   └── salida/
├── modelos/
│   ├── modelo_colorizacion.py
│   └── pesos_del_modelo.weights.h5
├── utilidades/
│   └── utilidades_imagenes.py
├── app.py
├── entrenar.py
└── README.md
```

## Requisitos

- Python 3.x
- TensorFlow 2.x
- Pillow
- NumPy

## Instalación

1. Clona este repositorio:
   ```
   git clone https://github.com/tu-usuario/proyecto-colorizacion-imagenes.git
   ```

2. Instala las dependencias:
   ```
   pip install tensorflow pillow numpy
   ```

## Uso

### Colorización de Imágenes con Modelo Pre-entrenado

El proyecto ya incluye un modelo pre-entrenado. Para colorizar imágenes usando este modelo:

1. Coloca tus imágenes en blanco y negro en la carpeta `datos/entrada/`
2. Ejecuta:
   ```
   python app.py
   ```
3. Las imágenes colorizadas se guardarán en la carpeta `datos/salida/`

### Mejora del Modelo

Si deseas mejorar la calidad de la colorización, puedes entrenar el modelo por más tiempo o con más datos:

1. Ajusta los parámetros de entrenamiento en `entrenar.py` (por ejemplo, aumenta el número de épocas o el tamaño del conjunto de datos)
2. Ejecuta:
   ```
   python entrenar.py
   ```
3. El modelo mejorado se guardará, reemplazando los pesos anteriores

Nota: Un entrenamiento más prolongado o con más datos puede resultar en una mejor colorización, pero también aumentará el tiempo de procesamiento.

## Estructura del Código

- `modelos/modelo_colorizacion.py`: Define la arquitectura del modelo de colorización.
- `utilidades/utilidades_imagenes.py`: Contiene funciones para cargar y guardar imágenes.
- `app.py`: Script principal para colorizar imágenes.
- `entrenar.py`: Script para entrenar y mejorar el modelo.

## Contribuciones

Las contribuciones son bienvenidas y pueden ayudar a mejorar la calidad de la colorización. Si deseas contribuir:

1. Haz un fork del repositorio.
2. Crea una nueva rama para tu característica o mejora.
3. Realiza tus cambios y haz commit de ellos.
4. Abre un pull request describiendo tus cambios.

Para cambios importantes, por favor abre primero un issue para discutir lo que te gustaría cambiar.

## Licencia

[MIT](https://choosealicense.com/licenses/mit/)
