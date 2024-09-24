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
   git clone https://github.com/Edison02m/ia-colorizer.git
   ```

2. Instala las dependencias:
   ```
   pip install tensorflow pillow numpy
   ```

## Uso

### Entrenamiento del Modelo

Para entrenar el modelo, ejecuta:

```
python entrenar.py
```

Este script cargará el conjunto de datos CIFAR-10, preparará los datos, entrenará el modelo y guardará los pesos en `modelos/pesos_del_modelo.weights.h5`.

### Colorización de Imágenes

Para colorizar imágenes, coloca tus imágenes en blanco y negro en la carpeta `datos/entrada/` y ejecuta:

```
python app.py
```

Las imágenes colorizadas se guardarán en la carpeta `datos/salida/`.

## Estructura del Código

- `modelos/modelo_colorizacion.py`: Define la arquitectura del modelo de colorización.
- `utilidades/utilidades_imagenes.py`: Contiene funciones para cargar y guardar imágenes.
- `app.py`: Script principal para colorizar imágenes.
- `entrenar.py`: Script para entrenar el modelo.

## Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue para discutir cambios importantes antes de hacer un pull request.

## Licencia

[MIT](https://choosealicense.com/licenses/mit/)
