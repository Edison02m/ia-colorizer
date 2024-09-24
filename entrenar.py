#Desarrollado por Edison Azogue 

import tensorflow as tf
from modelos.modelo_colorizacion import construir_modelo
from tensorflow.keras.datasets import cifar10
import numpy as np

# Cargar y preparar los datos
(x_train, y_train), (x_test, y_test) = cifar10.load_data()

# Utilizar solo una parte de los datos para reducir el tiempo de entrenamiento
x_train = x_train[:20000]
y_train = y_train[:20000]
x_test = x_test[:20000]
y_test = y_test[:20000]

x_train_gris = tf.image.rgb_to_grayscale(x_train)
x_test_gris = tf.image.rgb_to_grayscale(x_test)

x_train_gris = tf.cast(x_train_gris, tf.float32) / 255.0
x_test_gris = tf.cast(x_test_gris, tf.float32) / 255.0

x_train = x_train.astype(np.float32) / 255.0
x_test = x_test.astype(np.float32) / 255.0

# Construir y entrenar el modelo
modelo = construir_modelo()
modelo.fit(x_train_gris, x_train, epochs=100, batch_size=64, validation_data=(x_test_gris, x_test))

# Guardar el modelo entrenado
modelo.save_weights('modelos/pesos_del_modelo.weights.h5') 
